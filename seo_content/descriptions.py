"""/descriptions/{type}-in-{area}/ pages: listing description templates by property type x area.

Local facts are limited to well-known districts, roads and landmarks. Prices are always
placeholders (₦___, GH₵___, KSh ___, AED ___) — never invented.
"""

NG_PORTALS = "Nigeria Property Centre, PropertyPro or Jiji"
AREAS = {
 "lekki": dict(name="Lekki", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Lekki Phase 1", "Chevron", "Ikota", "Osapa London", "Agungi", "Orchid Road"],
   anchors=["the Lekki-Epe Expressway", "Admiralty Way", "the Lekki-Ikoyi Link Bridge", "the Lekki Conservation Centre"],
   perks=["gated-estate living", "quick access to Victoria Island and Ikoyi", "a deep rental and shortlet market", "plenty of new-build stock"],
   buyers="young families, Island professionals, diaspora investors and shortlet operators",
   title="Governor's Consent or C of O", tag="#LekkiHomes",
   notes=["Name the exact sub-area. \"Lekki\" stretches from Phase 1 to Ibeju-Lekki, and buyers price them very differently.",
          "Be ready for drainage questions: some Lekki streets flood in the rainy season, and serious buyers will ask about the specific road.",
          "Quote realistic off-peak drive times on the Lekki-Epe Expressway rather than \"minutes from everywhere\".",
          "Estate details sell here: the gate, security, road quality and estate dues."],
   faq=[("Which part of Lekki should I name in a listing?", "Always name the sub-area or estate, such as Lekki Phase 1, Chevron, Ikota or Osapa London, rather than just \"Lekki\"; buyers search and price by sub-area."),
        ("What title documents do Lekki buyers expect?", "Most buyers look for Governor's Consent or a C of O. For new estates, say exactly what exists, such as a registered survey or excision, and offer documents for their lawyer to verify.")]),
 "ikoyi": dict(name="Ikoyi", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Old Ikoyi", "Banana Island", "Parkview Estate", "Osborne Foreshore", "Bourdillon", "Dolphin Estate"],
   anchors=["Bourdillon Road", "Awolowo Road", "Falomo", "the Lekki-Ikoyi Link Bridge"],
   perks=["mature, tree-lined streets", "minutes from the Victoria Island business district", "high-end serviced buildings", "an established, prestigious address"],
   buyers="senior executives, expatriates, high-net-worth families and corporate tenants",
   title="C of O or Governor's Consent", tag="#IkoyiHomes",
   notes=["Corporate and expatriate leases in Ikoyi are often quoted in US dollars. State the currency clearly and whether naira is accepted.",
          "Name the micro-location: Banana Island, Parkview, Osborne Foreshore and Old Ikoyi each attract a different buyer.",
          "Lead with services: power arrangement, water treatment, staff quarters, security and facility management.",
          "Keep the tone understated. Ikoyi buyers respond to specifics, not superlatives."],
   faq=[("Should I price Ikoyi listings in dollars or naira?", "Use whatever the landlord or seller actually accepts. Many corporate leases are in dollars; if so, say so and note whether naira payment is possible."),
        ("What do Ikoyi tenants ask about most?", "Power (dedicated transformer and backup generators), service charge, security, parking and how the building is managed.")]),
 "victoria-island": dict(name="Victoria Island", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Oniru", "Adeola Odeku", "Ahmadu Bello Way", "Ozumba Mbadiwe", "Eko Atlantic axis"],
   anchors=["Adeola Odeku Street", "Ahmadu Bello Way", "Ozumba Mbadiwe Avenue", "the Lagos Civic Centre"],
   perks=["walking distance to banks and corporate offices", "restaurants, lounges and nightlife", "year-round business travel demand", "serviced high-rise living"],
   buyers="business travellers, corporate tenants, young executives and investors",
   title="C of O or Governor's Consent", tag="#VictoriaIsland",
   notes=["VI demand is driven by work. Mention walk or drive times to the business district and major hotels.",
          "Parking is scarce in VI; a dedicated parking space is a genuine selling point.",
          "Short-stay guests here are often on business, so lead with Wi-Fi, a desk and reliable power.",
          "If the building is in Oniru or on the Eko Atlantic side, say so; buyers treat them as distinct."],
   faq=[("Who rents in Victoria Island?", "Mostly corporate tenants, business travellers and young professionals who want to live close to work, restaurants and nightlife."),
        ("What sells a VI apartment fastest?", "Reliable power, parking, a good building manager and a short commute to the business district.")]),
 "ajah": dict(name="Ajah", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Badore", "Abraham Adesanya", "Sangotedo", "Thomas Estate", "Lakowe", "Ado Road"],
   anchors=["the Lekki-Epe Expressway", "Ajah roundabout", "Abraham Adesanya roundabout"],
   perks=["more space for the money than Lekki Phase 1", "fast-growing new estates", "first-time-buyer prices", "land with growth potential along the Lekki corridor"],
   buyers="first-time buyers, growing families, land bankers and investors",
   title="Governor's Consent, C of O, excision or gazette", tag="#AjahHomes",
   notes=["Ajah buyers compare value. Show what the price gets them versus closer-in Lekki.",
          "Be precise about the estate and the turn-off from the Lekki-Epe Expressway; \"Ajah\" covers a wide area.",
          "Drainage and access roads matter. If the estate road is tarred, say so.",
          "For land, state the exact title stage (excision, gazette, Governor's Consent) rather than \"good title\"."],
   faq=[("Is Ajah good for first-time buyers?", "It's popular with first-time buyers because homes and land cost less than closer-in Lekki. Present the value clearly and be honest about commute times."),
        ("What title documents are common for land around Ajah?", "You'll see Governor's Consent, C of O, excision and gazette. State exactly what the land has and invite buyers to verify.")]),
 "ikeja": dict(name="Ikeja", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Ikeja GRA", "Allen Avenue", "Opebi", "Oregun", "Alausa", "Adeniyi Jones"],
   anchors=["the Murtala Muhammed International Airport", "Ikeja City Mall", "Obafemi Awolowo Way", "the Alausa secretariat"],
   perks=["airport proximity", "mainland living without the bridge commute", "close to government offices in Alausa", "established shopping and schools"],
   buyers="mainland professionals, civil servants, frequent flyers and families",
   title="C of O or Governor's Consent", tag="#IkejaHomes",
   notes=["Name the pocket: Ikeja GRA is quiet and leafy, while Allen, Opebi and Oregun are busier and more commercial.",
          "Airport proximity is a real draw for frequent travellers and airline staff; mention it if it's genuinely close.",
          "Many Ikeja buyers work on the mainland and avoid the bridges, so frame commute times around mainland hubs.",
          "Mention power and water arrangements; mainland tenants ask early."],
   faq=[("Which parts of Ikeja are most sought after?", "Ikeja GRA is the premium residential pocket. Allen Avenue, Opebi and Oregun suit people who want to be close to business and shopping."),
        ("Is Ikeja good for rentals?", "Yes. Demand comes from mainland professionals, civil servants and people who want easy airport access.")]),
 "yaba": dict(name="Yaba", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Sabo", "Alagomeji", "Akoka", "Onike", "Jibowu", "Abule-Ijesha"],
   anchors=["the University of Lagos (UNILAG)", "Yaba College of Technology", "Herbert Macaulay Way", "the Third Mainland Bridge"],
   perks=["the heart of Lagos's tech scene", "students and young professionals", "a central mainland location", "easy routes to the Island"],
   buyers="tech workers, young professionals, students and landlords",
   title="C of O or Governor's Consent", tag="#YabaLagos",
   notes=["Yaba renters are young and budget-aware. Lead with rent, power and internet.",
          "Proximity to UNILAG or Yaba Tech matters for student and staff housing; name the campus only if it's genuinely nearby.",
          "Fibre or good 4G coverage is a selling point for remote and tech workers.",
          "Mention the route to the Island (Third Mainland Bridge) for tenants who work in VI or Ikoyi."],
   faq=[("Who rents in Yaba?", "Tech workers, young professionals, students and university staff. Lead with rent, power and internet."),
        ("Are shortlets viable in Yaba?", "There is demand from visiting tech teams, students' families and event-goers. Price below Island shortlets and highlight Wi-Fi and power.")]),
 "magodo": dict(name="Magodo", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Magodo GRA Phase 1", "Magodo GRA Phase 2", "Shangisha"],
   anchors=["CMD Road", "the Lagos-Ibadan Expressway", "Ojota", "Ketu"],
   perks=["a gated GRA with controlled access", "quiet, low-density streets", "family homes on generous plots", "mainland calm with good road links"],
   buyers="established families, senior civil servants and mainland professionals",
   title="C of O or Governor's Consent", tag="#MagodoGRA",
   notes=["Say which phase. Magodo GRA Phase 1 and Phase 2 (Shangisha) are distinct and buyers know the difference.",
          "Security and estate management are the main selling points; mention gates and estate rules.",
          "Plot size and compound space matter more here than in high-rise areas; give the land size.",
          "Mention road links to the Lagos-Ibadan Expressway and Ojota for commuters."],
   faq=[("Why do families choose Magodo?", "It's a gated, low-density GRA on the mainland with larger plots and quieter streets."),
        ("Should I mention the estate phase?", "Yes. Name Magodo GRA Phase 1 or Phase 2 (Shangisha); buyers value them differently.")]),
 "gbagada": dict(name="Gbagada", city="Lagos", group="Lagos", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Gbagada Phase 1", "Gbagada Phase 2", "Ifako", "Soluyi", "New Garage"],
   anchors=["the Third Mainland Bridge", "the Gbagada-Oworonshoki Expressway", "Gbagada General Hospital"],
   perks=["a midpoint between the mainland and the Island", "established residential estates", "good value for Island commuters", "easy Third Mainland Bridge access"],
   buyers="Island-working professionals, young families and landlords",
   title="C of O or Governor's Consent", tag="#GbagadaLagos",
   notes=["Gbagada's pitch is location: say how it connects to the Island via the Third Mainland Bridge.",
          "Name the phase or estate; Gbagada Phase 1 and Phase 2 are the recognised residential pockets.",
          "Buyers here compare with Yaba and Ikeja; position on value and access.",
          "Mention parking and estate security; both are frequent questions."],
   faq=[("Why market Gbagada to Island workers?", "It's a mainland location with direct Third Mainland Bridge access, often at lower rents than the Island."),
        ("What do Gbagada tenants ask about?", "Commute to the Island, parking, estate security, power and water.")]),
 "gwarinpa-abuja": dict(name="Gwarinpa", city="Abuja", group="Abuja", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["1st Avenue", "3rd Avenue", "6th Avenue", "7th Avenue", "Gwarinpa Estate"],
   anchors=["the Kubwa Expressway", "Jabi", "Life Camp", "Gwarinpa Avenue"],
   perks=["one of the largest housing estates in Nigeria", "family-friendly streets", "mid-market prices for Abuja", "plenty of terraces and duplexes"],
   buyers="Abuja families, civil servants, professionals and investors",
   title="C of O (FCT) or Right of Occupancy", tag="#GwarinpaAbuja",
   notes=["Use the avenue or street reference; Abuja buyers navigate Gwarinpa by its numbered avenues.",
          "Abuja title documents differ from Lagos: state whether there is an FCT Certificate of Occupancy, Right of Occupancy or allocation papers.",
          "Mention access to the Kubwa Expressway and Jabi for commuters.",
          "Gwarinpa is family territory: schools, playgrounds and quiet closes sell."],
   faq=[("What title documents apply to Gwarinpa property?", "Abuja property usually carries an FCT Certificate of Occupancy, Right of Occupancy or allocation papers. State exactly which, and encourage verification with AGIS through a lawyer."),
        ("How do buyers find homes in Gwarinpa?", "By avenue and street. Quote the avenue (for example 3rd or 6th Avenue) so buyers can place it instantly.")]),
 "maitama-abuja": dict(name="Maitama", city="Abuja", group="Abuja", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Maitama District", "Maitama Extension"],
   anchors=["Transcorp Hilton", "Millennium Park", "Aguiyi Ironsi Street", "the Central Business District"],
   perks=["embassies and diplomatic residences nearby", "low density and large plots", "a prestige address in the capital", "quick access to the Central Business District"],
   buyers="diplomats, senior executives, government officials and international organisations",
   title="C of O (FCT)", tag="#MaitamaAbuja",
   notes=["Diplomatic and corporate tenants care about security, privacy and staff quarters; lead with these.",
          "Leases here may be quoted in dollars for international tenants. Say which currency applies.",
          "Keep the tone formal and precise; many enquiries come from relocation managers and embassies.",
          "State the title (FCT C of O) and the plot size; both matter at this price point."],
   faq=[("Who rents or buys in Maitama?", "Diplomats, senior executives, government officials and international organisations, plus high-net-worth families."),
        ("What should a Maitama listing emphasise?", "Security, privacy, plot size, staff quarters, power arrangements and proximity to the Central Business District.")]),
 "wuse-abuja": dict(name="Wuse", city="Abuja", group="Abuja", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Wuse 2", "Wuse Zone 4", "Wuse Zone 5", "Wuse Zone 6"],
   anchors=["Banex Plaza", "Aminu Kano Crescent", "Wuse Market", "the Central Business District"],
   perks=["restaurants and nightlife on Aminu Kano Crescent", "a central base for business travellers", "strong shortlet demand", "walkable shops and services"],
   buyers="business travellers, young professionals, investors and shortlet operators",
   title="C of O (FCT)", tag="#Wuse2",
   notes=["Name the zone: Wuse 2 and the numbered Wuse zones are distinct, and Wuse 2 is the best known.",
          "Shortlet guests here are often in Abuja for meetings; highlight Wi-Fi, a workspace and quick routes to the Central Business District.",
          "Mention walkable conveniences such as Banex Plaza or Aminu Kano Crescent only if they're genuinely close.",
          "Parking and power are top questions for Wuse apartments."],
   faq=[("Is Wuse good for shortlets?", "Yes. Wuse 2 in particular attracts business travellers and visitors who want restaurants and shops nearby."),
        ("Should I say Wuse or Wuse 2?", "Be specific. Wuse 2 is a recognised, sought-after district, distinct from the other Wuse zones.")]),
 "port-harcourt-gra": dict(name="Port Harcourt GRA", city="Port Harcourt", group="Port Harcourt", cur="₦", unit="sqm", rent="per annum", portals=NG_PORTALS,
   subs=["Old GRA", "GRA Phase 1", "GRA Phase 2", "GRA Phase 3"],
   anchors=["Aba Road", "Tombia Street", "the Trans-Amadi industrial layout"],
   perks=["established, leafy and central", "close to oil and gas offices", "a steady corporate rental market", "restaurants and hotels nearby"],
   buyers="oil and gas professionals, corporate tenants, executives and families",
   title="C of O or Governor's Consent (Rivers State)", tag="#PortHarcourtGRA",
   notes=["Say which phase: Old GRA and GRA Phases 1–3 are all known by name.",
          "Corporate tenants from the oil and gas sector want security, power backup and parking; lead with these.",
          "Mention access to Aba Road and Trans-Amadi for commuters.",
          "Be clear about the currency and payment terms for corporate leases."],
   faq=[("Who rents in Port Harcourt GRA?", "Largely oil and gas professionals, corporate tenants and executives, plus families wanting a central, established area."),
        ("What sells a PH GRA property?", "Security, reliable power backup, parking and a central location close to Aba Road and business hubs.")]),
 "east-legon-accra": dict(name="East Legon", city="Accra", group="International", cur="GH₵", unit="sqm", rent="per month", portals="meQasa, Jiji Ghana or Tonaton",
   subs=["East Legon", "East Legon Hills", "American House", "Shiashie", "Adjiringanor"],
   anchors=["the University of Ghana, Legon", "Kotoka International Airport", "A&C Mall", "Lagos Avenue"],
   perks=["one of Accra's best-known upmarket neighbourhoods", "quick access to the airport", "gated townhouse communities", "popular with diaspora and expatriate buyers"],
   buyers="diaspora Ghanaians, expatriates, professionals and investors",
   title="registered leasehold (Lands Commission)", tag="#EastLegon",
   notes=["Rents in East Legon are often quoted monthly and frequently in US dollars, with one or two years paid in advance. State the currency and advance terms.",
          "Land in Ghana is leasehold. Non-citizens can hold leases of up to 50 years; confirm the lease term and registration with a lawyer.",
          "Name the pocket: East Legon proper, East Legon Hills and Adjiringanor differ in price and access.",
          "Diaspora buyers want verified documents, a reputable developer and video tours."],
   faq=[("Should I quote East Legon rent in cedis or dollars?", "Use what the landlord accepts; many East Legon rentals are quoted in US dollars. State the advance payment period too."),
        ("Can foreigners buy property in East Legon?", "Non-Ghanaians can hold leasehold interests (commonly up to 50 years). Encourage buyers to confirm lease terms and Lands Commission registration with a lawyer.")]),
 "westlands-nairobi": dict(name="Westlands", city="Nairobi", group="International", cur="KSh", unit="sqm", rent="per month", portals="BuyRentKenya, Property24 Kenya or Jiji Kenya",
   subs=["Westlands", "Parklands", "Rhapta Road", "Waiyaki Way corridor"],
   anchors=["Sarit Centre", "Westgate Mall", "Waiyaki Way", "the Nairobi Expressway"],
   perks=["Nairobi's office and nightlife hub", "apartments with gyms, pools and backup generators", "demand from professionals and international staff", "short commutes to major offices"],
   buyers="young professionals, international staff, investors and corporate tenants",
   title="title deed or sectional title", tag="#WestlandsNairobi",
   notes=["Westlands buyers compare amenities: gym, pool, backup generator, borehole and lifts. List them.",
          "Rent is quoted monthly in KSh, with a deposit (often one or two months). State service charge separately.",
          "Mention access to Waiyaki Way and the Nairobi Expressway for commuters.",
          "Investors ask about service charge and sectional title; have both ready."],
   faq=[("What do Westlands tenants look for?", "Modern amenities (gym, pool, backup power, borehole, lifts), security, parking and a short commute."),
        ("Should I mention sectional title?", "Yes, for apartment sales. Buyers and banks increasingly ask whether the unit has a sectional title.")]),
 "dubai-marina": dict(name="Dubai Marina", city="Dubai", group="International", cur="AED", unit="sq ft", rent="per year", portals="Bayut, Property Finder or Dubizzle",
   subs=["Dubai Marina", "Marina Walk", "Marina Promenade", "JBR side"],
   anchors=["the Marina Walk", "JBR beach", "Dubai Marina Mall", "the Dubai Tram and Metro", "Sheikh Zayed Road"],
   perks=["waterfront high-rise living", "freehold ownership open to foreign buyers", "strong holiday-home demand", "beach, dining and transport on the doorstep"],
   buyers="international investors, professionals, holiday-home operators and families",
   title="freehold title deed (Dubai Land Department)", tag="#DubaiMarina",
   notes=["Property ads in Dubai must carry the advertising permit number issued through the regulator's system. Add it before posting.",
          "Use square feet and state the view (full marina, partial sea, community). Views change prices sharply.",
          "Annual rents are often paid by a number of cheques; state how many the landlord accepts.",
          "Holiday homes need a permit from Dubai's tourism authority; don't advertise short stays without one."],
   faq=[("What must a Dubai Marina property ad include?", "Your brokerage details and the advertising permit number required for property ads in Dubai, plus accurate size in square feet, price in AED and the view."),
        ("Can I advertise a Dubai Marina apartment as a holiday home?", "Only if it holds a valid holiday-home permit from Dubai's tourism authority. Check current rules before listing.")]),
}

