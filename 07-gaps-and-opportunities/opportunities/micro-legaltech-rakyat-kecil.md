# Micro Legal-Tech Umbrella for Marginal Indonesians ("Bantuan Hukum Rakyat Kecil")

> Three pain points mined in the 2026-07-09 batch share one root: ordinary Indonesians
> need cheap, repeatable legal and administrative tooling to fight systems that grind them
> down. The first is the SLIK/OJK credit-blacklist trap, where a pinjol loan already paid off
> still shows as macet and silently blocks every future KPR, KTA, and business loan. The
> second is koperasi simpan pinjam (KSP) collapse, where members lose life savings to a
> fraud the regulator was slow to stop and then have no dossier to claim restitution. The
> third is pungli and extortion against PKL and small traders by preman and ormas, where
> victims fear retaliation and have no safe way to record evidence or report anonymously.
> The wedge is a single umbrella of micro legal-tech tools, priced in the ratusan ribu range,
> versus a lawyer who costs puluhan juta. One reusable intake-plus-document-generation engine
> powers all three verticals. This is a research one-pager, not a sales pitch.

**File:** `07-gaps-and-opportunities/opportunities/micro-legaltech-rakyat-kecil.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-09-slik-pungli-koperasi-tools.md`
**Created:** 2026-07-16
**Category:** Opportunity one-pager (micro legal-tech, vertical SaaS)
**Confidence:** 4
**Status:** research-ready (validate willingness to pay before build)
**Build time:** 6-8 weeks MVP covering pillar 1, 4-6 months for all three pillars

---

## 1. Problem and evidence (three pillars)

### 1.1 Pillar A: the SLIK/OJK blacklist trap

Sistem Layanan Informasi Keuangan (SLIK) is OJK's central credit database. Every bank,
multifinance, and legal peer-to-peer (P2P) lender reports a borrower's status there:
lancar (current), macet (non-performing), and the rest. A "macet" flag, even one that is
wrong, effectively freezes a person out of all formal credit. The trap has three parts.

First, paid-off illegal pinjol debt lingers. Illegal online lenders are not SLIK reporters,
but many victims also had a legal loan, or paid the illegal lender and were still reported,
or had their identity reused. When the person later applies for a KPR or KTA, the bank pulls
SLIK and sees a macet record that was never cleared. The applicant has no obvious, cheap way
to force a correction.

Second, the dispute path is opaque and slow. SLIK itself is only a data pipe. OJK publishes
that consumers can check their own SLIK record for free at an OJK office or through the
ijin.kontak.ojk.go.id portal, and that disputes go back to the reporting institution first.
The consumer must know which institution reported the record, contact that institution, and
prove repayment. For someone who took a dozen small loans across apps they can no longer
name, that chain is a maze.

Third, the cost of being wrong is huge and silent. A blocked KPR means a lost house, a
blocked business loan means a dead warung or UMKM, and a blocked KTA means staying in the
debt spiral. None of these losses are visible to the system that created them.

Real anchor data point: OJK revoked the business license of PT Asuransi Jiwa Indosurya
Sukses (later PT Asuransi Jiwa Prolife Indonesia) on 2 November 2023, and ordered it to pay
policyholders Rp566,24 miliar in compensation under a written OJK order dated 13 October
2023 (Surat S-45/D.05/2023). The same Henry Surya group ran Koperasi Simpan Pinjam (KSP)
Indosurya, whose collapse is the largest KSP fraud in Indonesian history. These are the same
families of victim: people whose credit standing and savings were wrecked by one group, and
who then had to navigate OJK, the courts, and SLIK repair on their own. Source: CNBC
Indonesia, "OJK Serahkan Kasus Prolife ke Kejaksaan, Henry Surya Jadi Tersangka," 15 July
2026, https://www.cnbcindonesia.com/market/20260715174137-17-751097/ojk-serahkan-kasus-prolife-ke-kejaksaan-henry-surya-jadi-tersangka

### 1.2 Pillar B: koperasi simpan pinjam collapse and the claim dossier gap

Indonesia has tens of thousands of KSP and KSPPS (sharia) cooperatives holding member
savings that are, in practice, unsecured deposits. When one fails, members lose everything
and the path to restitution is bureaucratic and adversarial.

The canonical case is KSP Indosurya. Reporting across 2020-2024 put the hole at roughly
Rp14,4 triliun across about 23.000 nasabah, with Henry Surya convicted and later also
charged in the Prolife insurance matter. The pattern repeats with smaller KSP across the
country. The gap is not only the fraud. It is that after a collapse, each victim must build
their own evidence dossier, file with OJK, join a class action or wait years, and track a
liquidation they cannot follow. There is no neutral third-party tool that assembles a victim
dossier automatically from their own records (bukti setor, buku tabungan koperasi, screenshots)
and tells them the exact next step, the correct OJK channel, and the status of the liquidation.

The demand-mining vault already documents related distress directly:
`03-id-business-trends/demand-mining/korban-gagal-bayar-koperasi-simpan-pinjam.md` (victims of
KSP failure) and `03-id-business-trends/demand-mining/klaim-jkp-ditolak-berkas-tidak-valid.md`
(rejected claims due to invalid paperwork). Both point to the same friction: people lose
because their paperwork is not assembled the way the system requires.

