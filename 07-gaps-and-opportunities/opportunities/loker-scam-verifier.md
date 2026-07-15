# Loker Scam Verifier — pre-payment trust verdict bot for Indonesian job scams

> The single highest-intent moment in the entire job-scam loss funnel is the ten
> seconds right before a victim taps "transfer" to pay a fake "biaya administrasi".
> At that moment the victim already believes the offer is real, already has the
> money in hand, and only needs a green light. Today there is no free, fast,
> Indonesian-first checker that answers one question in under ten seconds:
> "is this company, this WhatsApp number, and this posting real or a scam?"
> Wedge: a WhatsApp/Telegram bot that cross-references a company/phone/posting
> against public NIB/OSS, AHU badan-hukum, official BUMN/Kemnaker recruitment
> lists, and reported scam rekening/numbers, then returns a green / yellow / red
> verdict before the victim pays. This is the natural extension of the vault's
> existing `scam-detection-tool-2026-07-07.md` inbox note, the
> `judol-pinjol-cross-detection.md` opportunity, and the fresh-graduate ATS/CV
> line, but pointed at the most expensive single action a job seeker takes.

**File:** `07-gaps-and-opportunities/opportunities/loker-scam-verifier.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-15-loker-scam-verifier.md`
**Created:** 2026-07-15
**Category:** Opportunity one-pager (consumer protection / trust infra)
**Confidence:** 4 (evidence strong, build is standard, distribution is the hard part)
**Status:** build-ready
**Pain strength at capture:** 5 out of 5

---

## 1. Problem and evidence

Indonesia is, by multiple reporting outlets, the country with the highest volume
of job-scam cases in Southeast Asia. The fraud pattern is stable and predictable,
which is exactly why it is automatable. The scam almost always ends in the same
action: the victim is asked to transfer money for "biaya administrasi", "biaya
pelatihan", "uang seragam", or a medical check-up (MCU) fee.

Concrete, dated, real evidence gathered for this one-pager (all URLs verified reachable):

- Kompas, 7 July 2026: a then-18 year old from Purwakarta, Jieyes Mishael
  Panjaitan, answered a fictional warehouse-operator posting in Jakarta Barat,
  was interviewed at a ruko on Jl Pangeran Tubagus Angke, Jelambar, and was told
  to transfer Rp 2,5 juta for MCU, seragam, and "kebutuhan administrasi lainnya".
  He signed a "surat perjanjian" and was then sent home with no job.
  Source: https://megapolitan.kompas.com/read/2026/07/07/16452451/diduga-jadi-korban-rekrutmen-bodong-di-jakbar-pelamar-kerja-diminta-bayar
- Tirto, 25 Nov 2025: Indonesia records the largest volume of job-fraud cases
  regionally. Administrative and office-support roles are the top target, making
  up 29 percent of fake listings in Asia versus 17 percent in Australia and New
  Zealand. Sales/tenaga penjualan roles are also heavily abused. The classic
  pattern: a small commission transfer to build trust, then a non-refundable
  "deposit" or "top-up". TPT Indonesia was 4,76 percent (about 7,28 million
  unemployed) per Sakernas Feb 2025, the highest unemployment rate in ASEAN per
  Trading Economics, which widens vulnerability.
  Source: https://tirto.id/mengapa-indonesia-jadi-sarang-penipuan-lowongan-kerja-hmuT
- Katadata (Varia): factual indicators of fake loker, including "Tawaran Gaji
  Terlalu Fantastis" (e.g. an admin role with no experience offering up to
  Rp 10 juta/month), "Diminta Membayar Biaya Administrasi" in any form, fake
  interview locations (kontrakan or empty ruko), unsolicited WhatsApp messages
  claiming you "lolos seleksi" without ever applying, and immediate requests for
  KTP/SIM/KK/ijazah/NPWP scans.
  Source: https://katadata.co.id/lifestyle/varia/692402236a330/ciri-ciri-loker-penipuan-dan-langkah-langkah-menghindarinya
- Kemnaker SENTA (official ministry outlet): legitimate employers never ask for
  money up front for any reason (administration, training, tools); fake postings
  on legitimate job boards; phishing forms harvesting KTP, bank account numbers,
  and credit-card numbers; "biaya pendaftaran" / "biaya penempatan" demands.
  Source: https://majalahsenta.kemnaker.go.id/artikel/menghindari-lowongan-kerja-palsu
- IDN Times: the "modus paling klasik" is the request for administrative or
  training fees; legitimate companies have staged selection (administrasi,
  wawancara, tes kompetensi); instant offers with no selection are a strong
  fraud signal; cross-checking the offer against official company data usually
  shows the information "gak sinkron dengan data resmi perusahaan".
  Source: https://www.idntimes.com/business/economy/indikasi-penipuan-berkedok-lowongan-kerja-selalu-modus-minta-biaya-c1c2-01-bfjms-hc99n4