TYPE_NAMES = {"duplex": "duplex", "apartment": "apartment", "land": "land", "terrace": "terrace duplex", "bungalow": "bungalow", "shortlet": "shortlet apartment"}

PLAN = [("lekki", "duplex"), ("lekki", "apartment"), ("lekki", "land"), ("lekki", "terrace"), ("lekki", "shortlet"),
        ("ikoyi", "duplex"), ("ikoyi", "apartment"), ("ikoyi", "shortlet"),
        ("victoria-island", "apartment"), ("victoria-island", "shortlet"),
        ("ajah", "land"), ("ajah", "duplex"), ("ajah", "terrace"), ("ajah", "bungalow"),
        ("ikeja", "apartment"), ("ikeja", "duplex"), ("ikeja", "bungalow"),
        ("yaba", "apartment"), ("yaba", "shortlet"),
        ("magodo", "duplex"), ("magodo", "bungalow"),
        ("gbagada", "apartment"), ("gbagada", "terrace"),
        ("gwarinpa-abuja", "duplex"), ("gwarinpa-abuja", "terrace"), ("gwarinpa-abuja", "bungalow"),
        ("maitama-abuja", "duplex"), ("maitama-abuja", "apartment"),
        ("wuse-abuja", "apartment"), ("wuse-abuja", "shortlet"),
        ("port-harcourt-gra", "duplex"), ("port-harcourt-gra", "apartment"),
        ("east-legon-accra", "apartment"), ("east-legon-accra", "terrace"),
        ("westlands-nairobi", "apartment"),
        ("dubai-marina", "apartment"), ("dubai-marina", "shortlet")]