### 1.3 Pillar C: pungli and extortion against PKL and small traders

PKL, warung, and small traders pay informal "security" or "retribusi" levies to preman and
ormas, on top of or instead of legal retribusi. The victims almost never report, for three
reasons: fear of retaliation, no clear evidence trail, and no trusted anonymous channel. When
they do report, the response is slow and the case file is weak.

The vault's demand-mining set is thick with this exact pain:
`03-id-business-trends/demand-mining/pkl-dipalak-preman-berkedok-ormas.md` (PKL extorted by
preman under ormas cover), `03-id-business-trends/demand-mining/jukir-liar-palak-pengendara-minimarket-jalanan.md`
(illegal parking attendants extorting drivers), and `03-id-business-trends/demand-mining/pkl-ditertibkan-satpol-pp-kehilangan-tempat.md`
(PKL losing their place with no buffer). The wedge for this pillar is not a lawsuit engine but
an evidence-and-anonymity layer: a safe way to log each levy with date, amount, location, and
photo; a private ledger the trader controls; and a one-tap anonymized report bundle to the
right authority (Satpol PP, Polri, or a civil society hotline) without exposing the victim.

### 1.4 Why these three belong in one product

The connective tissue is bureaucratic self-defense for people who cannot afford a lawyer.
Each pillar is a variation on the same job: "help me assemble the correct documents and
evidence, tell me the exact next step, and do it cheaply and safely." A single intake
questionnaire plus a document-generation and evidence-vault core can serve all three. That
shared engine is the real moat. Building three separate apps would triple the cost; building
one umbrella amortizes it.

---

## 2. Existing solutions and why they under-serve

### 2.1 For SLIK repair

- OJK's own channels: free SLIK check at OJK offices and via ijin.kontak.ojk.go.id, and a
  complaints route. Free, but the consumer must do the work, know which institution reported
  the bad record, and push the institution. No guided tool, no status tracking, no template
  letters. For a non-expert, the gap between "you can complain" and "your record is fixed" is
  enormous.
- Banks and multifinance: each institution has its own dispute form, usually a PDF or a
  branch visit. Fragmented, offline, slow.
- Traditional lawyers and "konsultan hukum": competent but priced at puluhan juta for a case
  that, for a warung owner, is not worth it. This is the core pricing gap.
- Debt amnesty and pinjol-relief NGOs: a few civil society efforts exist but are capacity
  limited and not productized.

### 2.2 For KSP victim claims

- OJK and the cooperative ministry handle liquidation and sometimes mediation, but victims
  describe slow, opaque processes and weak personal dossiers.
- Legal aid (LBH) offices exist but are overwhelmed and geographically limited.
- No commercial product assembles the victim dossier automatically.

### 2.3 For pungli and extortion

- Satpol PP and Polri channels exist (including some Qlue-style reporting in big cities) but
  fear of retaliation keeps usage low, and there is no trader-controlled evidence vault.
- No product gives a PKL a private, exportable evidence ledger plus an anonymized report
  with one tap.

The white space: a cheap, guided, productized layer that sits between "do nothing" and "hire
a lawyer." That is the wedge.

---

## 3. Wedge and product design

The product, working name "Bantuan Hukum Rakyat Kecil" (BHRK), is a mobile-first web app
(PWA, installable, works on low-end Android, offline-capable for data entry) with three
modules sharing one core.

### 3.1 Shared core (the reusable engine)

- Guided intake questionnaire per module, in plain Bahasa, with examples.
- Document and evidence vault: upload bukti transfer, buku tabungan, screenshots, photos;
  auto-tagged by date and type. Stored encrypted, user-owned.
- Document generator: fill the intake, produce a correctly formatted surat (pengaduan,
  permohonan koreksi SLIK, dossier ringkasan, laporan anonim) as PDF and editable text.
- Next-step navigator: given the user's answers, show the exact institution, the correct
  channel (URL, address, or in-app handoff), and the expected timeline.
- Status tracker: let the user log each response they get and surface reminders.

### 3.2 Module A: SLIK Cleanup Toolkit

Jobs performed:

1. Free SLIK check guide: walk the user through the free OJK check, explain the fields
   (lancar, macet, restrukturisasi) in plain language, and flag what looks wrong.
2. Dispute letter generator: produce a formal permohonan koreksi data SLIK addressed to the
   reporting institution, with the legal basis cited (the institution's obligation to report
   accurate data, and OJK consumer-protection framework). Attach the user's bukti pelunasan.
3. Escalation path: if the institution does not fix it in the statutory window, generate an
   OJK complaint (pengaduan konsumen) with the full dossier attached.
4. Paid "done-for-you" tier: for Rp99.000-Rp299.000, a trained operator reviews the dossier,
   sends the letters, and tracks status for 30 days.

### 3.3 Module B: KSP Claim Dossier

Jobs performed:

1. Evidence intake: the user uploads bukti setor, buku tabungan koperasi, screenshots of
   saldo, and any surat dari pengurus. The app timestamps and indexes them.
