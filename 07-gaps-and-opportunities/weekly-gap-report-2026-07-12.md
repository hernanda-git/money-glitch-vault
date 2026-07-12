# Weekly Gap Report — 2026-07-12

**Synthesizer:** Money Glitch Weekly Gap Synthesizer (cron)
**Folders read:** 01-crawler-scrapper, 02-trading-bot, 03-id-business-trends (demand-mining), 05-market-cron, 06-harga-pangan-papan, 07-gaps-and-opportunities (inbox + opportunities)
**Structural flags found this run (read before the ranking):**
- `04-freelancer-ai-agent/` **does not exist** as a folder. It is referenced by 6+ opportunity one-pagers (judol-pinjol, bpr, halal, etc.) as the delivery/RegTech layer, but it was never scaffolded. Q3 is answered as "what 04 *should* be."
- `02-trading-bot/` contains only `brokers-apis/binance-spot-futures.md`. The strategy / risk-management / signals layers it references are absent.
- `03-id-business-trends/` has only `demand-mining/`. The `competitors/` and `bottlenecks/` folders named in the workflow exist elsewhere (e.g. `03/.../bottlenecks/qris-settlement-speed-arbitrage.md`, `03/.../competitors/lalamove-ankeraja-logistics-gaps.md`) but not the canonical paths — those links in the one-pagers are partially broken.
- `05-market-cron/data/latest.json` and the last 5 pulses are **100% errors** (CoinGecko `Connection reset`, Yahoo `429 Too Many Requests`, IHSG unreachable). The market feed is effectively dead this week. See "Things to kill."

---

## TOP-5 Best Opportunities This Week

| # | Title | One-sentence wedge | Est. IDR/month | Effort | Conf |
|---|-------|-------------------|---------------|--------|------|
| 1 | **Marketplace Net-Margin Calculator (Komisi Watch)** | Auto-updating cross-marketplace net-margin calculator that flags "this SKU loses money at this price" as TikTok/Shop/Tokped keep changing fees. | Rp 50–150 jt (5k sellers @ Rp 25–49k) | S | 5 |
| 2 | **HalalReady RegTech SaaS** | WhatsApp-first NPWP→NIB→SEHATI halal-cert wizard; deadline Oct 17 2026 is 3 months out and 64M UMKM are exposed. | Rp 100–400 jt (freemium + 15% P3H commission) | M/L | 5 |
| 3 | **Warung Collective-Buying + QRIS + Loyalty (WA-first)** | Give warungs pallet-scale buying, zero-fee QRIS, and a loyalty loop inside WhatsApp — no new app. | Rp 100–300 jt (1.5% pooled-buy spread per RW) | M | 4 |
| 4 | **Judol+Pinjol Cross-Detection B2B Feed** | Fuse Kominfo/OJK/PPATK blocklists + OSINT into one queryable mule-account risk graph sold to banks/e-wallets. | Rp 150 jt–1 M (10–20 partners @ Rp 15–50 jt) | L | 4 |
| 5 | **Seller Protection Clinic + Escrow Upah Tukang** | Dispute-resolution + balance-unfreeze assist for sellers; milestone escrow for construction labor. | Rp 30–120 jt (Rp 25k/mo + Rp 50–150k/case) | S/M | 4 |

---

## Q1 — Recurring pain in BOTH 03 (ID-business) AND social signals (01 scraper notes)

**The signal (verbatim / near-verbatim):**
- 03 demand-mining `seller-marketplace-komisi-ongkir-meroket.md` (strength 5/5): *"TikTok Shop akan menaikkan biaya komisi dinamis hingga 15 kali lipat mulai 18 Mei 2026… Biaya ini ditanggung oleh penjual dan tidak akan ditampilkan kepada pembeli saat checkout."*
- 03 `saldo-penjual-shopee-dibekukan.md` (strength 5/5): *"Saldo Penjual dibekukan sementara… sudah laporan 9 kali dan jawabannya tetap sama, penyesuaian saldo, uang tetap g bisa cair."*
- 01 `search-operators-playbook.md` defines the exact query that *should* be mining this: `(Gojek OR Grab OR "Tokopedia" OR "Shopee" OR "TikTok Shop") (komplain OR "tidak bisa" OR "mah") lang:in -filter:retweets within_time:2d min_faves:5` and the regulatory shock query `("PP" OR "Permen" OR "aturan" OR "pajak")(UMKM OR kreator) lang:in`.

