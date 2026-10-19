"""/alternatives/ pages. Competitor facts come only from research/competitors.md (checked 18 Oct 2026)."""
from html import escape as E

LK = "ListingKit"
LK_PRICE = "Free (3 listings/mo); Pro ₦5,000 or $15/mo; Agency ₦15,000 or $39/mo (up to 5 agents). First 100 agents get 3 months of Pro free."


def table(cols, rows):
    h = "<div class=\"table-scroll\"><table class=\"cmp\"><thead><tr><th scope=\"col\"></th>" + "".join(f"<th scope=\"col\">{E(c)}</th>" for c in cols) + "</tr></thead><tbody>"
    for r in rows:
        h += f"<tr><th scope=\"row\">{E(r[0])}</th>" + "".join(f"<td>{E(x)}</td>" for x in r[1:]) + "</tr>"
    return h + "</tbody></table></div><p class=\"note\" style=\"margin-top:12px\">Competitor details as shown on each company's own website on 18 October 2026. Prices and features change; check their site before deciding. ListingKit is in early access: the free generator is live now and full plans open to the waitlist first.</p>"


def prose(paras):
    return "<div class=\"prose\">" + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def kit(prop, area, cur, extra_hash):
    """One listing in, full kit out: 8 sample outputs."""
    return [("", [
        ("You paste", "The only input", f"{prop}, {area}. Price {cur}___. [Features]. Agent: [Name], [Phone]."),
        ("Instagram caption", "Output", f"✨ Just listed in {area}\n{prop}\n💰 {cur}___\n📲 DM or WhatsApp [Phone] to book a viewing.\n\n{extra_hash}"),
        ("TikTok caption", "Output", f"POV: you found a {prop.lower()} in {area} 👀 Full tour 👇 #realestate #housetour"),
        ("WhatsApp broadcast", "Output", f"🏡 *NEW LISTING – {area}*\n{prop}\n✅ [Feature 1]\n✅ [Feature 2]\n💰 {cur}___\nReply *VIEW* for the video."),
        ("WhatsApp status", "Output", f"New in {area} 🔑 {prop} · {cur}___ · Reply to view."),
        ("Flyer copy", "Output", f"FOR SALE · {area.upper()}\n{prop}\n• [Feature 1]\n• [Feature 2]\n• [Feature 3]\n{cur}___ · [Phone]"),
        ("Portal description", "Output", f"{prop} in {area}. [Two to three sentences on layout and finish]. Features: [list]. Price: {cur}___. Viewing by appointment: [Phone]."),
        ("30-second video script", "Output", f"[0–3s] \"This is the {prop.lower()} in {area}.\"\n[3–20s] Living, kitchen, bedrooms.\n[20–30s] \"{cur}___. WhatsApp [Phone].\""),
    ])]


