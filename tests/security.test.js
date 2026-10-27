const test = require('node:test');
const assert = require('node:assert/strict');

process.env.PAYSTACK_SECRET_KEY = 'test-paystack-secret';
process.env.FIREBASE_API_KEY = 'test-firebase-key';
process.env.FIREBASE_PROJECT_ID = 'listinkit-test';
process.env.GROQ_API_KEY = 'test-groq-key';
const billing = require('../functions/billing.js');
const generation = require('../functions/generate.js');
const json = (body, status = 200) => ({ ok: status >= 200 && status < 300, status, async json() { return body; } });
const jwt = (claims) => `synthetic.${Buffer.from(JSON.stringify(claims)).toString('base64url')}.fixture`;
const validUser = jwt({ aud: 'listinkit-test', iss: 'https://securetoken.google.com/listinkit-test', sub: 'uid-1', firebase: { sign_in_provider: 'password' } });
const otherUser = jwt({ aud: 'listinkit-test', iss: 'https://securetoken.google.com/listinkit-test', sub: 'uid-2', firebase: { sign_in_provider: 'google.com' } });
const wrongProject = jwt({ aud: 'another-project', iss: 'https://securetoken.google.com/another-project', sub: 'uid-1', firebase: { sign_in_provider: 'password' } });
const anonymousWithEmail = jwt({ aud: 'listinkit-test', iss: 'https://securetoken.google.com/listinkit-test', sub: 'anon-1', firebase: { sign_in_provider: 'anonymous' } });
const event = (body, token) => ({ httpMethod: 'POST', headers: token ? { authorization: `Bearer ${token}` } : {}, body: JSON.stringify(body) });

let originalFetch;
let paystackCalls;
test.beforeEach(() => {
  originalFetch = global.fetch;
  paystackCalls = [];
  global.fetch = async (url, options = {}) => {
    if (url.includes('identitytoolkit.googleapis.com')) {
      const token = JSON.parse(options.body).idToken;
      if (token === validUser) return json({ users: [{ localId: 'uid-1', email: 'user@example.com', providerUserInfo: [{ providerId: 'password' }] }] });
      if (token === otherUser) return json({ users: [{ localId: 'uid-2', email: 'other@example.com', providerUserInfo: [{ providerId: 'google.com' }] }] });
      if (token === anonymousWithEmail) return json({ users: [{ localId: 'anon-1', email: 'anon@example.com', providerUserInfo: [{ providerId: 'anonymous' }] }] });
      if (token === wrongProject) return json({ users: [{ localId: 'uid-1', email: 'user@example.com', providerUserInfo: [{ providerId: 'password' }] }] });
      return json({ error: { message: 'INVALID_ID_TOKEN' } }, 400);
    }
    if (url.startsWith('https://api.paystack.co')) {
      paystackCalls.push({ url, options });
      if (url.endsWith('/transaction/initialize')) return json({ status: true, data: { authorization_url: 'https://paystack.test/checkout', reference: 'ref-1' } });
      if (url.includes('/transaction/verify/')) return json({ status: true, data: { status: 'success', customer: { email: 'user@example.com' }, metadata: { uid: 'uid-1', plan: 'pro' } } });
    }
    if (url.startsWith('https://api.groq.com')) return json({ choices: [{ message: { content: JSON.stringify({ ig: 'ok' }) } }] });
    throw new Error(`unexpected provider URL ${url}`);
  };
});
test.afterEach(() => { global.fetch = originalFetch; billing._test.pending.clear(); });

test('unsigned billing request is rejected before Paystack', async () => {
  const r = await billing.handler(event({ action: 'checkout', plan: 'pro' }));
  assert.equal(r.statusCode, 401); assert.equal(paystackCalls.length, 0);
});
test('anonymous, wrong-project, and invalid Firebase tokens are rejected before Paystack', async () => {
  assert.equal((await billing.handler(event({ action: 'checkout', plan: 'pro' }, anonymousWithEmail))).statusCode, 401);
  assert.equal((await billing.handler(event({ action: 'checkout', plan: 'pro' }, wrongProject))).statusCode, 401);
  assert.equal((await billing.handler(event({ action: 'checkout', plan: 'pro' }, 'invalid'))).statusCode, 401);
  assert.equal(paystackCalls.length, 0);
});
test('valid authenticated checkout is fail-closed before any Paystack initialization', async () => {
  const r = await billing.handler(event({ action: 'checkout', plan: 'pro' }, validUser));
  assert.equal(r.statusCode, 503);
  assert.match(JSON.parse(r.body).error, /durable payment fulfilment/);
  assert.equal(paystackCalls.length, 0);
});
test('billing verification is also fail-closed without durable fulfilment', async () => {
  const r = await billing.handler(event({ action: 'verify', reference: 'ref-1' }, validUser));
  assert.equal(r.statusCode, 503); assert.equal(paystackCalls.length, 0);
});
test('generation rejects unauthenticated requests before Groq', async () => {
  const r = await generation.handler(event({ allFeats: [] }));
  assert.equal(r.statusCode, 401); assert.equal(paystackCalls.length, 0);
});
test('generation rejects wrong-project and anonymous-with-email claims', async () => {
  assert.equal((await generation.handler(event({ allFeats: [] }, wrongProject))).statusCode, 401);
  assert.equal((await generation.handler(event({ allFeats: [] }, anonymousWithEmail))).statusCode, 401);
});
test('generation accepts a verified non-anonymous user and then calls Groq', async () => {
  const r = await generation.handler(event({ allFeats: [], tone: 'pro' }, validUser));
  assert.equal(r.statusCode, 200); assert.deepEqual(JSON.parse(r.body), { ig: 'ok' });
});

test('theme has no anonymous localStorage persistence and uses project memory only', () => {
  const fs = require('node:fs');
  const hark = fs.readFileSync(require('node:path').join(__dirname, '../site/hark.js'), 'utf8');
  assert.doesNotMatch(hark, /localStorage/);
  assert.match(hark, /memoryClient\.set\("hark-theme"/);
  assert.match(hark, /project-memory-change/);
});
