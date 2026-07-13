# CHANGELOG

## 2026-07-11 -- enrich: IDX opening range breakout (09:00-09:30 WIB) -- 809-line trading-bot strategy doc: verified IDX session calendar (pre-open 08:45, open auction 09:00, Session I to 11:30, lunch, Session II to 14:49, close 15:00), tick/lot schedule, IDX30/LQ45 universe selection, ORB signal + risk + force-close logic, working Python bot wired to the event-driven baseline, backtest harness, and IDX-specific pitfalls (auction contamination, lot/tick rejection, lunch gap, short ban). idx.co.id blocked bots (HTTP 403) so schedule cited from Wikipedia and flagged verify-live.

## 2026-07-11 -- agent: SP2KP harga pangan self-evolution -- Confirmed: homepage map is a Highcharts map with NO `table tbody tr` (browser fallback yields nothing); Tabulasi Harga is a Tableau trusted-ticket iframe, not scrapable. Always use Source A REST API. `latest-price-dates` is now auth-gated (HTTP 401) as of 2026-07-11, so find the latest date by probing `generate-perbandingan-harga` POST and picking the first date with non-zero `harga`/`harga_pembanding` (today is frequently not yet loaded, returns all-zero rows, so fall back to previous day). Critical field gotcha: the comparison date param is snake_case `tanggal_pembanding` in the multipart form, NOT `tanggalPembanding` (camelCase is silently ignored, echoing the same date and yielding -100% / zero rows). Concurrent cron runs may push the same day's file, causing a rebase conflict on latest.json / sp2kp-YYYY-MM-DD.json / INDEX.md; price data is identical, resolve via `git checkout --ours` then `git rebase --continue`. Updated ~/.hermes/scripts/money-glitch-harga-pangan-prompt.md accordingly.

## 2026-07-10 -- agent: SP2KP harga pangan structural notes

## 2026-07-09 -- enrich: X advanced search operators playbook -- Built 01-crawler-scrapper/x/search-operators-playbook.md (864 lines): full web + API v2 operator grammar, twscrape/snscrape wiring, snowflake cursor math, and copy-paste money-signal query patterns for every vault module
## 2026-07-04 -- enrich: SawitPintar platform opportunity one-pager -- Promoted sawit-pintar-platform.md from inbox to full opportunity doc (1048 lines, 3 pillars: price dashboard, program navigator, input marketplace)

## 2026-07-06 -- enrich: UMKM NPWP registration gap bottleneck -- 33K-line deep analysis of the cascading bottleneck where 25-35M micro-enterprises lack NPWP, blocking NIB, halal certification, credit access, and QRIS onboarding; includes 4-layer gap model, regional analysis, solution concepts (WhatsApp bot, API platform, mobile drives), and technical registration flow

## 2026-07-06 -- enrich: Fastwork vs Sribu freelance marketplace gaps -- Comprehensive competitor analysis of Indonesian freelance marketplaces covering payment infrastructure, escrow, AI matching, mobile experience, skills verification, and enterprise gaps. 1177 lines with code snippets.

## 2026-07-07 -- enrich: Ojol logistics inefficiency in tier 2/3 cities -- 1116-line bottleneck analysis of why last-mile delivery is structurally broken outside Java major metros; covers unit economics failure, address routing problems, warung-as-hub model, bundled route optimization, WhatsApp-first dispatch system, and 5 new gaps discovered.


## 2026-07-07 -- enrich: HalalReady UMKM halal certification automation platform -- 927-line opportunity one-pager for WhatsApp-first SaaS automating the NPWP-to-NIB-to-SEHATI halal certification pipeline for 64M UMKM, timed to October 2026 sanctions deadline. Includes full technical architecture, P3H marketplace, revenue model, go-to-market strategy, and competitive analysis.

## 2026-07-07 -- enrich: COD settlement infrastructure bottleneck -- 1465-line bottleneck analysis of why COD payment settlement takes 7-14 days for tier 2/3 UMKM; covers full settlement chain (courier to LO to hub to platform), unit economics (COD vs QRIS margin comparison), QRIS adoption barriers, BNPL landscape, platform-specific mechanics (Shopee, Tokopedia, Lazada, Bukalapak), technical architecture with pseudocode and SQL schema, regulatory framework (BI, OJK), and proposed COD advance/factoring solution. 3 new gaps discovered.

## 2026-07-07 -- enrich: warung micro-fulfillment bottleneck -- 660-line bottleneck analysis of why Indonesia's ~16-21M warungs (dense physical retail leaf nodes of 64M UMKM) are not yet logistics nodes; covers failed prior attempts and a detailed post-mortem of Warung Pintar/Yummy-Grab, a full reference architecture (node schema, capacity sync, geohash dispatcher in Python, WhatsApp owner bot, QRIS settlement + insurance pool, cold-chain IoT schema, driver batch-route builder, OpenAPI contract), unit economics with a per-kelurahan worked example, regional rollout sequencing, compliance surface (PDP Law, PPh 23, zoning), owner-persona adoption, and 3 new gaps