2. Dossier builder: auto-generate a ringkasan klaim (nama, no anggota, total setor, saldo
   terakhir, kronologi) plus a daftar bukti, ready to submit to OJK or join a class action.
3. Liquidation tracker: let the user paste or record updates from OJK/pengurus and see a
   timeline; flag when a statutory deadline passes.
4. Neutral third-party stance: the tool does not take a side on fault, it only assembles the
   victim's own records into a form the authorities accept. This neutrality is what makes it
   trustworthy when the government itself is struggling with case accuracy.

### 3.4 Module C: PKL Pungli Evidence and Anonymous Report

Jobs performed:

1. Levy logger: each time the trader is asked for uang, they tap a preset (retribusi,
   "keamanan", parkir liar), enter amount and location, attach a photo, and the app stores it
   privately.
2. Evidence vault: the trader owns the ledger; it is exportable as a PDF if they later want
   to act.
3. Anonymized report: one tap produces a report bundle with identifying details stripped
   (no name, no face), sent to the chosen authority or a vetted civil-society hotline. The
   design protects the victim from retaliation by default.
4. Pattern view: aggregated, anonymized heatmaps of levy frequency by location could later
   help authorities target enforcement. This is a future data product, not the MVP.

---

## 4. Technical architecture

### 4.1 High-level components

```
Mobile PWA (React/Preact, offline-first via Service Worker + IndexedDB)
  |
  +-- Intake engine (JSON-driven question sets per module)
  +-- Evidence vault (IndexedDB locally; optional E2E-encrypted cloud sync)
  +-- Document generator (HTML/CSS -> PDF via client or server)
  +-- Next-step navigator (rule table keyed by module + answers)
  |
Backend (optional, only for paid tier + sync + report relay)
  +-- Auth (phone OTP, no email required)
  +-- Encrypted blob storage (user-owned keys)
  +-- Report relay (strips PII, posts to authority API or email)
  +-- Admin queue (for done-for-you operators)
```

### 4.2 Why offline-first matters

The users are warung owners, PKL, and informal workers on cheap Android phones, often on
spotty 4G. The evidence vault must work with no signal. IndexedDB holds the data locally;
sync is a background, opt-in, encrypted operation. This is not a nice-to-have, it is the
difference between usable and abandoned.

### 4.3 Document generator sketch (Python, server side for paid tier)

```python
# docgen.py  -- turn a validated intake + evidence index into a formal surat
from dataclasses import dataclass
from datetime import date
from jinja2 import Template

@dataclass
class SlikDispute:
    nama: str
    nik: str
    institusi_pelapor: str      # bank / multifinance that reported the bad record
    no_rekening: str
    tanggal_pelunasan: date
    bukti_paths: list[str]       # local evidence refs
    keterangan: str

SLIK_TEMPLATE = Template("""
Nomor: {{ no_surat }}
Hal: Permohonan Koreksi Data SLIK
Lampiran: {{ bukti_count }} berkas bukti pelunasan

Kepada Yth.
{{ institusi_pelapor }}
Di Tempat

Yang bertanda tangan di bawah ini:

Nama        : {{ nama }}
NIK         : {{ nik }}
No. Rekening: {{ no_rekening }}

Dengan ini menyatakan bahwa data saya pada SLIK yang dilaporkan oleh
{{ institusi_pelapor }} dengan status "macet" adalah TIDAK BENAR, karena
pinjaman tersebut telah lunas pada tanggal {{ tanggal_pelunasan }}.

Bersama surat ini kami lampirkan bukti pelunasan sebanyak
{{ bukti_count }} berkas. Kami mohon {{ institusi_pelapor }} melakukan
koreksi data paling lambat 7 (tujuh) hari kerja sesuai kewajiban
pelaporan data yang akurat.

Apabila tidak dikoreksi, kami akan menyampaikan pengaduan konsumen
kepada OJK sesuai ketentuan perlindungan konsumen.

Hormat kami,
{{ nama }}
""")

def render(d: SlikDispute, no_surat: str) -> str:
    return SLIK_TEMPLATE.render(
        no_surat=no_surat, bukti_count=len(d.bukti_paths),
        tanggal_pelunasan=d.tanggal_pelunasan.isoformat(), **d.__dict__
    )
```

### 4.4 Anonymous report relay (Module C)

```python
# relay.py  -- strip PII, then forward a pungli report
import re, json

def anonymize(report: dict) -> dict:
    out = {
        "kategori": report["kategori"],          # retribusi / keamanan / parkir liar
        "lokasi": report["lokasi"],              # kecamatan / pasar, NOT home address
        "tanggal": report["tanggal"],
        "jumlah": report["jumlah"],
        "bukti_hash": [h for h in report.get("bukti_hash", [])],
    }
    # explicitly drop anything that could identify the victim
    out.pop("nama", None); out.pop("nik", None); out.pop("foto_wajah", None)
    return out

def forward(out: dict, target: str):
    # POST to authority API or vetted NGO inbox; never include the raw victim object
    payload = json.dumps(out, ensure_ascii=False)
    # requests.post(target, data=payload, headers={"Content-Type": "application/json"})
    return payload
```

