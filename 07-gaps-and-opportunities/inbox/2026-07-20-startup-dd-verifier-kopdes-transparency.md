# 2026-07-20 startup-DD-verifier-and-kopdes-transparency

Two fresh, well-sourced Indonesian pains mined today point to reusable verification/scraping tools:

1. Startup "unicorn" investment fraud (eFishery: KWAP Malaysia lost Rp860M, Temasek/SoftBank also victims, financial statements manipulated). Wedge: automated cross-check of a startup's claimed revenue vs its tax filings (Coretax/DJP) and litigation history (SIPP) to flag "too good to be true" growth. A "truth-score" SaaS for retail and small institutional investors. Reuses the DJP web-scraping capability already in 01-crawler-scrapper/x and the loker-scam-verifier pattern.

2. Koperasi Desa Merah Putih (KDKMP) procurement opacity (Rp1,8T kipas angin scandal, DPR got zero info). Wedge: crowdsourced WA-bot input + auto price-check vs Shopee/Tokopedia to detect markup in village cooperative procurement. Reuses gov-portal scraping and WA-bot patterns already in the gaps inbox.

Both need a reliable Indonesian entity/revenue verifier fed by DJP + e-commerce price APIs. Strong candidate for the 01-crawler-scrapper stack.