**The bridge:** The 01 playbook is the *firehose* the 03 pain files are *supposed* to be sourced from. The recurring pain that shows up in both layers is **"platforms extract value from the little guy and the little guy has no settlement/recourse layer"** — marketplace fee hikes + frozen seller balances (03) are exactly the complaints the 01 competitor/platform-gap query is designed to surface (01). Cross-referencing the two, three sibling pains share one root cause: sellers squeezed by fees, tukang bangunan unpaid, warung losing to cashless chains — all are **"no trusted settlement / escrow layer between payer and payee."** This is the vault's oldest thesis (WhatsApp Financial Inclusion OS) re-confirmed for the 4th consecutive week.

**The opportunity:** A single "Settlement & Recourse" WhatsApp layer that serves all three: (a) marketplace seller balance-unfreeze clinic (from saldo-dibekukan), (b) milestone escrow for tukang (from tukang-tidak-dibayar), (c) QRIS acceptance for warung (from warung-kalah-minimarket). Build once, three customer segments. Who pays: sellers Rp 25k/mo + case fee; homeowners/developers 1–2% escrow; warungs via spread. 30-day target: launch the seller unfreeze clinic + tukang escrow as two WA flows (both are 2-week builds per their source files).

**Next action this week:** Stand up a single WhatsApp bot skeleton (FastAPI + WA Business API) with two flows: `/saldo` (guides seller through Shopee freeze-appeal with document template) and `/escrow` (milestone escrow via Xendit/Flip). Reuse the webhook + intent-router pseudo-code already written in the warung one-pager.

---

## Q2 — Which regional price gap (06) is mispriced / ignored by national players

**The signal (verbatim from `06-harga-pangan-papan/data/latest.json`, 2026-07-10):**
- Beras Medium — Nasional Rp 13.836/kg vs **Region C Rp 17.031/kg (+23.1%)**.
- Beras Premium — Nasional Rp 15.515/kg vs **Region C Rp 19.254/kg (+24.1%)**.
- Beras SPHP Bulog — Nasional Rp 12.270 vs Region C Rp 13.321 (+8.6%).
- Beras Premium Region A Rp 15.300 vs Region B Rp 16.599 (**−7.8% internal spread**).
- Meanwhile cabai/bola wangi are *falling* nationally (−0.3% to −0.85%) while staples flat — so the only real mispricing is the **persistent +23–24% Region-C rice premium**, which has not moved in 3 daily snapshots (07-08, 07-09, 07-10).

**The bridge:** 06 tracks the *symptom* (Region C pays 24% more for the same rice). 03 tracks the *cause* (warung/petani/umkm lose pricing power to scale; pupuk/servis logistik mahal di daerah). 01's "arbitrage and regional price chat" query pattern is literally built to mine this. National players price to the Nasional average and ignore the Region-C premium because the logistics to serve it look unprofitable — but that premium *is* the arbitrage margin nobody is capturing transparently.

**The opportunity:** A **"Fair-Price Regional Arbitrage" B2B product** — aggregate 06's regional price board into a daily alert that matches (a) buyers in Region C paying +24% with (b) suppliers/logistics in Region A/B where rice is 8–23% cheaper, and quotes a delivered price that collapses the premium while leaving a spread. Wedge: a WA/API "harga daerah" feed for koperasi & warung buying groups + a logistics-bid module. Who pays: 1–2% match fee; koperasi white-label. 30-day target: wire 06 `latest.json` → a simple regional-spread alert (Region C staples > +15% vs Nasional) pushed to a pilot koperasi WA group.