### 4.5 Data model for the shared vault

```
evidence_item:
  id, module, owner_id (hash), created_at, type (pdf/jpg/txt),
  tags (date, amount, institution), encryption_key_id, pii_strippable (bool)

intake_session:
  id, module, answers (json), status (draft/submitted/tracked), next_step, due_date

generated_doc:
  id, session_id, template, pdf_path (encrypted), created_at
```

---

## 5. Pricing and willingness to pay

The vault rule is to state the price people would pay, not the price we want. The signal:

- A warung or PKL operator who is blocked from a KPR or KTA by a wrong SLIK record loses far
  more than Rp299.000. The relief value is the loan they can now get. Even a 1 percent chance
  of unblocking a Rp200 juta KPR justifies paying ratusan ribu for the toolkit.
- A KSP victim who lost Rp10 juta-Rp100 juta in savings will pay for a dossier that improves
  their odds of restitution, especially if it is cheaper than a lawyer by 100x.
- A PKL paying Rp50.000-Rp200.000 per day in pungli has a recurring loss; a tool that helps
  stop or document it is worth a small monthly fee or a per-report micro-payment.

Proposed pricing (to validate, not gospel):

- Free tier: SLIK explainer + self-serve dispute letter generator (template only).
- Paid self-serve: Rp49.000-Rp99.000 per completed document pack (PDF + submit guide).
- Done-for-you: Rp99.000-Rp299.000 per case for 30 days of operator-assisted follow-up.
- PKL module: Rp15.000-Rp30.000 per month for the evidence vault + anonymous report, or free
  with a donation model.

The wedge versus a lawyer (puluhan juta) is 100x to 1.000x cheaper. That ratio is the whole
business.

---

## 6. Risks and honesty about the gaps

- Regulatory risk: any tool that touches SLIK disputes or OJK complaints must stay strictly
  within consumer self-help. It must not impersonate OJK or guarantee outcomes. The paid tier
  is "administrative assistance," not legal representation, to avoid unauthorized-practice-of-law
  exposure under Indonesian advocate law.
- Trust risk: victims fear retaliation (especially PKL). The anonymity design is the product;
  a single leak destroys it.
- Accuracy risk: an auto-generated dossier is only as good as the user's own evidence. The
  tool must refuse to file when evidence is too thin and say so plainly.
- Monetization risk: marginal users have low ability to pay. The model likely needs a mix of
  paid urban cases (SLIK/KPR unblock) subsidizing free PKL tools, plus possible NGO or
  donor funding for the pungli module.
- Data reachability note: web_search and web_extract were unavailable this tick (the Parallel
  API key was not set in the sandbox), so live re-fetch of every deep article URL was not
  possible. The anchor facts above were pulled directly from publisher pages via curl (CNBC
  Indonesia Prolife article, 15 July 2026; Kontan and Detik Finance KSP/Indosurya coverage)
  and from the vault's own demand-mining evidence files, which already carry dates and
  outlets. Treat any specific deep-link not re-fetched this tick as "source recorded, not
  re-verified this tick." The regulatory facts (SLIK is OJK's credit database, free SLIK check
  via OJK, disputes route to the reporting institution first) are consistent with OJK's public
  consumer-protection materials at https://www.ojk.go.id and the SLIK information page at
  https://www.ojk.go.id/id/kanal/perbankan/Pages/Sistem-Layanan-Informasi-Keuangan-SLIK.aspx
  (that page blocked automated fetch this tick; verify before citing the exact URL in copy).

---

## 7. Build sequence and what "done" looks like

Phase 1 (MVP, pillar A only): SLIK explainer + dispute letter generator + free check guide.
This is the fastest to validate willingness to pay because the loss (blocked loan) is acute
and the user is reachable via finance communities.

Phase 2 (pillar B): KSP claim dossier builder, validated against a real ongoing liquidation so
the next-step navigator reflects reality.

Phase 3 (pillar C): PKL evidence vault + anonymous report, piloted with one pasar or one
ormas-watch NGO.

Phase 4 (cross-sell): surface the shared core so a user who came for SLIK repair is offered
the KSP dossier if they also mention a cooperative, and vice versa.

Definition of done for the MVP: a user with a paid-off but still-flagged SLIK record can, in
under 20 minutes on a phone, produce a correctly formatted permohonan koreksi with their
bukti attached and know exactly where to send it. That single job, done well and cheaply, is
the wedge.

---

## 8. How this connects to the rest of the vault

- Directly extends `07-gaps-and-opportunities/opportunities/loker-scam-verifier.md` (another
  micro legal-tech for victims of job scams) and `07-gaps-and-opportunities/opportunities/qris-mdr-transparency-layer.md`
  (cheap transparency layer for warung). Same pricing philosophy: ratusan ribu, not puluhan juta.
- Feeds the demand-mining evidence: `korban-gagal-bayar-koperasi-simpan-pinjam.md`,
  `klaim-jkp-ditolak-berkas-tidak-valid.md`, `pkl-dipalak-preman-berkedok-ormas.md`,
  `jukir-liar-palak-pengendara-minimarket-jalanan.md`, `ktp-dipakai-pinjol-atas-nama.md`.
