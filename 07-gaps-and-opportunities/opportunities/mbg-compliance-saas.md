# MBG Compliance SaaS — kepatuhan Program Makan Bergizi Gratis dalam satu klik

> Ribuan dapur SPPG (Program Makan Bergizi Gratis) berhenti operasi karena dana VA tak cair
> akibat lupa pelaporan di dashboard BGN. Juknis berubah-ubah. Wedge: software kepatuhan MBG
> yang menyambungkan pembelian bahan, produksi, distribusi, dan pelaporan BGN dalam satu klik,
> plus layanan pendampingan admin. Vertical-specific, belum ada pemain.

**File:** `07-gaps-and-opportunities/opportunities/mbg-compliance-saas.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-11-sppg-mbg-compliance-saas.md`
**Created:** 2026-07-12
**Category:** Opportunity one-pager (compliance SaaS)
**Confidence:** 5
**Status:** build-ready

---

## 1. Problem & evidence
- 372 SPPG suspended in Jatim alone; investors out Rp 1–1.8M/dapur, funds not disbursed for months.
- Root cause: missed reporting in the BGN dashboard + shifting juknis (per
  `03/.../demand-mining/investor-dapur-mbg-merugi-dana-tak-cair.md`).
- The operator is a small caterer/dapur, not a compliance team — they lose the VA flow over
  a missed checkbox.

## 2. Wedge & product
WA-first + web dashboard that:
1. Connects bahan procurement → produksi → distribusi → BGN pelaporan in one click.
2. Auto-fills the BGN report from operational data (reduces missed fields).
3. Sends juknis-change alerts + deadline reminders.
4. Optional admin-pendampingan (human-in-loop) for dapur that want hands-off.

## 3. Technical architecture
- WhatsApp Business API ingress (per the vault's dominant "WA as OS" thesis).
- Backend: FastAPI + Postgres; BGN report model as a typed schema.
- Connector to BGN dashboard (scrape or API if available — `verify-live` on endpoint).
- Audit log per dapur (proves compliance to BGN on dispute).

```sql
CREATE TABLE dapur (
  id UUID PRIMARY KEY,
  nama TEXT,
  va_number TEXT,
  status TEXT,            -- aktif|suspended|pending
  last_report_at TIMESTAMPTZ
);
CREATE TABLE laporan_bgn (
  id UUID PRIMARY KEY,
  dapur_id UUID REFERENCES dapur(id),
  periode DATE,
  auto_filled BOOL,
  submitted_at TIMESTAMPTZ,
  status TEXT
);
```

## 4. Unit economics
- Rp 300–750rb/dapur/bulan (WTP proven: investors deployed billions, face debt).
- 1,000 dapurs = Rp 300jt–750jt/bulan gross.
- Admin-pendampingan add-on: Rp 500rb–1jt/dapur/bulan.
- CAC low: BGN/community channel, not paid ads.

## 5. Go-to-market
- Deadline-driven: suspended dapurs are a panic channel. Partner with dinas/community orgs.
- Cross-sell with the **deadline-driven SaaS bundle** (P4): one watcher, four products.

## 6. Competitive analysis
- No vertical-specific MBG compliance player yet (per seed). Generic accounting tools don't
  know BGN juknis. First mover advantage is real.

## 7. Risks & failure modes
- BGN endpoint/API may be unstable or auth-gated (verify-live). Build a resilient scraper.
- Juknis churn → product must absorb changes fast (templated report model).

## 8. New gaps discovered
- `deadline-driven-saas-bundle` (P4) — shared GTM with halal/margin/bills.
- A **BGN compliance status registry** could feed the anchor-of-trust concept (R3/P-anchor).

## 9. References
`03/.../demand-mining/investor-dapur-mbg-merugi-dana-tak-cair.md`; seed
`2026-07-11-sppg-mbg-compliance-saas.md`. All WTP figures from source pains; `verify-live`
on any external BGN endpoint.
