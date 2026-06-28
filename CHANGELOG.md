# Changelog

## 2026-06-24

- **03-id-business-trends/competitors**: Created ride-hailing-super-app-gaps.md -- deep competitor analysis of Gojek/Grab, their cross-sell failures, super-app bloat, financial pressures, and 12 unserved needs. 896 lines, 47K+ words covering 19 sections including market structure, driver ecosystem, QRIS settlement crisis, and opportunity map.

## 2026-06-26

- **07-gaps-and-opportunities/opportunities**: Created nib-halal-regtech-kreator-umkm.md - NIB + Sertifikasi Halal RegTech one-pager. 1,621 lines covering two converging regulatory deadlines (NIB wajib June 18, 2026 for creators; Sertifikasi Halal wajib October 17, 2026 for UMKM), market sizing (7-9M TAM), WhatsApp-native product architecture with AI KBLI wizard, OSS/SIHALAL scraper integration, revenue model (Rp50-150K/mo subscription), and go-to-market strategy.

## 2026-06-23

- **06-harga-pangan-papan**: Discovered and switched to direct SP2KP API access at `https://api-sp2kp.kemendag.go.id/report/api/`. The public endpoint `/average-price/generate-perbandingan-harga` returns JSON price comparison data without authentication. This replaces the previous browser-based scraping approach which was unreliable due to the SPA/Tableau rendering requirements.

- **Script evolution**: Updated money-glitch-harga-pangan-prompt.md to use curl-based API calls against the report API instead of browser navigation + DOM extraction.

## 2026-06-28

- **03-id-business-trends/bottlenecks**: Created driver-financial-inclusion.md -- bottleneck analysis of 3M ojol drivers trapped in triple financial exclusion (vehicle financing at 24-36% APR vs bank 8-12%, insurance penetration <15%, zero savings). 600+ lines covering market size (2.8-3.2M active drivers), cicilan-delusion trap, insurance coverage desert, income volatility patterns, existing solution failures (GoPay Later, GrabFinance, Pegadaian, koperasi), regulatory gaps, embedded insurance revenue model (Rp 450M/month TAM), and 3-phase wedge strategy (financial dashboard -> micro-insurance -> cooperative lending).
