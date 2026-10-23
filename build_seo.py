#!/usr/bin/env python3
"""Generate ListingKit programmatic SEO pages into deploy/site/.

Usage:  python3 deploy/build_seo.py          # build pages, sitemap.xml, robots.txt
        python3 deploy/build_seo.py --check  # build, then validate links/titles/HTML

Content lives in deploy/seo_content/*.py. Each module exposes pages() -> list of
page dicts (see PAGE FIELDS below). Hub pages are generated here from sections.
"""
import html, json, os, re, sys, datetime
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "site")
BASE = "https://listingkit-ai.netlify.app"
sys.path.insert(0, HERE)

from seo_content import captions, whatsapp, descriptions, hashtags, guides, alternatives  # noqa: E402

WA = "https://wa.me/2349133227445?text=" + "Hi%20ListingKit%2C%20I%27m%20an%20agent%20and%20I%27d%20like%20early%20access.%20My%20name%3A%20%20City%3A%20"
MAIL = "mailto:anyanwudiamond@gmail.com?subject=ListingKit%20early%20access&amp;body=Name%3A%0ACity%3A%0AHow%20many%20listings%20do%20you%20post%20a%20month%3F"
TODAY = datetime.date.today().isoformat()

E = html.escape

# PAGE FIELDS
# path: "/captions/just-listed/"   title, meta, h1, eyebrow, lede, intro [paras]
# groups: [(heading, [(label, sublabel, text)])]   examples (copy blocks)
# extra_html: raw html sections inserted after examples (list of (id, nav, heading, html))
# tips_title, tips [str]  faq [(q, a)]  related [paths]  section (key)

SECTIONS = {
    "captions": ("Real estate captions", "/captions/", "Ready-to-copy Instagram, TikTok and WhatsApp status captions for every listing moment."),
    "whatsapp": ("WhatsApp broadcast templates", "/whatsapp/", "Broadcast and follow-up messages for real estate agents who sell on WhatsApp."),
    "descriptions": ("Property descriptions by area", "/descriptions/", "Listing description templates for specific property types and neighbourhoods."),
    "hashtags": ("Real estate hashtags by city", "/hashtags/", "Grouped hashtag sets for Lagos, Abuja, Port Harcourt, Accra, Nairobi, Dubai and London."),
    "guides": ("Guides for agents", "/guides/", "Practical how-tos: advertising land, ChatGPT prompts and video script ideas."),
    "alternatives": ("Tool alternatives", "/alternatives/", "Honest comparisons with PropClips, ListingAI and Canva for realtors."),
}


def head(p):
    url = BASE + p["path"]
    t, d = E(p["title"]), E(p["meta"])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="ListingKit">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/listingkit-hero.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{t}">
<meta name="twitter:description" content="{d}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="/hark.css">
<link rel="stylesheet" href="/seo.css">
"""


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace("</", "<\\/") + "</script>\n"


def crumbs_for(p):
    c = [("Home", "/"), ("Free templates", "/resources/")]
    sec = p.get("section")
    if sec and p["path"] != SECTIONS[sec][1]:
        c.append((SECTIONS[sec][0], SECTIONS[sec][1]))
    if p["path"] != "/resources/":
        c.append((p.get("crumb") or p["h1"], p["path"]))
    return c


def cta_block(lead=None):
    lead = lead or "Paste your property details and get the caption, WhatsApp broadcast, flyer copy and video script in one go."
    return f"""<aside class="callout callout--wide" aria-label="Try ListingKit">