**Next action this week:** Write a 30-line script that diffs `06/.../latest.json` Region vs Nasional per commodity, flags any >15% gap, and posts to a WA group. This is the minimum viable "regional mispricing radar" and reuses the 06 data already being collected.

---

## Q3 — What the freelancer agent (04) can deliver that the trading-bot market (02) currently demands

**The signal:**
- 02 `binance-spot-futures.md` is a *broker/execution* reference only. It explicitly maps to layers that **do not exist in the repo**: `02-trading-bot/strategies/`, `02-trading-bot/risk-management/position-sizing-kelly.md`, `02-trading-bot/signals/news-sentiment-scoring.md`. The strategy + risk + signal layers are referenced but absent.
- 05-market-cron is the intended signal source for 02 — but this week it is **100% error** (no crypto/fx/ihsg data at all).
- The vault's dominant thesis (3 prior weekly syntheses) is **WhatsApp as the de-facto OS** for Indonesia's informal economy.

**The bridge:** Folder `04-freelancer-ai-agent` was planned as the *delivery/agent* layer but was **never built**. The trading-bot market (02) has execution plumbing (Binance sign/rate-limit/WS) but no brain and no mouth. The missing 04 is precisely the "agent" that would: (1) consume 05's market feed + 01's social sentiment, (2) run 02's risk engine (Kelly sizing, drawdown cap), and (3) push trade alerts + position sizing to the trader **inside WhatsApp/Telegram** — where retail Indonesian traders already live (the 01 playbook confirms cashtag monitoring `$BBRI $TLKM $BTC` is the highest-signal local query).

**The opportunity:** **Build 04 as the "Signal-to-Action WhatsApp Agent"** that 02 is missing. It wraps the (future) 05 feed + 01 sentiment into: "BTC broke Rp 1.14M, volatility high → size at 0.5× Kelly, set stop at −4%." Delivered as a WA bot. Who pays: Rp 49–99k/mo per trader (Fiverr/Fastwork comparable), or a 0.5% copy-fee on a signals group. 30-day target: scaffold `04-freelancer-ai-agent/` with one module — a WA bot that polls a *cached* 05 snapshot + a hardcoded risk rule and sends a daily "position-size + stop" message. (Fix 05 feed in parallel — see kill list.)

**Next action this week:** Create `04-freelancer-ai-agent/signal-agent/README.md` + a minimal WA echo-bot stub that accepts a ticker and returns a Kelly-suggested size using the formula referenced in 02's risk docs. Do NOT let the phantom 04 reference rot further — scaffold it now.

---

## Q4 — Which scraper (01) turns into a product in the ID-business folder (03)

**The signal:**
- 01 `search-operators-playbook.md` ships two product-ready query patterns: (1) **"Competitor and platform-gap discovery"** — `(Gojek OR Grab OR "Tokopedia" OR "Shopee" OR "TikTok Shop") (komplain...) lang:in`, and (2) **"Regulatory feed parser"** — referenced in judol-pinjol one-pager as `01-crawler-scrapper/regulatory/kominfo-judol-feed-parser.md` (never built) and the arbitrage/regional-price chat pattern (feeds 06).
- 03 + 07 inbox show direct demand: `07/inbox/2026-07-11-marketplace-net-margin-calc.md` (sellers don't know they're losing money to dynamic commissions) and `07/inbox/scam-detection-tool-2026-07-07.md` (no real-time scam detection integrated with WA).

**The bridge:** Two of 01's scrapers convert *directly* into 03/07 products without new invention:
1. **The marketplace-fee scraper** (01 competitor/platform-gap query) → the **Komisi Watch net-margin product** (07 inbox). The scraper already knows how to detect "TikTok naik komisi 16x" chatter; productize it into a standing monitor that watches Shopee/Tokped/TikTok/Lazada fee & policy pages and feeds the margin calculator.
2. **The regulatory/OSINT harvester** (01 judol feed parser + 01 social lexicon `slot gacor / cair cepat`) → the **judol-pinjol cross-detection** product (07 opportunity). The scraper's QR-OCR + phone/URL extraction is the exact ingest layer that one-pager needs.