ALTS = [
 dict(slug="propclips-alternative", name="PropClips",
  title="PropClips Alternative for African Agents — ListingKit Compared",
  meta="Looking for a PropClips alternative? ListingKit vs PropClips compared on price (naira vs USD), WhatsApp broadcasts, flyers and video scripts. Honest, side-by-side.",
  h1="PropClips alternative: ListingKit compared", crumb="PropClips alternative",
  lede="PropClips is the closest tool to ListingKit: it also targets African, WhatsApp-first agents. The differences are price, currency and what you get per listing.",
  intro=["PropClips (propclips.live) turns a listing into captions for Instagram, Facebook, X, WhatsApp, Snapchat and TikTok, plus branded 9:16 story cards and auto video reels. It explicitly markets to agents in Nigeria, Kenya, South Africa and Egypt.",
         "If auto-generated reels from your photos are the main thing you need, PropClips may suit you. If you want the full written kit (WhatsApp broadcast, flyer copy and a script you film yourself) priced in naira, ListingKit is built for that."],
  cols=["ListingKit", "PropClips"],
  rows=[("Price", LK_PRICE, "Free $0 (3 stories, 3 classic reels, 1 AI reel a month); Basic $39.99/mo; Pro $69.99/mo; Custom. Yearly saves 10%."),
        ("Currency", "Naira and US dollars", "US dollars"),
        ("Captions", "Instagram, TikTok, WhatsApp status", "Instagram, Facebook, X, WhatsApp, Snapchat, TikTok"),
        ("WhatsApp broadcast message", "Yes", "Captions only (no broadcast script)"),
        ("Printable flyer copy", "Yes", "No print/PDF flyer"),
        ("Video", "30-second tour script for you to film", "Auto reels made from your photos"),
        ("Best for", "Agents who want every written asset per listing at a naira price", "Agents who mainly want auto-generated story cards and reels")],
  verdict=["<strong>Choose PropClips</strong> if you want story cards and reels generated from photos and you're comfortable paying in dollars.",
           "<strong>Choose ListingKit</strong> if you sell mostly on WhatsApp, need a broadcast message and flyer copy for every listing, and want to pay ₦5,000 a month instead of $39.99 or more.",
           "They can work together: some agents will use ListingKit for the words and another tool for visuals."],
  kitargs=("4-bed duplex with BQ", "Lekki Phase 1", "₦", "#LekkiHomes #LagosRealEstate"),
  faq=[("Is ListingKit cheaper than PropClips?", "Yes. ListingKit Pro is ₦5,000 or $15 a month; PropClips Basic was $39.99 a month on its pricing page on 18 Oct 2026."),
       ("Does ListingKit make video reels like PropClips?", "No. ListingKit writes a 30-second video tour script you film yourself; PropClips generates reels from your photos."),
       ("Does PropClips write WhatsApp broadcasts?", "PropClips writes WhatsApp captions; it did not list a WhatsApp broadcast script or printable flyer when we checked."),
       ("Can I try ListingKit free?", "Yes. The free generator is live now, and the Free plan includes 3 listings a month.")]),
 dict(slug="listingai-alternative", name="ListingAI",
  title="ListingAI Alternative for Agents Outside the US — ListingKit",
  meta="ListingAI alternative for agents in Nigeria, Africa and beyond: ListingKit vs ListingAI on price, naira billing, WhatsApp support and what each tool is built for.",
  h1="ListingAI alternative: ListingKit compared", crumb="ListingAI alternative",
  lede="ListingAI is a full US-centric toolkit. ListingKit is narrower and cheaper, built for agents who sell on WhatsApp and Instagram outside the US MLS world.",
  intro=["ListingAI (listingai.co) offers listing descriptions, social posts and reels, listing websites, CMA, virtual staging and agent websites. It bills in USD, CAD, AUD, GBP, EUR and ZAR.",
         "Its CMA and market reports are US-only and it is MLS-oriented. If you're a US agent who wants an all-in-one suite, it's a strong option. If you need WhatsApp copy and naira pricing, ListingKit fits better."],
  cols=["ListingKit", "ListingAI"],
  rows=[("Price", LK_PRICE, "Free (1 listing); Essential $19/mo; Professional $36/mo; Expert $150/mo"),
        ("Currencies", "Naira and US dollars", "USD, CAD, AUD, GBP, EUR, ZAR (no NGN)"),
        ("WhatsApp copy", "Status captions and broadcast messages", "Not listed"),
        ("Listing descriptions", "Yes", "Yes"),
        ("Flyer copy & video script", "Yes", "Social posts and reels"),
        ("Extras", "Focused on per-listing marketing copy", "Listing websites, CMA (US-only), virtual staging, agent website"),
        ("Best for", "Agents in Africa and emerging markets selling on WhatsApp", "US agents wanting an MLS-oriented all-in-one suite")],
  verdict=["<strong>Choose ListingAI</strong> if you're in the US and want CMA, listing websites and virtual staging in one place.",
           "<strong>Choose ListingKit</strong> if you want WhatsApp broadcasts, flyers and video scripts for every listing, priced in naira from ₦5,000 a month.",
           "ListingKit's Free plan gives 3 listings a month versus 1 on ListingAI's free tier."],
  kitargs=("3-bed apartment", "East Legon", "GH₵", "#EastLegon #AccraRealEstate"),
  faq=[("Does ListingAI support naira?", "Its pricing page listed USD, CAD, AUD, GBP, EUR and ZAR, but not NGN, when we checked on 18 Oct 2026."),
       ("Is ListingKit a full ListingAI replacement?", "Not entirely. ListingKit doesn't do CMA, virtual staging or agent websites. It focuses on the marketing copy for each listing."),
       ("Which is cheaper?", "ListingKit Pro is $15 (₦5,000) a month; ListingAI Essential was $19 a month."),
       ("Does ListingKit work for agents outside Nigeria?", "Yes. It works for any city and currency, including Ghana, Kenya, the UAE and the UK.")]),
 dict(slug="canva-alternative-for-realtors", name="Canva",
  title="Canva Alternative for Realtors? ListingKit vs Canva Pro",
  meta="Is there a Canva alternative for real estate agents? ListingKit vs Canva Pro in Nigeria: price, who writes the captions, WhatsApp broadcasts and how they work together.",
  h1="Canva alternative for realtors: ListingKit vs Canva", crumb="Canva alternative for realtors",
  lede="Honestly, ListingKit doesn't replace Canva; it does the part Canva doesn't. Canva designs the flyer. ListingKit writes everything that goes with it.",
  intro=["Canva is the default design tool for Nigerian agents' flyers and Instagram graphics. It has AI writing features, but it isn't built around real estate listings, so you still write each caption, WhatsApp blast and video script yourself.",
         "Canva Pro was listed at ₦5,500 a month in Nigeria (App Store regional pricing, checked 8 Oct 2026; web or Android prices may differ). ListingKit Pro is ₦5,000 a month and writes the copy for every listing."],
  cols=["ListingKit", "Canva Pro"],
  rows=[("Price in Nigeria", "Pro ₦5,000/mo (Free: 3 listings/mo)", "₦5,500/mo (App Store, checked 8 Oct 2026); Business ₦7,900/mo"),
        ("What it does", "Writes captions, WhatsApp broadcasts, flyer copy, portal descriptions and video scripts", "Designs flyers, graphics and videos from templates"),
        ("Real-estate specific", "Yes, built around a property listing", "General-purpose, with real estate templates"),
        ("Who writes the words", "ListingKit, from your property details", "You (or general AI writing tools)"),
        ("Design", "Copy only; paste into your design tool", "Full design editor"),
        ("Best for", "Saving writing time on every listing", "Making the visuals")],
  verdict=["<strong>Keep Canva</strong> for designing flyers and graphics; it's excellent at that.",
           "<strong>Add ListingKit</strong> to write the caption, WhatsApp broadcast, flyer text and video script in seconds, then paste the flyer text into your Canva template.",
           "If you only post a few listings a month, ListingKit's Free plan (3 listings) may be all you need alongside Canva."],
  kitargs=("600 sqm plot with Governor's Consent", "Ajah", "₦", "#LandForSale #AjahHomes"),
  faq=[("Is ListingKit a replacement for Canva?", "No. Canva designs visuals; ListingKit writes the marketing copy. Most agents will use both."),
       ("Is ListingKit cheaper than Canva Pro in Nigeria?", "ListingKit Pro is ₦5,000 a month; Canva Pro was ₦5,500 a month on the App Store in Nigeria when checked on 8 Oct 2026."),
       ("Can I use ListingKit flyer copy in Canva?", "Yes. Copy the headline and bullets from ListingKit and paste them into any Canva real estate template."),
       ("Does Canva write WhatsApp broadcasts?", "Canva has general AI writing features, but it isn't set up to produce real-estate WhatsApp broadcasts from a listing.")]),
]


def pages():
    out = []
    for a in ALTS:
        extra = [("compare", f"{LK} vs {a['name']} at a glance", table(a["cols"], a["rows"])),
                 ("verdict", "Which should you choose?", prose(a["verdict"]))]
        out.append(dict(path=f"/alternatives/{a['slug']}/", section="alternatives", crumb=a["crumb"], title=a["title"], meta=a["meta"],
                        h1=a["h1"], eyebrow="Comparison", lede=a["lede"], intro=a["intro"], extra_html=extra,
                        groups=kit(*a["kitargs"]), groups_title="What one ListingKit input gives you",
                        tips=["Try the free generator with a real listing before deciding.", "Compare on the assets you actually post every week, not on feature counts.",
                              "Check prices on each tool's own site; they change.", "If you sell mostly on WhatsApp, test how each tool handles broadcast messages."],
                        tips_title="How to choose", faq=a["faq"],
                        related=[f"/alternatives/{x['slug']}/" for x in ALTS if x["slug"] != a["slug"]] + ["/guides/chatgpt-prompts-for-real-estate-agents/", "/whatsapp/new-listing/", "/captions/just-listed/"],
                        blurb=a["lede"][:120]))
    return out
