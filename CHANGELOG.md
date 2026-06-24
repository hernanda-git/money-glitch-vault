# Changelog

## 2026-06-23

- **06-harga-pangan-papan**: Discovered and switched to direct SP2KP API access at `https://api-sp2kp.kemendag.go.id/report/api/`. The public endpoint `/average-price/generate-perbandingan-harga` returns JSON price comparison data without authentication. This replaces the previous browser-based scraping approach which was unreliable due to the SPA/Tableau rendering requirements.

- **Script evolution**: Updated money-glitch-harga-pangan-prompt.md to use curl-based API calls against the report API instead of browser navigation + DOM extraction.