def r(lst, i):
    return lst[i % len(lst)]


def templates(t, a, k):
    """Return 10 (label, sub, text) for type t in area a. k varies sub-area/anchor picks per page."""
    N, C, U, P = a["name"], a["cur"], a["unit"], a["price"] if "price" in a else a["cur"] + " ___"
    s1, s2 = r(a["subs"], k), r(a["subs"], k + 1)
    l1, l2 = r(a["anchors"], k), r(a["anchors"], k + 1)
    p1, p2, p3 = r(a["perks"], k), r(a["perks"], k + 1), r(a["perks"], k + 2)
    ti, tag, city = a["title"], a["tag"], a["city"]
    citytag = "#" + city.replace(" ", "") + "RealEstate"
    intl = a["group"] == "International"
    sale_note = "" if intl else f"\n📄 Title: [{ti}]"
    if t == "duplex":
        label = "townhouse" if a["name"] == "East Legon" else "duplex"
        base = [
         ("Portal description (full)", a["portals"], f"[4]-Bedroom [Fully Detached] {label.title()} with BQ in {s1}, {N}\n\nSet on a [500] {U} plot in {s1}, this [4]-bedroom {label} offers {p1} and {p2}. The ground floor has a [spacious living room, guest toilet, dining area and fitted kitchen with pantry]. Upstairs are [four en suite bedrooms], including a master suite with [walk-in closet and private balcony].\n\nFeatures: [BQ / staff room], [parking for 4 cars], [water treatment], [inverter-ready wiring], [CCTV].\nLocation: [about X minutes] from {l1} off-peak.\nTitle: [{ti}].\nPrice: {P}\n\nInspection by appointment: [Phone]."),
         ("Short listing (Jiji / classifieds)", "Under 60 words", f"Newly built [4]-bed {label} + BQ, {s1}, {N}. All rooms en suite, [fitted kitchen], [ample parking], [gated estate]. Near {l1}. Title: [{ti}]. {P}. Call/WhatsApp [Phone]."),
         ("Flyer copy", "Headline + 4 bullets", f"FOR SALE · {s1.upper()}\n[4]-Bedroom {label.title()} + BQ\n• [All rooms en suite]\n• [Fitted kitchen & pantry]\n• [Gated, 24h security]\n• Near {l1}\n{P} · [Phone]"),
         ("WhatsApp broadcast", "For your buyer list", f"🏡 *[4]-BED {label.upper()} – {s1}, {N}*\n✅ [All rooms en suite + BQ]\n✅ [{p1}]\n✅ [Parking for 4]{sale_note}\n💰 {P}\nReply *VIEW* for the video tour."),
         ("Instagram caption", "With local hashtags", f"Room to grow in {s1} 🏡\n[4]-bed {label} with BQ, [fitted kitchen] and [private garden].\n{p1.capitalize()}, close to {l1}.\n💰 {P}\n📲 [Phone]\n\n{tag} {citytag} #{label.title()}ForSale"),
         ("Family angle", "For buyers with children", f"Designed for family life in {N}: [four] en suite bedrooms so everyone has their own space, a [family lounge upstairs], and a compound big enough for [the kids to play safely]. [Schools and shops nearby]. {s1}. {P}."),
         ("Investor angle", "Resale / rental pitch", f"For investors: a [4]-bed {label} in {s1}, an area with demand from {a['buyers']}. Comparable homes nearby rent for about {C} ___ {a['rent']} [source your comps]. Asking {P}. Title: [{ti}]."),
         ("Diaspora buyer version", "For clients abroad", f"Buying in {N} from abroad? This [4]-bed {label} in {s1} can be viewed by live video, documents ([{ti}]) can go to your lawyer, and payment is to [company account] only. {P} (approx. $___ at today's rate)."),
         ("Headline options", "For portals and ads", f"1. [4]-Bed {label.title()} with BQ in {s1}, {N}\n2. Newly Built {label.title()} Near {l2.replace('the ', '').title() if l2.startswith('the ') else l2}\n3. Family Home in {s2} with [Pool] and BQ\n4. [Fully Detached] {label.title()}, [{ti}], {N}"),
         ("30-second video tour script", "Film on your phone", f"[0–3s] Front gate opens: \"This is the [4]-bed {label} everyone in {s1} will be asking about.\"\n[3–10s] Living room pan: \"[Double-height] lounge and [guest toilet].\"\n[10–17s] Kitchen: \"[Fitted kitchen with pantry].\"\n[17–25s] Master suite + balcony: \"[Walk-in closet], [private balcony].\"\n[25–30s] To camera: \"{P}. Near {l1}. WhatsApp [Phone] to book a viewing.\""),
        ]
        return base
    if t == "apartment":
        dub = a["name"] == "Dubai Marina"
        permit = "\nPermit No.: [______]" if dub else ""
        view = "[full marina view]" if dub else "[balcony with city views]"
        svc = "[service charge AED ___ per sq ft]" if dub else f"[service charge {C} ___]"
        return [
         ("Portal description (full)", a["portals"], f"[3]-Bedroom [Serviced] Apartment in {s1}, {N}\n\nA [bright, well-finished] [3]-bedroom apartment on the [4th] floor with {view}. Open-plan living and dining, [fitted kitchen], [all rooms en suite] and a [guest toilet].\n\nBuilding: [elevator], [gym], [pool], [24h security], [backup power], [dedicated parking].\nLocation: {p1}, close to {l1}.\n{'Tenure: ' + ti + '.' if dub or intl else 'Title: [' + ti + '].'}\nPrice: {P} [or {C} ___ {a['rent']}]. {svc}.{permit}\n\nViewing: [Phone]."),
         ("Short listing", "Under 60 words", f"[3]-bed apartment, {s1}, {N}. [{'Size ___ sq ft' if dub else 'All rooms en suite'}], [elevator, gym, backup power], [parking]. Near {l1}. {P}{' / year' if dub else ''}. {svc}. Call [Phone].{permit}"),
         ("Flyer copy", "Headline + bullets", f"{'FOR SALE / TO LET'} · {N.upper()}\n[3]-Bed Apartment, [4th] Floor\n• {view}\n• [Gym · Pool · Lift]\n• [24h security & backup power]\n• {p1.capitalize()}\n{P} · [Phone]{permit}"),
         ("WhatsApp broadcast", "For buyers or tenants", f"🏢 *[3]-BED APARTMENT – {s1}, {N}*\n✅ {view}\n✅ [Lift · gym · pool]\n✅ [Backup power]\n💰 {P} [{a['rent']}]\nReply *VIEW* to book a viewing."),
         ("Instagram caption", "With hashtags", f"Lock-up-and-go living in {s1} ✨\n[3]-bed apartment, {view}, [gym & pool].\n{p2.capitalize()}.\n💰 {P}\n📲 [Phone]\n\n{tag} {citytag} #ApartmentFor{'Sale' if not intl else 'Rent'}"),
         ("Tenant angle", "For long-let renters", f"Move-in ready in {N}: [3] bedrooms, [fitted kitchen], [backup power and water], with {p1}. Rent {C} ___ {a['rent']}{', ' + svc if not dub else ''}. Ideal for {a['buyers'].split(',')[0]}."),
         ("Investor angle", "Yield pitch", f"Buy-to-let in {s1}: demand comes from {a['buyers']}. Similar units rent for about {C} ___ {a['rent']} [use your comps]. Asking {P}. {svc.strip('[]').capitalize()}.{permit}"),
         ("Corporate let version", "For HR / relocation managers", f"Executive [3]-bedroom apartment, {s1}, {N}, available for corporate lease from [date]. [Fully furnished option], [24h security], [backup power], [parking for 2], [facility management on site]. Minimum term [12 months]. Rent {C} ___ {a['rent']}."),
         ("Headline options", "For portals", f"1. [3]-Bed Apartment with {view.strip('[]').title()}, {s1}\n2. Serviced [3]-Bed in {N} with [Gym & Pool]\n3. Move-In Ready Apartment Near {l1.replace('the ', '')}\n4. [Furnished] [3]-Bed, {s2}, {N}"),
         ("30-second video tour script", "Film on your phone", f"[0–3s] Lobby or lift: \"Come up to the [4th] floor with me in {s1}.\"\n[3–10s] Living room to balcony: \"{view.strip('[]').capitalize()}.\"\n[10–17s] Kitchen: \"[Fitted kitchen], [appliances included].\"\n[17–25s] Bedrooms: \"[3] en suite bedrooms.\"\n[25–30s] Gym/pool shot, voice-over: \"{P}. WhatsApp [Phone].\"{' Permit [______] on screen.' if dub else ''}"),
        ]
    if t == "land":
        return [
         ("Portal description (full)", a["portals"], f"[1 Plot] ([600] sqm) of [Dry] Land for Sale in {s1}, {N}\n\n[Dry, fenced] plot in [estate name], {s1}, with [tarred access road] and [good drainage]. Suitable for [residential development]. {p1.capitalize()}, close to {l1}.\n\nTitle: [{ti} – state exactly].\nSurvey: [Registered survey plan available].\nPrice: {P} per plot. [Payment plan: __% deposit, balance over __ months.]\n\nFree site inspection every [Saturday]. Documents available for your lawyer to verify. Call [Phone]."),
         ("Short listing", "Classifieds", f"Land for sale: [600] sqm, [estate], {s1}, {N}. [Dry, fenced], [tarred road]. Title: [{ti}]. {P}/plot. [Payment plan]. Site inspection: [Phone]."),
         ("Flyer copy", "Estate land flyer", f"LAND FOR SALE · {s1.upper()}\n[Estate name]\n• [600] sqm plots\n• Title: [{ti}]\n• [Gated, perimeter fence]\n• Near {l1}\nFrom {P} · Pay [30%] and spread the rest\n[Phone]"),
         ("WhatsApp broadcast", "For land buyers", f"🌍 *LAND – {s1}, {N}*\n📐 [600] sqm\n📄 [{ti}]\n🛣 [Tarred access off {l1.replace('the ', '')}]\n💰 {P}/plot · [payment plan]\nReply *SEAT* for Saturday's free inspection."),
         ("Instagram caption", "With hashtags", f"Your future address in {s1} starts here 🌱\n[600] sqm plots at [estate], [{ti}].\n{p3.capitalize()}.\n💰 {P}/plot\n📲 [Phone]\n\n#LandForSale {tag} #{city.replace(' ', '')}Land"),
         ("Builder angle", "For people ready to build", f"Ready-to-build plot in {s1}: [dry land, no sand-filling needed], [corner piece], [estate approval for duplex/terrace]. Survey and title ([{ti}]) available for review. {P}."),
         ("Land banker angle", "Buy and hold", f"For land bankers: {s1} offers {p3}. [600] sqm plot with [{ti}], {P}. Prices in the area have [moved since ___ — cite your source or leave out]. Documents ready for verification."),
         ("Commercial frontage version", "Roadside land", f"[1,200] sqm frontage land on [road], {N}. Suitable for [plaza, filling station or warehouse, subject to approval]. Title: [{ti}]. {P}. Serious enquiries: [Phone]."),
         ("Verification-first version", "Builds trust", f"Before you pay for any land in {N}, verify. For this [600] sqm plot in {s1} we provide: [title: {ti}], [registered survey], [receipt and deed of assignment drafts], and a site visit. Payment to [company account] only. {P}."),
         ("Site inspection video script", "30 seconds", f"[0–3s] Drone/wide shot: \"This is [estate], {s1}.\"\n[3–10s] Walk the access road: \"[Tarred road] straight in from {l1.replace('the ', '')}.\"\n[10–20s] Stand on the plot: \"[600] sqm, [dry], [beacons in place].\"\n[20–26s] Show documents (blur personal data): \"[{ti}].\"\n[26–30s] \"{P} per plot. Free inspection Saturday. WhatsApp [Phone].\""),
        ]
    if t == "terrace":
        label = "townhouse" if a["name"] == "East Legon" else "terrace duplex"
        return [
         ("Portal description (full)", a["portals"], f"[4]-Bedroom {label.title()} in {s1}, {N}\n\nPart of a [gated development of 8 units] in {s1}, this [4]-bedroom {label} is [newly built] with [all rooms en suite], a [family lounge], [fitted kitchen] and a [room for a helper]. Shared [perimeter fence, 24h security and good internal roads]. {p1.capitalize()}, near {l1}.\n\n{'Tenure: ' + ti + '.' if intl else 'Title: [' + ti + '].'}\nPrice: {P}. [Off-plan payment plan available.]\n\nInspection: [Phone]."),
         ("Short listing", "Classifieds", f"Newly built [4]-bed {label}, {s1}, {N}. [All rooms en suite], [family lounge], [gated, 24h security]. Near {l1}. {P}. Call [Phone]."),
         ("Flyer copy", "Development flyer", f"[DEVELOPMENT NAME] · {s1.upper()}\n[4]-Bed {label.title()}s\n• [8 units only]\n• [All rooms en suite + family lounge]\n• [Gated, 24h security]\n• {p2.capitalize()}\nFrom {P} · [Phone]"),
         ("WhatsApp broadcast", "Buyer list", f"🏘 *[4]-BED {label.upper()} – {s1}*\n✅ [Gated, 8 units]\n✅ [All rooms en suite]\n✅ [{p1}]\n💰 {P} [· payment plan]\nReply *VIEW* to book an inspection."),
         ("Instagram caption", "Hashtags", f"Modern {label} living in {s1} 🏘\n[4] beds, [family lounge], [gated with 24h security].\n{p1.capitalize()}.\n💰 {P}\n📲 [Phone]\n\n{tag} {citytag} #NewHomes"),
         ("First-time buyer angle", "Value pitch", f"A {label} gives you a full family home in {N} for less than a detached house. [4] bedrooms, [shared security and maintenance], {p2}. {P}{' with a payment plan' if not intl else ''}."),
         ("Off-plan version", "If units are under construction", f"Off-plan: [4]-bed {label}s at [development], {s1}. [Deposit __%], balance over [__ months]. Completion [quarter, year]. Built by [developer]. From {P}."),
         ("Investor angle", "Rental pitch", f"{label.title()}s in {N} attract {a['buyers']}. Comparable units rent for about {C} ___ {a['rent']} [your comps]. {P}."),
         ("Headline options", "Portals", f"1. Newly Built [4]-Bed {label.title()} in {s1}\n2. Gated {label.title()} Near {l1.replace('the ', '')}\n3. [4]-Bed {label.title()} with Family Lounge, {N}\n4. Off-Plan {label.title()}s in {s2} – Payment Plan"),
         ("30-second video tour script", "Phone video", f"[0–3s] Gate and row of units: \"[8] {label}s, one gate, {s1}.\"\n[3–12s] Living + kitchen: \"[Open plan], [fitted kitchen].\"\n[12–22s] Upstairs: \"[Family lounge] and [4 en suite bedrooms].\"\n[22–30s] Outside: \"{P}. Near {l1}. WhatsApp [Phone].\""),
        ]
    if t == "bungalow":
        return [
         ("Portal description (full)", a["portals"], f"[3]-Bedroom [Detached] Bungalow in {s1}, {N}\n\nEverything on one level: [3 bedrooms (2 en suite)], a [spacious living and dining room], [fitted kitchen] and a [guest toilet], on a [compound with space for 4 cars]. [Room to extend upward — structure built to carry a second floor, if true].\n\nLocation: {p1}, close to {l1}.\nTitle: [{ti}].\nPrice: {P}.\n\nInspection: [Phone]."),
         ("Short listing", "Classifieds", f"[3]-bed detached bungalow, {s1}, {N}. [2 en suite], [big compound], [fenced and gated]. Near {l1}. Title: [{ti}]. {P}. [Phone]."),
         ("Flyer copy", "Bullets", f"FOR SALE · {s1.upper()}\n[3]-Bedroom Bungalow\n• Everything on one floor\n• [Large compound, parking for 4]\n• [Fenced & gated]\n• Title: [{ti}]\n{P} · [Phone]"),
         ("WhatsApp broadcast", "Buyer list", f"🏠 *[3]-BED BUNGALOW – {s1}, {N}*\n✅ [All on one level]\n✅ [Big compound]\n✅ [{ti}]\n💰 {P}\nReply *VIEW* for photos and video."),
         ("Instagram caption", "Hashtags", f"No stairs, no stress 🏠\n[3]-bed bungalow in {s1} with [a big compound] and [{ti}].\n{p2.capitalize()}.\n💰 {P}\n📲 [Phone]\n\n{tag} {citytag} #BungalowForSale"),
         ("Retirees & parents angle", "Accessibility pitch", f"A bungalow suits [parents, retirees or anyone avoiding stairs]: every room is on the ground floor, with [wide doorways] and [a short walk from parking to the front door]. {s1}, {N}. {P}."),
         ("Upgrade/extend angle", "For builders", f"Buy now, build up later: this [3]-bed bungalow in {s1} sits on a [600] {U} plot with [foundation/structure for a second floor — confirm with the seller]. {P}."),
         ("Rental version", "Long let", f"TO LET: [3]-bed bungalow, {s1}, {N}. [Fenced compound], [parking], [prepaid meter], [borehole]. Rent {C} ___ {a['rent']}. Inspection: [Phone]."),
         ("Headline options", "Portals", f"1. [3]-Bed Detached Bungalow in {s1}, {N}\n2. Bungalow with Big Compound Near {l1.replace('the ', '')}\n3. One-Level Family Home, [{ti}], {N}\n4. [3]-Bed Bungalow with Room to Extend, {s2}"),
         ("30-second video tour script", "Phone video", f"[0–4s] Gate to compound: \"Space, parking, and everything on one floor — {s1}.\"\n[4–14s] Living + kitchen.\n[14–24s] Bedrooms: \"[3] bedrooms, [2 en suite].\"\n[24–30s] Compound wide shot: \"{P}. [{ti}]. WhatsApp [Phone].\""),
        ]
    if t == "shortlet":
        dub = a["name"] == "Dubai Marina"
        permit = "\nHoliday home permit: [______]" if dub else ""
        night = f"{C} ___/night"
        power = "" if intl else "⚡ 24/7 power · "
        return [
         ("Airbnb / Booking.com description", "Full listing", f"[Stylish] [2]-Bedroom {'Holiday Home' if dub else 'Shortlet'} in {s1}, {N}\n\nStay in {s1}, with {p1}. The apartment has [2 en suite bedrooms], [an open-plan lounge with smart TV and Netflix], a [fully equipped kitchen] and [a balcony].\n\nAmenities: {'' if intl else '[24/7 power], '}[fast Wi-Fi], [air conditioning in every room], [pool and gym access], [secure parking], [24h security].\nNearby: {l1} and {l2}.\nHouse rules: [no parties], [max 4 guests], [check-in 2pm / check-out 12pm]{'' if dub else ', [refundable caution deposit]'}.{permit}"),
         ("Short listing", "For Instagram bio links / directories", f"[2]-bed {'holiday home' if dub else 'shortlet'} in {s1}, {N}. {'' if intl else '24/7 power, '}[fast Wi-Fi], [pool], [secure parking]. From {night}.{permit}"),
         ("Flyer / story card", "Square graphic", f"STAY IN {s1.upper()}\n[2]-Bed {'Holiday Home' if dub else 'Luxury Shortlet'}\n• {power}[Wi-Fi]\n• [Pool & gym]\n• Near {l1}\nFrom {night} · Book: [Phone]"),
         ("WhatsApp availability reply", "Quick reply", f"Hi! 👋 Our [2]-bed in {s1} is free [Fri–Sun].\n💰 {night}{'' if dub else ' · caution ' + C + ' ___ (refundable)'}\n{power}📶 Wi-Fi · 🏊 Pool\nShall I reserve it for you?"),
         ("Instagram caption", "Hashtags", f"Your {N} weekend, sorted 🌙\n[2]-bed {'holiday home' if dub else 'shortlet'}, [pool], [city views], {p1}.\nFrom {night}\n📲 [Phone]\n\n{tag} #{city.replace(' ', '')}Shortlet #Staycation"),
         ("Business traveller version", "Weekday stays", f"In {city} for work? Our {s1} apartment has a [proper desk], [fast Wi-Fi]{'' if intl else ', [24/7 power]'} and [daily cleaning on request], close to {l1}. Weekly rates available. From {night}."),
         ("Group/celebration version", "Birthdays, visiting family", f"Bringing the family to {N}? [3]-bed {'holiday home' if dub else 'shortlet'} in {s1}, sleeps [6], [big lounge], [pool]. [No parties; small gatherings by arrangement]. From {night}."),
         ("Long-stay version", "Monthly guests", f"Staying a month or more in {city}? Our {s1} apartment offers [monthly rates], [fast Wi-Fi], [washing machine] and [weekly cleaning]. Ask for the long-stay price."),
         ("Headline options", "Listing titles", f"1. [Stylish] 2-Bed in {s1} with Pool\n2. {'' if intl else '24/7 Power, '}Fast Wi-Fi & Pool – {N}\n3. [Cosy] {'Holiday Home' if dub else 'Shortlet'} Near {l1.replace('the ', '').title() if l1.startswith('the ') else l1}\n4. Work-Ready 2-Bed Apartment in {s2}"),
         ("30-second video tour script", "Night-time reel", f"[0–3s] Door opens, warm lights: \"Welcome to your {s1} stay.\"\n[3–12s] Lounge + TV: \"[Netflix], [smart TV], [fast Wi-Fi].\"\n[12–20s] Bedroom: \"[2 en suite bedrooms].\"\n[20–26s] Pool or balcony view.\n[26–30s] \"From {night}. Book on WhatsApp [Phone].\"{' Permit [______] on screen.' if dub else ''}"),
        ]
    raise ValueError(t)