- Complements `07-gaps-and-opportunities/opportunities/desil-dormant-checker-saas.md` (another
  checker that tells marginalized users their status in a government system).

---

## 9. Open questions to kill before building

- Will users pay Rp99.000-Rp299.000 upfront, or only after the record is fixed (pay-on-result,
  which creates incentive-alignment but also fraud surface)?
- Can the anonymous report actually reach an authority that acts, or does it become a dead
  letter drop? Pilot with one real NGO first.
- Is the SLIK dispute actually winnable self-serve, or does every institution just say "wait,"
  making the done-for-you tier the only thing that works (and therefore the only thing worth
  charging for)?
- Does the KSP dossier materially change restitution odds, or is it emotional closure only?
  Validate with one real liquidation before scaling.

These are the questions that decide whether this is a business or a charity. Research them
before writing a line of production code.

---

## 10. Technical deep-dive: data schema and validation

This section gives the concrete schema and validation code so an engineer can build the
shared core without re-deriving it. The design target is a single SQLite (local, for the PWA
IndexedDB mirror) plus an optional Postgres (server, paid tier + sync) with identical schema.

### 10.1 Evidence vault schema (SQL)

```sql
-- shared across all three modules; the vault is user-owned and encrypted at rest
CREATE TABLE evidence_item (
    id              TEXT PRIMARY KEY,          -- UUID v4, client-generated
    owner_hash      TEXT NOT NULL,             -- HMAC(NIK or phone) not the raw id
    module          TEXT NOT NULL              -- 'slik' | 'ksp' | 'pkl'
                    CHECK (module IN ('slik','ksp','pkl')),
    created_at      INTEGER NOT NULL,          -- epoch ms, set client-side
    type            TEXT NOT NULL,             -- 'pdf' | 'jpg' | 'png' | 'txt' | 'csv'
    tags            TEXT NOT NULL,             -- JSON array: [date, amount, institution]
    pii_strippable  INTEGER NOT NULL DEFAULT 1,-- 1 if safe to strip for anonymous relay
    enc_key_id      TEXT NOT NULL,             -- which user key encrypted the blob
    blob_ref        TEXT NOT NULL,             -- local path or encrypted cloud key
    deleted         INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX idx_ev_module ON evidence_item(module, owner_hash) WHERE deleted = 0;

CREATE TABLE intake_session (
    id              TEXT PRIMARY KEY,
    owner_hash      TEXT NOT NULL,
    module          TEXT NOT NULL,
    answers         TEXT NOT NULL,             -- JSON, schema validated per module
    status          TEXT NOT NULL              -- draft|submitted|tracked|closed
                    CHECK (status IN ('draft','submitted','tracked','closed')),
    next_step       TEXT,                      -- human-readable next action
    due_date        INTEGER,                   -- epoch ms reminder
    created_at      INTEGER NOT NULL,
    updated_at      INTEGER NOT NULL
);

CREATE TABLE generated_doc (
    id              TEXT PRIMARY KEY,
    session_id      TEXT NOT NULL REFERENCES intake_session(id),
    template        TEXT NOT NULL,             -- 'slik_dispute' | 'ksp_dossier' | 'pkl_report'
    pdf_ref         TEXT NOT NULL,             -- encrypted blob ref
    created_at      INTEGER NOT NULL
);

CREATE TABLE report_relay (
    id              TEXT PRIMARY KEY,
    session_id      TEXT NOT NULL,
    target          TEXT NOT NULL,             -- authority API or NGO inbox id
    sent_at         INTEGER,
    status          TEXT NOT NULL DEFAULT 'pending' -- pending|sent|failed|acked
);
```

### 10.2 Input validation per module (Python, used by the paid-tier backend)

```python
# validate.py  -- reject thin or impossible intakes before generating any doc
import re, json
from datetime import date

NIK_RE = re.compile(r'^\d{16}$')
PHONE_RE = re.compile(r'^(?:\+62|62|0)8\d{7,12}$')

def validate_slik(d: dict) -> list[str]:
    errs = []
    if not NIK_RE.match(d.get('nik', '')):
        errs.append('NIK harus 16 digit angka.')
    if not d.get('institusi_pelapor'):
        errs.append('Harus diisi: institusi yang melaporkan data SLIK.')
    if not d.get('no_rekening'):
        errs.append('Harus diisi: nomor rekening pinjaman.')
    try:
        pd = date.fromisoformat(d['tanggal_pelunasan'])
        if pd > date.today():
            errs.append('Tanggal pelunasan tidak boleh di masa depan.')
    except Exception:
        errs.append('Format tanggal pelunasan salah (YYYY-MM-DD).')
    if len(d.get('bukti_paths', [])) < 1:
        errs.append('Lampirkan minimal 1 bukti pelunasan (transfer/receipt).')
    return errs

def validate_ksp(d: dict) -> list[str]:
    errs = []
    if not d.get('nama_koperasi'):
        errs.append('Harus diisi: nama koperasi.')
    try:
        total = float(d['total_setor'])
        if total <= 0:
            errs.append('Total setor harus lebih dari nol.')
    except Exception:
        errs.append('Total setor harus angka (tanpa titik/koma).')
    if len(d.get('bukti_paths', [])) < 1:
        errs.append('Lampirkan bukti setor (buku tabungan / mutasi).')
    return errs

def validate_pkl(d: dict) -> list[str]:
    errs = []
    if d.get('jumlah') is None:
        errs.append('Harus diisi: jumlah uang yang diminta.')
    if not d.get('lokasi'):
        errs.append('Harus diisi: lokasi (pasar/kecamatan, BUKAN alamat rumah).')
    # deliberately: no NIK, no name. Anonymity is the product.
    return errs
```

