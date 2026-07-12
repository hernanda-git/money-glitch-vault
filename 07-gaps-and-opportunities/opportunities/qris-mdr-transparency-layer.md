# QRIS MDR Transparency and Literacy Layer for Micro-Merchants ("Kasir QRIS Jujur")

> Warung dan merchant mikro tidak paham aturan MDR QRIS (0,3 persen untuk UMKM, bebas biaya
> untuk transaksi tertentu di bawah Rp100 ribu) dan pelarangan BI membebankan admin ke
> konsumen. Akibatnya muncul konflik fisik (perusakan warung di Kemayoran, keributan di
> Malang) dan margin merchant tergerus diam-diam karena tidak ada visibilitas untung bersih
> per transaksi. Wedge: lapisan literasi + transparansi ringan di atas QRIS yang sudah
> dipakai, bukan payment gateway baru. Kalkulator untung bersih real-time setelah MDR,
> peringatan otomatis kategori bebas biaya, dan poster edukasi aturan BI untuk cegah cekcok
> dengan konsumen. Harga Rp15.000-30.000/bulan atau gratis dengan upsell pembukuan, sinergi
> dengan modul net-margin marketplace sebagai satu suite "keuangan warung jujur".

**File:** `07-gaps-and-opportunities/opportunities/qris-mdr-transparency-layer.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-12-qris-mdr-transparency-layer.md`
**Created:** 2026-07-12
**Category:** Opportunity one-pager (vertical SaaS, fintech-literacy layer)
**Confidence:** 5
**Status:** build-ready
**Build time:** 2 weeks MVP, 1 month with transaction feed, 3+ months full bookkeeping

---

## 1. Problem and evidence

The pain is documented locally in `03-id-business-trends/demand-mining/qris-biaya-admin-warung-konsumen-merchant-bingung.md` (signal strength 4/5, observed 2026-07-12). The evidence chain:

- Merchant kecil (warung Madura, PKL, kios) menghadapi MDR (Merchant Discount Rate) 0,3 persen untuk transaksi UMKM. Pada margin sembako yang sangat tipis, ini terasa memakan untung per transaksi.
- BI melarang membebankan biaya MDR ke konsumen. Merchant terjebak: kalau menaikkan harga atau menarik "admin Rp500-Rp1.000" mereka melanggar aturan dan berisiko ribut dengan pembeli, kalau menanggung sendiri untungnya makin tergerus.
- Insiden fisik sudah terjadi. Perusakan warung Madura di Kemayoran (Mei 2026) menyeret oknum TNI dan menembus perhatian nasional. Keributan serupa di Malang (November 2025) terkait pungutan admin Rp500 per transaksi QRIS.

Local source citations (from the demand-mining file, which itself cites national/regional news):

- "Anggota TNI Disebut Acak-acak Warung di Jakpus Perkara Admin QRIS Rp 1.000" (Kompas.com) - 2026-05-05. Konsumen mengamuk dan merusak warung Madura di Kemayoran karena tidak terima ditarik biaya admin QRIS Rp1.000.
- "Ricuh QRIS di Warung Madura, Ini Penjelasan Resmi BI" (Akurat.co) - 2026-05-06. BI menegaskan merchant dilarang membebankan biaya MDR ke konsumen, tapi merchant kecil merasa dipaksa menanggung biaya sendiri.
- "Tambahan Biaya Admin Rp500 Pembayaran Nontunai di Warung Tradisional, Begini Reaksi Konsumen" (Blok-a.com) - 2025-11-08. Warung di Malang menerapkan biaya admin Rp500 per transaksi QRIS, memicu keluhan konsumen.
- "Di Balik Kebijakan Warung Madura di Malang Terapkan Biaya Admin Rp500 untuk Transaksi QRIS" (Blok-a.com) - 2025-11-07. Pemilik warung menjelaskan mereka menarik biaya admin karena MDR memotong pendapatan tipis mereka.

Volume signal: minimal 6 artikel berita nasional dan daerah dalam 3 bulan terakhir soal ricuh/biaya admin QRIS di warung (Kompas, Akurat, Tribun, Gotvnews, Blok-a, AdaDiMalang). Pola berulang di beberapa kota (Jakarta, Malang) menunjukkan ini gesekan struktural aturan QRIS vs realitas margin warung, bukan kasus tunggal.

