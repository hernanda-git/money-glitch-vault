# 🕷️ 01 — Crawler & Scrapper

Real-cookie / real-token harvesting of public + semi-public signals from social platforms. Output feeds other folders (trends, gaps, market intel).

## Platforms

- **X (Twitter)** — search operators, bookmarks, lists, followers graph
- **Instagram** — hashtags, explore, reels, story viewers, creator insights
- **TikTok** — FYP sampling, hashtag velocities, comment mining
- **Discord** — server message archives, public invite scraping
- **Facebook** — groups, marketplace, public pages

## Sub-folders

- `cookies-tokens/` — how to obtain, rotate, store safely (local only, **never commit**)
- `x/` — X-specific scrapers + signal playbooks
- `instagram/`
- `tiktok/`
- `discord/`
- `facebook/`
- `community-discovery/` — finding new servers/groups/subreddits where money is being discussed
- `scripts/` — reusable Python/Node scrapers
- `signals/` — daily/weekly distilled output

## Cookbook (to populate)

- [ ] X search → CSV of last-7-day posts matching `$keyword AND min_faves:10 AND -filter:replies`
- [ ] TikTok hashtag → trending video velocity (views/hour)
- [ ] Discord public server → last 1000 messages from `#deals` `#side-hustle` `#crypto-pump`
- [ ] Instagram hashtag → top 50 creators by recent engagement rate
- [ ] Facebook Marketplace crawl → underpriced items in target city

## Safety checklist

- [ ] Use a **burner account** for scraping, not your main
- [ ] Store tokens in `.env` (gitignored), never in code
- [ ] Respect `robots.txt` for public pages, but understand it's not legally binding for public data
- [ ] Rate-limit: random 2-8s between requests, drop headers that scream "bot"
- [ ] Rotate residential proxies for >10k req/day volumes
