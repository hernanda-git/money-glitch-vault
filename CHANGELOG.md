# Changelog

## 2026-06-24

- **03-id-business-trends/competitors**: Created ride-hailing-super-app-gaps.md -- deep competitor analysis of Gojek/Grab, their cross-sell failures, super-app bloat, financial pressures, and 12 unserved needs. 896 lines, 47K+ words covering 19 sections including market structure, driver ecosystem, QRIS settlement crisis, and opportunity map.

## 2026-06-26

- **07-gaps-and-opportunities/opportunities**: Created nib-halal-regtech-kreator-umkm.md - NIB + Sertifikasi Halal RegTech one-pager. 1,621 lines covering two converging regulatory deadlines (NIB wajib June 18, 2026 for creators; Sertifikasi Halal wajib October 17, 2026 for UMKM), market sizing (7-9M TAM), WhatsApp-native product architecture with AI KBLI wizard, OSS/SIHALAL scraper integration, revenue model (Rp50-150K/mo subscription), and go-to-market strategy.

## 2026-06-23

- **06-harga-pangan-papan**: Discovered and switched to direct SP2KP API access at `https://api-sp2kp.kemendag.go.id/report/api/`. The public endpoint `/average-price/generate-perbandingan-harga` returns JSON price comparison data without authentication. This replaces the previous browser-based scraping approach which was unreliable due to the SPA/Tableau rendering requirements.

- **Script evolution**: Updated money-glitch-harga-pangan-prompt.md to use curl-based API calls against the report API instead of browser navigation + DOM extraction.

## 2026-06-28

- **03-id-business-trends/bottlenecks**: Created driver-financial-inclusion.md -- 653-line bottleneck analysis of 3M+ ojol drivers trapped in triple financial exclusion (vehicle financing at 24-36% APR vs bank 8-12%, insurance penetration <15%, zero savings). Covers the cicilan trap (25-40% of income to vehicle payments), 1.7M drivers without insurance, income-linked vehicle financing model, embedded micro-insurance architecture, automated savings sweep system, and 4-phase implementation roadmap. Includes working Python code for financing calculator, insurance premium calculator, savings sweep system, fraud detection, and WhatsApp bot interface. 10 Indonesian sources cited. Also discovered new gap: koperasi-simpan-pinjam-ojol.md (driver cooperative for savings and loans).

## 2026-06-29

- **03-id-business-trends/bottlenecks**: Created ojol-logistics-inefficiency.md -- 835-line bottleneck analysis of last-mile logistics pain in Tier 2/3 Indonesian cities. Covers Indonesia's 23% logistics-to-GDP cost premium, the four root causes (truck oligopoly, toll costs, Rupiah fluctuation, regulatory complexity), why ojol model breaks outside Tier 1 (short distances, high density, motorcycle-first, single-city architecture), infrastructure gaps (540K km road network quality disparity, no cold chain in Tier 3), unit economics showing Tier 3 cost per delivery (IDR 30-55K) exceeds consumer willingness to pay, 5 wedge opportunities (consolidated hub-and-spoke, reverse logistics marketplace, COD acceleration, inter-kabupaten freight aggregation, agricultural ojol), technical architecture with hybrid route optimization algorithm and offline-first mobile app design, 3 detailed case studies (warung owner, farmer, Makassar seller), competitive landscape, regulatory environment. 6 Indonesian and international sources cited. Also discovered 3 new gaps: fresh-produce-last-mile-cold-chain.md, cod-settlement-infrastructure.md, tracking-api-consolidation.md.

## 2026-06-30

- **07-gaps-and-opportunities/opportunities**: Created digital-credit-scoring-umkm-qris.md -- opportunity one-pager for QRIS-based digital credit scoring targeting 64M unbankable UMKM. 800+ lines covering the Rp2.500T undisbursed credit problem, QRIS 119% Q1-2026 growth as the unlock, 3 revenue streams (loan origination commission, B2B credit scoring SaaS, data analytics), technical architecture with working Python pseudo-code for QRIS ingestion, feature engineering, ML credit scoring, and WhatsApp onboarding bot, unit economics (LTV/CAC 12-40x, break-even month 18-24), regulatory landscape (BI, OJK, PDP law), competitive moat analysis (cross-platform aggregation, data network effects), 4-phase implementation roadmap, and 10 Indonesian sources cited. Discovered 3 new gaps: qris-settlement-speed-arbitrage.md, cross-border-qris-credit-scoring.md, bpr-digital-transformation-saas.md.

- **06-harga-pangan-papan**: Discovered and documented direct SP2KP API endpoints for HNT (Harga Nasional Tertimbang) data. Key endpoints: `/report/api/hnt?tanggal=YYYY-MM-DD` for national weighted prices, `/report/api/latest-price-dates` for current date discovery, `/report/api/average-price-public` for market-level prices. The HNT endpoint provides SBH-weighted national prices across 42 commodity variants. Previous date comparison available by querying both dates and computing delta. This replaces the unreliable browser-based approach entirely.

- **03-id-business-trends/bottlenecks**: Created same-day-economy-delivery.md -- 800+ line bottleneck analysis of the IDR 10-15K same-day urban delivery gap. Covers the structural unit economics problem (market wants IDR 10-15K but riders need IDR 30-40K per trip), the density threshold equation (8-12 deliveries per sq km per day required for viability), merchant pain points across 6 UMKM segments, consumer behavior shifts post-pandemic, existing solutions and their limitations (GoSend, GrabExpress, JNE/J&T, Lalamove, Astro, informal tukang antar), technical architecture with working Python pseudo-code for order aggregation, route optimization (VRPTW variant), and dynamic pricing engine, unit economics model projecting break-even at 800-1,000 deliveries/day, 4 wedge opportunities (merchant aggregation SaaS, COD settlement infrastructure, marketplace plugin, WhatsApp-first onboarding), competitive landscape, regulatory environment, 3 case studies (Pasar Pagi textile merchants, klinik/apotek network, TikTok Shop creators), and 3 new cross-cutting gaps discovered. 12 sources cited.
