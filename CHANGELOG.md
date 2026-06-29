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
