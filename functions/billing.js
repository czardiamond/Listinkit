// ListingKit billing via Paystack. Env: PAYSTACK_SECRET_KEY.
const crypto = require("crypto");
const PLANS = { pro: process.env.PLAN_PRO || "PLN_fn0d88ppmuypnoi", agency: process.env.PLAN_AGENCY || "PLN_hk1g6bg3rs0ddjl" };
const SITE = "https://listingkit-ai.netlify.app";
const H = { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type" };
const KEY = () => process.env.PAYSTACK_SECRET_KEY;
const ps = async (path, opt = {}) => {
  const r = await fetch("https://api.paystack.co" + path, { ...opt, headers: { Authorization: "Bearer " + KEY(), "Content-Type": "application/json" } });
  return r.json();
};
const sign = (email, plan) => {
  const exp = Date.now() + 35 * 864e5;
  const body = Buffer.from(JSON.stringify({ email, plan, exp })).toString("base64url");
  return body + "." + crypto.createHmac("sha256", KEY()).update(body).digest("base64url");
};
const planOf = (code) => Object.keys(PLANS).find((k) => PLANS[k] === code) || "pro";
const ok = (o) => ({ statusCode: 200, headers: H, body: JSON.stringify(o) });
const bad = (c, e) => ({ statusCode: c, headers: H, body: JSON.stringify({ error: e }) });

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: H, body: "" };
  if (!KEY()) return bad(503, "billing not configured");
  let d = {};
  try { d = JSON.parse(event.body || "{}"); } catch {}
  const q = event.queryStringParameters || {};
  const action = d.action || q.action;
  const email = String(d.email || q.email || "").trim().toLowerCase();
  try {
    if (action === "checkout") {
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return bad(400, "valid email needed");
      const plan = PLANS[d.plan] ? d.plan : "pro";
      const r = await ps("/transaction/initialize", { method: "POST", body: JSON.stringify({ email, amount: plan === "agency" ? 1500000 : 500000, plan: PLANS[plan], callback_url: SITE + "/generator/?paid=1", metadata: { product: "ListingKit", plan } }) });
      if (!r.status) return bad(502, r.message || "paystack error");
      return ok({ url: r.data.authorization_url });
    }
    if (action === "verify") {
      const ref = String(d.reference || q.reference || "");
      if (ref) {
        const r = await ps("/transaction/verify/" + encodeURIComponent(ref));
        if (r.status && r.data && r.data.status === "success") {
          const em = r.data.customer.email.toLowerCase();
          const plan = (r.data.metadata && r.data.metadata.plan) || (r.data.plan_object && planOf(r.data.plan_object.plan_code)) || "pro";
          return ok({ active: true, email: em, plan, token: sign(em, plan) });
        }
        return ok({ active: false });
      }
      if (email) {
        const c = await ps("/customer/" + encodeURIComponent(email));
        const subs = (c.status && c.data && c.data.subscriptions) || [];
        const live = subs.find((s) => ["active", "non-renewing", "attention"].includes(s.status));
        if (live) { const plan = planOf(live.plan && live.plan.plan_code); return ok({ active: true, email, plan, token: sign(email, plan) }); }
        return ok({ active: false });
      }
      return bad(400, "reference or email needed");
    }
    return bad(400, "unknown action");
  } catch (e) { return bad(500, "billing failed"); }
};
