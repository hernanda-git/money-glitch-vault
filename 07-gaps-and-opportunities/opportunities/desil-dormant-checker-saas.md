# Desil & Rekening-Dormant Checker SaaS — status warga vs negara, transparan

> Dua fresh pain converge: (1) warga miskin terblokir layanan kesehatan gratis karena status
> desil SIKS-NG salah, (2) nasabah kaget rekening dormant dibekukan PPATK tanpa pemberitahuan.
> Intinya: status warga vs negara tidak transparan dan lambat dilacak. Wedge: chatbot WhatsApp
> yang cek status desil dari NIK + ingatkan jendela perubahan data (tanggal 1–11), dan cek
> status dormant rekening + panduan buka blokir per bank. Sisi B2G: dashboard Dinsos/desa.
> Sisi B2B: modul notifikasi pengurang beban call center bank.

**File:** `07-gaps-and-opportunities/opportunities/desil-dormant-checker-saas.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-11-desil-dormant-checker-saas.md`
**Created:** 2026-07-12
**Category:** Opportunity one-pager (civic / regtech)
**Confidence:** 4
**Status:** build-ready

---

## 1. Problem & evidence
- `03/.../demand-mining/warga-miskin-terblokir-layanan-gratis-status-desil.md` — wrong desil
  blocks free health (bansos, BPJS subsided).
- `03/.../demand-mining/rekening-dormant-dibekukan-ppatk-tanpa-pemberitahuan.md` — dormant
  freeze with no notice; 28M accounts already re-opened, tens of millions still at risk.
- Both are "citizen vs opaque state" failures — same root, two surfaces.

## 2. Wedge & product
WA chatbot:
1. **Desil check:** NIK → SIKS-NG desil status; remind the 1–11 monthly data-change window;
   guide correction.
2. **Dormant check:** rekening → bank dormant status; step-by-step buka blokir per bank.
Sides: **B2G** Dinsos/desa dashboard (pelacakan perubahan data); **B2B** bank call-center
load reducer (proactive notification).

## 3. Technical architecture
- Desil: SIKS-NG lookup (if API; else guided manual check) — `verify-live` on endpoint.
- Dormant: per-bank status rules + unbinding guide DB.
- WA Business API ingress; Google Sheets state for B2G dashboards (2–4 wk build).

```sql
CREATE TABLE cek_desil (
  nik_hash TEXT PRIMARY KEY,
  desil INT,
  last_checked TIMESTAMPTZ,
  window_open BOOL          -- 1-11 of month
);
CREATE TABLE cek_dormant (
  rek_hash TEXT PRIMARY KEY,
  bank TEXT,
  status TEXT,              -- aktif|dormant|blokir
  unbinding_step TEXT
);
```

## 4. Unit economics
- B2C: freemium check; premium Rp 10–25rb for guided correction + reminders.
- B2G: Dinsos dashboard subscription.
- B2B: per-bank call-center reduction SaaS.
- Market: tens of millions of dormant accounts + hundreds of thousands of desil-affected
  citizens/year.

## 5. Go-to-market
- Deadline-driven bundle (P4): desil window (1–11) is a monthly panic moment.
- Cross-sell with micro-legaltech engine (P3): desil check is one of its 5 use cases.

## 6. Competitive analysis
- No consumer desil-checker exists; banks handle dormant reactivation via branches only.
- First WA-first player captures trust layer for "am I eligible / am I blocked?"

## 7. Risks & failure modes
- SIKS-NG / bank APIs may be auth-gated or unavailable → guided-manual fallback.
- PII sensitivity: NIK/rekening hashed, never plaintext at rest.

## 8. New gaps discovered
- `micro-legaltech-engine` (P3) — desil check is use-case #4 there.
- `anchor-of-trust-registry` (R3) — desil + dormant are two of its five consumer registries.

## 9. References
`03/.../demand-mining/warga-miskin-terblokir-layanan-gratis-status-desil.md`,
`03/.../demand-mining/rekening-dormant-dibekukan-ppatk-tanpa-pemberitahuan.md`; seed
`2026-07-11-desil-dormant-checker-saas.md`.