**The opportunity:** Ship **"Komisi Watch" as the scraper-to-product wedge** — it is the smallest, highest-confidence build this week (S effort, conf 5). A scheduler runs 01's platform-gap query daily, extracts fee/commission/policy-change posts, and pushes them into a WA alert for sellers + a structured feed for the net-margin calculator. Who pays: bundled into the Rp 25–49k/mo calculator subscription (TOP-5 #1). 30-day target: 2-week MVP (Apps Script + 01 query + WA push), then 1-month custom with marketplace API.

**Next action this week:** Fork the 01 platform-gap query into a cron job that posts new marketplace-fee complaints to a seller WA group daily; pair it with the net-margin calculator MVP from Q1's sibling inbox file.

---

## Things to Kill

1. **`05-market-cron` silent dead feed.** `latest.json` + last 5 pulses are 100% errors (CoinGecko `Connection reset`, Yahoo `429`). The cron is burning compute and reporting success while returning nothing. **Kill the false-green status:** add a health check that marks the feed DEGRADED and alerts, or fix the fetcher (rotate endpoint / add retry-backoff / use `ccxt` which 02 already references). Until fixed, Q3's signal agent must run on a cached snapshot.
2. **Phantom `04-freelancer-ai-agent` dependency.** 6+ one-pagers cite `04/...` files that don't exist. Either scaffold the folder this week or strip the dead cross-links. Don't let a non-existent folder keep being cited as a dependency.
3. **`scam-detection-tool-2026-07-07.md` (inbox) is fully subsumed** by the `judol-pinjol-cross-detection.md` opportunity one-pager (same thesis, far deeper). Keep as a one-line pointer, not a standalone idea. (Not yet 30 days stale, so not moved to graveyard — but stop treating it as separate.)
4. **Overlapped "legal-tech mikro" cluster.** `07/inbox/2026-07-09-slik-pungli-koperasi-tools.md` bundles 3 separate plays (SLIK cleanup, koperasi claims, PKL pungli) into one. Split into 3 one-liners or promote the strongest (SLIK cleanup, Rp 99–299k WTP) and drop the rest to keep the inbox signal-dense.
5. **Stale pulse files.** `05-market-cron/data/pulse-20260706-*.json` (4 files) predate the current dead-feed regime and add noise. Archive anything older than 7 days once the feed is healthy.
6. **Duplicate halal entries.** `07/inbox/2026-07-06-umkm-halal-cert-automation.md` + the promoted `opportunities/halalready-certification-platform.md` cover the same ground; the inbox copy is now redundant. Keep inbox as the origination log only.

*No opportunity in `/opportunities/` qualifies for the graveyard this run — the oldest (sawitpintar, 2026-07-04) is only 8 days stale, under the 30-day threshold.*

---

## Self-evolution note (appended to synthesizer prompt)

Two new cross-topic patterns emerged this run and are worth detecting automatically next week:

- **The "Dead Feed" pattern** — when `05-market-cron` (or any data folder) returns 100% errors, the synthesis must flag it as a "Things to kill" item and fall back to cached/latest-good data rather than silently producing a report on empty inputs. Future runs should diff `latest.json` against an expected schema and assert at least one source is live.
- **The "Phantom Folder" pattern** — when an opportunity one-pager references a vault folder that does not exist (`04-freelancer-ai-agent`), the synthesizer should (a) record it as a structural gap and (b) treat the missing folder's intended function as a buildable opportunity (Q3 this week). Future runs should `ls` the 7 canonical folders first and report any that are missing.

**Future synthesis Q9:** "Which data folder in the vault is currently returning degraded/error data, and which live product opportunity (in 07) is blocked until that feed is fixed?"
**Future synthesis Q10:** "Which referenced-but-missing vault folder, if built this week, would unblock the most existing opportunity one-pagers, and what is its smallest viable scaffold?"
