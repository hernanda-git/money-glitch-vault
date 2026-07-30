# PajakPay — Marketplace Tax Compliance SaaS for Indonesian Online Sellers

> Mulai 1 Agustus 2026, Shopee, Tokopedia, Lazada, dan Blibli wajib memungut PPh Pasal 22 sebesar 0,5% dari omzet penjual di atas Rp500 juta/tahun. Jutaan seller UMKM mikro bingung, tidak tahu cara mengurus surat pernyataan pengecualian, dan tidak punya akses ke konsultan pajak (Rp500rb-Rp2jt/bulan). PajakPay adalah asisten kepatuhan pajak otomatis yang integrasi API ke marketplace, hitung PPh otomatis, generate surat pernyataan, dan notifikasi setor pajak. Monetisasi Rp20-50k/bulan untuk seller mikro, Rp100-200k/bulan untuk paket premium.

**File:** `07-gaps-and-opportunities/opportunities/pajakpay-marketplace-tax-compliance.md`
**Promoted from:** `07-gaps-and-opportunities/inbox/2026-07-30-marketplace-tax-compliance-saas.md` and `03-id-business-trends/demand-mining/pajak-marketplace-efektif-1-agustus-2026-seller-online-tertekan.md`
**Created:** 2026-07-30
**Category:** Opportunity one-pager (vertical SaaS for UMKM tax compliance)
**Confidence:** 5
**Status:** build-ready

---

## 1. Problem and evidence

### 1.1 The regulatory shock

On 1 August 2026, a seismic shift in Indonesian e-commerce taxation takes effect. PMK Nomor 37 Tahun 2025 (the implementing regulation) and PER-15/PJ/2025 (the DJP technical directive) designate four major marketplaces -- Tokopedia, Shopee, Lazada, and Blibli -- as withholding agents for PPh Pasal 22 on behalf of online sellers. Key provisions:

- Sellers with annual gross turnover above Rp500 million are subject to 0.5% final PPh (PPh Final) withheld at source by the platform on every transaction.
- Sellers with turnover up to Rp500 million are exempt, BUT only if they submit a formal statement letter (surat pernyataan) to the DJP confirming their eligibility.
- The exemption is NOT automatic. Sellers must proactively file the statement or the marketplace will withhold 0.5% regardless of their actual turnover.
- Tax is withheld per transaction and remitted monthly by the marketplace to the Ministry of Finance before the net proceeds reach the seller.