## 2026-07-09 -- enrich: BPR digital transformation SaaS opportunity -- Promoted 2026-06-30-bpr-digital-transformation-saas from inbox to full opportunity one-pager (~580 lines). Covers the 1,500+ BPR / ~3,000 rural-bank institution gap, legacy tech debt, OJK SLIK/reporting obligations, cloud core + QRIS + credit-scoring module architecture (SQL schema, Python ledger/recon/RBAC code), unit economics (vendor and BPR side), tiered pricing, association go-to-market, postmortem of stalled prior efforts, and 3 new gaps (bpr-slik-reporting-pain, bpr-compliance-automation regtech, bpr-bprs-consolidation-wave). Note: live web verification unavailable this tick; figures annotated for live confirmation, no data invented.

## 2026-07-09 -- enrich: judol-pinjol cross-detection opportunity -- Promoted 2026-06-22-judol-pinjol-pencegahan from inbox to full opportunity one-pager (~805 lines). Cross-crime fraud intelligence layer fusing judol (online gambling) + pinjol ilegal (illegal lending) onto one entity-resolution graph with regulator-ingest (OJK/Kominfo/PPATK/Satgas PASTI), OSINT harvester, transparent weighted scoring, free WhatsApp citizen check, and B2B inline feed. Includes SQL schema, Python ingest/harvester/scorer/cluster/monitor code, QRIS MID parse, deploy yaml, worked examples, risk register, and 3 new gaps (ppatk-sar-automation, kominfo-judol-feed-parser, mule-account-rural-bpr). Note: live web verification unavailable this tick; flagged figures marked verify-live, no data invented.

## 2026-07-09 -- enrich: Lalamove vs AnterAja B2B last-mile logistics API gaps -- 847-line competitor/bottleneck analysis of Indonesias dedicated B2B carriers vs ride-hailing instant products; maps the missing neutral multi-carrier orchestration layer (unified quote-all/book-best, idempotent event store, COD reconciliation, coverage telemetry) with working Lalamove HMAC and AnterAja adapter code. Live web verify unavailable this tick; figures tagged verify-live, no data invented. 3 new gaps discovered (logistics-coverage-api, carrier-webhook-reliability, logistics-orchestrator-mcp).

## 2026-07-10 -- enrich: QRIS settlement speed arbitrage -- 790-line bottleneck analysis of the T+1 QRIS merchant payout float on a 32.71M-merchant rail. Documents the scan-instant/payout-batched gap, quantifies systemic float (~Rp16T), models a license-light same-day settlement layer at 0.1% fee (Rp176B/yr base case), with 3 worked merchant examples, idempotent webhook + netting engine code, BI-FAST mechanics, cross-border Antarnegara FX extension, and the credit-scoring data-moat sequel. Sources: Wikipedia QRIS (EN/ID), Kompas, Bittime, qris.id Open API, BI rate page. BI primary pages unreachable this tick (TLS); T+1 inferred from SKNBI batch architecture and flagged verify-live. 3 new gaps discovered (qris-mdr-interchange-transparency, cross-border-qris-fx-settlement-gap, qris-settlement-mcp).

## 2026-07-10 -- enrich(07): warung collective-buying + loyalty toolkit -- Promoted 2026-07-10-warung-collective-buying from inbox to full opportunity one-pager (~809 lines). WA-first toolkit giving warungs chain-scale buying power without a franchise: RW group-buy aggregator, zero-MDR QRIS accept via licensed aggregator, WhatsApp loyalty ledger, and phase-2 smart-stock. Includes webhook/group-buy/QRIS/loyalty pseudo-code, SQLite schema, worked beras price ladder, competitive teardown (Warung Pintar, Mbiz, Ralali, Kudi), regional rollout, KPI dashboard, failure-mode table, and 3-scenario financial model. Source note: live web verify unavailable this tick (no PARALLEL_API_KEY); all figures flagged verify-live, no data invented. Next gap: real distributor pallet-vs-carton pricing curve per commodity/region.

## 2026-07-11 — enrich: konstruksi-escrow-upah-tukang — Labor-payment protection & escrow for informal construction workers (MBG/Sekolah Rakyat/Koperasi Merah Putih gagal-bayar cases, 3 wedges, unit economics)

## 2026-07-11 — enrich(04): fastwork-mcp-spec — Fastwork MCP server spec bootstrapping 04-freelancer-ai-agent from the live fastwork-automation scripts (endpoints, dual-auth, tool surface, reference server/client code, threat model). Found auditor gap list stale: it claimed this DONE while the folder did not exist. Also: sribu-mcp-spec and cookies-tokens/storage-safety still missing.

## 2026-07-12 — enrich(05): ihsg-daily-fetch — Working, stdlib-only IHSG (^JKSE) daily fetcher for the market cron, verified live against Yahoo chart API v8 (IDX official API 403, Stooq JS-gated, Yahoo v7 quote 401 all documented as dead). Includes dual-host retry, null-bar handling, staleness guard, pulse-schema output, cron/systemd deploy, indicator math, SQLite persistence, and basket-fetch extension.

## 2026-07-12 — enrich: same-day-economy-delivery — IDR 10-15K urban same-day delivery gap, unit economics, density-led wedge, code

