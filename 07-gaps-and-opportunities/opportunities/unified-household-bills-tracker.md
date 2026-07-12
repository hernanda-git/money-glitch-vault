# Unified Household Bills Tracker — satu dashboard lintas-utilitas

> Tiga pain point di demand-mining (tagihan listrik PLN melonjak 3x, air PDAM keruh/mati, pajak
> kendaraan naik karena opsen) berujung pada satu kebutuhan: warga tidak punya alat untuk
> memantau, memprediksi, dan diingatkan soal semua tagihan rumah tangga dalam satu dashboard.
> Wedge: satu bot WhatsApp/Telegram yang menarik data PLN Mobile, status PDAM, dan tagihan
> Samsat, lalu kirim ringkasan bulanan + alarm anomali + reminder jatuh tempo.

**File:** `07-gaps-and-opportunities/opportunities/unified-household-bills-tracker.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-11-unified-household-bills-tracker.md`
**Created:** 2026-07-12
**Category:** Opportunity one-pager (consumer fintech)
**Confidence:** 4
**Status:** build-ready

---

## 1. Problem & evidence
- `03/.../demand-mining/tagihan-listrik-pln-melonjak-3x.md` — PLN spike shocks households.
- `03/.../demand-mining/krisis-air-pdam-keruh-mati.md` — PDAM quality/availability failure.
- `03/.../demand-mining/op sen-pkb-mencekik-setop-bayar.md` — vehicle tax jumps on opsen.
- Three unrelated utilities, one shared failure: no cross-utility visibility.

## 2. Wedge & product
WA/Telegram bot that:
1. Pulls PLN Mobile, PDAM status, Samsat tagihan into one view.
2. Sends monthly bill summary + anomaly alarm (spike vs baseline) + due-date reminder.
3. Freemium: basic check free; premium (prediksi + alert) Rp 15–25rb/bulan.

## 3. Technical architecture
- Connectors: PLN Mobile (scrape/API), PDAM (per-region, often no API → scrape),
  Samsat (state-based). Each connector isolated; one fails, others still serve.
- Anomaly engine: per-household baseline (EWMA) → flag > +X% as alert.
- WA Business API push (vault's "WA as OS" thesis).

```python
def anomaly(baseline_ewma, current, z=2.0):
    return current > baseline_ewma * (1 + 0.15)   # >15% over baseline = alert
```

## 4. Unit economics
- Rp 15–25rb/bulan premium; basic free.
- Natural cross-sell across the 3 pains (one household, all three bills).
- CAC: utility-community / neighborhood group (RW) distribution.

## 5. Go-to-market
- Deadline-driven bundle (P4): tax/rate changes are recurring panic → acquisition moments.
- RW-group pilot (matches warung collective-buying motion).

## 6. Competitive analysis
- No single Indonesian app aggregates PLN+PDAM+Samsat. Bank/ewallet bill-pay sees individual
  bills but not cross-utility anomaly/prediction.

## 7. Risks & failure modes
- PDAM has no standard API per region → connector maintenance.
- Data privacy: bills are sensitive; store minimally, encrypt at rest.

## 8. New gaps discovered
- `deadline-driven-saas-bundle` (P4) — shared GTM.
- A **utility-rate watchdog feed** (sibling to compliance-deadline watch).

## 9. References
`03/.../demand-mining/tagihan-listrik-pln-melonjak-3x.md`,
`03/.../demand-mining/krisis-air-pdam-keruh-mati.md`,
`03/.../demand-mining/op sen-pkb-mencekik-setop-bayar.md`; seed `2026-07-11-unified-household-bills-tracker.md`.