TYPE_INTRO = {
 "duplex": "A duplex listing has to sell space and status at the same time: room count, the BQ, parking and the finish level, all in the first lines a buyer sees.",
 "apartment": "Apartment buyers and tenants compare buildings as much as units, so the lift, power, security, parking and service charge belong in the description alongside the bedrooms.",
 "land": "Land descriptions win on trust and clarity: exact size, exact title, exact access, and an open invitation to verify before paying.",
 "terrace": "Terraces and townhouses sit between apartments and detached homes. The pitch is a full family home with shared security, at a lower price than detached.",
 "bungalow": "Bungalows sell to people who want everything on one level, a bigger compound, or a base to build on later. Say which of those this one is.",
 "shortlet": "Short-stay guests book on photos, amenities and trust. A good description answers the questions guests would otherwise message about: power, Wi-Fi, security, rules and check-in.",
}
TYPE_TIPS = {
 "duplex": ["Say fully detached, semi-detached or terrace in the first line; buyers filter on it.", "List bedroom count, en suites, BQ and parking before finishes.", "Use real measurements: plot size and, if known, built-up area."],
 "apartment": ["Give the floor level and whether there's a lift.", "State the service charge separately from the rent or price.", "Name the building's amenities: gym, pool, power backup, security, parking."],
 "land": ["Give size in square metres, not just \"plots\".", "Name the exact title document and stage; never write \"good title\" alone.", "Offer verification and site inspections before payment."],
 "terrace": ["Say how many units share the compound.", "Mention who manages shared areas and any estate dues.", "If off-plan, state the payment plan and completion date."],
 "bungalow": ["Highlight one-level living for older buyers and families with young children.", "Give the compound size and parking.", "Only mention extension potential if the structure genuinely supports it."],
 "shortlet": ["Only list amenities that work every night.", "Put house rules and the caution deposit in the description.", "Use night-time and golden-hour photos; shortlet guests buy the mood."],
}
TYPE_FAQ = {
 "duplex": ("What should a duplex listing description include?", "Bedroom count, en suites, BQ, parking, plot size, finishing, the exact location or estate, title document and price."),
 "apartment": ("What should an apartment description include?", "Bedrooms, floor level, lift, building amenities, power and water arrangements, parking, service charge and price or rent."),
 "land": ("What should a land description include?", "Size in square metres, exact location and access road, title document and stage, survey status, price per plot and any payment plan."),
 "terrace": ("What is the difference between a terrace and a duplex listing?", "A terrace duplex shares walls with neighbouring units in a row; say how many units share the compound and what's shared."),
 "bungalow": ("Who buys bungalows?", "Older buyers, families with young children, people who want a bigger compound and buyers planning to build up later."),
 "shortlet": ("What makes a shortlet description convert?", "Clear photos, honest amenities (especially power and Wi-Fi), house rules, a 'from' nightly rate and a fast way to book."),
}


