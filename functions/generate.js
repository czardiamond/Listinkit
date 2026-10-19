// ListingKit AI generation (Netlify Function). Key lives in env GROQ_API_KEY.
const MODEL = process.env.GROQ_MODEL || "openai/gpt-oss-120b";
const H = { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type" };
const clip = (v, n) => String(v == null ? "" : v).slice(0, n);

exports.handler = async (event) => {
  if (event.httpMethod === "OPTIONS") return { statusCode: 204, headers: H, body: "" };
  if (event.httpMethod !== "POST") return { statusCode: 405, headers: H, body: '{"error":"POST only"}' };
  if (!process.env.GROQ_API_KEY) return { statusCode: 503, headers: H, body: '{"error":"AI not configured"}' };
  let d;
  try { d = JSON.parse(event.body || "{}"); } catch { return { statusCode: 400, headers: H, body: '{"error":"bad json"}' }; }
  const p = {
    agent: clip(d.agent, 80), phone: clip(d.phone, 40), listing: clip(d.listing, 20), ptype: clip(d.ptype, 40),
    beds: clip(d.beds, 3), baths: clip(d.baths, 3), area: clip(d.area, 80), city: clip(d.city, 60), country: clip(d.country, 60),
    price: clip(d.priceTxt, 40), tone: clip(d.tone, 20),
    features: (Array.isArray(d.allFeats) ? d.allFeats : []).slice(0, 20).map((f) => clip(f, 60)),
  };
  const sys = `You are ListingKit, an expert real-estate copywriter for agents in Nigeria, Africa and worldwide.
Write marketing copy for ONE property using ONLY the facts given. Never invent features, sizes, prices, documents (e.g. C of O) or landmarks.
Use local conventions for the country (e.g. Nigeria: naira, BQ, "inspection", "C of O" only if given). Tone: ${p.tone}.
Return strict JSON with keys:
"ig": Instagram caption (hook line, emoji bullets of features, price, call to action with the agent contact, 12-18 relevant hashtags incl. area/city),
"tt": TikTok caption (short punchy hook, 2-3 lines, CTA, 5-8 hashtags),
"wa": WhatsApp broadcast message (use *bold* WhatsApp formatting, bullet features, price, "Reply or call to book an inspection" style CTA with contact),
"vid": 30-second video tour script as timed shots, e.g. "0-3s: ..." with on-screen text and voiceover lines; only film rooms/features listed (exterior, living room, bedrooms, bathrooms and listed features), no invented balconies, views or drone shots,
"desc": property portal description, 120-180 words, professional, no emoji, no hashtags.`;
  try {
    const r = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${process.env.GROQ_API_KEY}` },
      body: JSON.stringify({
        model: MODEL, temperature: 0.8, max_tokens: 4000, reasoning_effort: "low", response_format: { type: "json_object" },
        messages: [{ role: "system", content: sys }, { role: "user", content: "Property facts:\n" + JSON.stringify(p) }],
      }),
    });
    if (!r.ok) return { statusCode: 502, headers: H, body: JSON.stringify({ error: "upstream " + r.status }) };
    const j = await r.json();
    const out = JSON.parse(j.choices[0].message.content);
    const res = {};
    for (const k of ["ig", "tt", "wa", "vid", "desc"]) if (typeof out[k] === "string") res[k] = out[k]; else if (out[k]) res[k] = Array.isArray(out[k]) ? out[k].join("\n") : JSON.stringify(out[k]);
    return { statusCode: 200, headers: H, body: JSON.stringify(res) };
  } catch (e) {
    return { statusCode: 500, headers: H, body: JSON.stringify({ error: "generation failed" }) };
  }
};