<p class="callout__head">Skip the copy-paste</p>
<p class="callout__lead"><strong>{E(lead)}</strong> Free for 3 listings a month. The first 100 agents get 3 months of Pro free.</p>
<div class="links"><a class="btn" href="/generator/">Try the free generator</a><a class="btn" href="{WA}" target="_blank" rel="noopener">Join the waitlist on WhatsApp</a><a class="btn" href="{MAIL}">Join by email</a></div>
</aside>"""


def render(p, registry):
    out = [head(p)]
    if p.get("faq"):
        out.append(jsonld({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}))
    cr = crumbs_for(p)
    out.append(jsonld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": BASE + u} for i, (n, u) in enumerate(cr)]}))
    out.append("</head>\n<body>\n<div class=\"page\" id=\"top\">\n")
    out.append('<header class="topbar glass"><nav class="seg" aria-label="Site"><a class="brand" href="/">ListingKit</a><a href="/generator/">Free generator</a><a href="/resources/">Free templates</a></nav></header>\n')
    out.append('<main class="main">\n<ol class="crumbs" aria-label="Breadcrumb">' + "".join(
        f'<li><a href="{u}">{E(n)}</a></li>' if i < len(cr) - 1 else f'<li aria-current="page">{E(n)}</li>' for i, (n, u) in enumerate(cr)) + "</ol>\n")
    out.append(f'<section class="intro"><p class="intro__eyebrow">{E(p.get("eyebrow", ""))}</p><h1>{E(p["h1"])}</h1>')
    if p.get("lede"):
        out.append(f'<p class="lede">{E(p["lede"])}</p>')
    if p.get("intro"):
        out.append('<div class="prose">' + "".join(f"<p>{x}</p>" for x in p["intro"]) + "</div>")
    out.append('<div class="links"><a class="btn" href="/generator/">Try the free generator</a><a class="btn" href="#templates">Jump to templates</a></div></section>\n')

    if p.get("groups"):
        out.append(f'<section class="section" id="templates"><div class="head"><p class="head__eyebrow">Copy and adapt</p><h2>{E(p.get("groups_title", "Ready-to-copy templates"))}</h2></div><div>')
        n = 0
        for gh, items in p["groups"]:
            if gh:
                out.append(f'<h3 class="group-title">{E(gh)}</h3>')
            out.append('<div class="tpls">')
            for label, sub, text in items:
                n += 1
                out.append(f'<div class="tpl"><h3>{E(label)}' + (f"<small>{E(sub)}</small>" if sub else "") +
                           f'</h3><pre id="t{n}">{E(text.strip())}</pre><button class="btn copy" type="button" data-copy="t{n}">Copy</button></div>')
            out.append("</div>")
        out.append("</div></section>\n")
    for sid, heading, raw in p.get("extra_html", []):
        out.append(f'<section class="section" id="{sid}"><div class="head"><h2>{E(heading)}</h2></div>{raw}</section>\n')
    if p.get("tips"):
        out.append(f'<section class="section" id="tips"><div class="head"><p class="head__eyebrow">How to use them</p><h2>{E(p.get("tips_title", "Tips that get more enquiries"))}</h2></div><ol class="tips">' +
                   "".join(f"<li>{t}</li>" for t in p["tips"]) + "</ol></section>\n")
    out.append(f'<section class="section" id="cta">{cta_block(p.get("cta"))}</section>\n')
    if p.get("faq"):
        out.append('<section class="section" id="faq"><div class="head"><p class="head__eyebrow">FAQ</p><h2>Questions agents ask</h2></div><div class="faq">' +
                   "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in p["faq"]) + "</div></section>\n")
    rel = [r for r in p.get("related", []) if r != p["path"] and r in registry]
    if rel:
        out.append('<section class="section" id="related"><div class="head"><h2>Related templates</h2></div><ul class="related">' +
                   "".join(f'<li><a href="{r}">{E(registry[r].get("crumb") or registry[r]["h1"])}</a></li>' for r in rel) + "</ul></section>\n")
    out.append(f"""</main>