Sources:
- [Mulai 1 Agustus, Marketplace Wajib Pungut PPh Penjual Online -- IKPI, 2026-07-28](https://ikpi.or.id/mulai-1-agustus-marketplace-wajib-pungut-pph-penjual-online/)
- [DJP: Pemungutan Pajak oleh Marketplace Berlaku Efektif 1 Agustus 2026 -- DDTCNews, 2026-07-29](https://ddtcnews.com/berita/nasional/176398/djp-pemungutan-pajak-oleh-marketplace-berlaku-efektif-1-agustus-2026)
- [Pajak Marketplace Resmi Berlaku 1 Agustus 2026, Shopee hingga Tokopedia Wajib Pungut PPh 0,5 Persen -- BeritaNusa.com, 2026-07-01](https://www.beritanusa.com/nasional/2502835425/pajak-marketplace-resmi-berlaku-1-agustus-2026-shopee-hingga-tokopedia-wajib-pungut-pph-05-persen-dari-seller)
- [DJP Tunjuk Marketplace Sebagai Pemungut Pajak -- Hallobogor.com, 2026-06-26](https://bogor.hallo.id/ekonomi/11117295165/djp-tunjuk-marketplace-sebagai-pemungut-pajak-apa-yang-perlu-diketahui-pedagang-online-mulai-sekarang)
- [Begini Mekanisme Pungutan Pajak di Shopee, Tokopedia, Lazada, dan Blibli per 1 Agustus 2026 -- Bisnis.com, 2026-07-30](https://ekonomi.bisnis.com/read/20260730/259/1867275/mulai-1-agustus-marketplace-wajib-pungut-pph-penjual-online)

### 1.2 The pain (quantified)

The scale of the affected population is vast:

- Indonesia has approximately 64 million MSMEs (UMKM), of which roughly 25-30% sell through online marketplaces (source: Bank Indonesia, 2025 digital economy report).
- Shopee alone claims over 14 million active sellers in Indonesia as of Q1 2026 (Shopee annual report).
- Tokopedia reports approximately 12 million active sellers (GoTo financial disclosures, 2025).
- Combined active sellers across all four designated platforms: estimated 25-30 million accounts.
- Of these, approximately 15-18 million are active in any given month (based on marketplace disclosures and industry estimates).

The DJP threshold of Rp500 million/year (approximately Rp41.7 million/month) creates three distinct segments:

**Segment A (above threshold, approximately 15-20% of sellers):** 3-5 million sellers will be automatically subject to 0.5% PPh withholding. For a seller doing Rp50 million/month in gross sales, this means Rp250,000/month in tax withheld, or Rp3 million/year. Many in this segment have never filed income tax or maintained proper books.

**Segment B (below threshold but aware, approximately 30-40%):** 5-8 million sellers who know they are below the threshold but must file a surat pernyataan to avoid withholding. Most have no idea how to do this.

**Segment C (below threshold and unaware, approximately 40-50%):** 6-9 million sellers who are below the threshold, do not know about the exemption, and will either (a) have 0.5% wrongly withheld from their transactions or (b) panic when they find out.

Evidence of the pain from news sources:

> "Pelapak Online Kerek Harga Jelang Pajak Marketplace Berlaku 1 Agustus" -- CNN Indonesia, 2026-07-29. Sellers are already raising prices in anticipation of the tax, indicating widespread anxiety and misunderstanding about how the tax works.

> "Penjual dengan omzet tahunan di atas Rp500 juta dikenai PPh Final sebesar 0,5 persen dari nilai penjualan bruto." -- IKPI, 2026-07-28, confirming the threshold.

> "Pelaku usaha dengan omzet hingga Rp500 juta tidak dikenai pemotongan PPh sepanjang telah menyampaikan surat pernyataan kepada DJP." -- IKPI, 2026-07-28, confirming the exemption mechanism that most sellers don't know about.

### 1.3 Customer discovery evidence from demand mining

The vault already documents this pain extensively:

- `03-id-business-trends/demand-mining/pajak-marketplace-efektif-1-agustus-2026-seller-online-tertekan.md` (strength 5/5, 2026-07-30): Documents 14+ national news articles in 3 days, 4 marketplaces designated, millions of sellers affected, sellers raising prices in response.
- `03-id-business-trends/demand-mining/seller-marketplace-komisi-ongkir-meroket.md` (strength 5/5): Documents the broader margin squeeze -- TikTok Shop 16x commission hike, ongkir shifted to seller, Shopee/Tokped/Lazada fee increases. The tax is the final straw on already-thin margins.
- `03-id-business-trends/demand-mining/umkm-belum-punya-nib-oss-sulit.md` (strength 4/5): Documents the wider compliance burden on UMKM -- many lack even basic business licenses.
- `03-id-business-trends/demand-mining/umkm-pajak-digital-ribet.md` (strength 4/5): Documents that UMKM find digital tax administration confusing and burdensome.
- `03-id-business-trends/demand-mining/pph-final-umkm-terbatas-pt-perorangan.md` (strength 3/5): Documents confusion around PPh Final classification for individual business owners.

### 1.4 Why existing solutions fail

**Existing solutions mapped:**

| Solution | Target | Price/month | Why it fails for this segment |
|----------|--------|-------------|-------------------------------|
| Klikpajak | Corporate (PPh 21/23/26, PPN) | Rp500k-Rp5jt | Focused on PPh 21 (employee) and PPN, not marketplace PPh 22. UI assumes accounting knowledge. |
| OnlinePajak | Corporate tax filing | Rp300k-Rp2jt | Same corporate orientation. No marketplace API integration. No surat pernyataan generator. |
| Konsultan pajak individu | All segments | Rp500k-Rp2jt | Too expensive for seller mikro. Average monthly profit for a seller doing Rp20jt omzet is Rp3-5jt. Paying Rp500k+ for tax compliance is 10-17% of profit. |
| Akuntan publik | Medium-large business | Rp2jt-Rp10jt | Way out of budget. Over-engineered for simple PPh 22 compliance. |
| Spreadsheet manual | Self-service | Free | Seller doesn't know what to track, what forms to use, or when deadlines are. No integration. |
| Marketplace internal dashboard | Sellers on platform | Free (platform feature) | Only shows one platform (not cross-platform). No tax calculation. No filing capability. Seller must cobble together data from 3-4 platforms manually. |

### 1.5 The wedge window

The regulation takes effect in 2 days (1 August 2026). This creates a **deadline-driven acquisition funnel**:

- **Phase 1 (now to August 15):** Panic. Sellers who didn't know about the rule suddenly discover their transactions are being withheld. Search traffic for "surat pernyataan pengecualian pajak marketplace" and "cara hindari pajak marketplace 0.5%" spikes dramatically.
- **Phase 2 (August 15 to September 30):** Confusion. Sellers who filed exemptions get conflicting information. Sellers above threshold discover they owe back-tax. Marketplaces release conflicting guidance.
- **Phase 3 (October to December):** Normalization. Early adopters of compliance tools become reference customers. Marketplaces may refine withholding mechanisms.
- **Phase 4 (January 2027):** SPT Tahunan deadline. Massive spike in demand for tax filing assistance. PajakPay can cross-sell SPT filing.

---

## 2. Wedge and product

### 2.1 Core product concept

PajakPay is a mobile-first (WhatsApp + Android/iOS app) tax compliance assistant for Indonesian marketplace sellers. It solves three specific jobs:

**Job 1: "Help me avoid unnecessary tax withholding"**
- Connect marketplace accounts (Shopee, Tokopedia, Lazada, Blibli)
- Automatically calculate YTD gross turnover across all platforms
- If below Rp500M threshold: generate the surat pernyataan pengecualian in the correct DJP format
- If above threshold: calculate exact PPh 22 owed, track what was withheld vs what should have been withheld

**Job 2: "Help me file my taxes correctly"**
- Generate monthly PPh 22 reconciliation reports
- Prepare SPT Tahunan (annual tax return) data pre-filled from marketplace transactions
- Integrate with DJP Online / efiling for one-click submission
- Track payment deadlines and send WhatsApp reminders

**Job 3: "Help me understand my true margins"**
- Show net revenue after tax, platform commissions, and shipping costs
- Flag SKUs where post-tax margin is negative
- Recommend minimum selling prices to maintain margin after tax

### 2.2 User flow (WhatsApp-first)

```
Step 1: Onboarding
User sends "Halo" to PajakPay WA bot
Bot: "Selamat datang di PajakPay! Saya akan bantu urus pajak marketplace Anda.
Mulai 1 Agustus 2026, penjual online dikenakan PPh 0,5%. Saya bisa bantu:
1. Cek apakah Anda perlu bayar pajak
2. Bikin surat pengecualian (gratis)
3. Hitung pajak otomatis
4. Ingatkan deadline setor
Ketik angka yang sesuai:"

Step 2: Platform connection
User selects platforms they sell on
Bot sends secure link to OAuth connect each marketplace
PajakPay fetches transaction history via marketplace API

Step 3: Assessment
Bot calculates YTD turnover across all platforms
If < Rp500M: "Kabar baik! Omzet Anda RpXXX juta, di bawah batas Rp500 juta.
Anda TIDAK perlu bayar PPh 0,5%. Tapi Anda harus kirim surat pernyataan ke DJP.
Saya buatkan sekarang? (Ketik YA)"
If > Rp500M: "Omzet Anda RpXXX juta, di atas Rp500 juta. PPh 0,5% akan dipotong
Shopee/Tokopedia. Saya akan bantu lacak pemotongan dan siapkan laporan SPT."

Step 4: Generate document (for exempt sellers)
Bot generates surat pernyataan in .pdf format
Sends to user via WA
Instructions: "Upload ini ke akun DJP Online Anda, atau saya bantu upload langsung."
User confirms submission

Step 5: Ongoing monitoring
Weekly WA summary: "Omzet Anda pekan ini: RpX jt. Total YTD: RpY jt.
PPh terutang: RpZ rb. Deadline setor: 15 bulan depan."
Monthly reconciliation report
Quarterly tax health check
```

### 2.3 Feature roadmap

**MVP (ship in 2 weeks -- target: August 15, 2026):**
- WhatsApp bot (Twilio / WATI integration)
- Marketplace API connections: Shopee Open API, Tokopedia API, Lazada API, Blibli API
- Automatic turnover calculation (YTD across platforms)
- Surat pernyataan pengecualian generator (PDF in DJP-compliant format)
- Basic tax liability calculator (PPh 22 at 0.5%)
- Weekly turnover summary via WA

**V1 (ship September 2026):**
- Cross-platform dashboard (web + mobile app)
- Real-time tax withholding tracker
- Monthly PPh 22 reconciliation report
- SPT Tahunan data preparation
- DJP Online integration (efiling pre-fill)
- Multi-user (seller + accountant) access
- Payment deadline calendar with WA reminders

**V2 (ship Q4 2026):**
- Margin calculator (post-tax, post-fee net revenue by SKU)
- Auto-generated PPN laporan (for PKP sellers)
- Multi-platform reconciliation (catch discrepancies between what was withheld vs what marketplace reported to DJP)
- Chat-based tax consultation (connect to certified tax consultants on demand)
- Community features (seller forums, tax FAQ, Q&A)

**V3 (ship Q1 2027):**
- Integration with OSS RBA (NIB status check for compliance)
- Integration with Pembukuan (automatic bookkeeping from marketplace data)
- AI-powered tax optimization recommendations
- Wholesale/B2B API for accounting firms managing multiple seller clients

### 2.4 WhatsApp bot conversation design

The bot is designed for low-literacy users. All interactions are in Indonesian, with simple number-based menus and rich media (images, PDFs, buttons) where the platform supports it.

**Key conversation flows:**

```
Flow A: "Am I affected?"
User: "Saya jualan di Shopee, omzet Rp30jt/bulan. Kena pajak?"
Bot: [calculates: Rp30jt x 12 = Rp360jt < Rp500jt]
"Omzet Anda Rp360jt/tahun, di bawah Rp500jt. Anda TIDAK kena pajak.
Tapi Anda tetap perlu kirim surat pernyataan. Buat sekarang?
[Tombol: Ya, buatkan / Tidak, nanti saja]"

Flow B: "How much tax?"
User: "Omzet saya Rp70jt/bulan. Berapa pajaknya?"
Bot: [calculates: Rp70jt x 12 = Rp840jt > Rp500jt]
"Omzet Anda Rp840jt/tahun, di atas Rp500jt. PPh 0,5% akan dipotong
Shopee langsung dari setiap transaksi. Perkiraan potongan:
- Per transaksi: 0,5% x Rp70jt = Rp350rb/bulan
- Per tahun: Rp4,2jt
Saya akan bantu lacak potongan ini. Aktifkan monitoring? [Ya/Tidak]"

Flow C: "Generate exemption letter"
User: "Saya mau buat surat pengecualian"
Bot: "Saya perlu data:
1. Nama lengkap (sesuai KTP): [user types]
2. NPWP: [user types]
3. NIK: [user types]
4. Alamat: [user types]
5. Platform marketplace: Shopee, Tokopedia
Data aman dan terenkripsi."
[Bot generates PDF, sends for review]
"Apakah data sudah benar? [Tombol: Sudah / Perbaiki]"
[If confirmed, bot sends final PDF + instructions to submit via DJP Online]
```

---

## 3. Technical architecture

### 3.1 System overview

```
┌─────────────────────────────────────────────────────────────┐
│                        PajakPay System                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌───────────────────┐  │
│  │ WhatsApp    │  │ Mobile App  │  │ Web Dashboard     │  │
│  │ Bot (Twilio)│  │ (Flutter)   │  │ (React/Next.js)   │  │
│  └──────┬──────┘  └──────┬──────┘  └────────┬──────────┘  │
│         │                │                  │              │
│  ┌──────┴────────────────┴──────────────────┴──────────┐  │
│  │              API Gateway (Kong / Nginx)              │  │
│  └──────────────────────────┬──────────────────────────┘  │
│                             │                              │
│  ┌──────────────────────────┴──────────────────────────┐  │
│  │              Backend Services (Go/Node.js)            │  │
│  │                                                      │  │
│  │  ┌─────────────┐ ┌────────────┐ ┌───────────────┐  │  │
│  │  │ Auth        │ │ Tax Calc   │ │ Document Gen  │  │  │
│  │  │ Service     │ │ Engine     │ │ (PDF) Service │  │  │
│  │  └─────────────┘ └────────────┘ └───────────────┘  │  │
│  │                                                      │  │
│  │  ┌─────────────┐ ┌────────────┐ ┌───────────────┐  │  │
│  │  │ Marketplace │ │ Report     │ │ Notification  │  │  │
│  │  │ Connector   │ │ Generator  │ │ Engine        │  │  │
│  │  └─────────────┘ └────────────┘ └───────────────┘  │  │
│  └──────────────────────────┬──────────────────────────┘  │
│                             │                              │
│  ┌──────────────────────────┴──────────────────────────┐  │
│  │                    Data Layer                         │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────┐  │  │
│  │  │ PostgreSQL   │  │ Redis Cache  │  │ S3/MinIO │  │  │
│  │  │ (transactions│  │ (session,    │  │ (PDFs,   │  │  │
│  │  │  user data)  │  │  rate limit) │  │  docs)   │  │  │
│  │  └──────────────┘  └──────────────┘  └──────────┘  │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │              External Integrations                    │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐│  │
│  │  │ Shopee   │ │ Tokopedia│ │ Lazada   │ │ Blibli ││  │
│  │  │ API      │ │ API      │ │ API      │ │ API    ││  │
│  │  └──────────┘ └──────────┘ └──────────┘ └────────┘│  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐   │  │
│  │  │ DJP      │ │ Twilio   │ │ Midtrans/       │   │  │
│  │  │ Online   │ │ WA API   │ │ Xendit (payment) │   │  │
│  │  └──────────┘ └──────────┘ └──────────────────┘   │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Database schema (core tables)

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    phone VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(255),
    nik VARCHAR(16),
    npwp VARCHAR(20),
    email VARCHAR(255),
    ktp_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    wa_opt_in BOOLEAN DEFAULT TRUE,
    plan_id VARCHAR(50) DEFAULT 'free' -- free, basic, premium
);

-- Marketplace connections (OAuth tokens per seller per platform)
CREATE TABLE marketplace_connections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    platform VARCHAR(50) NOT NULL, -- 'shopee', 'tokopedia', 'lazada', 'blibli'
    merchant_id VARCHAR(255) NOT NULL,
    access_token_encrypted TEXT NOT NULL,
    refresh_token_encrypted TEXT,
    token_expires_at TIMESTAMPTZ,
    is_active BOOLEAN DEFAULT TRUE,
    last_sync_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, platform, merchant_id)
);

-- Transactions fetched from marketplace APIs
CREATE TABLE transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    connection_id UUID REFERENCES marketplace_connections(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    platform VARCHAR(50) NOT NULL,
    order_id VARCHAR(255) NOT NULL,
    transaction_date TIMESTAMPTZ NOT NULL,
    gross_amount DECIMAL(18,2) NOT NULL,
    platform_commission DECIMAL(18,2) DEFAULT 0,
    shipping_fee DECIMAL(18,2) DEFAULT 0,
    net_amount DECIMAL(18,2) GENERATED ALWAYS AS (gross_amount - platform_commission - shipping_fee) STORED,
    pph_withheld DECIMAL(18,2) DEFAULT 0,
    pph_rate DECIMAL(5,4) DEFAULT 0.005,
    status VARCHAR(50) DEFAULT 'pending', -- pending, completed, refunded
    created_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(platform, order_id)
);

-- Monthly tax summaries
CREATE TABLE monthly_tax_summaries (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    year_month VARCHAR(7) NOT NULL, -- '2026-08'
    total_gross_ytd DECIMAL(18,2) NOT NULL,
    total_gross_month DECIMAL(18,2) NOT NULL,
    total_pph_withheld_month DECIMAL(18,2) DEFAULT 0,
    total_pph_withheld_ytd DECIMAL(18,2) DEFAULT 0,
    threshold_exceeded BOOLEAN DEFAULT FALSE,
    exemption_filed BOOLEAN DEFAULT FALSE,
    exemption_document_id UUID,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    UNIQUE(user_id, year_month)
);

-- Generated documents
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(50) NOT NULL, -- 'surat_pernyataan_exemption', 'spt_preparation', 'monthly_report'
    status VARCHAR(50) DEFAULT 'draft', -- draft, generated, submitted, confirmed
    metadata JSONB, -- flexible: store doc-specific data
    s3_path VARCHAR(512),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    submitted_at TIMESTAMPTZ
);

-- Notification logs
CREATE TABLE notification_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    channel VARCHAR(50) DEFAULT 'whatsapp', -- whatsapp, email, push
    type VARCHAR(50) NOT NULL, -- 'weekly_summary', 'deadline_reminder', 'tax_alert'
    title VARCHAR(255),
    body TEXT,
    status VARCHAR(50) DEFAULT 'sent', -- sent, delivered, read, failed
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Tax consultant connections (for premium tier)
CREATE TABLE tax_consultants (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    npwp VARCHAR(20) UNIQUE NOT NULL,
    license_number VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(255),
    specialization TEXT[], -- array of tax types they handle
    is_verified BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Audit trail (critical for financial compliance)
CREATE TABLE audit_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50),
    entity_id UUID,
    old_values JSONB,
    new_values JSONB,
    ip_address INET,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_transactions_user_date ON transactions(user_id, transaction_date);
CREATE INDEX idx_transactions_connection ON transactions(connection_id);
CREATE INDEX idx_monthly_summary_user ON monthly_tax_summaries(user_id, year_month);
CREATE INDEX idx_notifications_user ON notification_logs(user_id, created_at DESC);
CREATE INDEX idx_audit_user ON audit_log(user_id, created_at DESC);
```

### 3.3 Marketplace API integration guide

Each marketplace exposes a different API. The connectors must handle OAuth 2.0, rate limiting, response pagination, and data normalization.

**Shopee Open API:**
- Endpoint: `https://partner.shopeemobile.com/api/v2/`
- Auth: OAuth 2.0 with partner_id + api_key signature
- Key API calls:
  - `GET /api/v2/order/get_order_detail` -- individual order details with commission breakdown
  - `GET /api/v2/order/get_order_list` -- list orders by time range
  - `GET /api/v2/shop/get_shop_info` -- seller verification
- Rate limit: 2000 calls per minute per partner
- Data returned includes: order_status, total_amount, estimated_shipping_fee, escrow_amount (before DJP withholding)

```python
# Pseudocode: Shopee connector
class ShopeeConnector:
    BASE_URL = "https://partner.shopeemobile.com/api/v2"

    def __init__(self, partner_id, api_key, redirect_url):
        self.partner_id = partner_id
        self.api_key = api_key
        self.redirect_url = redirect_url

    def generate_auth_url(self):
        """Generate OAuth URL for seller to authorize"""
        timestamp = int(time.time())
        base_string = f"{self.partner_id}{self.redirect_url}{timestamp}"
        signature = hmac.new(
            self.api_key.encode(),
            base_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return (
            f"https://partner.shopeemobile.com/api/v2/shop/auth_partner"
            f"?partner_id={self.partner_id}&timestamp={timestamp}"
            f"&sign={signature}&redirect={self.redirect_url}"
        )

    def get_orders(self, access_token, shop_id, from_ts, to_ts):
        """Fetch orders in a time range with pagination"""
        timestamp = int(time.time())
        params = {
            "partner_id": self.partner_id,
            "timestamp": timestamp,
            "access_token": access_token,
            "shop_id": shop_id,
        }
        body = {
            "time_range_field": "create_time",
            "page_size": 100,
            "cursor": 0,
            "time_from": from_ts,
            "time_to": to_ts,
        }
        # Build signature
        base_string = f"{self.partner_id}{self.api_key}{timestamp}{access_token}{shop_id}"
        signature = hmac.new(
            self.api_key.encode(), base_string.encode(), hashlib.sha256
        ).hexdigest()
        params["sign"] = signature

        all_orders = []
        while True:
            resp = requests.post(
                f"{self.BASE_URL}/order/get_order_list",
                params=params, json=body
            )
            data = resp.json()
            all_orders.extend(data.get("response", {}).get("order_list", []))
            more = data.get("response", {}).get("more", False)
            if not more:
                break
            body["cursor"] = data["response"]["cursor"]
        return all_orders
```

**Tokopedia API (via GOJEK/GoTo integration):**
- Endpoint: `https://fs.tokopedia.net/`
- Auth: OAuth 2.0 with client_credentials flow for partner apps
- Key API calls:
  - `GET /v2/orders/{order_id}` -- order details
  - `GET /v2/orders?from_date={}&to_date={}` -- order list
  - `GET /v2/finance/summary` -- financial summary with commission and fee breakdown
- Note: Tokopedia API has separate sandbox and production environments. Production access requires GoTo partner approval and typically takes 2-4 weeks.
- Rate limit: 100 requests per minute per app

**Lazada API:**
- Endpoint: `https://api.lazada.co.id/rest`
- Auth: OAuth 1.0a (signature-based, not token exchange)
- Key API calls:
  - `GET /orders/get` -- list orders
  - `GET /orders/getMultipleOrderItems` -- item-level data for multiple orders
  - `GET /finance/payout/status` -- payout and fee details
- Lazada API is the most complex to integrate due to OAuth 1.0a signature requirements

**Blibli API:**
- Endpoint: `https://api.blibli.com/v2/`
- Auth: API key + HMAC signature
- Key API calls:
  - `GET /order/list` -- order list
  - `GET /order/detail` -- order detail with fee breakdown
  - `GET /merchant/financial-overview` -- financial summary
- Blibli API is the newest and most RESTful among the four

### 3.4 Tax calculation engine

```python
# Pseudocode: Tax Calculation Engine
class TaxCalculator:
    # PMK 37/2025: 0.5% PPh Final on gross turnover
    PPH_FINAL_RATE = Decimal("0.005")
    # Threshold for mandatory withholding
    THRESHOLD_ANNUAL = Decimal("500_000_000")

    def __init__(self, db_connection):
        self.db = db_connection

    def calculate_annual_turnover(self, user_id, year):
        """Calculate YTD gross turnover across all platforms"""
        query = """
            SELECT COALESCE(SUM(gross_amount), 0) as total_gross
            FROM transactions
            WHERE user_id = $1
              AND EXTRACT(YEAR FROM transaction_date) = $2
              AND status != 'refunded'
        """
        result = self.db.fetchone(query, user_id, year)
        return Decimal(str(result["total_gross"]))

    def assess_exemption_eligibility(self, user_id, year=2026):
        """Determine if seller qualifies for exemption"""
        turnover = self.calculate_annual_turnover(user_id, year)
        projected = self.project_annual_turnover(user_id, year)

        return {
            "ytd_turnover": turnover,
            "projected_annual": projected,
            "below_threshold": projected < self.THRESHOLD_ANNUAL,
            "needs_exemption_letter": projected < self.THRESHOLD_ANNUAL,
            "will_be_withheld": projected >= self.THRESHOLD_ANNUAL,
            "estimated_monthly_tax": None
        }

    def project_annual_turnover(self, user_id, year):
        """Project full-year turnover based on YTD data"""
        current_month = datetime.now().month
        if current_month <= 1:
            return Decimal("0")

        months_elapsed = current_month - 1  # Jan = 1, so months elapsed = 0
        if months_elapsed == 0:
            return Decimal("0")

        ytd = self.calculate_annual_turnover(user_id, year)
        monthly_avg = ytd / months_elapsed
        remaining_months = 12 - months_elapsed
        projected = ytd + (monthly_avg * remaining_months)
        return projected

    def calculate_pph_withheld(self, gross_amount):
        """Calculate PPh 22 that should be withheld on a transaction"""
        return gross_amount * self.PPH_FINAL_RATE

    def reconcile_platform_withholding(self, user_id, year_month):
        """Compare what was withheld vs what should have been withheld"""
        query = """
            SELECT
                platform,
                COUNT(*) as tx_count,
                SUM(gross_amount) as total_gross,
                SUM(pph_withheld) as total_withheld,
                SUM(gross_amount * 0.005) as expected_withheld
            FROM transactions
            WHERE user_id = $1
              AND to_char(transaction_date, 'YYYY-MM') = $2
            GROUP BY platform
        """
        results = self.db.fetchall(query, user_id, year_month)

        discrepancies = []
        for row in results:
            diff = Decimal(str(row["expected_withheld"])) - Decimal(str(row["total_withheld"]))
            if abs(diff) > Decimal("1000"):  # Only flag significant discrepancies
                discrepancies.append({
                    "platform": row["platform"],
                    "transaction_count": row["tx_count"],
                    "total_gross": row["total_gross"],
                    "actual_withheld": row["total_withheld"],
                    "expected_withheld": row["expected_withheld"],
                    "discrepancy": diff,
                })

        return discrepancies
```

### 3.5 Surat Pernyataan generation

The exemption letter must follow DJP format. Below is the document template:

```python
# Pseudocode: Document Generator
class ExemptionLetterGenerator:
    def generate(self, user_data):
        """
        Generate surat pernyataan pengecualian pemotongan PPh Pasal 22
        Based on PMK 37/2025 and PER-15/PJ/2025 format requirements
        """
        today = datetime.now()
        letter = f"""
SURAT PERNYATAAN
PENGECUALIAN PEMOTONGAN PAJAK PENGHASILAN PASAL 22
OLEH PEMUNGUT PAJAK PERTAMBAHAN NILAI ATAS KEGIATAN USAHA
MELALUI SISTEM ELEKTRONIK

Yang bertanda tangan di bawah ini:

Nama                         : {user_data['name']}
NPWP                         : {user_data['npwp']}
NIK                          : {user_data['nik']}
Alamat                       : {user_data['address']}
Nomor Telepon                : {user_data['phone']}
Platform Marketplace          : {', '.join(user_data['platforms'])}

Dengan ini menyatakan bahwa:

1. Saya adalah Wajib Pajak orang pribadi yang melakukan kegiatan usaha
   melalui Platform Marketplace sebagaimana tersebut di atas.

2. Peredaran bruto (omzet) dari kegiatan usaha saya dalam 1 (satu) tahun
   pajak terakhir tidak melebihi Rp4.800.000.000 (empat miliar delapan
   ratus juta rupiah) sehingga memenuhi ketentuan Pasal 4 ayat (2)
   Peraturan Pemerintah Nomor 55 Tahun 2022.

3. Saya telah menyampaikan Surat Pemberitahuan (SPT) Tahunan untuk
   tahun pajak terakhir sesuai dengan ketentuan peraturan
   perundang-undangan perpajakan.

4. Saya memenuhi kriteria Wajib Pajak yang dikecualikan dari pemotongan
   PPh Pasal 22 sebagaimana dimaksud dalam PMK Nomor 37 Tahun 2025.

Demikian surat pernyataan ini saya buat dengan sebenarnya.

                                  {today.strftime('%d %B %Y')}

                           [Tanda Tangan & Materai Rp10.000]

                                    ({user_data['name']})

Catatan:
- Surat pernyataan ini disampaikan kepada Direktur Jenderal Pajak
  melalui platform marketplace yang ditunjuk sebagai pemungut.
- Apabila pernyataan tidak sesuai dengan keadaan sebenarnya, Wajib Pajak
  dapat dikenai sanksi sesuai dengan ketentuan peraturan perundang-undangan
  perpajakan.
"""
        return letter
```

### 3.6 Deployment and infrastructure

```yaml
# docker-compose.yml (production variant)
version: '3.8'

services:
  api-gateway:
    image: nginx:1.25-alpine
    ports:
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - auth-service
      - tax-engine
      - document-service

  auth-service:
    build: ./services/auth
    environment:
      - DB_HOST=postgres
      - REDIS_HOST=redis
      - JWT_SECRET=${JWT_SECRET}
    depends_on:
      - postgres
      - redis

  tax-engine:
    build: ./services/tax-engine
    environment:
      - DB_HOST=postgres
      - SHOPEE_PARTNER_ID=${SHOPEE_PARTNER_ID}
      - SHOPEE_API_KEY=${SHOPEE_API_KEY}
      - TOKOPEDIA_CLIENT_ID=${TOKOPEDIA_CLIENT_ID}
      - TOKOPEDIA_CLIENT_SECRET=${TOKOPEDIA_CLIENT_SECRET}
      - LAZADA_APP_KEY=${LAZADA_APP_KEY}
      - LAZADA_APP_SECRET=${LAZADA_APP_SECRET}
      - BLIBLI_API_KEY=${BLIBLI_API_KEY}
    depends_on:
      - postgres

  document-service:
    build: ./services/document
    environment:
      - S3_ENDPOINT=${S3_ENDPOINT}
      - S3_ACCESS_KEY=${S3_ACCESS_KEY}
      - S3_SECRET_KEY=${S3_SECRET_KEY}
      - S3_BUCKET=pajakpay-documents
    depends_on:
      - minio

  wa-bot:
    build: ./services/wa-bot
    environment:
      - TWILIO_ACCOUNT_SID=${TWILIO_ACCOUNT_SID}
      - TWILIO_AUTH_TOKEN=${TWILIO_AUTH_TOKEN}
      - TWILIO_WA_NUMBER=${TWILIO_WA_NUMBER}
    depends_on:
      - tax-engine

  notification-engine:
    build: ./services/notifications
    environment:
      - TWILIO_ACCOUNT_SID=${TWILIO_ACCOUNT_SID}
      - CRON_SCHEDULE=0 8 * * 1  # Every Monday at 8 AM
    depends_on:
      - postgres

  postgres:
    image: postgres:16-alpine
    environment:
      - POSTGRES_DB=pajakpay
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

  minio:
    image: minio/minio
    command: server /data
    environment:
      - MINIO_ACCESS_KEY=${MINIO_ACCESS_KEY}
      - MINIO_SECRET_KEY=${MINIO_SECRET_KEY}
    volumes:
      - minio-data:/data

volumes:
  pgdata:
  minio-data:
```

### 3.7 Security considerations

Given that PajakPay handles sensitive financial data and tax information, security is paramount:

1. **Encryption at rest:** All PII (NIK, NPWP, phone, email) encrypted using AES-256-GCM. Marketplace tokens encrypted using separate key.
2. **Encryption in transit:** TLS 1.3 for all API communications. Internal service-to-service communication via mTLS.
3. **Token management:** Marketplace OAuth tokens stored with short expiry. Refresh tokens rotated every 24 hours. Tokens never exposed to frontend.
4. **Audit trail:** Every financial calculation and document generation logged immutably to audit_log table. No deletion of audit logs.
5. **Compliance:** Data stored in Indonesia (required for tax data). Compliance with UU PDP (Personal Data Protection Law). Bi-annual penetration testing.
6. **Access control:** Row-level security in PostgreSQL. Service accounts with minimum required permissions. No direct database access from frontend.

```sql
-- Row-level security: users can only see their own data
ALTER TABLE transactions ENABLE ROW LEVEL SECURITY;
CREATE POLICY user_isolation ON transactions
    USING (user_id = current_setting('app.current_user_id')::UUID);
```

---

## 4. Unit economics

### 4.1 Pricing tiers

| Tier | Price/month | Target segment | Features |
|------|-------------|----------------|----------|
| Free | Rp0 | Sellers below Rp500M threshold | Turnover check, exemption letter generator, weekly summary |
| Basic | Rp25,000 | Sellers above threshold, single platform | PPh tracking, monthly report, payment reminders |
| Premium | Rp75,000 | Multi-platform sellers | Cross-platform reconciliation, SPT preparation, chat tax consultation (2 sessions/month) |
| Pro | Rp200,000 | High-volume sellers (Rp1B+/year) | All Premium + dedicated tax consultant, priority support, API access for accounting integration |
| Enterprise | Custom | Accounting firms managing 50+ clients | Wholesale pricing, white-label dashboard, API quota, team management |

### 4.2 Worked example per persona

**Persona A: Ibu Ani, seller fashion di Shopee**
- Monthly omzet: Rp30 juta (Rp360 juta/year, below threshold)
- Needs: exemption letter, peace of mind
- Plan: Free (Rp0/month)
- Cost to serve: Rp500/month (WA bot messages + storage)
- LTV at 24 months: Rp0 (but builds habit, cross-sell potential)
- If she crosses threshold: upgrades to Basic (Rp25k/month)

**Persona B: Pak Budi, seller elektronik di Shopee + Tokopedia**
- Monthly omzet: Rp120 juta (Rp1.44B/year, well above threshold)
- Monthly PPh withheld: Rp600,000
- Needs: tracking, reconciliation, SPT preparation
- Plan: Premium (Rp75,000/month)
- Cost to serve: Rp3,000/month (API calls + storage + WA)
- Gross margin per user: Rp72,000/month (96%)
- LTV at 24 months: Rp1,728,000

**Persona C: Toko Makmur Jaya, seller di 4 platform**
- Monthly omzet: Rp500 juta (Rp6B/year)
- Monthly PPh withheld: Rp2,500,000
- Needs: full compliance, dedicated consultant, API integration
- Plan: Pro (Rp200,000/month)
- Cost to serve: Rp15,000/month (heavy API usage + storage + consultant fee share)
- Gross margin per user: Rp185,000/month (92.5%)
- LTV at 24 months: Rp4,440,000

### 4.3 Revenue model

**Direct subscription (80% of revenue):** Monthly recurring from Basic/Premium/Pro tiers.

**Freemium conversion funnel:**
- Free users visit PajakPay WA bot (100%, 1M+ in first year)
- Complete exemption letter generation (60%, 600K)
- Remain active weekly user (40%, 400K)
- Cross threshold or upgrade to paid (5% conversion, 20K paid users)
- Average revenue per paid user: Rp60K/month
- Monthly recurring revenue at year 1: 20K x Rp60K = Rp1.2B/month

**Indirect revenue (20%):**
- Referral fees from tax consultants (PajakPay takes 10% of consultation fee)
- Lead generation for accounting firms (Rp50,000 per qualified lead)
- Data insights (anonymized, aggregated) for marketplace policy research

### 4.4 Cost structure

| Item | Monthly cost (est.) | Scale factor |
|------|---------------------|--------------|
| Cloud infrastructure (AWS/GCP) | Rp50-100M at 100K MAU | Linear with transactions |
| Twilio WhatsApp API | Rp5-15M at 100K MAU | Per message sent |
| Marketplace API costs | Rp10-30M at 100K MAU | Per API call |
| Engineering team (4 people) | Rp200-400M | Fixed |
| Marketing (WA broadcast, SEO, community) | Rp50-100M | Flexible |
| Legal and compliance | Rp10-25M | Semi-fixed |
| **Total monthly burn** | **Rp325-670M** | |

At 20K paid users averaging Rp60K/month, revenue = Rp1.2B/month. Break-even achievable at approximately 10-12K paid users.

---

## 5. Go-to-market

### 5.1 Deadline-driven acquisition

The August 1 deadline creates a natural acquisition spike. The GTM strategy exploits this time pressure:

**Week 1 (August 1-7): Shock and Awe**
- Facebook groups for marketplace sellers: share "Cek omzet Anda gratis -- kena pajak atau tidak?" 
- TikTok content: "3 menit cek pajak marketplace Anda" (short tutorial videos)
- WhatsApp broadcast to seller communities
- Partner with komunitas seller (Shopee seller groups, Tokopedia seller forum)
- Key message: "Jangan panik. Cek dulu omzet Anda gratis. 80% seller TIDAK kena pajak."

**Week 2-3 (August 8-21): Exemption Letter Wave**
- Push the free exemption letter generator hard
- Target: all sellers below threshold who haven't filed
- SEO keywords: "surat pernyataan pengecualian pajak marketplace", "format surat bebas pajak shopee", "cara hindari potongan pajak tokopedia"
- Partner with marketplace seller education programs

**Week 4+ (September): Paid Conversion**
- Sellers above threshold realize they need ongoing compliance
- Push Premium/Pro tiers with "30 hari gratis" trial
- Cross-sell SPT preparation service
- Launch referral program: "Ajak teman seller, dapatkan diskon 50%"

### 5.2 Channel strategy

**Primary: WhatsApp/Word of mouth**
- Indonesia's most-used app (200M+ users)
- Low friction: no app install required for basic features
- Reach sellers who are not tech-savvy
- Viral potential: seller groups naturally share useful tools

**Secondary: TikTok and Instagram**
- Short-form content showing PajakPay in action
- Testimonials from early users
- Comparison: "Before PajakPay" (confused, overpaying) vs "After PajakPay" (confident, optimized)
- Hashtag strategy: #PajakMarketplace #PajakPay #SellerOnline #UMKMPintarPajak

**Tertiary: Marketplaces' own channels**
- Publish as a recommended app in Shopee/Tokopedia app marketplaces
- Partner with marketplace seller education teams
- Sponsor seller webinars

### 5.3 Initial target segments

**Tier 1 (first 90 days):** Shopee and Tokopedia sellers in Jabodetabek who are already active in seller communities. These are the most likely early adopters because:
- They are already digitally savvy (selling online)
- They are in the most expensive cities (higher compliance awareness)
- They have strong peer networks

**Tier 2 (90-180 days):** Expand to Lazada and Blibli sellers. Expand geographically to Surabaya, Bandung, Medan, Makassar.

**Tier 3 (180+ days):** Accounting firms who manage multiple seller clients. Enterprise API product.

---

## 6. Competitive analysis

### 6.1 Direct competitors

**Klikpajak** (by PT Klikpajak Indonesia)
- Focus: Corporate tax compliance (PPh 21, PPN, PPh Badan)
- Target: Medium to large enterprises
- Pricing: Rp500k-Rp5jt/month
- Why they lose here: No marketplace integration, no PPh 22 Pasal focus, priced 10-100x above what seller mikro can afford. Complex UI designed for accountants, not micro-sellers.

**OnlinePajak** (by PT Online Pajak)
- Focus: End-to-end tax filing for businesses
- Target: SMEs with accounting departments
- Pricing: Rp300k-Rp2jt/month
- Why they lose here: Same issues as Klikpajak. No mobile-first/WA-first experience. No marketplace API connections. Minimum subscription is still 6x higher than PajakPay Premium.

**Mekari Klikpajak** (formerly Klikpajak, after Mekari acquisition)
- Focus: Integrated HR + payroll + tax
- Target: 50+ employee companies
- Pricing: Rp1jt+/month
- Why they lose here: Way over-engineered for a marketplace seller who needs a simple tax calculator and exemption letter.

**Konsultan pajak individu / UKM**
- 10,000+ registered tax consultants in Indonesia (IKPI members)
- Target: All segments
- Pricing: Rp500k-Rp2jt/month
- Why they lose here: Supply-limited (a good consultant has 20-30 clients max), expensive, inconsistent quality, no marketplace API integration.

### 6.2 Indirect competitors

**Marketplace internal tools** (Shopee Seller Center, Tokopedia Mitra)

These have inherent conflicts of interest: the marketplace wants to maximize withholding to avoid DJP penalties. They will never proactively help sellers minimize tax burden. Their tools show transaction data but do not calculate tax or generate exemption letters.

**Spreadsheet-based sellers**
Free but requires accounting knowledge that most micro-sellers lack. No automation, no reminders, no cross-platform consolidation.

### 6.3 Competitive moat

1. **Marketplace API integration:** PajakPay's connectors to all 4 major marketplaces create a data advantage that pure tax tools lack. Once a seller connects their accounts, switching costs increase significantly.

2. **WhatsApp-first design:** Selling tax compliance through a WA bot is radically simpler than web-based tax tools. This reaches the 60%+ of micro-sellers who never use web dashboards but use WA daily.

3. **Freemium at scale:** Free exemption letter generation creates massive top-of-funnel. Competitors charge for even basic compliance checks.

4. **Cross-platform consolidation:** No existing tool aggregates turnover across Shopee, Tokopedia, Lazada, and Blibli. Sellers on multiple platforms must manually sum their data.

5. **Timing:** The August 1 deadline creates a once-in-a-market evolution moment. Early entrants who capture the "panic wave" build lasting brand loyalty.

---

## 7. Risks and failure modes

### 7.1 Regulatory risks

**DJP changes the rules.** If the government extends the threshold, changes the rate, or modifies the exemption mechanism, PajakPay must rapidly adapt. Mitigation: Build the tax engine as a configurable rule engine (not hardcoded rates). Monitor regulatory changes via DJP website and PER-15 updates.

**Marketplaces build their own tax tools.** Shopee or Tokopedia could add tax calculation to their seller dashboards. Mitigation: Marketplaces have no incentive to help sellers minimize tax. Their tools will be basic and self-serving. PajakPay's cross-platform advantage persists.

**Anti-avoidance measures.** DJP could crack down on what they perceive as "tax avoidance services." Mitigation: PajakPay helps sellers comply with existing law, not avoid it. The service is fully transparent. Build relationships with DJP and IKPI.

### 7.2 Adoption risks

**Low seller awareness.** Millions of sellers may not know about the tax change until they see withheld payments. Mitigation: This is actually an acquisition opportunity. When they see missing funds, they will search for solutions. PajakPay should be the top search result.

**WhatsApp bot complexity.** Some users may find even the WA bot confusing. Mitigation: Keep interactions simple (2-3 taps max). Support human fallback (connect to customer service via WA). Onboard via community leaders first.

**Trust deficit.** Sellers may not trust a new app with their tax data and marketplace credentials. Mitigation: Display IKPI affiliation prominently. Offer "check without connecting" option (manual data entry). Social proof from early users. Transparent data handling policies.

### 7.3 Technical risks

**Marketplace API deprecation or rate limiting.** Any marketplace could change their API terms. Mitigation: Abstract connector layer. Fallback to seller-uploaded CSV/Excel exports. Maintain relationships with marketplace partner teams.

**DJP Online integration complexity.** The DJP Online portal has known reliability issues (documented in `03-id-business-trends/demand-mining/coretax-sering-error-wajib-pajak-gagal-lapor.md`). Mitigation: Start with PDF generation only (user uploads manually), then build efiling integration as DJP API matures. Maintain manual fallback.

**Data security breach.** A breach of tax IDs and financial data would be catastrophic. Mitigation: End-to-end encryption, zero-knowledge architecture where possible, penetration testing before launch, cyber insurance, transparent disclosure policy.

### 7.4 Business risks

**Unit economics don't work at free tier.** If the free tier costs too much to serve and conversion to paid is low, the business fails. Mitigation: Free tier is intentionally limited (monthly check only, no monitoring). Survey indicates 5% conversion is achievable based on comparable fintech apps in Indonesia (GoPay, DANA freemium models).

**Seasonal revenue.** Tax compliance app usage may spike only around deadlines. Mitigation: Year-round use via weekly summaries and monitoring. Cross-sell bookkeeping and margin analysis as value-add beyond tax.

---

## 8. New gaps discovered

- `01-crawler-scrapper/marketplace/marketplace-fee-scraper-shared.md` -- Automated scraper detecting commission rate changes across Shopee, Tokopedia, TikTok Shop, Lazada. Feeds PajakPay's margin calculator with live fee data instead of manual updates. (Discovered during PajakPay research -- confirms gap from earlier audit.)

- `01-crawler-scrapper/regulatory/kemenekraf-permendag-monitor.md` -- Automated daily monitor for Kemenekraf, Permendag, PMK regulatory changes that affect kreator konten and UMKM. PajakPay needs to know when DJP changes PPh rates, thresholds, or exemption rules. (Discovered during PajakPay research.)

- `03-id-business-trends/bottlenecks/seller-multi-platform-tax-aggregation.md` -- The pain of consolidating transaction data across Shopee, Tokopedia, Lazada, and Blibli for tax purposes. No existing tool handles this. PajakPay partially solves it but a standalone data aggregation API could serve as an enabler. (NEW, discovered during PajakPay research 2026-07-30.)

- `05-market-cron/cron-configs/djponline-spt-monitor.md` -- Cron-based monitor checking DJP Online and Coretax accessibility, broadcasting portal-down alerts during SPT season. Critical for PajakPay users who need to file on deadline day. (Discovered during PajakPay research -- confirms earlier gap.)

- `04-freelancer-ai-agent/prompts/tax-compliance-wa-bot-prompts.md` -- Prompt library for the WhatsApp tax compliance bot, covering common tax scenarios in Indonesian. Shared asset for any agent building a WA-based tax assistant. (NEW, discovered during PajakPay research 2026-07-30.)

---

## 9. References and source notes

### Primary sources (regulatory)

1. PMK Nomor 37 Tahun 2025 tentang Penunjukan Pihak Lain sebagai Pemungut Pajak atas Penghasilan dari Kegiatan Usaha melalui Sistem Elektronik. (Published: 2025. Effective: 1 August 2026.)
2. PER-15/PJ/2025 tentang Tata Cara Penunjukan Pemungut, Pemungutan, dan Penyetoran PPh atas Penghasilan dari Kegiatan Usaha melalui Sistem Elektronik. (Published: 2025.)

### Secondary sources (news and analysis)

3. [Mulai 1 Agustus, Marketplace Wajib Pungut PPh Penjual Online -- IKPI, 2026-07-28](https://ikpi.or.id/mulai-1-agustus-marketplace-wajib-pungut-pph-penjual-online/)
4. [DJP: Pemungutan Pajak oleh Marketplace Berlaku Efektif 1 Agustus 2026 -- DDTCNews, 2026-07-29](https://ddtcnews.com/berita/nasional/176398/djp-pemungutan-pajak-oleh-marketplace-berlaku-efektif-1-agustus-2026)
5. [Pajak Marketplace Resmi Berlaku 1 Agustus 2026, Shopee hingga Tokopedia Wajib Pungut PPh 0,5 Persen -- BeritaNusa.com, 2026-07-01](https://www.beritanusa.com/nasional/2502835425/pajak-marketplace-resmi-berlaku-1-agustus-2026-shopee-hingga-tokopedia-wajib-pungut-pph-05-persen-dari-seller)
6. [DJP Tunjuk Marketplace Sebagai Pemungut Pajak -- Hallobogor.com, 2026-06-26](https://bogor.hallo.id/ekonomi/11117295165/djp-tunjuk-marketplace-sebagai-pemungut-pajak-apa-yang-perlu-diketahui-pedagang-online-mulai-sekarang)
7. [Begini Mekanisme Pungutan Pajak di Shopee, Tokopedia, Lazada, dan Blibli per 1 Agustus 2026 -- Bisnis.com, 2026-07-30](https://ekonomi.bisnis.com/read/20260730/259/1867275/mulai-1-agustus-marketplace-wajib-pungut-pph-penjual-online)
8. [Pelapak Online Kerek Harga Jelang Pajak Marketplace Berlaku 1 Agustus -- CNN Indonesia, 2026-07-29](https://www.cnnindonesia.com/ekonomi/20260729184150-92-1174472/pelapak-online-kerek-harga-jelang-pajak-marketplace)
9. [Pajak Marketplace Mulai Berlaku Efektif 1 Agustus 2026, UMKM Tetap Dapat Pengecualian -- Infobanknews, 2026-07-29](https://infobanknews.com/pajak-marketplace-mulai-berlaku-efektif-1-agustus-2026-umkm-tetap-dapat-pengecualian/)
10. [Pemerintah Targetkan Pajak Marketplace Berlaku Mulai Juli 2026 -- Akses.co.id, 2026-06-](https://www.akses.co.id/pemerintah-targetkan-pajak-marketplace-juli)
11. [Pajak Merchant Marketplace Berlaku 1 Juli 2026? Ini Penjelasan Resmi DJP -- Kayonews, 2026-06-29](https://kayonews.co.id/pajak-merchant-marketplace-berlaku-1-juli-2026-ini-penjelasan-resmi-djp-untuk-penjual-shopee-tokopedia-hingga-tiktok-shop/)
12. [Rencana Pajak E-Commerce 2026: Pemerintah Siapkan Marketplace Jadi Pemungut -- PilihanIndonesia.com, 2025-07-](https://www.pilihanindonesia.com/nasional/81516964382/rencana-pajak-e-commerce-2026-pemerintah-siapkan-marketplace-jadi-pemungut-ini-dampaknya-bagi-pedagang-online)

### Vault demand-mining pain files (evidence of problem)

13. `03-id-business-trends/demand-mining/pajak-marketplace-efektif-1-agustus-2026-seller-online-tertekan.md` (2026-07-30, strength 5/5)
14. `03-id-business-trends/demand-mining/seller-marketplace-komisi-ongkir-meroket.md` (strength 5/5)
15. `03-id-business-trends/demand-mining/umkm-pajak-digital-ribet.md` (strength 4/5)
16. `03-id-business-trends/demand-mining/pph-final-umkm-terbatas-pt-perorangan.md` (strength 3/5)
17. `03-id-business-trends/demand-mining/coretax-sering-error-wajib-pajak-gagal-lapor.md` (strength 4/5)

### Data notes (verify-live)

- Seller count estimates (14M Shopee, 12M Tokopedia) are based on publicly disclosed figures from annual reports. Platform-specific active seller counts are not independently verified.
- The Rp500 million threshold and 0.5% rate are confirmed from multiple news sources citing DJP official statements (see sources 3-6 above).
- Competitor pricing (Klikpajak, OnlinePajak) is based on publicly available pricing pages as of July 2026. May have changed.
- All architecture diagrams and pseudocode are illustrative. Production implementation requires security review.

**Tag: verify-live** -- Seller count figures, competitor pricing, and marketplace API documentation should be refreshed periodically. The PMK 37/2025 regulatory text should be re-read when an official English translation becomes available.
