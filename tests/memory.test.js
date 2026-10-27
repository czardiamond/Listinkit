const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const root = path.join(__dirname, '..');
const read = file => fs.readFileSync(path.join(root, file), 'utf8');

test('memory assets are present and loaded before account-backed page behavior', () => {
  const landing = read('site/index.html');
  const generator = read('site/generator/index.html');
  for (const file of ['site/memory-config.js', 'site/memory/bootstrap.js', 'site/memory-bridge.js']) {
    assert.ok(fs.existsSync(path.join(root, file)), `missing ${file}`);
  }
  assert.ok(landing.indexOf('memory-config.js') < landing.indexOf('hark.js'));
  assert.ok(generator.indexOf('../memory-config.js') < generator.indexOf('../memory/bootstrap.js'));
  assert.ok(generator.indexOf('../memory/bootstrap.js') < generator.indexOf('../memory-bridge.js'));
  assert.ok(generator.indexOf('../memory-bridge.js') < generator.indexOf('src="hark.js"'));
});

test('ListingKit generator emits explicit private work and bridge requires an owner account', () => {
  const generator = read('site/generator/index.html');
  const bridge = read('site/memory-bridge.js');
  assert.match(generator, /project-memory-work/);
  assert.match(generator, /input:\s*read\(\)/);
  assert.match(generator, /output:/);
  assert.match(bridge, /!client\.user\.isAnonymous/);
  assert.match(bridge, /client\.set\(`work:/);
  assert.match(bridge, /project-memory-restore/);
  assert.match(bridge, /onAuth/);
});

test('Firebase remains deliberately unconfigured in the local staging config', () => {
  assert.match(read('site/memory-config.js'), /firebaseConfig:\s*null/);
});