### 10.3 Why validation refuses thin evidence

Each validator returns a non-empty error list when evidence is missing. The document generator
must refuse to produce a "submitted-ready" PDF when errors exist. Instead it returns a draft
with the missing items flagged in plain Bahasa. This is the honesty guard: the tool never
implies a case is strong when the user's own records are thin. It says "lengkapi dulu" and
tells them exactly what is missing.

### 10.4 The next-step navigator as a rule table

```python
# navigator.py  -- pure function, easy to test, easy to localize
NAV = {
    'slik': {
        'has_bukti':  ('Kirim permohonan koreksi ke {institusi} via surat + email resmi.',
                       'Tunggu 7 hari kerja. Jika tidak ada respons, lanjut ke OJK.'),
        'no_bukti':   ('Kumpulkan dulu bukti pelunasan (transfer/receipt).',
                       'Tanpa bukti, institusi akan menolak koreksi.'),
    },
    'ksp': {
        'default':    ('Susun dossier, serahkan ke OJK kanal pengaduan konsumen.',
                       'Pantau status likuidasi via pengumuman OJK.'),
    },
    'pkl': {
        'default':    ('Simpan bukti di vault. Untuk lapor, tekan "Lapor Anonim".',
                       'Jangan cantumkan nama/alamat rumah pada laporan.'),
    },
}

def next_steps(module: str, answers: dict) -> tuple[str, str]:
    table = NAV.get(module, {})
    if module == 'slik':
        key = 'has_bukti' if answers.get('bukti_paths') else 'no_bukti'
        act, wait = table[key]
        return act.format(institusi=answers.get('institusi_pelapor','')), wait
    return table.get('default', ('Hubungi layanan bantuan.', ''))
```

---

## 11. Provider and authority adapter layer

The paid tier needs to actually reach the right institution or authority. Each is a small
adapter behind one interface so adding a new one is a config change, not a rewrite.

```python
# adapters.py  -- one interface, many implementations
from abc import ABC, abstractmethod

class AuthorityAdapter(ABC):
    name: str
    @abstractmethod
    def submit(self, payload: dict) -> dict:
        """Return {'status': 'sent'|'failed', 'ref': str}"""

class OjkComplaintAdapter(AuthorityAdapter):
    name = 'ojk'
    # POST to OJK consumer-complaint API or generate the email-ready bundle
    def submit(self, payload):
        # in practice: render the dossier to a single PDF and either POST to the
        # OJK portal or hand the user a pre-addressed email. OJK portal auth and
        # exact endpoint must be verified live before production (Cloudflare-gated
        # this tick; see section 6 reachability note).
        return {'status': 'sent', 'ref': 'OJK-' + payload.get('session_id','')}

class SlikInstitutionAdapter(AuthorityAdapter):
    name = 'slik_inst'
    def submit(self, payload):
        # each bank/multifinance has its own channel; store the known ones in a table
        return {'status': 'sent', 'ref': payload.get('institusi_pelapor','')}

class PklAnonymousRelay(AuthorityAdapter):
    name = 'pkl_relay'
    def submit(self, payload):
        anonymized = anonymize(payload)        # from relay.py in section 4.4
        # forward to Satpol PP API / Polri / vetted NGO; never include raw victim object
        return {'status': 'sent', 'ref': 'PKL-' + payload.get('lokasi','')}
```

---

## 12. Privacy, security, and the anonymity guarantee

The PKL module's entire value is that victims will not be identified. Concretely:

- No name, NIK, or face photo is ever stored in the pkl evidence vault by default. The schema
  for pkl omits those columns; only kategori, lokasi (public place, not home), tanggal, jumlah,
  and bukti_hash are kept.
- The relay strips PII server-side even if the client sent it (defense in depth).
- The evidence vault is encrypted with a user-held key (derived from phone OTP + device key).
  The server stores only ciphertext; a compromise yields nothing usable.
- The SLIK and KSP modules DO need identity (NIK, name) because the dispute is about the
  user's own record. That is a different trust boundary and is disclosed explicitly in the
  intake: "Data ini digunakan untuk mengajukan koreksi atas nama Anda."

A threat model worth writing down: the biggest risk is not a server breach but a subpoena or
a leak that de-anonymizes a PKL reporter. The design answer is that the server never had the
PII to begin with, so there is nothing to leak. That property must be tested, not assumed.

---

## 13. Go-to-market and where the users actually are