Note on external verification: web_search and web_extract tools were unavailable during this tick (PARALLEL_API_KEY not set in the sandbox), so the live article URLs above could not be re-fetched. The citations are carried verbatim from the vault's own demand-mining evidence file, which already recorded them with dates and outlets. Treat the deep-link URLs as "source recorded, not re-verified this tick." The regulatory facts (0,3 percent MDR for UMKM, prohibition on passing MDR to consumers, fee-free threshold) are consistent with the BI QRIS framework cited elsewhere in the vault (see `03/.../bottlenecks/qris-settlement-speed-arbitrage.md`, regulatory frame BI PADG 21/18 and MDR caps).

## 2. Wedge and product

A **QRIS literacy and transparency layer** that sits on top of the QRIS codes merchants already display, not a new payment rail. The product, "Kasir QRIS Jujur," does three concrete jobs:

1. **Real-time net-received calculator.** For every transaction amount the merchant types in, show exactly how many rupiah land in their pocket after the 0,3 percent MDR, before the customer pays. No more guessing whether a Rp10.000 sale leaves Rp9.970 or something else.
2. **Fee-free category alert.** Automatically flag when a transaction qualifies as MDR-exempt (the sub-Rp100.000 UMKM category) so the merchant knows they must NOT charge the customer any admin, and so they understand their own cost is zero on that sale. This single alert directly prevents the Kemayoran/Malang style confrontation.
3. **Printable BI-rule poster.** A one-page, plain-Bahasa edukasi sheet the merchant tapes to the warung wall: "Merchant dilarang membebankan biaya QRIS ke pembeli. Kalau ada yang minta admin, itu melanggar aturan BI." This de-escalates the in-person conflict at the moment of payment.

Differentiation: we do not compete as a payment gateway, aggregator, or full POS. Moka, Majoo, Olsera charge Rp100.000-Rp300.000+ per month and are too heavy for warung. The wedge is the ultra-cheap, single-job transparency layer for the 32.71 million QRIS merchants (BI data cited in `qris-settlement-speed-arbitrage.md`) who already accept QRIS but do not understand its fee math.

## 3. Technical architecture

MVP is a PWA, no install, no merchant bank integration required. It is a calculator plus a rules table plus a PDF poster generator.

```
User flow (MVP, offline-capable PWA)
1. Merchant opens PWA, types nominal transaksi (or taps preset: 5rb / 10rb / 20rb).
2. App looks up active MDR rule for the merchant's category (UMKM 0,3%, exempt < Rp100rb).
3. App shows:
   - "Bersih diterima: Rp9.970" (after 0,3% MDR)
   - "Kategori: BEBAS biaya, JANGAN pungut admin ke pembeli" OR
     "Kena MDR 0,3%, sudah otomatis dipotong, jangan pungut admin lagi."
4. Merchant taps "Cetak poster edukasi" -> generates A5 PDF ready to print.
```

Fee rule data model (the part that needs upkeep and the crawler extension):

```python
# qris_mdr_rules.py  -- local copy of BI/provider MDR schedule
from dataclasses import dataclass
from datetime import date

@dataclass
class MdrRule:
    provider: str          # "BI-UMKM", "Bank X", "E-wallet Y"
    merchant_segment: str  # "UMKM" | "non-UMKM"
    rate_bps: int          # basis points, 30 == 0,3%
    exempt_below_idr: int  # 100_000 for the UMKM fee-free category
    effective: date
    source_url: str        # official BI / provider tariff page

RULES = [
    MdrRule("BI-UMKM", "UMKM", 30, 100_000, date(2026,1,1),
            "https://www.bi.go.id (PADG 21/18 / MDR cap)"),
]

def net_received(nominal: int, rule: MdrRule) -> tuple[int, bool]:
    """Return (rupiah net, is_exempt). Exempt = no MDR charged."""
    if nominal < rule.exempt_below_idr and rule.merchant_segment == "UMKM":
        return nominal, True           # fee-free category
    fee = nominal * rule.rate_bps // 10_000
    return nominal - fee, False

# Example
print(net_received(10_000, RULES[0]))   # (10000, True)  -> bebas, jangan pungut admin
print(net_received(250_000, RULES[0]))  # (249250, False) -> MDR 0,3% = Rp750
```

V2 transaction feed (1 month): read the merchant's QRIS transaction notifications (manual paste of bank/e-wallet statement, or optional API if provider allows) and produce a daily "untung bersih setelah MDR" summary. This is where it converges with the marketplace net-margin calculator (`07/opportunities/marketplace-net-margin-calc.md`) into one "keuangan warung jujur" suite.

V3 (3+ months): lightweight bookkeeping, stock tracking for sembako, and settlement reconciliation (cross-sell from `qris-settlement-speed-arbitrage.md`, where merchants do not know when funds land).

## 4. Unit economics

