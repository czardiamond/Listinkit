// ListingKit billing via Paystack. Required env: PAYSTACK_SECRET_KEY, FIREBASE_API_KEY, FIREBASE_PROJECT_ID.
const PLANS = { pro: process.env.PLAN_PRO || "PLN_fn0d88ppmuypnoi", agency: process.env.PLAN_AGENCY || "PLN_hk1g6bg3rs0ddjl" };
const SITE = "https://listingkit-ai.netlify.app";
const H = { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type, Authorization" };
const KEY = () => process.env.PAYSTACK_SECRET_KEY;
const FIREBASE_KEY = () => process.env.FIREBASE_API_KEY || process.env.FIREBASE_WEB_API_KEY;
const FIREBASE_PROJECT = () => process.env.FIREBASE_PROJECT_ID;
// Deliberately hard-disabled: pending is process memory and cannot durably fulfil payments after a cold start.
const BILLING_FULFILMENT_READY = false;
const pending = new Map();
const ps = async (path, opt = {}) => {
  const r = await fetch("https://api.paystack.co" + path, { ...opt, headers: { Authorization: "Bearer " + KEY(), "Content-Type": "application/json" } });
  return r.json();
};
const decodePayload = (token) => {
  try {
    const part = String(token).split(".")[1];
    if (!part) return null;
    return JSON.parse(Buffer.from(part.replace(/-/g, "+").replace(/_/g, "/"), "base64").toString("utf8"));
  } catch { return null; }
};
const lookupFirebaseToken = async (token) => {
  if (!FIREBASE_KEY() || !FIREBASE_PROJECT() || !token) return null;
  const r = await fetch("https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=" + encodeURIComponent(FIREBASE_KEY()), {
    method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ idToken: token })
  });
  if (!r.ok) return null;
  const j = await r.json();
  const u = j && Array.isArray(j.users) ? j.users[0] : null;
  // accounts:lookup validates the token signature. Only after that success do we inspect its claims.
  const claims = decodePayload(token);
  const provider = claims && claims.firebase && claims.firebase.sign_in_provider;
  const expectedIssuer = "https://securetoken.google.com/" + FIREBASE_PROJECT();
  if (!u || !u.localId || u.disabled || (!u.email && !(Array.isArray(u.providerUserInfo) && u.providerUserInfo.length))) return null;
  if (!claims || claims.aud !== FIREBASE_PROJECT() || claims.iss !== expectedIssuer || claims.sub !== u.localId || !provider || provider === "anonymous") return null;
  return { uid: u.localId, email: String(u.email || "").trim().toLowerCase() };
};
const authUser = async (event) => {
  const h = event.headers || {};
  const raw = h.authorization || h.Authorization || "";
  const m = /^Bearer\s+([^\s]+)$/.exec(raw);
  return m ? lookupFirebaseToken(m[1]) : null;
};
const ok = (o) => ({ statusCode: 200, headers: H, body: JSON.stringify(o) });
const bad = (c, e) => ({ statusCode: c, headers: H, body: JSON.stringify({ error: e }) });

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: H, body: "" };
  if (event.httpMethod !== "POST") return bad(405, "POST only");
  let d = {};
  try { d = JSON.parse(event.body || "{}"); } catch { return bad(400, "bad json"); }
  const action = d.action;
  if (!KEY() || !FIREBASE_KEY() || !FIREBASE_PROJECT()) return bad(503, "billing not configured");
  const user = await authUser(event);
  if (!user) return bad(401, "authenticated non-anonymous account required");
  try {
    if (action === "checkout") {
      if (!BILLING_FULFILMENT_READY) return bad(503, "checkout unavailable until durable payment fulfilment is implemented");
      const plan = PLANS[d.plan] ? d.plan : null;
      if (!plan) return bad(400, "valid plan needed");
      const metadata = { product: "ListingKit", plan, uid: user.uid };
      const r = await ps("/transaction/initialize", { method: "POST", body: JSON.stringify({ email: user.email, amount: plan === "agency" ? 1500000 : 500000, plan: PLANS[plan], callback_url: SITE + "/generator/", metadata }) });
      if (!r.status || !r.data || !r.data.authorization_url || !r.data.reference) return bad(502, r.message || "paystack error");
      pending.set(String(r.data.reference), { uid: user.uid, email: user.email, plan });
      return ok({ url: r.data.authorization_url, reference: r.data.reference });
    }
    if (action === "verify") {
      if (!BILLING_FULFILMENT_READY) return bad(503, "payment verification unavailable until durable payment fulfilment is implemented");
      const ref = String(d.reference || "").trim();
      if (!ref) return bad(400, "reference needed");
      const owner = pending.get(ref);
      if (!owner || owner.uid !== user.uid) return bad(403, "payment ownership could not be established");
      const r = await ps("/transaction/verify/" + encodeURIComponent(ref));
      if (!r.status || !r.data || r.data.status !== "success") return ok({ active: false });
      const metadata = r.data.metadata || {};
      const customerEmail = String(r.data.customer && r.data.customer.email || "").trim().toLowerCase();
      if (String(metadata.uid || "") !== user.uid || customerEmail !== user.email || metadata.plan !== owner.plan) return bad(403, "payment ownership mismatch");
      pending.delete(ref);
      return ok({ active: true, uid: user.uid, plan: owner.plan });
    }
    return bad(400, "unknown action");
  } catch (e) { return bad(500, "billing failed"); }
};

exports._test = { pending, lookupFirebaseToken };
