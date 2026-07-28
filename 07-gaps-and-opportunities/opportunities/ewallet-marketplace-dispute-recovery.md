# PengaduanKu: Unified E-Wallet & Marketplace Dispute Recovery Platform

**Date:** 2026-07-28
**Promoted from:** inbox/2026-07-14-ewallet-seller-dispute-tools.md
**Signal strength:** 5/5
**Category:** B2C/B2B dispute resolution SaaS
**Target market:** Indonesian e-wallet users, marketplace sellers, affiliate creators
**TAM:** Rp 3.2 trillion/year (based on Rp 3 trillion TikTok Shop frozen balance alone, plus GoPay/OVO/DANA incidents, plus Shopee/Lazada/Tokopedia frozen seller balances)

---

## Executive Summary

PengaduanKu is a WhatsApp-first platform that helps Indonesian consumers and sellers recover frozen e-wallet balances and marketplace funds. The platform solves a structural gap in Indonesia's digital economy: when GoPay, OVO, DANA, Shopee, TikTok Shop, or Tokopedia freeze an account (often by automated systems), the victim currently has no fast, affordable way to recover their funds. The platform connects victims with the right dispute channels (in-app CS, OJK Consumer Protection, BI Payment System, Kementerian UMKM, MediaKonsumen, KPPU) through automated evidence gathering, template generation, status tracking, and optional concierge escalation.

The wedge is simple: for Rp 25,000 to Rp 150,000 per case (or Rp 30,000/month subscription for active sellers), a victim regains access to funds that can be tens of millions to billions of rupiah. With 500 TikTok Shop cases alone representing Rp 3 trillion in frozen funds (CNBC Indonesia 2026-07-09), and recurring e-wallet incidents affecting thousands of users annually, the willingness-to-pay is extreme.

The product is anchored on four demand-mining pain files already in the vault: saldo-ewallet-dibekukan-terblokir.md, saldo-penjual-shopee-dibekukan.md, tiktok-shop-akun-dibekukan-saldo-tertahan.md, and seller-rugi-retur-fiktif-cod.md. It also consolidates two inbox seeds (2026-07-14-ewallet-seller-dispute-tools.md and 2026-07-14-marketplace-saldo-escrow.md).

---

## 1. The Problem Space

### 1.1 E-Wallet Frozen Accounts

Indonesia has three dominant e-wallet platforms — GoPay (GoTo), OVO (Grab/Stanchart), and DANA (EMTEK/Ant Financial) — plus dozens of smaller players. Combined they serve over 100 million registered users. However, account freezes and balance discrepancies are endemic:

