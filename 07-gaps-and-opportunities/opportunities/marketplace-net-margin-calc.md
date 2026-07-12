# Marketplace Net-Margin Calculator (Komisi Watch) — "produk ini rugi di harga ini"

> TikTok Shop menaikkan komisi penjual hingga 16x lipat (18 Mei 2026) dan memindahkan ongkir
> ke beban seller. Shopee/Tokopedia/Lazada ikut naikkan biaya 2026. Ribuan UMKM seller tidak
> tahu produk mereka rugi di harga jual karena tidak ada tool yang hitung net margin setelah
> semua potongan baru. Wedge: kalkulator laba-bersih lintas-marketplace yang auto-update tarif
> resmi dan ngasih alert "produk ini rugi di harga ini" + rekomendasi harga jual minimum.

**File:** `07-gaps-and-opportunities/opportunities/marketplace-net-margin-calc.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-11-marketplace-net-margin-calc.md`
**Created:** 2026-07-12
**Category:** Opportunity one-pager (vertical SaaS)
**Confidence:** 5
**Status:** build-ready

---

## 1. Problem & evidence
- `03/.../demand-mining/seller-marketplace-komisi-ongkir-meroket.md` (strength 5/5): TikTok
  16x commission hike, ongkir moved to seller, Shopee/Tokped/Lazada follow.
- `03/.../demand-mining/saldo-penjual-shopee-dibekukan.md` (5/5): frozen balances compound
  the pain — sellers lose on fees AND can't access capital.
- Minister of UMKM intervened → signal 5/5, mass complaint confirmed.

## 2. Wedge & product
A **cross-marketplace net-margin calculator** that:
1. Auto-updates official fee schedules (dynamic commission + seller-paid ongkir + admin) per
   platform via the `01` marketplace-fee scraper (Q4 of weekly report → Komisi Watch).
2. Flags "SKU X loses money at price Y" and recommends minimum sell price per SKU.
3. Pushes a daily WA alert to sellers + a structured feed.

## 3. Technical architecture
- Fee-ingest: cron runs `01` platform-gap query → parser → fee DB (per platform, per date).
- Calc engine: `net = price - commission - ongkir_seller - admin - cogs`.
- WA push: Business API; alert on threshold breach.
- MVP: Apps Script + `01` query + WA (2wk); custom: marketplace API (1mo).

```python
def net_margin(price, commission_bps, ongkir, admin, cogs):
    fee = price * commission_bps / 10_000
    net = price - fee - ongkir - admin - cogs
    return net, (net / price if price else 0)
```

## 4. Unit economics
- Freemium: basic check free; premium Rp 25–49rb/bulan (calculator + alert + platform-move rec).
- 5,000 sellers @ Rp 35rb = Rp 175jt/bulan.
- Cross-sell: platform-switch module, bulk repricer.

## 5. Go-to-market
- Scraper-to-product wedge (weekly report Q4): smallest, highest-confidence build (S, conf 5).
- Deadline-driven bundle (P4): fee hikes are recurring panic moments → always-on acquisition.

## 6. Competitive analysis
- Generic P&L tools don't track *dynamic, per-platform* commission in real time.
- First to wire the `01` scraper → live fee DB → seller alert loop wins the trust layer.

## 7. Risks & failure modes
- Platform fee pages are JS-rendered / change often → scraper maintenance burden.
- Sellers may not act on alerts (behavior change) → bundle with repricer for stickiness.

## 8. New gaps discovered
- `deadline-driven-saas-bundle` (P4) — shared GTM.
- A **fee-transparency registry** (mirrors anchor-of-trust, R3) for platform T&Cs.

## 9. References
`03/.../demand-mining/seller-marketplace-komisi-ongkir-meroket.md`,
`03/.../demand-mining/saldo-penjual-shopee-dibekukan.md`; seed `2026-07-11-marketplace-net-margin-calc.md`.