- Pricing: Rp15.000-Rp30.000 per month for micro-merchants (calculator + alert + poster), or free with upsell to bookkeeping module.
- Willingness-to-pay evidence: warung already voluntarily charge "admin Rp500-Rp1.000" to customers to cover MDR, which means they are acutely margin-sensitive and actively trying to protect pennies. They would rather pay a transparent Rp15.000/month than bleed unseen MDR or get into a fight.
- Benchmark: Moka/Majoo/Olsera at Rp100.000-Rp300.000/month is 4-20x our price and targets bigger F&B, leaving the ultra-micro warung segment open.
- Back-of-envelope: 5.000 warung @ Rp20.000 = Rp100jt/bulan. At 0,3% MDR on a warung doing Rp30jt/bulan QRIS volume, the merchant "loses" ~Rp90.000/month to MDR silently; Rp20.000 for visibility is a cheap insurance against both bleed and confrontation.

## 5. Go-to-market

- Wedge is emotional and physical, not abstract: "jangan sampai warung Anda rusak gara-gara salah paham admin QRIS." The Kemayoran incident is the scare story that drives installs.
- Distribute the printable poster free (viral, word-of-mouth among warung associations / paguyuban). The poster carries the PWA QR code. Poster = free customer acquisition.
- Bundle with the marketplace net-margin calculator as one "keuangan warung jujur" subscription (cross-sell, shared GTM with `marketplace-net-margin-calc.md`).
- Partner angle: warung cooperative / koperasi (see `03/.../bottlenecks/koperasi-simpan-pinjam-ojol.md` pattern) can white-label the poster + PWA for their members.

## 6. Competitive analysis

- Generic POS (Moka, Majoo, Olsera): too expensive and feature-heavy; do not center the MDR-literacy job.
- BI socialization campaigns: official but do not reach warung owners who never read press releases; no in-pocket calculator at point of sale.
- Bank/e-wallet built-in QRIS screens: show confirmation but not "net received after MDR" prominently, and no fee-free-category warning, and no printable rule poster.
- First mover that wires a live MDR rule table (via the `01` crawler extension below) to a pocket calculator + poster wins the trust layer.

## 7. Risks and failure modes

- MDR rules and provider tariffs change; the rule table needs maintenance. Mitigation: a small crawler (`01-crawler-scrapper`, see new gap below) that auto-scrapes official BI and provider tariff pages and flags changes.
- Behavior change: merchants may still quietly charge admin. Mitigation: the poster + consumer-facing "scan to check if admin is legal" QR code shifts social pressure to the merchant side.
- Regulatory sensitivity: we must never advise merchants to charge consumers; the product is explicitly compliance-preserving. Keep messaging aligned with BI statements.

## 8. New gaps discovered

- `01-crawler-scrapper/qris-mdr-tariff-monitor.md` (NEW, discovered this tick): a crawler that auto-scrapes official BI and each bank/e-wallet QRIS MDR tariff page (they change and are JS-rendered) and updates the rule table with change alerts. This is the data backbone for the calculator's accuracy and belongs in `01-crawler-scrapper`.
- `07/opportunities/qris-consumer-checker.md` (NEW, discovered this tick): the consumer-side flip, a "apakah warung boleh pungut admin QRIS?" checker consumers can scan, complementary GTM and a virality loop from the buyer side.
- Convergence note: this product and `marketplace-net-margin-calc.md` should share one "keuangan warung jujur" suite and one fee/rule registry (relates to the anchor-of-trust-registry concept in `03/.../bottlenecks/anchor-of-trust-registry.md`).

## 9. References

- `03-id-business-trends/demand-mining/qris-biaya-admin-warung-konsumen-merchant-bingung.md` (primary source pain, strength 4/5, 2026-07-12).
- `03-id-business-trends/bottlenecks/qris-settlement-speed-arbitrage.md` (QRIS scale: 32.71M merchants, BI PADG 21/18 MDR caps; regulatory frame).
- `03-id-business-trends/bottlenecks/anchor-of-trust-registry.md` (shared rule/registry pattern).
- `07-gaps-and-opportunities/opportunities/marketplace-net-margin-calc.md` (cross-sell suite partner).
- `07-gaps-and-opportunities/inbox/2026-07-12-qris-mdr-transparency-layer.md` (seed note).
- External news carried from the demand-mining file: Kompas.com 2026-05-05, Akurat.co 2026-05-06, Blok-a.com 2025-11-07 and 2025-11-08. (Live URLs not re-verified this tick; web tools unavailable. Marked "source recorded, not re-fetched.")