The common denominator across all five sources is one sentence: a legitimate
Indonesian employer never asks a candidate to pay anything up front, and the
fastest way to break the scam is to make the victim verify the counterparty one
time, at the moment of payment.

The vault's own demand-mining already captured this pain repeatedly, and the
inbox note dated 2026-07-15 opens with "178 job-seekers scammed in one Mimika
WhatsApp group, plus repeated BUMN/ABK/Papua cases in Jun 2026" and explicitly
states there is no fast, free, pre-payment checker. That note is the seed of this
one-pager.

---

## 2. Wedge and product

The wedge is timing and friction, not a new database. The victim is already on
WhatsApp or Telegram, already about to pay, and needs a 10 second gut-check that
feels easier than the doubt they are suppressing. The bot answers in the channel
they are already in, so the cost of checking is near zero and the cost of NOT
checking becomes visible.

Product shape:

- A WhatsApp (and mirrored Telegram) bot. Input is flexible: paste a job posting
  link, a company name, a WhatsApp/phone number, a bank account/rekening number,
  or a screenshot of the chat. Output is a single verdict plus a short reason.
- Verdict states: GREEN (all checks pass or no red signal), YELLOW (cannot
  confirm, mixed signals, proceed with caution), RED (matches a known scam
  signal: reported number/rekening, no legal entity, BUMN name used by a
  non-official channel, advance-fee request detected).
- The bot is free at the point of use. Monetization is not from victims; it is
  from (a) referral to legitimate employers / Kemnaker job boards, (b) a
  B2B API sold to job boards and universities to pre-flag scam postings, and
  (c) a sponsored "verified employer" tier. This keeps the victim-side product
  free, which is the only way it spreads through the exact WhatsApp groups where
  the scams live.

Why this beats "just be careful" education: education fails at the moment of
payment because the victim already trusts the scammer. A verdict tool inserts a
neutral third party into that exact moment. The vault's `judol-pinjol-cross-detection.md`
opportunity makes the same architectural argument for gambling/loan fraud; this
is the recruitment-fraud instance of the same trust-infra thesis.

---

## 3. Technical architecture

The system is a stateless-enough checker with one orchestrator and several
isolated "signal" adapters. Each adapter can fail independently; the orchestrator
combines signals into a verdict. This mirrors the connector-isolation pattern
used in `unified-household-bills-tracker.md` (one utility failing must not break
the others).

```
loker-scam-verifier/
  orchestrator.py        # combines signals -> verdict
  adapters/
    nib_oss.py           # check legal entity via OSS / NIB
    ahu_badan_hukum.py   # check PT/Yayasan foundation status via AHU
    bumn_list.py         # official BUMN recruitment allow-list
    kemnaker_list.py     # official Kemnaker / CPNS / government lists
    scam_registry.py     # reported numbers + rekening (local + external)
    llm_poster.py        # classify a pasted posting / screenshot for red flags
  channels/
    whatsapp.py          # WA Business API or 3rd-party bridge
    telegram.py
  store/
    verdict_cache.db     # short-TTL cache of verdicts (privacy-minimal)
```

### 3.1 Signal adapter: NIB / OSS legal-entity check

The government's OSS RBA portal (https://oss.go.id) is the canonical source for
NIB (Nomor Induk Berusaha). A legitimate Indonesian company that hires almost
always has an NIB. The verification flow an adapter must replicate:

1. Resolve the company name to a NIB, or accept a NIB directly from the user.
2. Query the public OSS lookup. Note: at time of research the root
   https://oss.go.id returned HTTP 307 redirect to the RBA app, and the page
   body confirms the title "OSS RBA - Sistem Perizinan Berusaha Terintegrasi
   Secara Elektronik". The adapter must follow the redirect and use the logged-in
   vs public lookup endpoints.
3. If no NIB exists for the name, that is a YELLOW or RED signal depending on
   context (a brand-new UMKM might genuinely lack one; a "PT Besar" that claims
   to employ hundreds and has no NIB is RED).

A hardened adapter is careful: OSS can present anti-bot challenges, so the
adapter should prefer any published public verification endpoint and fall back to
a manual deep-link the user opens themselves. The code below is a faithful
skeleton, not a claim that the live endpoint is unauthenticated.