def pages():
    out = []
    for k, (ak, t) in enumerate(PLAN):
        a = AREAS[ak]
        tn = TYPE_NAMES[t]
        disp_t = "townhouse" if (a["name"] == "East Legon" and t == "terrace") else ("holiday home" if (a["name"] == "Dubai Marina" and t == "shortlet") else tn)
        loc = a["name"] if a["name"] in (a["city"],) or a["city"] in a["name"] else f"{a['name']}, {a['city']}"
        slug = f"{t}-in-{ak}"
        h1 = f"{disp_t.capitalize()} listing descriptions for {loc}"
        title = f"{disp_t.title()} in {a['name']} — Listing Description Templates"
        if len(title) < 52:
            title += " | ListingKit"
        meta = (f"Copy-ready {disp_t} description templates for {loc}: portal listing, flyer, WhatsApp, Instagram and a 30-second video script, "
                f"with local detail and {a['cur']} price placeholders.")
        if len(meta) > 165:
            meta = f"Free {disp_t} description templates for {loc}: portal, flyer, WhatsApp, Instagram and video script, with local detail and {a['cur']} placeholders."
        intro = [TYPE_INTRO[t],
                 f"In {a['name']}, your audience is mostly {a['buyers']}. The selling points that come up again and again are {a['perks'][0]}, {a['perks'][1]} and {a['perks'][2]}. "
                 f"Prices below are left blank ({a['cur']} ___) on purpose: use the seller's real figure and verified comparables, never a guess."]
        notes_html = "<ol class=\"tips\">" + "".join(f"<li>{n}</li>" for n in a["notes"]) + "</ol>"
        same_area = [f"/descriptions/{tt}-in-{ak}/" for aa, tt in PLAN if aa == ak and tt != t]
        same_type = [f"/descriptions/{t}-in-{aa}/" for aa, tt in PLAN if tt == t and aa != ak][:3]
        cap = {"land": "/captions/land-for-sale/", "shortlet": "/captions/shortlet/"}.get(t, "/captions/just-listed/")
        wa = {"land": "/whatsapp/land/", "shortlet": "/whatsapp/rent-shortlet/"}.get(t, "/whatsapp/new-listing/")
        htag = {"Lagos": "/hashtags/lagos/", "Abuja": "/hashtags/abuja/", "Port Harcourt": "/hashtags/port-harcourt/", "Accra": "/hashtags/accra/", "Nairobi": "/hashtags/nairobi/", "Dubai": "/hashtags/dubai/"}[a["city"]]
        out.append(dict(path=f"/descriptions/{slug}/", section="descriptions", city_group=a["group"],
                        crumb=f"{disp_t.capitalize()} in {a['name']}", title=title, meta=meta, h1=h1,
                        eyebrow=f"Property descriptions · {a['city']}",
                        lede=f"Ten ready-to-edit versions for one {disp_t} in {a['name']}: the full portal listing, a short classified, flyer copy, WhatsApp, Instagram, three buyer angles, headlines and a video script.",
                        intro=intro, groups=[("", templates(t, a, k))], groups_title=f"{disp_t.capitalize()} description templates for {a['name']}",
                        extra_html=[("local", f"Writing for {a['name']} buyers", notes_html)],
                        tips=TYPE_TIPS[t] + ["Paste the finished description into the free generator to get matching captions and a WhatsApp broadcast."],
                        tips_title=f"Getting the {disp_t} details right",
                        faq=[TYPE_FAQ[t]] + a["faq"] + [("Can ListingKit write this for my listing?", f"Yes. Enter the property type, {a['name']} location, price and features in the free generator and it writes the description, captions, WhatsApp message and video script together.")],
                        related=same_area + same_type + [cap, wa, htag],
                        blurb=f"{a['city']} · {a['buyers'].split(',')[0].capitalize()} and more"))
    return out