**GoPay:**
- August 4, 2025: mass outage where top-up funds were deducted from bank accounts but never credited to GoPay balances. Head of Corporate Communications GoTo Financial Audrey Petriny confirmed "technical disruption" (Liputan6 2025-08-04, source: https://www.liputan6.com/bisnis/read/6123589/saldo-gopay-error-tak-bisa-top-up-ada-apa). Victims reported being told to "wait 2 working days" via FAQ while their money was inaccessible.
- Recurring pattern: X (Twitter) threads show hundreds of users reporting GoPay top-up failures where bank deducted but GoPay never credited. The only recourse is GoPay CS which is slow and FAQ-driven.

**OVO:**
- January 3, 2026: mass panic when user balances displayed Rp 0. Trending on social media (MSN/Detik, source: https://www.msn.com/id-id/ekonomi/umum/ovo-kenapa-hari-ini-3-januari-2026-saldo-tiba-tiba-0-rupiah-ramai-dikeluhkan-apakah-error-dan-gangguan/ar-AA1TuKLX). Users had no immediate recourse while the system was down.

**DANA:**
- P2P crypto transaction linking: accounts frequently get restricted after P2P transfers to/from crypto exchanges. A dedicated tutorial industry has emerged explaining how to unblock accounts (czneo.com, 2026, source: https://czneo.com/id/articles/akun-ewallet-dibekukan-p2p).

**Cross-platform pattern:** E-wallet freezes are triggered by automated anti-fraud systems when they detect "unusual volume, repeated transfer patterns, reports from senders, or identity re-verification needed" (czneo). The user is locked out with no human escalation. CS wait times are hours to days. The only formal recourse is filing a complaint with BI's Consumer Protection Portal or OJK's Portal Perlindungan Konsumen — a process most users don't know exists.

### 1.2 Marketplace Seller Frozen Balances

**TikTok Shop (TikTok Tokopedia):**
- July 9, 2026: CNBC Indonesia reported 500 UMKM seller accounts frozen with an estimated Rp 3 trillion in trapped balances. Kementerian UMKM Deputy Temmy Satya Permana confirmed receiving reports from Peradi Bekasi Raya. Komisi VII DPR RI summoned TikTok, Tokopedia, and Shopee for clarification (CNBC Indonesia 2026-07-09, source: https://www.cnbcindonesia.com/tech/20260709102947-37-749380/500-akun-tiktok-shop-mendadak-beku-rp-3-triliun-tak-bisa-ditarik).
- One seller (MeowBee store): Rp 65 million frozen on accusation of "promo abuse" with no clear evidence. Appeal rejected for "insufficient proof" without specifying what proof is needed (MediaKonsumen 2026-05-14, source: https://mediakonsumen.com/2026/05/14/surat-pembaca/toko-saya-diblokir-tiktok-shop-tokopedia-dengan-tuduhan-penyalahgunaan-promo-saldo-rp65-juta-ditahan).
- TikTok Shop changed 7 policies in 2026, and sellers who don't adapt lose access. Automated enforcement with no manual review.

**Shopee:**
- Seller with 7 years of operation: Rp 28 million frozen because facial recognition verification kept failing. After "verification failed" errors, the seller submitted 9 complaints and all received the same template response: "penyesuaian saldo" (MediaKonsumen 2026-05-14, source: https://mediakonsumen.com/2026/05/14/surat-pembaca/28-juta-rupiah-saldo-penjualan-di-shopee-ditahan-dengan-alasan-keamanan-verifikasi-data-gagal-terus-dengan-pesan-error-sistem).
- Another seller: balance went negative Rp 130,000 because Shopee's system automatically deducted return shipping from their account before the item even arrived back (MediaKonsumen 2026-06-29, source: https://mediakonsumen.com/2026/06/29/surat-pembaca/sistem-shopee-merugikan-penjual-barang-retur-sudah-diterima-tapi-saldo-toko-malah-dibuat-minus).
- Facebook seller community posts show dozens of similar cases with the same "adjustment" template response.

**Retur Fiktif (Fake Returns):**
- Sellers across TikTok Shop, Shopee, and Lazada report losses from fake COD returns. The system records "buyer rejected package" or "address unclear" but these often differ from what buyers claim. Sellers have no independent verification tool (Jambisun 2026, source: https://jambisun.id/skandal-cod-ecommerce-2026-seller-rugi-retur-tiktok-shopee/).
- TikTok Shop starting June 1, 2026: return shipping costs charged to seller up to Rp 10,000 per transaction (Bisnis Teknologi 2026-04-14, source: https://teknologi.bisnis.com/read/20260414/84/1966421/beda-kebijakan-shopee-dan-tiktok-shop-soal-biaya-retur-seller — note: Cloudflare-blocked at time of writing, content confirmed via demand-mining file).
- Aggregate losses: individual sellers report puluhan to ratusan juta rupiah in losses from COD return disputes.

### 1.3 The Structural Gap

The common thread across all these cases: **there is no independent, fast, affordable third-party that helps victims navigate the dispute resolution process.** The players in the ecosystem are:

| Actor | Role | Failure |
|-------|------|---------|
| Platform CS (GoPay, Shopee, TikTok, etc.) | First-line dispute handler | Template responses, no human escalation, "wait 2 days" |
| OJK Portal Perlindungan Konsumen | Formal complaint body | Slow (weeks), bureaucratic, requires specific formats |
| BI Consumer Protection | Payment dispute handler | Only for systemic payment failures, not individual merchant freezes |
| MediaKonsumen | Public complaint platform | Non-binding, no enforcement power, slow |
| Kementerian UMKM | Government mediator | Only for cases that reach DPR attention (500+ cases minimum) |
| Lawyer/advocate | Legal escalation | Rp 5-50 million fees, prohibitive for Rp 28-65 million claims |
| Seller community groups (Facebook, X) | Peer support | No formal process, no leverage with platforms |

The gap: a **guided dispute assistant** that sits between the victim and the formal channels, providing:
- Evidence collection templates (screenshots, transaction IDs, bank statements)
- Formatted complaint drafts for the right channel (CS, OJK, BI, KPPU, MediaKonsumen)
- Status tracking across multiple channels
- Escalation playbook (when to escalate, to whom, and how)
- Optional concierge service for complex cases

---

## 2. Evidence & Signal Strength

### 2.1 Quantitative Signals

| Indicator | Value | Source | Date |
|-----------|-------|--------|------|
| TikTok Shop frozen accounts | 500 sellers | CNBC Indonesia | 2026-07-09 |
| Total frozen balance TikTok Shop | Rp 3 trillion | CNBC Indonesia | 2026-07-09 |
| Single seller frozen balance (TikTok) | Rp 65 million | MediaKonsumen | 2026-05-14 |
| Single seller frozen balance (Shopee) | Rp 28 million | MediaKonsumen | 2026-05-14 |
| GoPay technical outage users | Thousands on X | Liputan6 | 2025-08-04 |
| OVO balance-zero panic users | Trending national | MSN/Detik | 2026-01-03 |
| Guide articles "akun e-wallet terblokir" | 50+ published 2025-2026 | Multiple ID portals | 2025-2026 |
| TikTok Shop policy changes 2026 | 7 rules | Desa Karang Bendo | 2026 |
| Return fee per transaction (TikTok Shop) | Max Rp 10,000 | Bisnis Teknologi | 2026-04-14 |
| DANA P2P restriction guides | Multiple articles | czneo.com | 2026 |

### 2.2 Qualitative Signals

**Recurring social media patterns:** Every few months, a wave of complaints about frozen e-wallet or marketplace balances trends on X (Twitter). The pattern is predictable:
1. Platform auto-freeze triggers (algorithm detects anomaly)
2. User tries CS, gets template response
3. User posts on X/Twitter, goes viral
4. Platform eventually resolves after social media pressure
5. Repeat cycle

This cycle means individual resolutions are reactive, not systematic. A platform that provides systematic resolution (evidence packs, status tracking, escalation timing) breaks the cycle.

**Media coverage density:** In 2026 alone, at least 5 major news outlets covered TikTok Shop frozen balances (CNBC, MediaKonsumen, Detik, Kompasiana, multiple local news sites). E-wallet issues are covered every few months by Liputan6, Detik, and MSN. The coverage frequency indicates a systemic problem, not isolated incidents.

### 2.3 Market Size Estimate

**E-wallet dispute market:**
- GoPay: 45M+ monthly active users (GoTo 2025 annual report estimate)
- OVO: 25M+ monthly active users
- DANA: 20M+ monthly active users
- Estimated incident rate: 1-2% of users experience freeze/error annually = 900,000 to 1.8M potential cases/year
- Average frozen balance: Rp 500,000 to Rp 5 million per e-wallet case

**Marketplace seller dispute market:**
- TikTok Shop: 500+ known frozen accounts, likely undercount (many don't report to Peradi)
- Shopee: 10M+ active sellers, estimated 0.1% experience freeze = 10,000 cases/year
- Tokopedia: 5M+ active sellers, estimated 0.1% = 5,000 cases/year
- Average frozen balance: Rp 28M to Rp 65M+ (from documented cases)

**Total addressable frozen balance:** Rp 3 trillion (TikTok Shop only) + estimated Rp 500B (Shopee) + Rp 200B (Tokopedia) + Rp 100B (e-wallet) = Rp 3.8 trillion trapped annually

---

## 3. Existing Solutions & Why They Fail

### 3.1 Platform Customer Service

Every platform has an in-app CS channel. The failure modes are:
- **Template responses:** Shopee's "penyesuaian saldo" is a copy-paste answer that doesn't address the specific case. One seller sent 9 complaints and got 9 identical responses.
- **No human escalation:** TikTok Shop's dispute process is entirely AI-driven. Appeals go to the same system that flagged the account in the first place.
- **2-day wait periods:** GoPay FAQ tells users to wait 2 business days for top-up resolution. For a merchant who needs that money to restock today, this is unacceptable.
- **Identity verification failures:** Shopee's facial recognition verification fails for some users with no alternative. The system loops: "verify your face" -> "verification failed" -> "try again."
- **No status tracking:** After filing a complaint, users have no way to check progress or see where their case is in the pipeline.

### 3.2 Regulatory Bodies

**OJK Portal Perlindungan Konsumen:**
- Website: konsumen.ojk.go.id
- Requires detailed complaint form with specific formats
- Case resolution: 14-30 days
- Best for systemic issues, not urgent fund recovery
- Many victims don't know it exists

**BI Consumer Protection:**
- Handles payment system disputes
- Requires formal letter with supporting documents
- Focused on systemic payment failures rather than individual merchant disputes
- Process takes weeks

**KPPU (Competition Commission):**
- Only engages when there is evidence of anti-competitive behavior
- Not designed for individual fund recovery
- Requires legal representation

### 3.3 Media & Public Pressure

Platforms like MediaKonsumen.com publish complaint letters from consumers. This sometimes works (platforms respond to avoid negative PR) but:
- Non-binding: platforms can simply ignore
- Slow: letters go through editorial review before publication
- One-shot: no follow-up mechanism after publication
- Narrow reach: not all cases get published

### 3.4 Legal Recourse

Hiring a lawyer to pursue a frozen balance case:
- Cost: Rp 5-50 million retainer
- Time: 3-12 months
- Scale: only viable for claims above Rp 50 million
- For Rp 28 million Shopee case: lawyer fees eat half the recovery

### 3.5 Community Groups

Facebook groups like "Seller Shopee Indonesia" and "Komunitas Seller TikTok Shop" provide emotional support and tips but:
- No standard process
- No leverage with platforms
- Information is anecdotal
- Success stories are rare

---

## 4. Target Personas

### Persona A: Nirma, TikTok Shop Seller (Bandung)
- **Profile:** 28 years old, sells handmade accessories on TikTok Shop, average monthly revenue Rp 15 million
- **Pain:** Account frozen on "suspicious activity" flag. Rp 8.3 million in seller balance trapped. Has appealed 3 times with no response.
- **Behavior:** Active on X, member of 2 seller Facebook groups, not aware of OJK consumer protection portal.
- **Willingness to pay:** Rp 50,000 for a guided dispute pack. Rp 150,000 for concierge service that drafts the perfect appeal.
- **Outcome if unresolved:** Cannot restock, loses regular customers, considers closing shop.

### Persona B: Budi, GoPay Power User (Jakarta)
- **Profile:** 34 years old, freelancer, receives 80% of payments via GoPay, monthly transaction volume Rp 25 million.
- **Pain:** GoPay account restricted after receiving a Rp 5 million transfer from a new client. Balance frozen at Rp 3.2 million. CS says "wait 2 days" but 5 days have passed.
- **Behavior:** Tech-savvy, follows Gojek X account, frustrated but doesn't know where to escalate beyond CS.
- **Willingness to pay:** Rp 25,000 for phone consultation. Rp 30,000/month for "seller protection" subscription that includes e-wallet dispute assistance.
- **Outcome if unresolved:** Misses payment deadlines, loses client trust.

### Persona C: Dewi, Small Online Reseller (Semarang)
- **Profile:** 45 years old, resells fashion items on Shopee and TikTok Shop. Total monthly revenue Rp 8 million. Manages everything from her phone.
- **Pain:** COD return dispute: buyer claimed "item not as described" and returned a different item. Shopee deducted Rp 130,000 from her balance for return shipping.
- **Behavior:** Not on Twitter, relies on WhatsApp groups for seller tips, low digital literacy.
- **Willingness to pay:** Rp 15,000 per dispute case (one-off). Prefers WhatsApp interface.
- **Outcome if unresolved:** Loses Rp 130,000 + cost of goods. Margin too thin to absorb repeated losses.

### Persona D: Fajar, Affiliate Creator (Yogyakarta)
- **Profile:** 22 years old, TikTok affiliate creator, earns commissions from TikTok Shop affiliate program.
- **Pain:** TikTok Shop affiliate commission frozen because "policy violation" (allegedly free shipping abuse by the seller he promoted). Rp 1.7 million commission not disbursed.
- **Behavior:** Active on TikTok, follows creator communities, scared of platform ban.
- **Willingness to pay:** Rp 35,000 for one-time assistance. Prefers anonymous service (doesn't want platform to know he consulted a third party).
- **Outcome if unresolved:** Loses confidence in affiliate model, reduces content production.

---

## 5. The Product: PengaduanKu

### 5.1 Product Vision

PengaduanKu is a WhatsApp-first dispute recovery assistant and escalation platform. Users interact via WhatsApp (most accessible channel for Indonesian users). The platform guides them through evidence collection, generates the right complaint for the right channel, tracks status across multiple channels, and optionally provides concierge escalation.

The name "PengaduanKu" means "My Complaint" — positioning the platform as the user's personal advocate, not just a tool.

### 5.2 Core Modules

**Module 1: Case Intake & Triage (WhatsApp Bot)**

The user sends a simple message describing their problem. The bot triages the case into one of:
1. **E-Wallet Frozen/Error** (GoPay, OVO, DANA, LinkAja, ShopeePay)
2. **Marketplace Seller Balance Frozen** (Shopee, TikTok Shop, Tokopedia, Lazada)
3. **COD Return Dispute** (buyer returned item, seller disagrees)
4. **E-Wallet Top-Up Failed** (bank deducted, e-wallet not credited)
5. **Affiliate Commission Frozen** (TikTok Shop affiliate)
6. **Account Banned/Blocked** (any platform)

Each case type triggers a specific evidence checklist.

**Module 2: Evidence Collection Engine**

The bot guides the user to collect the right evidence for their case type:

```
For e-wallet frozen cases:
1. Screenshot of account showing "frozen" or "restricted" message
2. Transaction history showing balance
3. Any error messages received
4. Bank statement if top-up failed
5. Previous CS chat logs
6. Account registration details (phone number linked, email)

For marketplace frozen balance:
1. Screenshot of seller dashboard showing frozen balance
2. Order history related to frozen amount
3. Previous appeal/complaint ticket numbers
4. Screenshots of CS responses
5. Identity verification attempts (if relevant)
6. Product listings, store performance data
```

Each evidence item has a template instruction ("kirim screenshot halaman saldo dengan nomor order terlihat"). The bot validates completeness before proceeding.

**Module 3: Complaint Generator**

Based on the case type and evidence collected, the bot generates one or more tailored complaint documents:

1. **Platform Appeal Template:** Formatted for the specific platform's appeal system. Includes the correct language, references to specific platform policies, and clearly stated demand (unfreeze balance, credit missing funds, etc.).
2. **OJK Consumer Complaint:** Formatted for Portal Perlindungan Konsumen OJK with required fields and supporting attachments.
3. **BI Payment System Complaint:** For payment failure cases, formatted for BI's consumer protection channel.
4. **MediaKonsumen Letter:** A public complaint letter draft the user can publish.
5. **Kementerian UMKM Report:** For marketplace seller cases, a report format suitable for UMKM complaint channels.

Each template includes:
- User's identifiable information (name, contact, account details)
- Chronological narrative of events
- Evidence attached (screenshot filenames, timestamps)
- Specific demand (Rp amount to be released, account to be reactivated)
- Legal references (platform TOS clauses, OJK regulations, ITE Law)

**Module 4: Multi-Channel Filing**

The bot doesn't just generate documents — it tells the user exactly how and where to file each one:

```
Step 1: Kirim template banding ini ke Shopee Seller Center
  -> Buka Seller Center -> Pilih order terkait -> Klik "Banding"
  -> Paste teks template ke kolom komentar
  -> Lampirkan screenshot sesuai checklist

Step 2: Kirim pengaduan ke Portal Perlindungan Konsumen OJK
  -> Buka https://konsumen.ojk.go.id
  -> Klik "Buat Pengaduan Baru"
  -> Isi form sesuai data yang sudah dikumpulkan
  -> Lampirkan template komplain OJK (PDF yang sudah digenerate)

Step 3: Post keluhan ke MediaKonsumen
  -> Buka https://mediakonsumen.com/kirim-surat-pembaca
  -> Paste surat pembaca yang sudah digenerate
  -> Upload screenshot sebagai bukti
```

Each step is a separate WhatsApp message with a "done" button so the bot can track progress.

**Module 5: Status Tracker**

The user can check their case status anytime by sending "STATUS" to the WhatsApp bot:

```
Kasus #PKD-20260728-001
Jenis: TikTok Shop Saldo Dibekukan
Tanggal dibuka: 28 Juli 2026
Status saat ini:
  [X] Template banding dikirim ke TikTok Seller Center
  [ ] OJK pengaduan diajukan
  [ ] MediaKonsumen surat diterbitkan
  [X] Kementerian UMKM dilaporkan
  
Terakhir diperbarui: 28 Juli 2026 14:30 WIB
Catatan: TikTok Seller Center menampilkan "dalam proses" sejak 28 Juli 2026 10:00 WIB

Kirim "DETAIL" untuk info lebih lanjut.
```

**Module 6: Escalation Engine**

If a case is not resolved within a timeframe (configurable per platform), the bot suggests escalation:

```
[ESCALATION] Kasus #PKD-20260728-001 sudah 7 hari sejak template banding dikirim.
Platform belum memberikan tanggapan. Anda bisa melakukan eskalasi:

Pilihan 1: Hubungi Komisi VII DPR RI
  Template surat sudah siap. Biaya cetak & kirim: Rp 15,000.

Pilihan 2: Laporkan ke KPPU (Komisi Pengawas Persaingan Usaha)
  Untuk kasus dugaan penyalahgunaan posisi dominan.
  Template laporan sudah siap.

Pilihan 3: Konsultasi Hukum Online
  Terhubung dengan mitra advokat (Rp 150,000/sesi 30 menit).
  
Pilihan 4: Gunakan Layanan Concierge Premium
  Tim kami akan menangani komunikasi dengan platform atas nama Anda.
  Biaya: Rp 250,000 per kasus (atau 10% dari saldo berhasil dicairkan).
```

**Module 7: Concierge Service (Premium)**

For users who pay extra (or a percentage of recovered funds), a human team handles the entire dispute process:
- Submit appeals through platform channels
- Follow up via phone/email with CS escalations
- Coordinate with OJK/BI/KPPU filings
- Arrange media publication through MediaKonsumen
- Track all communications and provide weekly updates
- Negotiate directly with platform dispute teams

This is the high-margin offering. The concierge team needs deep knowledge of each platform's appeal system, escalation paths, and common resolution patterns.

### 5.3 Technical Architecture

**Frontend: WhatsApp Business API + Web Dashboard**
- Primary interface: WhatsApp (Twilio/WATI/Meta WhatsApp Cloud API)
- Secondary interface: Web dashboard for case management, document generation, and analytics
- Language: Indonesian primary, English backup

**Backend: Python/FastAPI**
- Case state machine
- Template engine (Jinja2)
- Document generation (ReportLab for PDF, python-docx for Word)
- File storage (S3-compatible for screenshots)
- Database: PostgreSQL (cases, users, logs)

**Key Components:**

```python
# Case State Machine (pseudo-code excerpt)

class CaseState(Enum):
    INITIATED = "initiated"          # User first contacts bot
    TRIAGED = "triaged"              # Case type identified
    EVIDENCE_COLLECTING = "evidence_collecting"  # Gathering screenshots/docs
    EVIDENCE_REVIEW = "evidence_review"          # Auto-validating evidence
    COMPLAINT_GENERATED = "complaint_generated"  # Templates ready
    FILING_IN_PROGRESS = "filing_in_progress"    # User filing through channels
    FILING_COMPLETE = "filing_complete"          # All channels filed
    MONITORING = "monitoring"                    # Awaiting response
    ESCALATED = "escalated"                      # Escalation triggered
    RESOLVED = "resolved"                        # Fund recovered
    CLOSED_UNRESOLVED = "closed_unresolved"      # Gave up or failed

transitions = {
    INITIATED: [TRIAGED],
    TRIAGED: [EVIDENCE_COLLECTING],
    EVIDENCE_COLLECTING: [EVIDENCE_REVIEW],
    EVIDENCE_REVIEW: [COMPLAINT_GENERATED, EVIDENCE_COLLECTING],
    COMPLAINT_GENERATED: [FILING_IN_PROGRESS],
    FILING_IN_PROGRESS: [FILING_COMPLETE],
    FILING_COMPLETE: [MONITORING],
    MONITORING: [RESOLVED, ESCALATED, CLOSED_UNRESOLVED],
    ESCALATED: [RESOLVED, CLOSED_UNRESOLVED],
}
```

**Template Generation Engine:**

```python
# Template generator for OJK complaint (pseudo-code)

from jinja2 import Template

ojk_template = Template("""
PERIHAL: Pengaduan Konsumen {{ case_type }} - {{ user_name }}

Kepada Yth.
Otoritas Jasa Keuangan
Portal Perlindungan Konsumen

Dengan hormat,

Saya yang bertanda tangan di bawah ini:
Nama: {{ user_name }}
No. Identitas (KTP): {{ user_ktp }}
Alamat: {{ user_address }}
No. Telepon: {{ user_phone }}
Email: {{ user_email }}

Dengan ini mengajukan pengaduan mengenai:

1. Identitas Pelaku Usaha Jasa Keuangan:
   Nama Platform: {{ platform_name }}
   Layanan: {{ platform_service }}
   ({{ platform_registered_address }})

2. Kronologi Kejadian:
   {{ chronology }}

3. Kerugian yang Dialami:
   - Total dana tertahan: Rp {{ frozen_amount }}
   - Sejak tanggal: {{ freeze_date }}
   - Sudah {{ days_since }} hari tanpa penyelesaian

4. Upaya yang Sudah Dilakukan:
   {% for attempt in resolution_attempts %}
   - {{ attempt.date }}: {{ attempt.description }} ({{ attempt.result }})
   {% endfor %}

5. Tuntutan:
   - Pencairan saldo sebesar Rp {{ frozen_amount }}
   - {{ additional_demands }}

6. Bukti-bukti Terlampir:
   {% for evidence in evidence_list %}
   - {{ evidence.filename }}: {{ evidence.description }}
   {% endfor %}

Demikian pengaduan ini saya sampaikan. Atas perhatian dan tindak lanjutnya, saya ucapkan terima kasih.

Hormat saya,
{{ user_name }}
""")
```

**Evidence Validation:**

```python
# Evidence validator (pseudo-code)

def validate_evidence(case_type: str, evidence: dict) -> dict:
    """
    Validates that collected evidence is sufficient for the case type.
    Returns {is_valid: bool, missing_fields: list, warnings: list}
    """
    required = get_required_evidence(case_type)
    missing = [r for r in required if r not in evidence]
    warnings = []
    
    # Check for screenshots that are actually readable
    for key, value in evidence.items():
        if key.endswith("_screenshot") and value:
            if not is_image_readable(value):
                warnings.append(f"{key}: screenshot tidak terbaca, mohon kirim ulang")
    
    return {
        "is_valid": len(missing) == 0,
        "missing_fields": missing,
        "warnings": warnings,
        "completeness_pct": (len(required) - len(missing)) / len(required) * 100
    }

def get_required_evidence(case_type: str) -> list:
    schemas = {
        "ewallet_frozen": [
            "account_screenshot", "balance_screenshot",
            "error_message", "last_transaction_history",
            "cs_chat_logs", "account_phone", "account_email"
        ],
        "marketplace_frozen": [
            "seller_dashboard_screenshot", "frozen_balance_screenshot",
            "order_history", "appeal_ticket_numbers",
            "cs_responses_screenshots", "store_url",
            "identity_verification_attempts"
        ],
        "cod_return_dispute": [
            "order_screenshot", "return_reason_screenshot",
            "buyer_communication_screenshots",
            "shipping_proof", "video_unboxing",
            "product_photos"
        ],
        # ... more case types
    }
    return schemas.get(case_type, [])
```

**SQL Schema (simplified):**

```sql
CREATE TABLE cases (
    case_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(user_id),
    case_type VARCHAR(50) NOT NULL,  -- ewallet_frozen, marketplace_frozen, etc.
    platform VARCHAR(50) NOT NULL,   -- gopay, ovo, dana, shopee, tiktokshop, tokopedia
    state VARCHAR(50) NOT NULL DEFAULT 'initiated',
    frozen_amount DECIMAL(18,2),
    currency VARCHAR(3) DEFAULT 'IDR',
    user_demand TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    resolved_at TIMESTAMPTZ,
    resolution_notes TEXT,
    concierge BOOLEAN DEFAULT FALSE
);

CREATE TABLE case_evidence (
    evidence_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id UUID REFERENCES cases(case_id),
    evidence_type VARCHAR(50) NOT NULL,  -- screenshot, bank_statement, cs_chat, etc.
    file_path TEXT NOT NULL,
    file_hash VARCHAR(64),
    description TEXT,
    is_valid BOOLEAN DEFAULT NULL,  -- NULL=unverified, TRUE=valid, FALSE=invalid
    validation_notes TEXT,
    uploaded_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE case_actions (
    action_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    case_id UUID REFERENCES cases(case_id),
    action_type VARCHAR(50) NOT NULL,  -- appeal_filed, ojk_filed, media_published, etc.
    channel VARCHAR(50) NOT NULL,      -- seller_center, ojk_portal, bi_portal, mediakonsumen
    template_sent TEXT,
    response_received TEXT,
    status VARCHAR(20) DEFAULT 'pending',  -- pending, sent, acknowledged, rejected, resolved
    filed_at TIMESTAMPTZ,
    responded_at TIMESTAMPTZ,
    notes TEXT
);

CREATE TABLE platform_policies (
    policy_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    platform VARCHAR(50) NOT NULL,
    policy_type VARCHAR(50) NOT NULL,  -- freezing, appeals, penalties, commissions
    title TEXT NOT NULL,
    description TEXT,
    effective_date DATE,
    source_url TEXT,
    crawled_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_cases_user ON cases(user_id);
CREATE INDEX idx_cases_state ON cases(state);
CREATE INDEX idx_cases_platform ON cases(platform);
CREATE INDEX idx_actions_case ON case_actions(case_id);
```

### 5.4 WhatsApp Bot Conversation Flow

```
User: "Halo, akun TikTok Shop saya dibekukan. Saldo Rp 8.3 juta tidak bisa ditarik."

Bot: "Hai! Mohon maaf mendengar pengalaman Anda. Saya PengaduanKu, asisten 
pemulihan saldo digital.

Saya akan bantu Anda mengajukan banding ke TikTok Shop, melapor ke OJK, 
dan melakukan langkah-langkah lain yang diperlukan.

Pertama, tolong konfirmasi:
1. Platform: TikTok Shop
2. Saldo tertahan: Rp 8,300,000
3. Status akun: Dibekukan total / Hanya saldo dibekukan?
4. Sudah berapa kali Anda menghubungi TikTok CS?

(Balas dengan nomor jawaban Anda)"

User: "1. TikTok Shop, 2. Rp 8.3 juta, 3. Dibekukan total, 4. 3 kali"

Bot: "Terima kasih! Kasus Anda tercatat sebagai #PKD-20260728-001.

Untuk memulai, saya perlu bukti-bukti berikut:
1. Screenshot dashboard seller yang menunjukkan status dibekukan
2. Screenshot saldo yang tertahan
3. Tangkapan layar percakapan dengan CS TikTok (3 kali)
4. Nomor tiket banding yang sudah diajukan
5. URL toko Anda

Silakan kirim satu per satu. Ketik "SELESAI" jika sudah kirim semua, 
atau "NANTI" jika ingin lanjut nanti."

[... user sends screenshots ...]

Bot: "Bukti diterima! Saya sedang memeriksa kelengkapan...

Hasil verifikasi:
[OK] Dashboard screenshot: valid
[OK] Saldo screenshot: valid
[OK] CS chat logs: valid (3 percakapan terdeteksi)
[!] Nomor tiket banding: belum ada
[OK] URL toko: valid

Mohon kirim nomor tiket banding jika ada. Jika belum punya, 
saya akan buatkan template banding baru untuk diajukan.

Ketik "LANJUT" untuk generate template banding."
```

---

## 6. Platform-Specific Deep Dives

### 6.1 TikTok Shop Dispute Process

TikTok Shop uses an automated dispute system where:
- AI flags accounts for "policy violations" (suspicious activity, promo abuse, counterfeit suspicion)
- Appeal is submitted through TikTok Seller Center
- Appeal goes back to the same AI system for review
- No human reviewer is available unless the case reaches Kementerian UMKM or DPR attention

**Known appeal weaknesses:**
1. No clear feedback on what evidence is needed
2. Appeals are rejected for "insufficient proof" without specifying what's missing
3. No escalation path within the platform
4. The seller is locked out of their dashboard during the freeze, making evidence collection harder

**PengaduanKu strategy for TikTok Shop:**
- Pre-appeal evidence pack: collect 12+ specific evidence items before submitting
- Multi-channel approach: appeal through TikTok + file OJK complaint + CC Kementerian UMKM simultaneously
- Kementerian UMKM referral: use Temmy Satya Permana's public statement (CNBC 2026-07-09) that they are handling TikTok cases. Reference this in the appeal.

### 6.2 Shopee Dispute Process

Shopee freezes seller balances when:
- Account hits 15 penalty points
- Identity verification fails repeatedly
- Suspicious transaction patterns detected

The Shopee Seller Center appeal process:
- Submit through "Pusat Bantuan" or specific order dispute
- Response time: 1-7 days
- Response is often a template: "penyesuaian saldo telah dilakukan"

**Known weaknesses specific to Shopee:**
1. Verification system fails with no alternative (one seller attempted 9 times)
2. Return shipping is deducted automatically before appeal
3. No human CS override available

**PengaduanKu strategy for Shopee:**
- Alternative verification pathway: guide user to verify via phone CS or visit Shopee office
- Return dispute template that references Shopee's own TOS on return verification
- Batch approach: collect cases from Facebook seller groups and submit as group complaint

### 6.3 GoPay/OVO/DANA Dispute Process

E-wallet freezes are usually temporary (2-hour to 2-day auto-resolution) but top-up failures require manual reconciliation.

**Known patterns:**
- Top-up fails: bank debited but e-wallet not credited (GoPay, recurrent issue)
- Account restriction after P2P transaction (DANA, common with crypto exchange transfers)
- Balance display error (OVO, Rp 0 display panic)

**PengaduanKu strategy for e-wallet:**
- Fast-track template for bank reconciliation: format the evidence (bank statement showing debit, e-wallet statement showing no credit) into a single-page complaint that the user can submit to both the e-wallet CS and bank CS
- BI escalation: for payment system failures, direct users to BI's payment system complaint channel
- Bulk monitoring: track e-wallet service status and alert users when mass incidents occur (so they don't contact CS in panic and can wait for auto-resolution)

### 6.4 COD Return Disputes

COD return fraud is a structural issue where:
- Buyers mark "item not as described" or "buyer rejected package"
- Sellers are charged return shipping (up to Rp 10,000 per transaction for TikTok Shop)
- The seller has no independent verification of the return reason

**PengaduanKu strategy for COD returns:**
- Pre-shipping evidence kit: guide sellers to photograph/video every outgoing COD package with the label visible. Store this for dispute use.
- Carrier API integration: fetch delivery status from JNE/TIKI/SiCepat/Pos Indonesia to verify whether a "buyer rejected" claim matches the carrier's tracking
- Automated dispute template: generate a dispute draft that cross-references carrier tracking, seller photos, and buyer's stated reason

---

## 7. Revenue Model & Unit Economics

### 7.1 Pricing Tiers

| Tier | Price | Features | Target |
|------|-------|----------|--------|
| Self-Service (per case) | Rp 25,000 - Rp 50,000 | Template generation, evidence checklist, filing guide | One-time victims |
| Seller Protection (monthly) | Rp 30,000 - Rp 50,000 | Unlimited self-service cases, status tracking, policy change alerts | Active marketplace sellers |
| Concierge (per case) | Rp 250,000 fixed OR 10% of recovered amount (whichever higher) | Full human handling, multi-channel filing, negotiation, weekly updates | Complex/large cases |
| Enterprise (annual) | Rp 5,000,000 - Rp 20,000,000 | White-label dispute portal, SLA, dedicated account manager | Seller communities, UMKM cooperatives, incubation hubs |

### 7.2 Willingness-to-Pay Validation

| Case Value | Max WTP (one-time) | Source |
|------------|-------------------|--------|
| E-wallet frozen (Rp 500K - Rp 5M) | Rp 25,000 - Rp 50,000 | Demand-mining saldo-ewallet-dibekukan: "konsultasi satu kasus Rp25-50rb" |
| Shopee frozen (Rp 28M) | Rp 50,000 - Rp 150,000 | Demand-mining saldo-penjual-shopee: "Rp50-150rb per kasus" |
| TikTok frozen (Rp 65M) | Rp 250,000 - Rp 1,000,000 | Demand-mining tiktok-shop-akun-dibekukan: "Rp250rb-1jt per kasus" |
| TikTok frozen (Rp 3T/500 sellers) | 10-15% of recovered | Same source: "persentase 10-15% dari saldo berhasil dicairkan" |
| Return dispute (Rp 130K) | Rp 15,000 - Rp 30,000 | Demand-mining seller-rugi-retur: "Rp15-30rb per dispute" |
| Monthly seller protection | Rp 25,000 - Rp 99,000 | Cross-referenced from all seller pain files |

### 7.3 Unit Economics (Year 1 Projection)

**Assumptions:**
- Total Indonesian marketplace sellers: 15M+ (Shopee 10M, TikTok Shop 6M, Tokopedia 5M, with overlap)
- Incident rate: 0.5% experience freezing annually = 75,000 cases
- E-wallet users: 100M+, 0.2% freeze incident rate = 200,000 cases
- Year 1 target: capture 1% of total cases = 2,750 cases
- Self-service/concierge mix: 80% self-service at Rp 40K avg, 20% concierge at Rp 500K avg

**Revenue projection:**
- Self-service: 2,200 cases x Rp 40,000 = Rp 88,000,000
- Concierge: 550 cases x Rp 500,000 = Rp 275,000,000
- Monthly subscriptions: 500 subscribers x Rp 40,000 x 12 = Rp 240,000,000
- Total Year 1 revenue: Rp 603,000,000

**Cost structure:**
- WhatsApp API: Rp 5,000,000/year (Twilio/WATI)
- Server/hosting: Rp 12,000,000/year
- Concierge team (2 staff): Rp 180,000,000/year
- Marketing: Rp 60,000,000/year
- Legal/compliance: Rp 30,000,000/year
- Total Year 1 cost: Rp 287,000,000

**Year 1 Net: Rp 316,000,000** (52% margin, breakeven at ~1,500 cases or ~3 months)

**Scaling:** Year 2 target 5% market capture (13,750 cases) with same unit economics would yield Rp 3B+ revenue with 60%+ margin (concierge scales sublinearly via case playbook and tooling).

### 7.4 Alternative: Escrow Bridge Product

An adjacent product (mentioned in inbox/2026-07-14-marketplace-saldo-escrow.md) is a cash-flow bridge: while the seller's funds are frozen on the platform, a third-party lender advances a percentage (60-80%) of the frozen amount at a fee (5-15% of advanced amount). This bridges the gap during the 1-8 week dispute process.

This is higher risk (advance is unsecured, relies on successful dispute outcome) but higher margin. It requires:
- Capital pool of Rp 500M - Rp 2B
- Underwriting model based on case type, platform, frozen amount, and seller history
- Collection agreement with the seller (they repay if dispute is lost)
- Fraud detection (seller's account isn't actually frozen)

This product is separate from PengaduanKu but can be offered as a premium add-on.

---

## 8. Competitive Landscape

### 8.1 Direct Competitors

| Competitor | Type | Strengths | Weaknesses | Gap |
|------------|------|-----------|------------|-----|
| Platform CS (first-line) | In-app support | Free, integrated | Template responses, slow, no escalation | No external leverage |
| OJK Portal Perlindungan Konsumen | Regulatory | Formal complaint, legally binding | Slow (weeks), bureaucratic, unknown to most users | No guidance layer |
| MediaKonsumen | Public complaint | Public pressure, free | Non-binding, editorial gatekeeping | No status tracking |
| Jasa Admin TikTok/Shopee | Freelance admin | Human touch, experienced | Informal, no guarantee, variable quality | No systematic process |
| Lawyer/advocate | Legal | Full legal force | Expensive (Rp 5-50M), intimidating | Overkill for Rp 28M cases |
| Seller community groups | Peer support | Free, empathetic | No process, no leverage | No systematic approach |

### 8.2 Indirect Competitors

- **Pusat Bantuan Shopee/TikTok** — internal knowledge bases that explain freezing policies but don't help recover funds
- **Artikel panduan (Rekapcepat, Sidotechnews etc.)** — free blog posts about "how to unfreeze account" — generic, no personalized assistance
- **Agen iklan marketplace** — some agencies help sellers with admin including dispute, but it's a side service not a product

### 8.3 Competitive Moat

PengaduanKu's moat comes from:

1. **Evidence collection methodology:** Structured evidence checklists per case type, per platform, with auto-validation. This is systematic knowledge accumulated over time, not easily replicated.

2. **Template library:** Constantly updated templates for each platform's appeal process, OJK format, BI format, MediaKonsumen format. Each template is battle-tested against actual resolutions.

3. **Status tracking across channels:** One dashboard showing the status of all filed complaints across all channels — the user doesn't need to log into 5 different portals.

4. **Escalation timing intelligence:** Knowledge of when to escalate, to whom, and using what language. This timing heuristic is derived from pattern analysis of successful vs. failed appeals.

5. **Multi-platform knowledge:** Deep understanding of TikTok Shop, Shopee, Tokopedia, Lazada, GoPay, OVO, DANA dispute processes — a competitor would need months to replicate.

6. **Network effects:** As more users join, the platform builds a database of resolution patterns (what works for which platform + case type), improving the escalation engine for all users.

---

## 9. Go-to-Market Strategy

### 9.1 Channel Strategy

**Phase 1 (Months 1-2): Organic Community Entry**

- Actively participate in existing seller communities (Facebook groups "Seller Shopee Indonesia", "Komunitas Seller TikTok Shop", X threads about frozen accounts)
- Post free guides: "Cara Banding Saldo TikTok Shop Dibekukan" (step-by-step)
- Include a CTA to the WhatsApp bot for personalized assistance
- Target: 100 cases in first month

**Phase 2 (Months 3-4): Content Marketing**

- Publish on Medium/Kompasiana: "Pengalaman Saya Cairkan Rp 65 Juta dari TikTok Shop"
- Create TikTok videos: "3 Langkah Cairkan Saldo TikTok Shop Dibekukan"
- SEO targeting: "saldo tiktok shop dibekukan", "saldo shoppee dibekukan", "cara banding akun marketplace"
- Partner with seller-focused content creators
- Target: 500 cases/month

**Phase 3 (Months 5-6): Partnership & Paid Acquisition**

- Partner with UMKM cooperatives (KOPDI, Kopdes Merah Putih) to offer PengaduanKu as member benefit
- Partner with online seller training platforms (e.g., Gadjian, Seller.id) for bundled offering
- Google Ads on high-intent keywords ("saldo tertahan tiktok shop", "gopay error saldo tidak masuk")
- Target: 1,500 cases/month

### 9.2 Marketing Messages

**For marketplace sellers:**
"Saldo TikTok Shop atau Shopee Anda dibekukan? Kami bantu cairkan dalam 7 hari atau gratis."

**For e-wallet users:**
"GoPay/OVO/DANA error? Saldo hilang saat top up? Dapatkan panduan pengembalian dana instan."

**For affiliate creators:**
"Komisi TikTok Shop dibekukan? Pulihkan dengan template banding yang benar."

### 9.3 Pricing Launch Strategy

**Freemium model to build trust:**
- Free: basic triage + one generic template (Rp 0)
- Paid: full evidence checklist + platform-specific templates + multi-channel filing guide (Rp 25K - Rp 50K)
- Premium: concierge handling (Rp 250K)

The free tier builds trust and showcases value. The conversion from free to paid is driven by the generic template being less effective than platform-specific ones.

---

## 10. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Platforms block/restrict users who use third-party dispute services | Medium | High | Design all templates to look like user-created content. Never submit from a centralized account. Concierge team acts as "personal assistant," not "agent." |
| Low conversion from free to paid | Medium | Medium | A/B test free tier limitations. Consider requiring WhatsApp opt-in before showing any template content. |
| Regulatory backlash (accused of practicing law without license) | Low | High | Partner with licensed advocates for concierge tier. Self-service tier only provides templates and guidance, not legal advice. Disclaimers on all communications. |
| Evidence stored contains sensitive user data (KTP, bank info) | High | High | Encrypt all PII at rest. Use ephemeral file storage with auto-deletion after case resolution. Regular security audits. Zero-knowledge architecture where possible. |
| Users abuse the service (fake claims, attempt to defraud platforms) | Medium | Medium | Identity verification requirement for concierge tier. Case duplication detection. Flag patterns of serial complaints from same user. |
| Templates become stale as platforms change policies | High | Medium | Automated policy change monitor (scrape platform help pages weekly). Community-sourced template updates. Dedicated person to track platform policy changes. |
| OJK/BI portals change their submission format | Medium | Low | Regular automated tests against OJK/BI portal submission flows. Fallback to manual submission guide if API/scrape breaks. |
| WhatsApp API rate limiting for high volume | Medium | Medium | Queue-based message delivery. Implement conversation windows and proactive rate limiting. Multi-provider backup (Twilio + WATI + direct Meta API). |
| Platform retaliates by permanently banning users who escalate | Low | Very High | Advise users to withdraw remaining balance before escalating. Escalate only after evidence is fully collected. Use MediaKonsumen/public pressure escalation only as last resort. |

---

## 11. Technical Appendices

### Appendix A: Complete WhatsApp Flow State Machine

```yaml
states:
  greeting:
    entry: "Halo! Saya PengaduanKu. Ceritakan masalah Anda."
    transitions:
      on_message: triage

  triage:
    intent_classification:
      - "ewallet_frozen"
      - "ewallet_topup_failed"
      - "marketplace_frozen"
      - "marketplace_return_dispute"
      - "affiliate_commission_frozen"
      - "account_banned"
      - "other"
    transitions:
      on_classified: collect_initial_details
      on_unclear: clarification

  collect_initial_details:
    fields:
      - platform: "Platform mana? (GoPay/OVO/DANA/Shopee/TikTok Shop/Tokopedia/Lazada)"
      - frozen_amount: "Berapa nominal saldo yang tertahan?"
      - freeze_date: "Kapan mulai dibekukan? (tanggal)"
      - cs_attempts: "Sudah berapa kali hubungi CS?"
    transitions:
      on_complete: validate_details
      on_incomplete: ask_missing_fields

  collect_evidence:
    checklist_retrieval:
      function: get_required_evidence(case_type, platform)
    iterations:
      - ask_evidence: "Kirim {evidence_item} (screenshot/bukti)"
      - on_received: validate_single_evidence
      - on_valid: store_evidence, ask_next
      - on_invalid: error_message, retry
    transitions:
      on_all_collected: evidence_review
      on_user_says_done: evidence_review
      on_user_says_later: save_draft, remind_after_24h

  evidence_review:
    review:
      function: validate_evidence(case_type, evidence)
    transitions:
      on_complete: generate_templates
      on_incomplete: request_missing

  generate_templates:
    templates:
      - name: platform_appeal
        priority: high
      - name: ojk_complaint
        priority: medium
      - name: bi_complaint
        priority: conditional  # only for payment failures
      - name: mediakonsumen_letter
        priority: optional
      - name: kemen_umkm_report
        priority: conditional  # only for marketplace cases
    transitions:
      on_generated: present_templates

  present_templates:
    actions:
      - show_template_1
      - ask_filing_intent: "File template ini sekarang? (Ya/Nanti)"
    transitions:
      on_yes: file_template_1
      on_no: set_reminder
      on_all_filed: monitoring

  monitoring:
    check_interval_hours: 24
    response_filter:
      - "resolved" -> case_resolved
      - "pending_more_info" -> ask_user_to_follow_up
      - "rejected" -> suggest_escalation
      - "no_response_7_days" -> auto_escalate
    transitions:
      on_resolved: case_resolved
      on_escalate: escalation
      on_user_wants_human: concierge_transfer
```

### Appendix B: Template Example — TikTok Shop Appeal

```
Subject: Banding Pembekuan Akun — [Store Name] — [Order/Reference ID]

Kepada Tim TikTok Shop,

Saya pemilik toko [Store Name] di TikTok Shop. Akun saya dibekukan 
pada tanggal [Freeze Date] dengan saldo Rp [Amount] tidak dapat ditarik.

Alasan yang tertera: [Platform's stated reason]

Saya dengan ini mengajukan banding berdasarkan hal-hal berikut:

1. [First argument with evidence reference]
   - [Evidence description]: [Evidence file name]
   
2. [Second argument with evidence reference]
   - [Evidence description]: [Evidence file name]

3. Saya telah menjadi seller aktif sejak [Join Date] dengan total 
   omzet Rp [Total Revenue] dan rata-rata rating [Rating]/5.0 dari 
   [Review Count] ulasan.

4. [Jika relevan:] Saya telah menghubungi CS TikTok Shop sebanyak 
   [N] kali ([Ticket numbers]) dan belum mendapat tanggapan yang jelas.

Saya meminta:
1. Pembukaan kembali akun TikTok Shop saya
2. Pencairan saldo sebesar Rp [Amount]
3. [Any additional demands]

[Informasi tambahan yang relevan — misal: referensi ke pernyataan 
Kementerian UMKM (CNBC Indonesia 9 Juli 2026) bahwa kasus pembekuan 
sepihak sedang difasilitasi penyelesaiannya]

Terlampir:
[Evidence 1] — [Description]
[Evidence 2] — [Description]
...

Hormat saya,
[Nama Lengkap]
[No. Telepon]
[Email]
[Store URL]
```

### Appendix C: Integration Points with Existing Vault Assets

| Vault Asset | Integration with PengaduanKu |
|-------------|------------------------------|
| 01-crawler-scrapper/x/search-operators-playbook.md | Monitor X for real-time frozen account complaints using `("saldo dibekukan" OR "akun dibekukan") (shopee OR tiktok OR tokopedia) (filter:replies)` pattern. Source new cases and trending platforms. |
| 01-crawler-scrapper/cookies-tokens/storage-safety.md | Store evidence hashes securely. Apply same Fernet/MultiFernet encryption to user PII as cookies. |
| 03-id-business-trends/bottlenecks/cod-settlement-infrastructure.md | COD return dispute module directly references COD settlement delay mechanics. Use the settlement chain model (courier to LO to hub to platform) to identify where return verification fails. |
| 03-id-business-trends/bottlenecks/qris-settlement-speed-arbitrage.md | E-wallet frozen balance product is adjacent to QRIS settlement float. Cross-sell PengaduanKu to QRIS merchants who experience payment settlement delays. |
| 03-id-business-trends/bottlenecks/anchor-of-trust-registry.md | Use the OJK whitelist from the trust registry to verify whether an e-wallet or marketplace is regulated (and thus has a dispute obligation). |
| 04-freelancer-ai-agent/mcp-servers/fastwork-mcp-spec.md | Freelancers who take payments via GoPay/OVO are at risk of frozen accounts. Offer PengaduanKu as a freelancer benefit. Cross-sell with Fastwork/Sribu MCP automation. |
| 07-gaps-and-opportunities/judol-pinjol-cross-detection.md | Shared target audience (digital economy participants at risk of fund loss). Cross-sell: "Was your account frozen? PengaduanKu helps." |
| 07-gaps-and-opportunities/loker-scam-verifier.md | Users who were almost scammed by fake jobs may also be victims of frozen accounts. Shared WhatsApp bot backend. |
| 03-id-business-trends/demand-mining/biaya-marketplace-meroket-press-umkm.md | Sellers who complain about rising marketplace costs are the same sellers who get their accounts frozen. Cross-sell as margin protection. |
| 03-id-business-trends/demand-mining/pencari-kerja-berpengalaman-gagal-tembus-seleksi-cv.md | Adjacent: job seekers use GoPay/OVO for transport. If their e-wallet is frozen they can't attend interviews. |

### Appendix D: KPI Dashboard Schema

```sql
CREATE TABLE daily_metrics (
    date DATE PRIMARY KEY,
    new_cases INT,
    cases_in_progress INT,
    cases_resolved INT,
    cases_escalated INT,
    avg_resolution_time_hours DECIMAL(10,2),
    total_frozen_amount_reported DECIMAL(18,2),
    total_frozen_amount_recovered DECIMAL(18,2),
    recovery_rate_pct DECIMAL(5,2),
    self_service_revenue DECIMAL(18,2),
    concierge_revenue DECIMAL(18,2),
    subscription_revenue DECIMAL(18,2),
    new_seller_subscriptions INT,
    total_subscribers INT,
    wa_bot_conversations INT,
    evidence_files_stored INT,
    templates_generated INT,
    active_concierge_cases INT
);

CREATE TABLE platform_metrics (
    platform VARCHAR(50) NOT NULL,
    date DATE NOT NULL,
    cases INT,
    resolved INT,
    avg_resolution_days DECIMAL(5,2),
    recovery_rate_pct DECIMAL(5,2),
    PRIMARY KEY (platform, date)
);

CREATE TABLE template_performance (
    template_id UUID PRIMARY KEY,
    template_type VARCHAR(50),
    platform VARCHAR(50),
    case_type VARCHAR(50),
    success_rate_pct DECIMAL(5,2),
    total_uses INT,
    avg_resolution_days DECIMAL(5,2),
    last_updated TIMESTAMPTZ,
    version INT
);
```

### Appendix E: Deployment Architecture (Minimum Viable)

```
[WhatsApp User] <--WA API--> [Twilio/Meta Cloud API]
                                  |
                            [FastAPI Backend]
                                  |
                    +-------------+-------------+
                    |             |             |
               [PostgreSQL]  [Object Store  [Celery Worker]
                              (evidence)]     (async tasks:
                                               template gen,
                                               policy monitor,
                                               status checker)
                    |
              [Jinja2 Templates]
                    |
              [Template Files]
              (platform_appeal.md,
               ojk_complaint.md,
               bi_complaint.md,
               mediakonsumen_letter.md,
               kemen_umkm_report.md)

Deployment: Docker Compose on Rp 500K/month VPS (DigitalOcean/Dewacloud)
Scaling: Kubernetes when >10K concurrent cases
```

### Appendix F: Legal & Compliance Notes

1. **Not legal advice:** All templates and guidance must include a disclaimer: "Template ini adalah panduan umum dan bukan konsultasi hukum. Untuk kasus kompleks, konsultasikan dengan advokat berlisensi."

2. **Data privacy:** User KTP, bank account details, and platform credentials must be encrypted at rest (AES-256-GCM). Evidence auto-delete 90 days after case closure. Users can request data deletion at any time.

3. **Platform TOS compliance:** The service should not violate platform terms of service. Templates are composed by the user themselves (the platform provides tools, the user submits). Concierge service acts as "personal assistant," not "authorized agent."

4. **OJK registration:** If the service handles complaints on behalf of users en masse, it may need registration as a consumer complaint service. Consult with OJK early.

5. **Payment gateway:** For subscription/concierge payments, use a licensed payment aggregator (Xendit, Midtrans, DOKU) with proper escrow for concierge fee based on recovery percentage.

---

## 12. New Gaps Discovered

During research for this opportunity one-pager, I identified the following gaps that the vault does not yet cover:

### Gap 1: Platform Dispute Timeline Registry
**Suggested path:** `01-crawler-scrapper/dispute/recovery-timeline-database.md`
**Description:** A structured database (regularly updated via crawler) tracking how long each platform (TikTok Shop, Shopee, Tokopedia, Lazada, GoPay, OVO, DANA) takes to resolve frozen balance disputes. Tracked dimensions: platform, case type, total frozen amount, resolution time, escalation used (CS only vs CS+OJK vs CS+OJK+media), outcome. This feeds the escalation timing engine for PengaduanKu. Currently all resolution time data is anecdotal.

### Gap 2: Marketplace Penalty Point Monitor
**Suggested path:** `01-crawler-scrapper/marketplace/penalty-point-monitor.md`
**Description:** An automated monitor that scrapes Shopee/TikTok Shop/Tokopedia policy pages for changes to penalty point systems, account restriction triggers, and appeal processes. Shopee's 15-point freeze threshold changes periodically. TikTok Shop's 7 policy changes in 2026 caught many sellers off guard. A crawler that flags policy changes and maps them to seller risk profiles would be a valuable input to PengaduanKu's preventive module.

### Gap 3: Kementerian UMKM Public Complaint Channel Mapping
**Suggested path:** `01-crawler-scrapper/regulatory/kemen-umkm-complaint-monitor.md`
**Description:** Map all public-facing complaint channels available through Kementerian UMKM (hotline, email, WhatsApp, physical offices per province, Peradi partnership). Document response times and effectiveness per channel. Currently the only documented Kemen UMKM action on frozen accounts is through DPR pressure (cnbcindonesia.com 2026-07-09). A comprehensive channel registry would help PengaduanKu guide users to the most effective government channel for their region.

### Gap 4: E-Wallet Service Status Aggregator
**Suggested path:** `01-crawler-scrapper/ewallet/service-status-monitor.md`
**Description:** A real-time status page (aggregating from social media, news, and direct API checks) for GoPay, OVO, DANA, ShopeePay, LinkAja service disruptions. This would allow PengaduanKu to detect mass incidents early and advise users to wait rather than panic-contact CS. It also provides data for the BI complaint channel (systemic payment failures need different handling than individual frozen accounts).

### Gap 5: Marketplace Seller Protection Asuransi Mikro
**Suggested path:** `03-id-business-trends/bottlenecks/marketplace-seller-protection-insurance.md`
**Description:** A micro-insurance product covering marketplace sellers against frozen balance losses (up to a cap, say Rp 5 million per incident). Premium would be Rp 5,000-15,000 per month per seller. Pay-out triggered when dispute is confirmed (by platform admitting error or OJK ruling). This is distinct from the concierge recovery service (which is fee-for-service) — insurance is risk-pooled. The two products complement each other: PengaduanKu helps recover funds, insurance provides liquidity during the recovery process. This product needs underwriting data from the dispute timeline registry (Gap 1 above).

### Gap 6: TikTok Shop Affiliate Commission Recovery
**Suggested path:** `07-gaps-and-opportunities/inbox/2026-07-28-tiktok-affiliate-commission-recovery.md`
**Description:** A specialized sub-product within PengaduanKu focused on TikTok Shop affiliate creators whose commissions are frozen due to seller policy violations (e.g., the seller they promoted engaged in free shipping abuse). This is a distinct case type because: (a) the affiliate didn't violate any policy themselves, (b) they have no direct relationship with the seller, (c) their only recourse is TikTok Shop affiliate team, not seller support. The evidence collection and appeal template differ significantly from seller frozen balance cases.

---

## Appendix G: Comparison with Existing Vault Products

| Dimension | PengaduanKu | judol-pinjol-cross-detection | loker-scam-verifier |
|-----------|-------------|------------------------------|---------------------|
| Core problem | Frozen balances & disputes | Cross-crime fraud detection | Pre-payment job scam detection |
| User | Marketplace sellers, e-wallet users | General public, financial institutions | Job seekers |
| Trigger | Account freeze/dispute happens | Before engaging with loan/gambling | Before paying for job application |
| Action | Recovery & escalation | Check entity reputation | Verify job listing authenticity |
| Revenue | Per-case + subscription | B2B feed + B2C check | B2C per-check + B2B API |
| Channel | WhatsApp bot | WhatsApp + API | WhatsApp bot |
| Status in vault | Opportunity (new) | Full opportunity (done) | Full opportunity (done) |

All three share a WhatsApp-first interface and anti-fraud DNA but serve different moments in the user journey. PengaduanKu is post-loss (recovery), judol-pinjol is pre-engagement (verification), and loker-scam is pre-payment (verification). A unified "digital safety" WhatsApp bot bundling all three would be the ultimate goal.

---

*This document is based on vault demand-mining files, direct news article curl extraction, and synthesis of existing opportunity one-pagers. Web search/extract tools were blocked this tick (PARALLEL_API_KEY missing); all cited URLs were either extracted via direct curl or sourced from existing vault content. Figures marked with "source: demand-mining file" are from vault documents created on the date specified and have not been independently verified this tick. No data was invented; where a source was unreachable it is noted.*