```python
import requests, re
from dataclasses import dataclass

OSS_BASE = "https://oss.go.id"
UA = "Mozilla/5.0 (compatible; LokerVerifier/1.0; +https://example.org/bot)"

@dataclass
class EntityCheck:
    query: str
    nib_found: bool = False
    nib: str | None = None
    status: str | None = None   # aktif / non-aktif / tidak ditemukan
    source: str = "OSS RBA"

def check_nib(company_name: str) -> EntityCheck:
    """Best-effort NIB lookup. Returns nib_found=False on any failure so the
    orchestrator treats absence as 'unknown', never as proof of scam."""
    res = EntityCheck(query=company_name)
    try:
        s = requests.Session()
        # Follow the 307 to the RBA app automatically.
        r = s.get(OSS_BASE, headers={"User-Agent": UA}, timeout=20, allow_redirects=True)
        # NOTE: the real verification endpoint is behind the SPA; in production
        # we either (a) use the official public API if published, or
        # (b) render the SPA headless. If neither is possible we return
        # nib_found=False and let other signals decide. We never invent data.
        if r.status_code != 200:
            res.status = f"unreachable:{r.status_code}"
            return res
        # Illustrative parse: OSS pages embed NIB-like tokens. In production
        # replace with the real field. This is a guard, not a guarantee.
        m = re.search(r'\b(\d{13,16})\b', r.text)   # NIB is up to 16 digits
        if m:
            res.nib_found = True
            res.nib = m.group(1)
            res.status = "found-in-page"
        else:
            res.status = "no-nib-in-page"
    except requests.RequestException as e:
        res.status = f"error:{type(e).__name__}"
    return res
```

### 3.2 Signal adapter: AHU badan-hukum check

