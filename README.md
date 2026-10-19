# ListingKit

AI listing-content kit for real estate agents. Paste a property's details and get ready-to-post Instagram and TikTok captions, a WhatsApp broadcast message, a portal description, flyer copy and a 30-second video-tour script, built WhatsApp-first for agents in Nigeria, Africa and worldwide.

**Live:** https://listingkit-ai.netlify.app/
**Free caption generator:** https://listingkit-ai.netlify.app/generator/
**Free templates (74 SEO pages):** https://listingkit-ai.netlify.app/resources/

## What's in this repo
- `site/` — the static site deployed to Netlify: landing page, client-side caption generator (`/generator/`), and programmatically generated template pages (captions, WhatsApp broadcasts, area listing descriptions, city hashtags, guides, competitor comparisons), plus `sitemap.xml` and `robots.txt`.
- `build_seo.py` — Python generator for the SEO pages, with a `--check` mode that validates internal links, unique titles and meta descriptions, HTML nesting and heading structure.
- `seo_content/` — page content as Python data.

## Build
```bash
python3 build_seo.py --check   # regenerate pages into site/ and validate
```
Deploy `site/` to any static host (Netlify manual deploy or API zip upload).

## Pricing (launch)
Free: 3 listings/month · Pro: ₦5,000 or $15/month · Agency: ₦15,000 or $39/month. First 100 agents get 3 months of Pro free.

## Roadmap
- Real LLM-powered generation with agent branding
- Branded flyer export
- Accounts and naira billing

Built by Chihurumnanya Diamond Anyanwu, Lagos.