<footer class="foot">
<p>ListingKit — built in Lagos for agents everywhere. Contact: <a class="link" href="mailto:anyanwudiamond@gmail.com">anyanwudiamond@gmail.com</a> · WhatsApp <a class="link" href="https://wa.me/2349133227445" target="_blank" rel="noopener">+234 913 322 7445</a></p>
<nav aria-label="Site links"><a href="/">Home</a><a href="/generator/">Generator</a><a href="/resources/">Free templates</a><a href="/captions/">Captions</a><a href="/whatsapp/">WhatsApp</a><a href="/descriptions/">Descriptions</a><a href="/hashtags/">Hashtags</a><a href="/guides/">Guides</a><a href="/alternatives/">Alternatives</a></nav>
</footer>
</div>
<script>document.addEventListener("click",function(e){{var b=e.target.closest("[data-copy]");if(!b)return;var t=document.getElementById(b.getAttribute("data-copy")).textContent;function ok(){{b.textContent="Copied";setTimeout(function(){{b.textContent="Copy"}},1500)}}if(navigator.clipboard)navigator.clipboard.writeText(t).then(ok);else{{var a=document.createElement("textarea");a.value=t;document.body.appendChild(a);a.select();document.execCommand("copy");a.remove();ok()}}}});</script>
</body>
</html>
""")
    return "".join(out)


def hub_list(items, registry):
    return '<ul class="hub-list">' + "".join(
        f'<li><a href="{r}"><strong>{E(registry[r].get("crumb") or registry[r]["h1"])}</strong><span>{E(registry[r].get("blurb") or registry[r]["meta"][:110])}</span></a></li>' for r in items) + "</ul>"


def build_hubs(pages, registry):
    hubs = []
    hub_meta = {
        "captions": dict(title="Real Estate Captions for Instagram, TikTok & WhatsApp | ListingKit",
                         meta="Free real estate caption templates for just listed, sold, open house, price reduced, land, off-plan, shortlet, luxury, rental and commercial listings.",
                         h1="Real estate captions for every listing moment", lede="Pick the moment, copy the caption, swap in your details. Every page has Instagram, TikTok and WhatsApp status versions."),
        "whatsapp": dict(title="WhatsApp Broadcast Messages for Real Estate Agents (Templates) | ListingKit",
                         meta="Free WhatsApp broadcast templates for realtors: new listing, land, off-plan launch, inspection invite, price drop, follow-up and rent/shortlet messages.",
                         h1="WhatsApp broadcast templates for real estate", lede="Most African agents close on WhatsApp, not Instagram. These are broadcast-list messages built to get replies, not blue ticks."),
        "descriptions": dict(title="Property Listing Descriptions: Lagos, Abuja, PH, Accra, Nairobi, Dubai",
                             meta="Property description templates for duplexes, flats, land, terraces, bungalows, shortlets in Lekki, Ikoyi, VI, Ajah, Ikeja, Abuja, Port Harcourt, Accra, Nairobi and Dubai.",
                             h1="Property description templates by area", lede="Area-specific listing descriptions for portals, flyers and WhatsApp. Fill the blanks, keep the local detail buyers search for."),
        "hashtags": dict(title="Real Estate Hashtags — Lagos, Abuja, Accra, Nairobi, Dubai | ListingKit",
                         meta="Copy-ready real estate hashtag sets grouped by city and listing type for Lagos, Abuja, Port Harcourt, Accra, Nairobi, Dubai and London agents.",
                         h1="Real estate hashtags by city", lede="Grouped sets you can paste under a post: broad, area, property type and buyer intent."),
        "guides": dict(title="Real Estate Marketing Guides for Agents in Nigeria & Beyond | ListingKit",
                       meta="Practical guides for agents: how to advertise land for sale in Nigeria, ChatGPT prompts for real estate, and TikTok/reel script ideas.",
                       h1="Marketing guides for real estate agents", lede="Short, practical playbooks with templates you can use today."),
        "alternatives": dict(title="ListingKit vs PropClips, ListingAI & Canva | Real Estate Tools",
                             meta="Honest comparisons of ListingKit with PropClips, ListingAI and Canva for realtors: pricing, WhatsApp support, flyers, video scripts and naira pricing.",
                             h1="Real estate marketing tool alternatives", lede="Where ListingKit fits next to the tools agents already know, with prices as shown on each tool's own site in October 2026."),
    }
    for key, (name, path, blurb) in SECTIONS.items():
        children = [p["path"] for p in pages if p.get("section") == key]
        extra = []
        if key == "descriptions":
            groups = {}
            for p in pages:
                if p.get("section") == key:
                    groups.setdefault(p["city_group"], []).append(p["path"])
            for g, items in groups.items():
                extra.append((re.sub(r"[^a-z]+", "-", g.lower()).strip("-"), g, hub_list(items, registry)))
        else:
            extra.append(("all", "All " + name.lower(), hub_list(children, registry)))
        m = hub_meta[key]
        hubs.append(dict(path=path, section=key, crumb=name, eyebrow="Free templates", blurb=blurb,
                         intro=[], extra_html=extra, faq=[], related=[s[1] for k, s in SECTIONS.items() if k != key] + ["/resources/"], **m))
    res_extra = []
    for key, (name, path, blurb) in SECTIONS.items():
        children = [p["path"] for p in pages if p.get("section") == key]
        res_extra.append((key, name, f'<p class="note" style="margin-bottom:14px">{E(blurb)} <a class="link" href="{path}">See the {E(name.lower())} hub</a></p>' + hub_list(children, registry)))
    hubs.append(dict(path="/resources/", crumb="Free templates", eyebrow="ListingKit resources",
                     title="Free Real Estate Marketing Templates | ListingKit",
                     meta="Every free ListingKit template in one place: real estate captions, WhatsApp broadcasts, property descriptions by area, hashtags, guides and tool comparisons.",
                     h1="Free real estate marketing templates", lede="Captions, WhatsApp broadcasts, area descriptions, hashtags and guides, written for how agents in Africa and beyond actually sell.",
                     intro=["Every template here is free to copy. When you'd rather not fill blanks by hand, the <a class=\"link\" href=\"/generator/\">free ListingKit generator</a> writes all of them from one property input."],
                     extra_html=res_extra, faq=[], related=[]))
    return hubs


def collect():
    pages = []
    for mod in (captions, whatsapp, descriptions, hashtags, guides, alternatives):
        pages.extend(mod.pages())
    registry = {p["path"]: p for p in pages}
    hubs = build_hubs(pages, registry)
    for h in hubs:
        registry[h["path"]] = h
    return pages + hubs, registry


def write_all():
    allp, registry = collect()
    for p in allp:
        d = os.path.join(SITE, p["path"].strip("/"))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(render(p, registry))
    urls = ["/", "/generator/"] + [p["path"] for p in allp]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"  <url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod></url>")
    sm.append("</urlset>")
    open(os.path.join(SITE, "sitemap.xml"), "w").write("\n".join(sm) + "\n")
    open(os.path.join(SITE, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    return allp


VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.links, self.title, self.desc, self.h1 = [], [], [], None, None, 0
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "link" and a.get("rel") == "stylesheet":
            self.links.append(a["href"])
        if tag == "meta" and a.get("name") == "description":
            self.desc = a.get("content")
        if tag == "h1":
            self.h1 += 1
        if tag == "title":
            self._in_title = True
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"unexpected </{tag}> (open: {self.stack[-3:]})")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title = (self.title or "") + data


def check(allp):
    problems, titles, descs = [], {}, {}
    files = []
    for root, _, fs in os.walk(SITE):
        for f in fs:
            if f.endswith(".html"):
                files.append(os.path.join(root, f))
    for fp in files:
        c = Checker()
        c.feed(open(fp, encoding="utf-8").read())
        rel = "/" + os.path.relpath(fp, SITE).replace("index.html", "")
        if c.stack and c.stack != []:
            problems.append(f"{rel}: unclosed {c.stack}")
        problems += [f"{rel}: {e}" for e in c.errors]
        if c.h1 != 1:
            problems.append(f"{rel}: {c.h1} h1 tags")
        titles.setdefault(c.title, []).append(rel)
        descs.setdefault(c.desc, []).append(rel)
        for h in c.links:
            if h.startswith(("http", "mailto:", "#", "tel:")):
                continue
            path = h.split("#")[0].split("?")[0]
            if not path.startswith("/"):
                path = os.path.normpath(os.path.join(os.path.dirname(rel), path))
            target = os.path.join(SITE, path.lstrip("/"))
            if path.endswith("/") or os.path.isdir(target):
                target = os.path.join(target, "index.html")
            if not os.path.exists(target):
                problems.append(f"{rel}: broken link {h}")
    for t, ps in titles.items():
        if len(ps) > 1:
            problems.append(f"duplicate title {t!r}: {ps}")
    for d, ps in descs.items():
        if len(ps) > 1:
            problems.append(f"duplicate meta description: {ps}")
    for p in allp:
        if len(p["title"]) > 75:
            problems.append(f"{p['path']}: long title ({len(p['title'])})")
        if not (70 <= len(p["meta"]) <= 170):
            problems.append(f"{p['path']}: meta length {len(p['meta'])}")
        n = sum(len(i) for _, i in p.get("groups", []))
        if p.get("groups") and not (8 <= n <= 15):
            problems.append(f"{p['path']}: {n} examples")
    return problems, len(files)


if __name__ == "__main__":
    allp = write_all()
    counts = {}
    for p in allp:
        counts[p.get("section") or "resources"] = counts.get(p.get("section") or "resources", 0) + 1
    print("built", len(allp), "pages", counts)
    if "--check" in sys.argv:
        probs, nfiles = check(allp)
        print("html files checked:", nfiles)
        for x in probs:
            print("PROBLEM", x)
        print("problems:", len(probs))
        # A check command must be usable by CI and deploy scripts. Printing
        # validation failures with status 0 made broken output look successful.
        if probs:
            sys.exit(1)