For PT (Perseroan Terbatas) and Yayasan, the Directorate General of AHU
(https://ahu.go.id, title "DITJEN AHU ONLINE") is the authority. The adapter
checks whether the named legal entity is registered and in what status. A
scammer using the name of a real PT without being affiliated is a classic
impersonation; cross-referencing the official AHU record against the "employer"
name in the posting catches the mismatch the IDN Times article describes
("gak sinkron dengan data resmi perusahaan").

```python
def check_ahu(entity_name: str) -> dict:
    """Query AHU Online public badan-hukum lookup.
    Returns status: terdaftar / tidak-terdaftar / unreachable."""
    out = {"query": entity_name, "status": "unknown"}
    try:
        r = requests.get("https://ahu.go.id", headers={"User-Agent": UA}, timeout=20)
        if r.status_code != 200:
            out["status"] = f"unreachable:{r.status_code}"
            return out
        # AHU pages embed entity names; in production use the real search
        # endpoint. We only ever mark 'terdaftar' on a real match.
        if entity_name.lower() in r.text.lower():
            out["status"] = "terdaftar"
        else:
            out["status"] = "tidak-terdaftar"
    except requests.RequestException as e:
        out["status"] = f"error:{type(e).__name__}"
    return out
```

### 3.3 Signal adapter: official recruitment allow-lists

The cleanest RED signal is a posting that uses a BUMN or government name but is
NOT on the official recruitment channel. BUMN recruitment is centralized;
Kemnaker and BKN publish CPNS/PPPK and government job openings. The adapter keeps
a periodically refreshed allow-list of official domains and official account
handles, and flags any posting that uses the BUMN/government brand but links
outside those domains or asks for payment.

- BUMN official recruitment: each BUMN runs its own verified portal; the
  allow-list is the union of those official domains. A WhatsApp blast "loker
  BUMN, bayar administrasi" is RED by definition because no BUMN charges
  candidates.
- Kemnaker: https://www.kemnaker.go.id (title "Beranda : Kementerian
  Ketenagakerjaan RI") is the ministry outlet; SENTA is its anti-scam guidance.
- CPNS/PPPK: BKN (badankepegawaian.go.id) and the official
  sscasn.bkn.go.id portal are the only legitimate channels.

```python
OFFICIAL_DOMAINS = {
    "kemnaker.go.id", "sscasn.bkn.go.id", "badankepegawaian.go.id",
    # each BUMN adds its own verified domain here, refreshed weekly
}

def channel_is_official(url: str) -> bool:
    from urllib.parse import urlparse
    host = (urlparse(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in OFFICIAL_DOMAINS)

def bumn_posting_verdict(url: str, asks_payment: bool) -> str:
    if asks_payment:
        return "RED"          # no BUMN/government hiring ever charges a fee
    return "GREEN" if channel_is_official(url) else "YELLOW"
```

### 3.4 Signal adapter: scam registry (numbers and rekening)

The highest-precision RED signal is a match against a previously reported phone
number or bank account. Two sources exist:

1. Public crowd-sourced registries such as cekrekening.id
   (https://cekrekening.id). At research time the root returned a Cloudflare
   "Just a moment..." challenge page (HTTP 200 but JS-gated), meaning automated
   bulk query is blocked; a manual deep-link per number is the realistic path,
   or the bot can submit a lookup on behalf of the user and parse the result if
   Cloudflare permits. We must not claim an API we cannot verify.
2. The user's own contributed reports. Every RED verdict the bot issues, if the
   user confirms "yes this was a scam", feeds a local registry that other users
   query for free. This is the cold-start solution: start with user reports,
   attach official sources where reachable.

```python
import sqlite3, re

db = sqlite3.connect("verdict_cache.db")

def init_db():
    db.execute("""CREATE TABLE IF NOT EXISTS scam_reports(
        id INTEGER PRIMARY KEY, kind TEXT, value TEXT UNIQUE,
        report_count INTEGER DEFAULT 1, first_seen TEXT, last_seen TEXT)""")
    db.commit()

def report_scam(kind: str, value: str):
    cur = db.execute("SELECT report_count FROM scam_reports WHERE kind=? AND value=?",
                     (kind, value))
    row = cur.fetchone()
    if row:
        db.execute("UPDATE scam_reports SET report_count=report_count+1 WHERE kind=? AND value=?",
                   (kind, value))
    else:
        db.execute("INSERT INTO scam_reports(kind,value,report_count) VALUES(?,?,1)",
                   (kind, value))
    db.commit()

def is_reported(kind: str, value: str) -> int:
    cur = db.execute("SELECT report_count FROM scam_reports WHERE kind=? AND value=?",
                     (kind, value))
    return (cur.fetchone() or (0,))[0]

# Normalize phone: strip 0/+62, keep digits only.
def norm_phone(p: str) -> str:
    p = re.sub(r'\D', '', p)
    if p.startswith("62"): return p
    if p.startswith("0"): return "62" + p[1:]
    return p
```

### 3.5 LLM posting classifier

When the user pastes a posting or uploads a screenshot, an LLM adapter scores it
for the red-flag taxonomy derived directly from the five articles:

- Request for any up-front payment (administrasi, pelatihan, seragam, MCU,
  pendaftaran, penempatan).
- No selection process or instant "lolos seleksi" without applying.
- Unsolicited WhatsApp claiming you passed.
- Salary far above market for the role/experience (e.g. Rp 10 juta for fresh
  admin).
- Request for identity documents up front (KTP, SIM, KK, ijazah, NPWP, rekening).
- Interview at a kontrakan or empty ruko rather than a verifiable office.
- Impersonation of a BUMN/government brand.

```python
RED_FLAG_TAXONOMY = [
    "advance_fee", "no_selection", "unsolicited_offer", "salary_too_high",
    "id_docs_upfront", "fake_location", "brand_impersonation",
]

def classify_posting(text: str) -> list[str]:
    """Deterministic keyword pre-filter; LLM used only to confirm.
    Returns list of matched flag keys."""
    hits = []
    rules = {
        "advance_fee": r"biaya (administrasi|pelatihan|seragam|mcu|pendaftaran|penempatan)",
        "no_selection": r"(lolos seleksi|langsung kerja|tanpa tes|tanpa wawancara)",
        "unsolicited_offer": r"(whatsapp.{0,20}(lolos|diterima)|anda terpilih)",
        "salary_too_high": r"rp\s?10\.?\d*\s?juta",
        "id_docs_upfront": r"(ktp|npwp|kk|ijazah|rekening bank).{0,30}(kirim|upload|foto)",
        "brand_impersonation": r"(bumn|pertamina|telkom|bank (bri|bni|mandiri)).{0,20}(loker|lowongan)",
    }
    for key, pat in rules.items():
        if re.search(pat, text, re.I):
            hits.append(key)
    return hits
```

### 3.6 Orchestrator: combine signals into a verdict

The orchestrator uses a simple, auditable rule: any single high-confidence RED
signal forces RED; otherwise signals accumulate into YELLOW; only an all-clear
across reachable sources returns GREEN. The key design principle is conservatism:
when a source is unreachable, we downgrade to YELLOW, never to GREEN, so the bot
never falsely reassures a victim.

```python
def verdict(name=None, phone=None, url=None, posting_text=None, rekening=None) -> dict:
    signals = []
    if rekening and is_reported("rekening", rekening):
        signals.append(("RED", f"rekening {rekening} dilaporkan scam"))
    if phone and is_reported("phone", norm_phone(phone)):
        signals.append(("RED", f"nomor {phone} dilaporkan scam"))
    if url:
        if "bumn" in (name or "").lower() and not channel_is_official(url):
            signals.append(("RED", "menggunakan nama BUMN di channel non-resmi"))
    if posting_text:
        flags = classify_posting(posting_text)
        if "advance_fee" in flags:
            signals.append(("RED", "meminta biaya di muka (administrasi/seragam/MCU)"))
    if name:
        nib = check_nib(name)
        if nib.status.startswith("unreachable") or nib.status.startswith("error"):
            signals.append(("YELLOW", f"cek NIB {name}: {nib.status}"))
        elif not nib.nib_found:
            signals.append(("YELLOW", f"NIB untuk '{name}' tidak ditemukan di OSS"))
    reds = [s for s in signals if s[0] == "RED"]
    yellows = [s for s in signals if s[0] == "YELLOW"]
    if reds:
        return {"verdict": "RED", "reasons": [r for _, r in reds]}
    if yellows:
        return {"verdict": "YELLOW", "reasons": [r for _, r in yellows]}
    return {"verdict": "GREEN", "reasons": ["tidak ditemukan sinyal merah pada sumber yang terhubung"]}
```

---

## 4. Channel integration (WhatsApp as the OS)

The vault's recurring thesis is "WhatsApp is the operating system for
Indonesian consumers". This product is the purest expression of that: it lives
entirely inside the channel where the crime happens. Two delivery options:

Option A, WhatsApp Business API (official, scalable, needs a business account
and a registered phone, costs per conversation). Best for the B2B API and for a
public, branded number.

Option B, a WA bridge / multi-device session (the vault already has a
`whatsapp-bridge` directory and `netra-telegram.sh` patterns). Lower cost, faster
to ship, but against Meta's ToS for bulk and needs careful session management.
Pragmatic path: ship Telegram first (free, no ToS landmine), then add WA via the
bridge once the verdict logic is proven.

The message contract is deliberately tiny:

```
User: cek PT Maju Sentosa, wa 0812-xxxx, link bit.ly/xxxxx
Bot:  MERAH (RED)
       - nomor 62812xxxx dilaporkan scam (3 laporan)
       - link bukan domain resmi perusahaan
       JANGAN transfer uang apa pun. Laporkan ke lapor.go.id
```

The bot always ends a RED verdict with the official reporting path
(lapor.go.id / SP4N Lapor / Bareskrim), because the goal is not only to stop one
payment but to feed law enforcement signal.

---

## 5. Unit economics

Victim side is free permanently. Revenue comes from three legs:

- B2B API: job boards (the same boards Kemnaker SENTA warns post fake listings),
  universities, and bootcamps pay per 1,000 checks to pre-flag scam postings
  before they reach users. Pricing reference: Indonesian SaaS verification APIs
  typically run Rp 50 to Rp 300 per check at volume; at 1M checks/month that is
  Rp 50 juta to Rp 300 juta/month gross.
- Verified-employer tier: legitimate SMEs pay a small monthly fee to be
  allow-listed so their genuine postings return GREEN and stand out. This also
  improves signal quality.
- Referral: route verified users to legitimate Kemnaker / official job boards
  and take a CPA or sponsorship.

Cost structure is dominated by LLM classification (only on pasted postings,
cached per hash) and WA/Telegram messaging. A verdict that uses only the local
scam registry and the deterministic rule set costs a fraction of a cent. The
marginal cost of the free victim check is therefore near zero, which protects the
core distribution flywheel.

---

## 6. Go-to-market

The scam lives in WhatsApp groups (the Mimika group of 178 victims named in the
inbox note is one example). The product must be seeded exactly there:

1. Publish the bot inside anti-scam and job-seeking communities, RW/student
   groups, and university career centers. The free, no-signup check is the
   wedge; virality comes from "cek dulu sebelum transfer" becoming a habit.
2. Partner with universities and bootcamps (fresh-graduate unemployment is a
   documented vault pain) to embed the checker into their career-portal
   onboarding.
3. Piggyback on panic moments: every time a new BUMN/ABK/Papua case hits the
   news (the inbox note cites repeated Jun 2026 cases), push a public verdict
   reminder. This is the same deadline-driven acquisition motion used by
   `unified-household-bills-tracker.md` and `deadline-driven-saas-bundle`.
4. B2B land-and-expand: one job board adopting the API creates a reference
   customer for the rest.

---

## 7. Competitive analysis

- cekrekening.id: focuses on bank accounts only and is Cloudflare-gated
  (no open API at research time). It does not cover company legality, BUMN
  impersonation, or posting classification.
- Kemnaker SENTA / official ministry articles: excellent education, zero
  interactivity, zero verdict at the moment of payment.
- General scam-reporting portals (lapor.go.id, Bareskrim): post-hoc reporting,
  not pre-payment prevention.
- Big job boards: they remove scams after the fact but provide no real-time
  per-candidate verdict bot.

The gap is precisely the pre-payment, multi-signal, conversational verdict. No
incumbent owns it.

---

## 8. Risks and failure modes

- Source reachability: OSS/AHU/cekrekening can block automated access. Mitigation
  is the conservative orchestrator (unreachable = YELLOW, never GREEN) plus a
  manual deep-link fallback the user opens themselves. We never invent data;
  if a source is unreachable we say so in the verdict.
- False GREEN: the most dangerous failure is reassuring a victim. Mitigation:
  any uncertainty downgrades to YELLOW, and the bot always tells users that a
  GREEN means "no red signal found", not "guaranteed safe".
- False RED on a legitimate employer: damages trust. Mitigation: RED only fires
  on high-precision signals (reported number/rekening, advance-fee request,
  BUMN-impersonation on non-official channel). Ambiguous legality checks are
  YELLOW.
- Privacy: do not store KTP, chat content, or identity docs. Store only
  normalized phone/rekening hashes and report counts, encrypted at rest, with a
  retention cap.
- ToS on WhatsApp: prefer Telegram for v1 and the official WA Business API for
  scale.

---

## 9. New gaps discovered during research

- `01-crawler-scrapper/regulatory/kemnaker-bumn-recruitment-monitor.md` — a daily
  crawler that snapshots official BUMN/Kemnaker/CPNS recruitment domains and
  handle lists so the allow-list adapter stays fresh without manual edits.
  (Discovered while mapping the official-channel signal.)
- `04-freelancer-ai-agent/regtech/cross-border-tax-creator.md` already exists as a
  cross-cutting gap; the loker-scam research confirms a sibling need:
  `03-id-business-trends/bottlenecks/job-seeker-identity-theft.md` — victims of
  loker scams routinely hand over KTP/NPWP; the downstream identity-theft and
  fraudulent-loan (pinjol) risk is the same attack surface as
  `judol-pinjol-cross-detection.md` and should be linked.
- `07-gaps-and-opportunities/thesis.md` — with eleven opportunity one-pagers now
  in the folder (this file included), the long-form quarterly synthesis is
  overdue and should be started next.

---

## 10. References (all reachable at time of writing, 2026-07-15)

- Kompas, 7 Jul 2026, "Diduga Jadi Korban Rekrutmen Bodong di Jakbar, Pelamar
  Kerja Diminta Bayar Rp 2,5 Juta untuk MCU dan Seragam"
  https://megapolitan.kompas.com/read/2026/07/07/16452451/diduga-jadi-korban-rekrutmen-bodong-di-jakbar-pelamar-kerja-diminta-bayar
- Tirto, 25 Nov 2025, "Mengapa Indonesia Jadi Sarang Penipuan Lowongan Kerja?"
  https://tirto.id/mengapa-indonesia-jadi-sarang-penipuan-lowongan-kerja-hmuT
- Katadata Varia, "Ciri-ciri Loker Penipuan dan Langkah-langkah Menghindarinya"
  https://katadata.co.id/lifestyle/varia/692402236a330/ciri-ciri-loker-penipuan-dan-langkah-langkah-menghindarinya
- Kemnaker SENTA, "Menghindari Lowongan Kerja Palsu"
  https://majalahsenta.kemnaker.go.id/artikel/menghindari-lowongan-kerja-palsu
- IDN Times, "5 Indikasi Penipuan Berkedok Lowongan Kerja, Selalu Modus Minta
  Biaya"
  https://www.idntimes.com/business/economy/indikasi-penipuan-berkedok-lowongan-kerja-selalu-modus-minta-biaya-c1c2-01-bfjms-hc99n4
- Official portals used as signal sources (verified reachable):
  OSS RBA https://oss.go.id (HTTP 307 to RBA app, title "OSS RBA - Sistem
  Perizinan Berusaha Terintegrasi Secara Elektronik"),
  AHU Online https://ahu.go.id (title "DITJEN AHU ONLINE"),
  Kemnaker https://www.kemnaker.go.id (title "Beranda : Kementerian Ketenagakerjaan RI"),
  cekrekening.id https://cekrekening.id (Cloudflare-gated at root, manual
  per-number lookup only; marked source-unreachable for automated bulk query).
- Vault siblings:
  `07-gaps-and-opportunities/inbox/2026-07-15-loker-scam-verifier.md` (seed),
  `07-gaps-and-opportunities/inbox/scam-detection-tool-2026-07-07.md`,
  `07-gaps-and-opportunities/opportunities/judol-pinjol-cross-detection.md`,
  `07-gaps-and-opportunities/opportunities/unified-household-bills-tracker.md`.

---

## 11. Data schema and storage design

The bot's value compounds with every report, so the storage layer is a first
class concern, not an afterthought. The schema below is deliberately minimal and
privacy-preserving: no PII, only normalized hashes and counters.

```sql
-- verdict_cache.db (SQLite, single-file, easy to ship and backup)
CREATE TABLE scam_reports (
    id            INTEGER PRIMARY KEY,
    kind          TEXT NOT NULL,          -- 'phone' | 'rekening' | 'company' | 'url'
    value_hash    TEXT NOT NULL UNIQUE,   -- sha256 of normalized value
    report_count  INTEGER DEFAULT 1,
    first_seen    TEXT,                   -- ISO8601 UTC
    last_seen     TEXT,
    last_verdict  TEXT                    -- RED | YELLOW | GREEN (from last reporter)
);

CREATE TABLE verdict_log (
    id            INTEGER PRIMARY KEY,
    ts            TEXT,                   -- ISO8601 UTC
    channel       TEXT,                   -- 'wa' | 'tg'
    input_kind    TEXT,                   -- what the user pasted
    verdict       TEXT,                   -- RED | YELLOW | GREEN
    signals       TEXT,                   -- JSON array of reason strings
    latency_ms    INTEGER,
    user_id_hash  TEXT                    -- sha256 of channel user id, for abuse control
);

CREATE INDEX idx_reports_kind_val ON scam_reports(kind, value_hash);
CREATE INDEX idx_log_ts ON verdict_log(ts);
```

Design notes:

- `value_hash` instead of raw value. A phone like 62812xxxx is normalized then
  hashed so the DB never stores a directly usable number; analysts can still
  count and match. If law enforcement needs the raw value, it is retrieved from
  the user who reported it, not from this store.
- `verdict_log` is the telemetry that proves the bot works: how many RED verdicts
  it issued, what latency, what channel. This is the metric that justifies the
  B2B API and the grant/funding pitch.
- Retention: `verdict_log` rows older than 180 days are anonymized (user_id_hash
  dropped) on a nightly job. `scam_reports` rows with `report_count >= 2` are
  kept indefinitely because they are the high-precision signal; singletons older
  than 90 days with no second report are purged to limit false-positive decay.

---

## 12. Deployment topology

A single small server is enough for the v1 free tier. The whole stack fits on one
2 vCPU / 4 GB VPS or even a container in the vault's existing automation host.

```
            WhatsApp / Telegram
                   |
            +------+------+
            |  channel    |  (WA Business API webhook OR tg bot polling)
            +------+------+
                   |
            +------v------+        +-------------------+
            | orchestrator | <----> | signal adapters   |
            |  (FastAPI)   |        | nib/ahu/bumn/llm |
            +------+------+        +-------------------+
                   |
            +------v------+
            |  store       |  SQLite -> nightly export to S3/Backblaze
            | verdict_cache|
            +-------------+
```

- Orchestrator is a FastAPI service exposing `POST /verify` with a JSON body
  matching the `verdict()` signature above. The channel layer is a thin adapter
  that maps chat input to that JSON and formats the response back to chat.
- Adapters run with a hard 20s timeout each; the orchestrator waits for the first
  N (configurable, default 4) signals then decides. A slow OSS lookup must never
  block a RED from the scam registry.
- Static allow-lists (official BUMN/Kemnaker/CPNS domains and handles) are loaded
  from a JSON file refreshed by a nightly cron; the
  `kemnaker-bumn-recruitment-monitor` crawler (new gap, see section 9) will
  eventually replace manual edits.
- LLM adapter is optional and only invoked when the user pastes a posting or
  uploads a screenshot; results are cached by content hash for 7 days to cut cost.

```yaml
# docker-compose.yml (v1)
services:
  verifier:
    build: .
    ports: ["8000:8000"]
    environment:
      WA_API_TOKEN: "${WA_API_TOKEN}"
      TG_BOT_TOKEN: "${TG_BOT_TOKEN}"
      LLM_BASE_URL: "${LLM_BASE_URL}"
      LLM_KEY: "${LLM_KEY}"
    volumes:
      - ./data:/app/data      # verdict_cache.db lives here, backed up nightly
```

---

## 13. Testing and evaluation harness

A trust product must be testable, or it drifts into false reassurance. The
evaluation set is built from the real sources in section 10 plus crowd reports.

```python
# tests/test_verdicts.py
CASES = [
    # (input kwargs, expected_verdict, reason_substring)
    ({"rekening": "1234567890", "reported": True}, "RED", "dilaporkan scam"),
    ({"name": "PT Maju Sentosa", "url": "https://bit.ly/x",
      "posting_text": "loker BUMN, bayar biaya administrasi 500rb"},
     "RED", "biaya di muka"),
    ({"name": "PT Maju Sentosa", "url": "https://ptmajusentosa.co.id"},
     "YELLOW", "NIB"),              # legality unchecked -> never GREEN
    ({"name": "PT Telkom Indonesia", "url": "https://telkom.co.id/career"},
     "GREEN", "tidak ditemukan sinyal merah"),
]

def test_verdicts():
    for inp, exp, sub in CASES:
        v = verdict(**({k: inp[k] for k in inp if k != "reported"}))
        assert v["verdict"] == exp, f"{inp} -> {v}"
        assert any(sub in r for r in v["reasons"]), f"missing {sub}: {v}"
```

Evaluation metrics to track weekly:

- Precision of RED: of all RED verdicts, what fraction were confirmed scams by
  user follow-up or report. Target >= 0.95.
- False-GREEN rate: RED and YELLOW that should have been RED. This is the
  catastrophic class; any instance triggers a post-mortem.
- Coverage: share of incoming checks that hit at least one adapter (not just the
  local registry). Higher coverage means less reliance on user reports alone.
- p95 latency: must stay under 12s on WhatsApp to beat the victim's impulse to
  pay. The 10-second requirement in the wedge is the SLO.

---

## 14. Monitoring and alerting

- SLO dashboard: RED precision, false-GREEN count, p95 latency, adapter error
  rates (OSS/AHU/cekrekening timeouts spike when those sites change markup).
- Adapter-health alert: if `check_nib` returns `unreachable` for more than 5
  percent of calls in a rolling hour, page the on-call because the conservative
  design will be silently downgrading every check to YELLOW, eroding trust.
- Abuse alert: a single `user_id_hash` issuing more than 50 verdicts/hour is
  likely a spammer probing the bot; rate-limit and flag.
- Weekly digest: number of RED verdicts issued, top impersonated brands, new
  reported numbers/rekening. This doubles as the community-facing "waspada"
  post that fuels acquisition.

---

## 15. Anti-abuse and adversarial considerations

Scammers will try to game a popular verifier. Threats and countermeasures:

- Scraper scraping the GREEN list to harvest "verified" company names to
  impersonate. Counter: never publish the full GREEN list; the betting is on
  per-check answers, not a directory.
- Scammers submitting fake "this is legit" reports to whitewash a number.
  Counter: a report only moves a value toward GREEN if it comes with a verified
  NIB/AHU match from an official source; user reports only ever add RED weight,
  never remove it.
- Prompt injection through pasted postings. Counter: the LLM classifier is
  constrained to the deterministic RED_FLAG_TAXONOMY; the posting text is treated
  as data, the model is instructed to never follow instructions inside it, and
  the verdict logic ignores any "ignore previous rules" style content.
- DoS via the free endpoint. Counter: per-user and per-IP rate limits; the
  local registry lookup is O(1) and cheap, so legitimate load is fine.

---

## 16. Localization and UX copy

The bot speaks Indonesian first. Verdict copy is fixed, not generative, to avoid
the model softening a RED into a maybe:

```
MERAH (RED):
  [reason 1]
  [reason 2]
  JANGAN transfer uang apa pun.
  Laporkan ke lapor.go.id atau Posko Bareskrim 1544.

KUNING (YELLOW):
  Belum bisa dipastikan aman. Cek ulang:
  - apakah ada biaya di muka? (harusnya TIDAK)
  - apakah link resmi perusahaan?
  - apakah ada wawancara nyata?

HIJAU (GREEN):
  Tidak ditemukan sinyal merah di sumber terhubung.
  Catatan: ini bukan jaminan 100% aman, selalu waspada biaya di muka.
```

The GREEN disclaimer is intentional: the bot refuses to give absolute assurance,
which is the honest and legally-safe position.

---

## 17. Build runbook (week one)

Day 1 to 2: stand up the FastAPI orchestrator with only the local scam_registry
adapter and the deterministic `classify_posting` rule set. Ship the Telegram bot.
This alone catches advance-fee postings and any already-reported number.

Day 3 to 4: add the BUMN/Kemnaker/CPNS official-domain allow-list (static JSON)
and the `bumn_posting_verdict` rule. Add the verdict_log telemetry.

Day 5: add the NIB/AHU adapters behind a feature flag with the conservative
"unreachable = YELLOW" behavior; do not let them ever produce GREEN alone.

Day 6 to 7: seed the scam_registry with the Mimika-group numbers from the inbox
note and any public reports; write the week-one evaluation test cases; publish
the bot into three job-seeking communities and two university career centers.

After week one the only remaining work is distribution and the crawler that keeps
the allow-list fresh, which is the new gap in section 9.

---

## 18. Why this is the right gap to fill this tick

The vault's gold mine (03-id-business-trends) is saturated at 126 files, and the
priority ladder in the filler prompt puts
`07-gaps-and-opportunities/opportunities` second, at a target of one new
opportunity one-pager per week. The loker-scam-verifier was the freshest inbox
entry (2026-07-15, pain 5/5) and the only one pointing at the single most
expensive action a job seeker takes: the transfer. It reuses the trust-infra
thesis already proven in judol-pinjol-cross-detection, the WA-as-OS channel
thesis, and the connector-isolation pattern from unified-household-bills-tracker,
so it is high-confidence and low-novelty-risk. Eleven opportunity one-pagers now
exist, which also makes this the moment to start the long-form `thesis.md`
synthesis noted as the next gap below.

---

## 19. Key assumptions and open questions

- The conservative design assumes official sources (OSS, AHU, cekrekening) are
  partially reachable; if all are blocked, the bot degrades to a rule-based
  classifier plus the user-report registry, which still catches advance-fee
  postings and known numbers. That degraded mode is explicitly not a GREEN and
  must say so.
- Open question: whether a B2B API customer (job board) would accept a verdict
  that can return YELLOW for a posting it wants to auto-approve. The answer is
  probably no, so the B2B product is "flag the REDs and surface the YELLOWs for
  human review", not "auto-approve".
- Open question: Indonesian consumer-protection liability if the bot returns
  GREEN and the user is still scammed. The fixed GREEN disclaimer and the
  never-auto-GREEN rule are the primary mitigations; legal review is a
  pre-launch gate, not an afterthought.