- SLIK repair: finance-themed WhatsApp groups, the r/finansial (and Indonesian personal-finance
  communities), TikTok "pinjol survivor" creators, and warung/UMKM associations. The message is
  "cek SLIK gratis, benerin kalau salah, cuma ratusan ribu."
- KSP dossier: victim support groups that already form after a KSP collapse (these appear on
  social media within days of a failure), and cooperative ministry grievance channels.
- PKL: on the ground at pasar, through PKL associations, and via ormas-watch NGOs that already
  collect reports. A free tool spreads by word of mouth in a pasar faster than any ad.

The cross-sell is natural because the same person often has two of the three problems: a PKL
who was extorted may also have a blocked SLIK from a failed pinjol, and may also have lost
savings in a KSP. One umbrella, three doors.

---

## 14. Competitor and non-competitor landscape

- OJK and the cooperative ministry: free, authoritative, but not productized and not guided.
  We are not competing with them; we route to them. Potential partner, not rival.
- LBH / legal aid: mission-aligned, capacity-limited, geography-bound. We could refer heavy
  cases to them and take the light, high-volume cases they cannot serve.
- Commercial "konsultan hukum" and lawyers: 100x more expensive. We do not replace them for
  complex litigation; we replace the Rp299.000 administrative step they would bill puluhan
  juta for.
- Other micro legal-tech in the vault (loker-scam-verifier, desil-dormant-checker): siblings,
  not competitors. A bundle play: "cek status pemerintah + benerin kalau salah" across SLIK,
  DTKS/desil, and job-scam surfaces from one account.

The moat is the shared intake-plus-document engine and the user-owned evidence vault, not any
single letter template. Templates are commodity; the engine that assembles them from a
person's own records, safely and cheaply, is the asset.

---

## 15. Metrics that decide survival

- SLIK module: percent of paid cases where the institution confirms correction within 14 days.
  If it stays near zero, the self-serve tier is theater and only the done-for-you tier has
  value. That changes the whole pricing and headcount plan.
- KSP module: percent of dossiers the user reports as "accepted by OJK without resubmission."
  Acceptance-on-first-try is the only metric that matters; resubmission means the dossier was
  wrong and the tool failed its one job.
- PKL module: reports sent per active user per month, and (with NGO partners) reports that
  led to enforcement action. If sent-but-never-acted, the relay is a dead letter and the
  module becomes a journaling app, not a tool.
- Unit economics: average revenue per paid user must exceed acquisition + operator cost by
  3x within 90 days of the paid tier launch, or the model is charity.

---

## 16. Pilot runbook (first 30 days, pillar A only)

Week 1: ship the SLIK explainer + free check guide as a static PWA. No auth, no storage.
Measure: how many people open it, how far they scroll, how many tap "mulai."
Week 2: add the dispute letter generator (self-serve, Rp49.000 per pack). Recruit 50 testers
from a personal-finance community. Measure: completion rate, payment rate, and a 2-week
follow-up on whether their record moved.
Week 3: add the done-for-you tier (Rp199.000) with one operator. Cap at 20 cases. Measure:
operator time per case, correction rate, refund/refusal rate.
Week 4: decide. If correction rate in done-for-you is materially above self-serve, lead with
done-for-you and price it higher. If self-serve already works, kill the operator cost and
scale the cheap tier.

Do not build pillar B or C until pillar A shows a real correction rate. The engine is reused,
but the willingness-to-pay hypothesis is what is unproven, and pillar A is the cheapest place
to prove it.

---

## 17. Anti-abuse and fraud-surface controls for the paid tier

A tool that helps people fight scams is itself a target for abuse, by two opposite groups:
scammers impersonating the service to harvest NIK/bukti, and users gaming the SLIK dispute to
erase a legitimate debt. Both must be designed against.

- Impersonation defense: the app never asks for a full NIK over an unencrypted channel and
  never sends bukti to anyone except the user-named institution via the adapter. All
  communications come from one verified sender id. A scammer clone will lack the encrypted
  vault and the signed PDF; users are taught to check the sender id in onboarding.
- Dispute gaming defense: the validator requires real bukti (a transfer receipt with a date
  and amount). A user trying to erase a legitimately unpaid debt has no bukti, so validation
  fails and no disputable letter is produced. The tool explicitly states it will not generate
  a dispute without evidence, which also keeps it on the right side of consumer-protection law.
- Operator integrity: in the done-for-you tier, the operator handles sensitive data. Logs are
  append-only, every send is recorded with a ref, and the user can see the full action history.
  An operator who "fixes" a record without sending is detectable, because the relay ref is
  shown to the user.
- Money-laundering adjacency: a KSP dossier that suddenly shows a huge saldo with no bukti is a
  red flag. The tool should refuse to generate such a dossier and, where required by law,
  the reporting of suspicious structuring is the user's responsibility, not the tool's blind
  enabler. The honesty guard applies here too: thin or impossible claims are refused, not filed.

These controls are not optional polish. They are what keep the product legal and trusted. A
micro legal-tech that becomes a dispute-fraud factory gets shut down, and rightly so.

## 18. FAQ (plain Bahasa, for the in-app help)

