# Changelog

## 2026-06-24

- **03-id-business-trends/competitors**: Created ride-hailing-super-app-gaps.md -- deep competitor analysis of Gojek/Grab, their cross-sell failures, super-app bloat, financial pressures, and 12 unserved needs. 896 lines, 47K+ words covering 19 sections including market structure, driver ecosystem, QRIS settlement crisis, and opportunity map.

## 2026-06-23

- **06-harga-pangan-papan**: Discovered and switched to direct SP2KP API access at `https://api-sp2kp.kemendag.go.id/report/api/`. The public endpoint `/average-price/generate-perbandingan-harga` returns JSON price comparison data without authentication. This replaces the previous browser-based scraping approach which was unreliable due to the SPA/Tableau rendering requirements.

- **Script evolution**: Updated money-glitch-harga-pangan-prompt.md to use curl-based API calls against the report API instead of browser navigation + DOM extraction.