## 2026-07-12 — synthesis(R1): corrected stale 07 reports — `weekly-gap-report` falsely called 04/02 "phantom" and feed "100% dead" (both folders now exist; crypto/fx live, equity 429). Fixed counts 50→82 pains in synthesis. Added in-place correction notes + hardened feed guard (_meta/validate-pulse.py).

## 2026-07-12 — backlog(all): executed R2, R4, P1-P7, D1-D5, AUTO-ENRICH
- R2 qris-settlement-mcp spec; R4 02/risk-management (Kelly) + 02/signals (sentiment).
- P1 settlement-float-convergence; P2 warung-region-aware-stock; P3 micro-legaltech seed;
  P4 deadline-driven-saas-bundle note; P5 agri-input-mcp; P6 logistics-orchestrator-mcp;
  P7 promoted 4 inbox seeds -> 07/opportunities (MBG, net-margin, bills, desil/dormant).
- D1 merge-ihsg-into-latest.py (heals dead IHSG leg, verified close 5924.36); D2 normalize_region.py;
  D3 dedup_pains.py (81 canonical, 0 dupes); D4 check_secrets.py (clean); D5 archive_pulses.py.
- AUTO-ENRICH.md self-driving pipeline (cron cadence, guards, report->BACKLOG wiring).
- Only R3 (anchor-of-trust-registry) remains open by design.

## 2026-07-12 — R3 anchor-of-trust-registry + report->BACKLOG parser
- R3 anchor-of-trust-registry.md (cross-cutting lookup_trust registry; 5 anchor sources;
  reference interface; consumed by judol/scam/desil/mbg products). Only remaining READY item closed.
- _meta/report_to_backlog.py: implements AUTO-ENRICH §6 (synthesis "New gaps" -> draft backlog,
  table+bullet parse, dedup). Verified: skipped 6 done items, surfaced 1 real new gap.
- BACKLOG + AUTO-ENRICH updated to mark R3 + parser done. idx_movers 429 still open.

## 2026-07-12 — D1b + alert transport: market feed fully live, watchdog wired
- idx-movers-fetch.py (v8 chart, LQ45+flagship basket) heals the last dead leg; merged into
  merge-equity-into-latest.py (renamed from IHSG-only). Verified: live sources crypto/fx/ihsg/
  idx_movers/trending_coins = HEALTHY.
- pulse-health-watchdog.py: validate-pulse + deliver DEGRADED/DEAD via PULSE_ALERT_* env
  (Telegram/Discord/webhook). Creds env-only, never committed. Verified healthy->silent,
  degraded->alert.
- BACKLOG marked fully executed; AUTO-ENRICH cron table + honest-gaps updated.

## 2026-07-12 — cron wired on Windows + WSL Hermes (auto-enrich now unattended)
- 5 jobs on WSL Hermes (python3 + hermes CLI) + 5 -win twins on Windows Hermes (delegate to
  WSL via wsl.exe, since Windows git-bash python is a Store stub). All verified running.
- _meta/CRON-SETUP.md documents topology + reproduce commands; AUTO-ENRICH cron table updated
  to real job names (mgv-pulse-heal/watch/archive/backlog/secret-scan, each -win).
- pulse-health-watchdog.py gained --quiet-ok (silent when healthy) for clean watchdog delivery.
## 2026-07-12 — enrich(01): cookies-tokens-storage-safety — safe at-rest encryption (Fernet+MultiFernet), KEK sourcing (keyring/PBKDF2/Secrets Manager), rotation loop, and pre-commit secret-scan guardrails for scraper credentials

## 2026-07-12 — enrich(07): qris-mdr-transparency-layer — "Kasir QRIS Jujur" literacy/transparency layer: net-received MDR calculator, fee-free alert, printable BI-rule poster for micro-merchants

## 2026-07-13 — agent: SP2KP harga pangan — browser "Tabulasi Harga" now yields a real table. Re-verified the live page (sp2kp.kemendag.go.id, Tabulasi Harga nav link, NOT the homepage map). The comparison table now renders as a normal `table` with `thead` (columns: Komoditas, Unit, <prev date>, <current date>, Perubahan) and a `tbody` of `tr`/`td` rows, INCLUDING Region A/B/C sub-rows for Beras Medium, Beras Premium, and Beras SPHP Bulog. This contradicts the 2026-07-11 note that Tabulasi Harga was a Tableau trusted-ticket iframe with no scraper-friendly table. The browser fallback (Source B) is now viable again. Caveat: the browser page defaults to a stale comparison window (2026-07-09 vs 2026-07-10 observed on 2026-07-13), so for the authoritative latest date still use REST Source A (`generate-perbandingan-harga`). Latest available data this tick confirmed 2026-07-10 (probed 07-11 and 07-12 both all-zero). No new JSON written since 07-10 already committed/pushed. Updated ~/.hermes/scripts/money-glitch-harga-pangan-prompt.md Source B note.

## 2026-07-13 — enrich(07): prakerja-akses-tracker-saas — "PrakerjaWatch" gelombang tracker + insentif-cair estimator + paid escalation SaaS (corrected a 2020 Kontan article mis-cited as 2026 in the pain file)