- "Apakah ini jasa hukum resmi?" Tidak. Ini bantuan administrasi: menyusun dokumen dan
  panduan pengaduan. Untuk gugatan, hubungi LBH atau pengacara.
- "Apakah data saya aman?" Untuk modul PKL, kami tidak menyimpan nama/NIK. Untuk SLIK/KSP,
  data wajib ada karena laporan atas nama Anda, dan disimpan terenkripsi.
- "Apakah jaminan SLIK saya pasti hilang?" Tidak ada jaminan. Kami bantu mengajukan koreksi
  kalau bukti Anda lengkap. Kalau tidak lengkap, kami bilang terus terang.
- "Berapa lama?" Surat jadi dalam 20 menit. Respons institusi 7 hari kerja. OJK bisa lebih
  lama. Kami pantau dan ingatkan Anda.

---

## 18. Why now (timing and tailwinds)

Three things make this window better than it was two years ago. First, the OJK consumer
complaint and SLIK self-check infrastructure exists and is free, which was not uniformly true
before; the job is now "guide the user through what already exists," not "build the registry."
Second, the KSP Indosurya and Prolife/Indosurya cases have put cooperative fraud and insurance
misselling squarely in public view through 2023-2026, so victims are searching for help and
civil society is organized. Third, cheap on-device AI (tiny local models on Android) now makes
a guided intake that understands photos of bukti transfer practical without sending sensitive
data to the cloud, which closes the privacy gap that killed earlier attempts. None of these
alone is a business, but together they lower the build cost and raise the reachable demand at
the same time. The risk is not feasibility, it is willingness to pay, which is exactly what the
30-day pillar-A pilot is designed to measure before any larger build.

## 19. Sources (real, with dates; see reachability note in section 6)

- CNBC Indonesia, "OJK Serahkan Kasus Prolife ke Kejaksaan, Henry Surya Jadi Tersangka,"
  15 July 2026, https://www.cnbcindonesia.com/market/20260715174137-17-751097/ojk-serahkan-kasus-prolife-ke-kejaksaan-henry-surya-jadi-tersangka
  (OJK revoked PT Asuransi Jiwa Indosurya Sukses license 2 Nov 2023; ordered Rp566,24 miliar
  compensation to policyholders via Surat S-45/D.05/2023 dated 13 Oct 2023; Henry Surya also
  convicted in KSP Indosurya fraud.)
- Detik Finance, "Ada Kabar Koperasi Merah Putih di Melawai Cuma Untung Rp 78.000, Menkop Buka
  Suara," 15 July 2026, https://finance.detik.com/berita-ekonomi-bisnis/d-8575236/ada-kabar-koperasi-merah-putih-di-melawai-cuma-untung-rp-78000-menkop-buka-suara
- Detik Finance, "Indomaret, FamilyMart, dan Koperasi Desa Merah Putih," 14 July 2026,
  https://finance.detik.com/berita-ekonomi-bisnis/d-8573610/indomaret-familymart-dan-koperasi-desa-merah-putih
- Tempo.co (Bisnis), "Menteri Ferry Jelaskan Gaji Pegawai Koperasi Merah Putih," 16 July 2026,
  https://bisnis.tempo.co/read/2113892/menteri-ferry-jelaskan-gaji-pegawai-koperasi-merah-putih
- OJK consumer protection / SLIK public materials, https://www.ojk.go.id and
  https://www.ojk.go.id/id/kanal/perbankan/Pages/Sistem-Layanan-Informasi-Keuangan-SLIK.aspx
  (free SLIK check via OJK; disputes route to the reporting institution first; page blocked
  automated fetch this tick, verify exact URL before citing in copy).
- Vault demand-mining evidence files (carry their own outlet citations):
  `03-id-business-trends/demand-mining/korban-gagal-bayar-koperasi-simpan-pinjam.md`,
  `03-id-business-trends/demand-mining/klaim-jkp-ditolak-berkas-tidak-valid.md`,
  `03-id-business-trends/demand-mining/pkl-dipalak-preman-berkedok-ormas.md`,
  `03-id-business-trends/demand-mining/jukir-liar-palak-pengendara-minimarket-jalanan.md`,
  `03-id-business-trends/demand-mining/ktp-dipakai-pinjol-atas-nama.md`.
- Promoted from `07-gaps-and-opportunities/inbox/2026-07-09-slik-pungli-koperasi-tools.md`
  (original mined pain-point note, 2026-07-09).

## 20. One-paragraph thesis

The throughline of this one-pager is that Indonesia's marginal economic actors, warung owners,
PKL, informal workers, and small savers, lose money not mainly to single big frauds but to a
thousand small administrative defeats: a wrong SLIK flag, an unclaimed KSP loss, a weekly pungli
they cannot report. Each defeat is individually too small to justify a lawyer yet collectively
enormous across tens of millions of people. A micro legal-tech umbrella priced in ratusan ribu,
built on one reusable intake-plus-document engine and a user-owned evidence vault, attacks all
three at once. The decisive unknown is not whether the tool can be built, it is whether people
will pay for it, so the first shipped artifact must be the pillar-A SLIK repair pilot and its
measured correction rate, not a polished three-module suite.

<!-- end of document -->
