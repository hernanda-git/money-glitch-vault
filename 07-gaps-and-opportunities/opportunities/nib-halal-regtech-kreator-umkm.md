# NIB + Sertifikasi Halal RegTech: One-Stop Legalitas Platform for Kreator Konten and UMKM

**Date observed:** 2026-06-26
**Signal strength:** 5 (two converging regulatory deadlines, verified media noise, confirmed demand-mining files, large addressable market)
**Category:** cross (03-id-business-trends + 01-crawler-scrapper + 04-freelancer-ai-agent)
**Synthesis thesis type:** Regulatory compliance platform (RegTech)
**Cross-folders:** 03 (NIB wajib kreator, Sertifikasi Halal wajib UMKM), 01 (scraping OSS/BPJPH portal status), 04 (WhatsApp MCP delivery), 07 (opportunity one-pager)

---

## 1. Synthesis Thesis: The RegTech Moment Indonesia Has Been Waiting For

Two regulatory deadlines are colliding in 2026 that together create a rare, time-boxed window for a compliance platform targeting Indonesia's digital creators and micro-businesses.

**Deadline A: NIB Wajib for Content Creators (effective June 18, 2026).** Pemerintah resmi memasukkan profesi kreator digital ke dalam KBLI 2025 melalui Permendag Nomor 19 Tahun 2026. Mulai 18 Juni 2026, seluruh kreator konten komersial -- YouTuber, TikToker, selebgram, podcaster, affiliate marketer -- diwajibkan memiliki Nomor Induk Berusaha (NIB). Regulasi ini memicu perdebatan sengit di media sosial dengan tagar #NIBKreatorKonten trending di X (formerly Twitter). Lebih dari 15 artikel berita dari media nasional terbit dalam minggu pertama saja (Kontan, Kompas, Tirto, Medcom, MSN Indonesia, yoursay.id). Kemenekraf mengadakan dialog darurat dengan asosiasi kreator konten. (Source: Kontan, 2026-06-20, https://lifestyle.kontan.co.id/news/content-creator-komersial-wajib-punya-nib-ini-syarat-daftar-dan-aturan-kbli; Kompas, 2026-06-20, https://www.kompas.com/read/2026/06/20/11000081/nib-untuk-influencer-negara-tak-boleh-kalah-cepat-dari-algoritma)

**Deadline B: Sertifikasi Halal Wajib (effective October 17, 2026).** Berdasarkan PP No. 42 Tahun 2024 tentang Penyelenggaraan Bidang Jaminan Produk Halal, pemerintah akan menerapkan wajib sertifikasi halal untuk produk makanan, minuman, jasa makanan, dan produk konsumen lainnya. BPJPH menyediakan 1,35 juta kuota SEHATI (Sertifikasi Halal Gratis) tahun 2026 tetapi kuota ini jauh dari cukup untuk 5+ juta UMKM makanan/minuman yang terdampak. Asosiasi UMKM Indonesia (Akumindo) menyuarakan kekhawatiran serius tentang biaya dan kerumitan proses. (Source: BPJPH, 2025-12-23, https://bpjph.halal.go.id/detail/pemerintah-gratiskan-1-35-juta-sertifikat-halal-bagi-usaha-mikro-dan-kecil-di-tahun-2026; Kontan, 2026-06-19, https://industri.kontan.co.id/news/wajib-sertifikasi-halal-berlaku-oktober-2026-umkm-soroti-kendala-biaya)

**The wedge:** Kedua regulasi ini memiliki overlapping target audience (kreator konten yang juga jualan makanan/minuman, UMKM yang butuh NIB dulu baru bisa halal) dan proses yang sama-sama rumit, birokratis, dan membingungkan bagi pelaku usaha kecil. Tidak ada platform yang menyatukan keduanya dalam satu pengalaman pengguna yang sederhana, mobile-first, dan dibantu AI.

**Why now (urgency):**
- NIB sudah wajib per 18 Juni 2026 -- kreator yang belum punya NIB terancap kendala administratif dan tidak bisa kerja sama dengan platform/brand resmi
- Sertifikasi Halal wajib 17 Oktober 2026 -- kurang dari 4 bulan lagi
- Kuota SEHATI gratis terbatas (1,35 juta) dan proses self-declare masih membingungkan bagi UMKM non-digital
- Keduanya membutuhkan dokumen dan data yang sama (NIK, NPWP, alamat usaha, jenis usaha)
- Pemerintah tidak menyediakan asistensi yang memadai -- sosialisasi masih sporadis dan tidak menjangkau pelaku usaha di daerah
- Regulasi baru sering berubah -- pelaku usaha butuh notifikasi real-time tentang perubahan aturan

**Market size estimate:**
- Creator economy Indonesia: 2-4 juta kreator konten aktif (estimasi berdasarkan data We Are Social 2025 dan laporan Kemenekraf 2025)
- UMKM makanan/minuman: 5+ juta unit (data Kemenkop UKM 2025)
- Overlap (kreator yang juga jualan F&B): estimasi 500.000 - 1 juta
- Total TAM: 7-9 juta pengguna potensial dalam 12 bulan pertama
- Regtech market Indonesia: diperkirakan USD 150-300 juta pada 2026 (Frost & Sullivan, 2025)

---

## 2. Problem Deep-Dive: The Bureaucracy Spiral

### 2.1. The NIB Maze for Content Creators

The core problem is not that NIB is mandatory. It is that the process assumes a level of bureaucratic literacy that most creative professionals do not have.

**Step 1: Choose the right KBLI code.** KBLI 2025 introduced new codes for digital activities but the differentiation is subtle and confusing:
- KBLI 59112: Aktivitas produksi film, video, dan program televisi untuk berbagai media digital -- cocok untuk YouTuber, TikToker video
- KBLI 59201: Aktivitas perekaman suara dan produksi audio -- cocok untuk podcaster
- KBLI 73100: Periklanan -- cocok untuk influencer yang endorsement
- KBLI 90200: Aktivitas seni dan hiburan -- cocok untuk streamer, entertainer digital
- KBLI 90111: Aktivitas penciptaan karya tulis -- cocok untuk blogger, copywriter
- KBLI 63990: Aktivitas situs jejaring sosial dan distribusi konten digital (KATEGORI BARU KBLI 2025)

Seorang kreator yang melakukan SEMUA aktivitas di atas (video, podcast, endorse, tulis artikel) harus memilih SATU kode KBLI yang paling dominan. Kesalahan pemilihan berimplikasi pada klasifikasi pajak dan akses program pemerintah. (Source: Kontan, 2026-06-20, https://lifestyle.kontan.co.id/news/content-creator-komersial-wajib-punya-nib-ini-syarat-daftar-dan-aturan-kbli)

**Step 2: Register on OSS-RBA.** Sistem OSS (Online Single Submission) berbasis risk-based approach (OSS-RBA) adalah portal resmi pendaftaran NIB. Tantangannya:
- UI/UX tidak ramah pengguna individu (dirancang untuk perusahaan)
- Banyak field yang membingungkan: modal usaha, skala usaha, alamat kantor (kreator sering kerja dari rumah/kosan)
- Verifikasi NIK dan NPWP kadang gagal karena data Dukcapil tidak sinkron
- Proses memakan waktu 30 menit - 2 jam untuk yang sudah paham, bisa berhari-hari untuk pemula
- Tidak ada panduan dalam bahasa yang sederhana

(Source: Observasi langsung dari laporan pengguna di media sosial, tagar #NIBKreatorKonten, Juni 2026)

**Step 3: Tax implications.** Ironisnya, setelah punya NIB, kreator konten menghadapi masalah pajak yang lebih kompleks:
- Kreator konten TIDAK BISA menggunakan skema PPh UMKM 0.5% (PP 55/2022) karena aktivitas mereka tidak masuk kategori UMKM tertentu
- Mereka harus menggunakan tarif progresif Pasal 17 UU PPh (5-30%) atau tarif final untuk pekerjaan bebas
- Banyak kreator yang sebelumnya tidak lapor pajak sama sekali
- Kebingungan antara pajak final (untuk endorsement) dan pajak progresif (untuk AdSense/afiliasi)
- (Source: Kompas.id, 2026-06-22, https://www.kompas.id/baca/riset/2026/06/22/kreator-konten-tak-bisa-gunakan-pph-umkm-05-persen -- paywalled, confirmed via multiple secondhand reports)

**Step 4: Platform requirements.** Platform digital (YouTube, TikTok, Shopee, Instagram) kini diwajibkan melakukan verifikasi legalitas pelaku usaha. Kreator tanpa NIB berisiko:
- Tidak bisa menerima pendapatan dari brand partnership resmi
- Diblokir dari program afiliasi tertentu
- Tidak bisa mengikuti program kemitraan platform
- Dilepas dari tanggung jawab perlindungan hukum jika terjadi sengketa konten

### 2.2. The Sertifikasi Halal Labyrinth for UMKM

Sertifikasi Halal wajib Oktober 2026 menimbulkan kepanikan yang berbeda tapi sama akutnya di kalangan UMKM makanan dan minuman.

**The SEHATI program (Sertifikasi Halal Gratis):**
- BPJPH menyediakan 1,35 juta kuota gratis untuk usaha mikro dan kecil tahun 2026
- Proses: self-declare oleh pelaku usaha dengan didampingi Pendamping Proses Produk Halal (P3H)
- Syarat: memiliki NIB, NPWP, daftar produk, daftar bahan baku, dan deskripsi proses produksi
- Masalah: kuota 1,35 juta tidak cukup untuk 5+ juta UMKM makanan/minuman yang wajib bersertifikat
- Banyak UMKM tidak tahu cara self-declare, tidak punya NIB, tidak punya NPWP
- Pendamping (P3H) jumlahnya terbatas dan distribusinya tidak merata
- (Source: BPJPH, 2025-12-23, https://bpjph.halal.go.id/detail/pemerintah-gratiskan-1-35-juta-sertifikat-halal-bagi-usaha-mikro-dan-kecil-di-tahun-2026)

**The reguler certification path (for those who miss SEHATI quota):**
- Biaya sertifikasi reguler: Rp 230.000 - Rp 5.000.000+ tergantung skala usaha
- Melibatkan Lembaga Pemeriksa Halal (LPH) untuk audit
- Proses memakan waktu 2-6 minggu
- Harus melalui ptsp.halal.go.id (portal terpisah dari OSS)
- (Source: BPJPH official site, https://bpjph.halal.go.id)

**The sequential dependency problem:**
UMKM yang belum punya NIB (karena tidak paham cara daftar, tidak punya NPWP, atau usaha masih informal) tidak bisa mengikuti SEHATI. Mereka harus:
1. Urus NPWP dulu (jika belum punya)
2. Daftar NIB via OSS
3. Baru bisa daftar SEHATI

Setiap langkah memiliki UI, proses, dan persyaratan yang berbeda. Tidak ada panduan terintegrasi.

### 2.3. The Combined Pain

Pelaku usaha yang terdampak KEDUA regulasi (kreator konten yang juga jualan F&B, UMKM kuliner yang juga aktif di media sosial) menghadapi beban ganda:

| Step | Platform | Time Estimate | Difficulty | Cost |
|------|----------|--------------|-----------|------|
| Daftar NPWP | DJP Online | 1-3 hari | Medium | Rp0 |
| Pilih KBLI | Manual/OSS | 1-7 hari | Hard (salah pilih = konsekuensi pajak) | Rp0 |
| Daftar NIB | OSS-RBA | 30 menit - 2 hari | Medium-Hard | Rp0 |
| Pahami kewajiban pajak | Manual | Tak terbatas | Very Hard | Rp0 |
| Self-declare halal | SIHALAL | 1-7 hari | Medium (butuh pendamping) | Rp0 (kuota) |
| Atau daftar sertifikasi reguler | ptsp.halal.go.id | 2-6 minggu | Hard | Rp230K-5JT |

Total beban kognitif dan waktu: 1-8 minggu untuk menyelesaikan semua step. Tidak ada satu pun platform yang mengintegrasikan kelima langkah ini.

---

## 3. Market Sizing: Three Segments, One Platform

### Segment A: Kreator Konten Murni (3-4M users)

Kreator yang hanya membuat konten dan tidak menjual produk fisik. Mereka butuh:
- NIB dengan KBLI yang tepat (73100, 59112, 59201, 90200, atau 63990)
- Panduan pajak penghasilan kreator konten
- Template invoice dan kontrak endorsement
- Pembukuan sederhana untuk pemasukan AdSense/endorse/afiliasi

Willingness to pay: Rp 50.000 - 150.000/bulan (komparasi: Canva Pro Rp 100.000/bln, CapCut Pro Rp 70.000/bln, Spotify Rp 55.000/bln)

### Segment B: UMKM Makanan/Minuman (5-6M users)

Pelaku usaha kuliner yang butuh:
- NIB (jika belum punya)
- Sertifikasi Halal (wajib Oktober 2026)
- PIRT/BPOM (jika produk dikemas)
- Pembukuan sederhana

Willingness to pay: Rp 25.000 - 75.000/bulan (komparasi: biaya jasa konsultan Rp 500.000 - 2.000.000 one-time)

### Segment C: Kreator + UMKM Hybrid (500K-1M users)

Kreator konten yang juga menjual produk (makanan, merchandise, digital product). Mereka butuh SEMUA layanan di atas. Willingness to pay tertinggi: Rp 100.000 - 200.000/bulan.

### Total Addressable Market

| Segment | Size | ASP/mo | Annual Revenue Potential |
|---------|------|--------|------------------------|
| Kreator Murni (10% capture Y1) | 300K-400K | Rp 75.000 | Rp 270-360 M |
| UMKM Makanan (5% capture Y1) | 250K-300K | Rp 50.000 | Rp 150-180 M |
| Hybrid (15% capture Y1) | 75K-150K | Rp 125.000 | Rp 112-225 M |
| **Total Y1** | **625K-850K** | | **Rp 532-765 M** |

Catatan: Ini hanya subscription revenue. Belum termasuk one-time fees untuk layanan premium (full-service pendampingan, konsultasi prioritas, dll).

---

## 4. Existing Solutions and Why They Fail

### 4.1. Government Platforms

**OSS-RBA (oss.go.id)**
- Pros: Gratis, resmi, terintegrasi dengan data Dukcapil dan DJP
- Cons: UI rumit untuk individu, tidak ada panduan KBLI untuk kreator konten, tidak ada notifikasi perubahan regulasi, tidak mobile-friendly, tidak ada fitur asistensi
- Coverage: Hanya NIB, tidak mencakup sertifikasi halal

**SIHALAL (bpjph.halal.go.id)**
- Pros: Gratis untuk self-declare, terintegrasi dengan data NIB
- Cons: UI kurang intuitif, proses self-declare membutuhkan pendampingan, tidak ada panduan langkah-demi-langkah dalam bahasa sederhana, tidak ada fitur tracking real-time yang user-friendly
- Coverage: Hanya sertifikasi halal, tidak mencakup NIB atau perpajakan

**DJP Online (djponline.pajak.go.id)**
- Pros: Gratis, fitur pelaporan SPT
- Cons: Sangat teknis, tidak ada panduan untuk kreator konten, error-prone untuk WP baru
- Coverage: Hanya pajak

**Why government fails:** Setiap kementerian/lembaga memiliki portal sendiri-sendiri dengan login, UI, dan proses yang berbeda. Tidak ada integrasi horizontal. Sosialisasi terbatas dan tidak menjangkau pelaku usaha non-formal.

### 4.2. Private Sector Competitors

**Jasa Konsultan Perizinan (offline/online)**
- Contoh: Jasa urus NIB di Shopee (Rp 150.000-500.000), jasa notaris, biro jasa
- Pros: Full-service, handle semua dokumen
- Cons: Mahal (Rp 500K-5JT), proses lambat, tidak scalable, tidak ada digital tracking, kualitas bervariasi
- Coverage: Biasanya hanya satu jenis layanan (NIB ATAU halal, tidak keduanya)

**Platform LegalTech (existing)**
- LegalGo (legalgo.id): Fokus pada dokumen legal perusahaan, kontrak, dan badan hukum. Tidak spesifik untuk kreator konten atau UMKM mikro.
- Pajak.io (pajak.io): Fokus pada pelaporan pajak UMKM. Tidak mencakup NIB atau sertifikasi halal.
- KlinikHukum (klinikhukum.id): Fokus pada konsultasi hukum umum. Tidak spesifik perizinan.
- Gap: Tidak ada platform yang mengintegrasikan NIB + Sertifikasi Halal + Pajak untuk kreator konten dan UMKM mikro.

**Platform Freelance (indirect competitors)**
- Fastwork, Sribu: Ada jasa desain logo, urus dokumen, dll -- tapi bukan platform terintegrasi
- Gap: Tidak ada end-to-end solution, hanya marketplace jasa lepas

**Asosiasi dan Komunitas**
- Asosiasi Kreator Konten Indonesia (AKKI): Baru terbentuk, belum punya solusi konkret
- Akumindo: Fokus advokasi kebijakan, bukan platform layanan
- Komunitas Facebook/Telegram: Saling tanya jawab, informasi tidak terstruktur, risiko misinformation

### 4.3. The Market Gap (Why a New Player Wins)

| Feature | OSS-RBA | SIHALAL | DJP Online | Konsultan | LegalGo | Proposed Platform |
|---------|---------|---------|-----------|-----------|---------|-------------------|
| NIB registration | Yes | No | No | Yes | Yes | Yes |
| KBLI wizard for creators | No | No | No | Manual | No | Yes (AI) |
| Halal self-declare | No | Yes | No | Yes | No | Yes |
| Pajak kreator | No | No | Partial | Yes | No | Yes |
| WhatsApp delivery | No | No | No | No | No | Yes |
| Notifikasi regulasi | No | No | No | No | No | Yes |
| AI chatbot assistance | No | No | No | No | No | Yes |
| Mobile-first | No | Partial | No | No | No | Yes |
| Integrated tracking | No | No | No | Manual | No | Yes |
| Multi-account (bisnis + pribadi) | No | No | Yes | N/A | Yes | Yes |
| Pricing | Free | Free | Free | Rp500K-5JT | Rp150K-5JT | Rp50-150K/mo |

---

## 5. The Product: Halal.in Aja (Working Title)

### 5.1. Product Vision

A mobile-first, WhatsApp-native platform that guides kreator konten and UMKM through the entire legalitas journey in one seamless flow. The user does not need to know what KBLI, NIB, OSS, SIHALAL, or NPWP means. They just answer simple questions in Indonesian, and the platform handles the rest.

### 5.2. User Journey (WhatsApp-First)

**Step 1: Discovery.** User finds the platform via:
- Organic search "cara daftar NIB kreator konten" or "sertifikasi halal gratis 2026"
- Referral from fellow creator/UMKM
- Instagram/TikTok content (short educational reels)
- Facebook groups (komunitas kreator konten, UMKM makanan)

**Step 2: Onboarding via WhatsApp.** User sends "Halo" to a WhatsApp Business number. Bot responds in Indonesian:

> "Hai! Saya Asisten Legalitas kamu. Dalam 10 menit, saya bisa bantu kamu:
> 1. Cek apakah kamu wajib NIB
> 2. Bantu pilih kode KBLI yang tepat
> 3. Panduan daftar NIB step-by-step
> 4. Cek apakah kamu perlu sertifikasi halal
>
> Mulai dengan jawab: 'NIB' atau 'Halal' atau 'Dua-duanya'"

**Step 3: AI-Powered KBLI Wizard.** For NIB seekers, the bot asks 5 simple questions:
1. "Apa sumber penghasilan utama kamu? (Video/YouTube, Podcast/Audio, Endorse/Sponsor, Tulisan/Blog, Jualan Produk)"
2. "Apakah kamu menerima endorsemen dari brand?"
3. "Apakah kamu membuat konten video secara rutin?"
4. "Apakah kamu punya podcast atau konten audio?"
5. "Apakah kamu menjual produk fisik atau digital?"

Berdasarkan jawaban, AI menentukan kode KBLI yang paling tepat dengan confidence score dan penjelasan.

**Step 4: NIB Registration Assistant.** Bot provides:
- Link ke OSS-RBA dengan panduan spesifik per field (dalam bahasa Indonesia sederhana)
- Screenshot annotated untuk setiap langkah
- Fallback: jika user kesusahan, bisa request full-service (ditangani admin) dengan biaya Rp 99.000

**Step 5: Halal Self-Declare Wizard.** For halal seekers, the bot guides through:
- Cek NIB (jika belum, redirect ke step 3-4)
- Cek NPWP (jika belum, panduan daftar via DJP Online)
- Pengisian data produk (nama produk, bahan baku, proses produksi)
- Upload dokumen pendukung (foto produk, label kemasan)
- Koneksi dengan Pendamping P3H terdekat (via API SIHALAL)
- Submit ke SIHALAL

**Step 6: Dashboard & Tracking.** After initial setup, user gets:
- Status real-time: "NIB: Terbit ✅ | NPWP: Ada ✅ | Halal: Diproses (75%) ⏳"
- Notifikasi via WhatsApp jika ada perubahan status
- Notifikasi jika ada perubahan regulasi yang mempengaruhi usaha mereka
- Reminder tenggat waktu (sertifikasi halal wajib Oktober 2026)

**Step 7: Premium Features (Rp 99.000/bulan).**
- Konsultasi prioritas dengan legal expert via WhatsApp
- Template invoice, kontrak endorsement, dan laporan keuangan sederhana
- Auto-generated laporan pajak bulanan
- Notifikasi perubahan KBLI/regulasi real-time
- Akses ke komunitas eksklusif sesama kreator/UMKM

### 5.3. Technical Architecture

```
                    +-----------------+
                    |   WhatsApp       |
                    |   Business API   |
                    +--------+--------+
                             |
                    +--------v--------+
                    |  Dialogflow CX   |
                    |  + Claude API    |
                    |  (NLU + Agent)   |
                    +--------+--------+
                             |
              +--------------+--------------+
              |              |              |
     +--------v------+ +---v---------+ +---v----------+
     | OSS API       | | SIHALAL API | | DJP Online    |
     | (NIB check,   | | (status,    | | (NPWP check,  |
     |  register)    | |  self-decl) | |  tax guide)   |
     +---------------+ +-------------+ +--------------+
              |              |              |
     +--------v------+ +---v---------+ +---v----------+
     | KBLI Engine   | | P3H Matcher | | Tax Calc      |
     | (rule-based   | | (location+  | | (PPh 17/21    |
     |  + ML)        | |  expertise) | |  estimator)   |
     +---------------+ +-------------+ +--------------+
              |              |              |
              +--------------+--------------+
                             |
                    +--------v--------+
                    |  Database        |
                    |  (PostgreSQL)    |
                    +-----------------+
```

**Component Breakdown:**

**A. WhatsApp Business API Layer**
- Provider: Twilio atau WATI (WATI lebih murah untuk Indonesia: Rp 500-1.000/pesan, vs Twilio USD 0.005-0.08/pesan)
- Template messages untuk onboarding, status updates, reminders
- Interactive buttons untuk navigasi wizard
- Media upload support untuk dokumen (foto KTP, NPWP, produk)
- Fallback: jika API down, SMS gateway sebagai backup

**B. Conversational AI Layer (Dialogflow CX + Claude API)**
- Dialogflow CX untuk intent routing utama (20+ intents: daftar_nib, cek_kbli, sertifikasi_halal, cek_status, dll)
- Claude API untuk:
  - KBLI recommendation engine (few-shot prompting dengan dataset KBLI codes + contoh kasus)
  - Penyederhanaan bahasa regulasi (legal-to-plain-Indonesian translation)
  - Auto-generate jawaban untuk pertanyaan rumit (pajak, kewajiban hukum)
- Fallback: jika API LLM tidak available, gunakan decision tree rules

**C. OSS-RBA Integration**
- OSS API endpoint: https://api.oss.go.id (perlu registrasi sebagai mitra integrasi)
- Data flow:
  - Check existing NIB via NIK (read-only)
  - Pre-fill form data untuk user
  - Panduan field-by-field dengan screenshot annotated
  - Tidak melakukan registrasi atas nama user (legal risk) -- user tetap klik "Daftar" sendiri
- Alternatif: Web scraping OSS portal (jika API mitra tidak tersedia untuk publik) menggunakan Playwright + rotasi IP (infrastruktur dari 01-crawler-scrapper)

**D. SIHALAL Integration**
- BPJPH SIHALAL system: https://sihalal.halal.go.id
- Self-declare flow:
  - API check ketersediaan kuota SEHATI
  - Validasi NIB user
  - Panduan pengisian self-declare
  - Matching dengan Pendamping P3H terdekat berdasarkan lokasi user (kabupaten/kota)
- Status tracking via scraping dashboard SIHALAL (karena webhook tidak tersedia)

**E. KBLI Engine**
- Rule-based system dengan 30+ profiling questions
- Decision matrix: 6 KBLI codes x 8 business characteristics
- Machine learning enhancement: setelah 1.000+ users, train classifier untuk prediksi KBLI otomatis
- Output: recommended KBLI + confidence score + plain-language explanation

**F. Database Schema (Simplified)**

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    wa_number VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(255),
    nik VARCHAR(16),
    npwp VARCHAR(20),
    -- Onboarding state machine
    onboarding_step INTEGER DEFAULT 0,
    onboarding_status VARCHAR(50) DEFAULT 'started',
    -- Timestamps
    created_at TIMESTAMP DEFAULT NOW(),
    last_active_at TIMESTAMP DEFAULT NOW()
);

-- Business profiles
CREATE TABLE business_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    business_name VARCHAR(255),
    business_type VARCHAR(100), -- 'kreator', 'umkm', 'hybrid'
    main_revenue_source VARCHAR(100), -- 'video', 'audio', 'endorse', 'writing', 'product'
    kbli_code VARCHAR(10),
    kbli_confidence DECIMAL(3,2),
    -- Address
    province VARCHAR(100),
    city VARCHAR(100),
    district VARCHAR(100),
    -- Halal
    has_nib BOOLEAN DEFAULT FALSE,
    nib_number VARCHAR(50),
    has_halal_cert BOOLEAN DEFAULT FALSE,
    halal_status VARCHAR(50), -- 'not_started', 'self_declare', 'pending_audit', 'certified'
    created_at TIMESTAMP DEFAULT NOW()
);

-- KBLI recommendations log
CREATE TABLE kbli_recommendations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    questions_answers JSONB,
    recommended_code VARCHAR(10),
    confidence DECIMAL(3,2),
    user_accepted BOOLEAN,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Notification preferences
CREATE TABLE notification_prefs (
    user_id UUID PRIMARY KEY REFERENCES users(id),
    regulatory_changes BOOLEAN DEFAULT TRUE,
    deadline_reminders BOOLEAN DEFAULT TRUE,
    status_updates BOOLEAN DEFAULT TRUE,
    promo_messages BOOLEAN DEFAULT FALSE
);

-- Subscription tracking
CREATE TABLE subscriptions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    plan VARCHAR(50), -- 'free', 'premium', 'full_service'
    amount DECIMAL(12,2),
    start_date DATE,
    end_date DATE,
    status VARCHAR(50), -- 'active', 'expired', 'cancelled'
    payment_method VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 5.4. Sample Conversation Flow (English Translation)

```
User: Halo
Bot: Hai! Selamat datang di Legal.in Aja! Saya bisa bantu kamu urus NIB dan Sertifikasi Halal.
     Mau mulai dari mana?
     [NIB] [Sertifikasi Halal] [Tanya dulu]

User: NIB
Bot: Oke! Pertama, apa sumber penghasilan utama kamu?
     [Video/YouTube] [Podcast/Audio] [Endorse/Sponsor] [Tulisan/Blog] [Jualan produk]

User: Video/YouTube
Bot: Apakah kamu juga menerima endorsemen dari brand?
     [Ya, rutin] [Kadang-kadang] [Tidak]

User: Ya, rutin
Bot: Berdasarkan jawaban kamu, kode KBLI yang paling sesuai adalah:
     * 59112 (Produksi film, video, dan program televisi) -- cocok untuk konten video
     * 73100 (Periklanan) -- cocok untuk aktivitas endorse
     
     Karena aktivitas utama kamu adalah video dan kamu juga terima endorse,
     rekomendasi saya: KBLI 59112.
     Alasan: KBLI 59112 mencakup produksi konten video digital komersial.
     Aktivitas endorse bisa dicatat sebagai pendapatan tambahan.
     
     Setuju dengan rekomendasi ini?
     [Setuju] [Saya pilih yang lain] [Tanya kenapa]

User: Setuju
Bot: Bagus! Sekarang saya akan pandu kamu daftar NIB di OSS.
     Siapkan: KTP, NPWP (kalau belum punya, saya bantu daftar).
     
     Langkah 1: Buka https://oss.go.id
     Langkah 2: Klik "Daftar" dan masukkan NIK kamu...
     [Kirim screenshot annotated]
     
     Kalau ada kesulitan, ketik "BANTUAN" dan admin kami akan membantu.
```

---

## 6. Revenue Model

### 6.1. Freemium Tier (Rp 0)

- KBLI wizard AI (up to 3 checks)
- Panduan NIB step-by-step (text-only)
- Cek status NIB (read-only)
- Notifikasi regulasi umum (broadcast)

Goal: Viral acquisition. Target conversion rate: 15-20% to premium.

### 6.2. Premium Tier (Rp 99.000/month)

- Unlimited KBLI checks
- Panduan NIB + screenshot annotated
- Self-declare halal wizard
- Auto-track status SIHALAL
- Notifikasi perubahan regulasi personalized
- Template invoice dan kontrak endorsement
- Komunitas eksklusif WhatsApp/Telegram
- Prioritas chat support

Target: 625K-850K subscribers Y1.

### 6.3. Full-Service Tier (Rp 299.000 one-time or Rp 50.000/month add-on)

- Admin handles NIB registration end-to-end
- Admin handles halal self-declare submission
- Notaris digital untuk legalisir dokumen
- Target: 10-15% of premium users upgrade.

### 6.4. Enterprise Tier (custom pricing)

- Untuk asosiasi (Akumindo, AKKI): bulk subscription with white-label
- Untuk dinas/departemen: platform sosialisasi dan monitoring kepatuhan UMKM
- Untuk platform digital (Shopee, TikTok, Gojek): API akses untuk verifikasi NIB kreator mereka
- Target: 20-30 enterprise accounts Y1.

### 6.5. Ancillary Revenue

- One-time fee pendampingan khusus: Rp 199.000/sesi (video call 30 menit dengan legal expert)
- Affiliate revenue: rekomendasi platform akuntansi (BukuWarung, BukuKas), asuransi, dll
- Data insights agregat (anonymized): tren KBLI, demografi kreator, tingkat kepatuhan -- dijual ke Kemenekraf, platform digital, brand

### 6.6. Unit Economics

| Metric | Free | Premium (Rp99K) | Full-Service (Rp299K OT) |
|--------|------|-----------------|-------------------------|
| Monthly churn (est.) | 40% | 8% | 12% |
| CAC (WhatsApp ads) | Rp 3.000 | Rp 15.000 | Rp 25.000 |
| Gross margin | 0% | 85% | 50% |
| LTV (12 mo) | Rp 0 | Rp 594.000 | Rp 449.000 |
| LTV/CAC | - | 39.6x | 18.0x |
| Payback period | - | 2 months | 3 months |

---

## 7. Go-to-Market Strategy

### 7.1. Phase 1: Organic Virality (Weeks 1-4)

**Content Marketing:**
- TikTok/IG Reels: "Cek KBLI kamu dalam 30 detik" series -- 10-15 short videos
- Each video targets a specific creator type (YouTuber, TikToker, Podcaster, Blogger)
- Each video ends with: "Kirim 'HALO' ke WA 08xxxx buat cek gratis"
- Target: 10M+ views total across platforms

**SEO Landing Pages:**
- "KBLI untuk content creator 2026" -- explainer with interactive wizard
- "Cara daftar NIB kreator konten" -- step-by-step with screenshots
- "Sertifikasi halal gratis 2026" -- SEHATI guide
- "Pajak kreator konten 2026" -- tax guide
- Target: #1 position for 10+ long-tail keywords within 4 weeks

**Community Seeding:**
- Post in 20+ Facebook groups: Komunitas Kreator Konten Indonesia, UMKM Makanan Indonesia, Bisnis Online Pemula
- Join 10+ Telegram groups for creators, offer free KBLI check
- Kolaborasi dengan mikro-influencer (10K-50K followers) yang relevan -- barter akses premium for promo

### 7.2. Phase 2: Paid Acquisition (Weeks 5-12)

- Facebook/IG Ads: Target "entrepreneurship" + "content creator" interest segments
- WhatsApp click-to-CTA ads: direct to WhatsApp bot
- Google Ads: "daftar NIB", "sertifikasi halal", "KBLI kreator"
- Budget: Rp 50-100M/month for first 3 months
- Target CAC: Rp 3.000-5.000 per lead (WhatsApp Opt-in)

### 7.3. Phase 3: Partnership (Weeks 8-24)

- **Kemenekraf:** Offer platform sebagai alat sosialisasi NIB untuk kreator konten
- **BPJPH:** Integrasi resmi dengan SIHALAL untuk tracking sertifikasi
- **Platform Digital (Shopee, TikTok, Gojek):** API verification layer -- "verified NIB" badge untuk kreator/UMKM di platform mereka
- **Asosiasi (Akumindo, AKKI, APROISI):** Bulk subscription for members
- **Bank (Bank Mandiri, BSI, BCA):** Bundling with business account opening -- "Buka rekening bisnis + urus NIB gratis"

### 7.4. Phase 4: Expansion (Month 6+)

- Tambah layanan: PIRT/BPOM, Hak Cipta (HAKI), SIUP/SITU
- Tambah fitur: e-invoice, laporan keuangan auto-generate, SPT tahunan auto-fill
- Tambah channel: Telegram bot, website dashboard, mobile app (React Native)
- Ekspansi ke Malaysia/Singapura: adaptasi untuk SSM (Suruhanjaya Syarikat Malaysia) dan MAMPU

---

## 8. Risk Analysis

### 8.1. Regulatory Risks

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|------------|
| Perubahan KBLI codes | Medium | High | Modular KBLI engine; update via config not code; monitor Permendag releases |
| Penundaan wajib halal | Low-Medium | Medium | Diversifikasi revenue (tidak hanya halal); tetap fokus NIB + pajak |
| OSS API ditutup/dibatasi | Low | High | Web scraping sebagai backup (infrastruktur dari 01-crawler-scrapper); bangun relasi dengan OSS team |
| Perubahan kebijakan pajak kreator | Medium | Medium | Monitoring DJP regulation changes; update tax calculator accordingly |
| Data privacy regulation (UU PDP) enforcement | Medium | High | Encrypt all user data at rest and transit; store NIK/NPWP with AES-256; get explicit consent per-purpose |

### 8.2. Competitive Risks

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|------------|
| Existing LegalTech expands to kreator segment | Medium | High | First-mover advantage in WhatsApp-native delivery; build community moat |
| Government launches integrated portal | Low | High | Become the "frontend" layer; API integration with gov portal; focus on UX layer |
| Copycat by large tech company (Gojek, Grab) | Low-Medium | Medium | Focus on niche (kreator konten); build specialized KBLI AI that general platforms can't easily replicate |
| Price war with konsultan offline | Low | Low | Differentiate on price, speed, and digital experience; offline konsultan can't compete on scale |

### 8.3. Execution Risks

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|------------|
| WhatsApp API rate limits | High | Medium | Queue system; multiple WA numbers with load balancing; Telegram backup channel |
| LLM hallucination in KBLI advice | Medium | High | Human-in-the-loop for high-stakes recommendations; confidence threshold for auto-recommend |
| Low conversion from free to premium | Medium | High | A/B test pricing; add urgency (limited-time promo); improve premium value prop with community |
| NIB registration complexity too high for bot | High | Medium | Fallback to human admin; create video tutorials for each OSS field |
| Seasonal dip after regulatory deadline passes | High | High | Build recurring value (tax filing, community, ongoing compliance monitoring); expand to new regulations |

---

## 9. Technical Implementation Roadmap

### Week 1-2: MVP (WhatsApp Bot + KBLI Engine)
- WhatsApp Business API account setup
- Dialogflow CX agent with 10 core intents
- KBLI decision tree (rule-based, 6 codes x 8 questions)
- PostgreSQL database (users, profiles, KBLI logs)
- Manual OSS guide (static text + screenshots)
- Launch to 100 beta testers (recruit from Facebook groups)

### Week 3-4: Core Features
- Claude API integration for KBLI recommendation with explanations
- SIHALAL self-declare wizard (static guide)
- Status tracking (manual update by admin)
- Premium subscription (Midtrans payment gateway)
- Automated WhatsApp reminders
- Beta launch to 1,000 users

### Week 5-8: Integration
- OSS API integration (read NIB status, pre-fill form)
- SIHALAL scraping for status tracking (Playwright + cookie persistence)
- P3H matching by location (scrape BPJPH directory)
- Tax calculator for kreator konten (PPh 17/21)
- Template library (invoice, kontrak endorse, laporan keuangan)
- Public launch + paid ads

### Week 9-12: Scale
- KBLI ML model training (after 1K+ samples)
- Full-service tier (admin team handles registration)
- Community platform (WhatsApp group with auto-moderation)
- Partnership outreach (Kemenekraf, BPJPH, asosiasi)
- SEO content machine (20+ landing pages)
- Analytics dashboard for business tracking

### Month 4-6: Platform
- Web dashboard (React-based)
- Mobile app (React Native, optional)
- Enterprise API for platform partners
- Additional services: PIRT, BPOM, HAKI
- Ekspansi ke layanan pajak: auto-generate SPT Tahunan

---

## 10. Why This Wins: The WhatsApp-Native Thesis

The key insight that makes this different from existing LegalTech platforms is the **WhatsApp-first delivery model**.

**Why WhatsApp:**
- 96% of Indonesian smartphone users have WhatsApp (We Are Social, 2025)
- Average user checks WhatsApp 25+ times per day
- No app download friction -- user just saves a contact number
- Familiar interface (chat) reduces intimidation factor for non-digital-native UMKM
- Push notifications langsung ke HP user (tidak terfilter spam)
- Shareable: user bisa forward chat ke teman yang butuh

**Why a bot, not a human:**
- Scalability: 1 bot can handle 10,000+ conversations simultaneously
- Cost: Rp 500-1.000/conversation vs Rp 50.000-100.000 for human admin
- Consistency: every user gets the same quality of guidance
- Availability: 24/7, no queue, no office hours

**Why not an app:**
- App download conversion rate: 10-20% from ad click to install
- WhatsApp opt-in conversion rate: 30-50% from ad click to chat
- Cost per acquisition is 3-5x lower via WhatsApp
- Zero uninstall risk (they never installed anything)

**The playbook:** This is the same playbook used by:
- Halodoc (Indonesia's healthtech unicorn) -- started as WhatsApp-based booking
- TaniHub (agritech) -- WhatsApp orders from farmers
- Bukalapak's Mitra -- WhatsApp/Telegram groups for warung

---

## 11. Code Snippets for Key Components

### 11.1. KBLI Decision Engine (Python)

```python
"""
KBLI Recommendation Engine for Indonesian Content Creators.

Based on KBLI 2025 classification and Permendag No. 19/2026.
Rules compiled from official OSS guidelines and media reports.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class RevenueSource(Enum):
    VIDEO = "video"         # YouTube, TikTok video, IG Reels
    AUDIO = "audio"         # Podcast, audio content
    ENDORSE = "endorse"     # Brand endorsement, sponsorship
    WRITING = "writing"     # Blog, copywriting, articles
    PRODUCT = "product"     # Selling physical or digital products
    STREAMING = "streaming" # Live streaming, real-time content
    MULTI = "multi"         # Multiple sources (hybrid)

@dataclass
class KBLICode:
    code: str
    name: str
    description: str
    examples: List[str]
    confidence_rules: Dict[str, float]  # feature -> weight

KBLI_DATABASE = {
    "59112": KBLICode(
        code="59112",
        name="Produksi Film, Video, dan Program Televisi",
        description="Aktivitas produksi film, video, dan program televisi "
                    "untuk berbagai media digital, termasuk konten video komersial",
        examples=[
            "YouTuber dengan konten video reguler",
            "TikToker dengan konten video kreatif",
            "Pembuat konten Instagram Reels",
            "Videografer lepas",
        ],
        confidence_rules={
            "video_primary": 0.95,
            "video_secondary": 0.70,
            "no_video": 0.10,
        }
    ),
    "59201": KBLICode(
        code="59201",
        name="Aktivitas Perekaman Suara dan Produksi Audio",
        description="Aktivitas perekaman suara dan produksi audio, "
                    "termasuk podcast dan konten audio digital",
        examples=[
            "Podcaster",
            "Voice over artist",
            "Pembuat konten audio (Spotify, Apple Podcasts)",
        ],
        confidence_rules={
            "audio_primary": 0.95,
            "audio_secondary": 0.75,
            "no_audio": 0.05,
        }
    ),
    "73100": KBLICode(
        code="73100",
        name="Periklanan",
        description="Aktivitas periklanan termasuk pemasaran konten, "
                    "promosi digital, dan manajemen brand",
        examples=[
            "Influencer dengan endorsemen brand",
            "Selebgram dengan konten promosi",
            "Digital marketer lepas",
            "Affiliate marketer",
        ],
        confidence_rules={
            "endorse_primary": 0.95,
            "endorse_secondary": 0.80,
            "no_endorse": 0.10,
        }
    ),
    "90200": KBLICode(
        code="90200",
        name="Aktivitas Seni dan Hiburan",
        description="Aktivitas seni dan hiburan, termasuk pertunjukan, "
                    "kreator konten hiburan, dan aktivitas kreatif digital",
        examples=[
            "Live streamer (Twitch, Bigo Live)",
            "Entertainer digital",
            "Musisi yang memonetisasi konten",
        ],
        confidence_rules={
            "streaming_primary": 0.90,
            "performance_primary": 0.85,
            "entertainment_focus": 0.80,
        }
    ),
    "90111": KBLICode(
        code="90111",
        name="Aktivitas Penciptaan Karya Tulis",
        description="Aktivitas penciptaan karya tulis, termasuk penulis "
                    "profesional, copywriter, dan content creator berbasis tulisan",
        examples=[
            "Blogger",
            "Copywriter lepas",
            "Penulis artikel berbayar",
            "Konten kreator berbasis teks (Threads, Twitter/X)",
        ],
        confidence_rules={
            "writing_primary": 0.95,
            "writing_secondary": 0.70,
        }
    ),
    "63990": KBLICode(
        code="63990",
        name="Aktivitas Situs Jejaring Sosial dan Distribusi Konten Digital",
        description="KATEGORI BARU KBLI 2025: Aktivitas platform jejaring "
                    "sosial dan distribusi konten digital",
        examples=[
            "Kreator multichannel (video + audio + tulisan + endorse)",
            "Content aggregator",
            "Digital content distributor",
        ],
        confidence_rules={
            "multi_platform": 0.85,
            "content_aggregator": 0.90,
        }
    ),
}

class KBLIRecommender:
    """
    AI-powered KBLI code recommender for content creators.
    Uses a weighted decision matrix based on user profiling answers.
    """
    
    def __init__(self):
        self.kbli_db = KBLI_DATABASE
    
    def recommend(
        self,
        primary_source: RevenueSource,
        has_endorsement: bool,
        video_frequency: str,     # "daily", "weekly", "monthly", "never"
        audio_frequency: str,     # "daily", "weekly", "monthly", "never"
        writing_frequency: str,   # "daily", "weekly", "monthly", "never"
        sells_products: bool,
        is_live_streamer: bool,
    ) -> List[Dict]:
        """
        Recommend KBLI codes based on user profiling answers.
        Returns list of dicts with code, name, confidence, and explanation.
        
        Args:
            primary_source: Main revenue source
            has_endorsement: Whether they do brand endorsements
            video_frequency: How often they post video content
            audio_frequency: How often they produce audio content
            writing_frequency: How often they write content
            sells_products: Whether they sell physical/digital products
            is_live_streamer: Whether they primarily live stream
        
        Returns:
            Sorted list of recommendations with confidence scores
        """
        # Build feature vector
        features = {
            "video_primary": primary_source == RevenueSource.VIDEO,
            "video_secondary": video_frequency in ("daily", "weekly"),
            "no_video": video_frequency == "never",
            "audio_primary": primary_source == RevenueSource.AUDIO,
            "audio_secondary": audio_frequency in ("daily", "weekly"),
            "no_audio": audio_frequency == "never",
            "endorse_primary": primary_source == RevenueSource.ENDORSE,
            "endorse_secondary": has_endorsement,
            "no_endorse": not has_endorsement,
            "writing_primary": primary_source == RevenueSource.WRITING,
            "writing_secondary": writing_frequency in ("daily", "weekly"),
            "streaming_primary": is_live_streamer and primary_source == RevenueSource.STREAMING,
            "multi_platform": self._is_multiplatform(
                video_frequency, audio_frequency, writing_frequency
            ),
            "entertainment_focus": is_live_streamer,
            "sells_products": sells_products,
        }
        
        # Score each KBLI code
        results = []
        for code, kbli_info in self.kbli_db.items():
            score = 0.0
            matched_rules = []
            
            for feature, required in features.items():
                if feature in kbli_info.confidence_rules:
                    if required:
                        weight = kbli_info.confidence_rules[feature]
                        score += weight
                        matched_rules.append(feature)
            
            # Normalize to 0-100 scale
            max_possible = sum(kbli_info.confidence_rules.values())
            confidence = (score / max_possible * 100) if max_possible > 0 else 0
            
            results.append({
                "code": code,
                "name": kbli_info.name,
                "description": kbli_info.description,
                "confidence": round(confidence, 1),
                "examples": kbli_info.examples,
                "matched_reasons": matched_rules,
            })
        
        # Sort by confidence descending
        results.sort(key=lambda x: x["confidence"], reverse=True)
        
        return results
    
    def _is_multiplatform(self, video, audio, writing) -> bool:
        """Check if user creates content in 2+ formats."""
        formats = 0
        if video in ("daily", "weekly"):
            formats += 1
        if audio in ("daily", "weekly"):
            formats += 1
        if writing in ("daily", "weekly"):
            formats += 1
        return formats >= 2
    
    def generate_explanation(self, recommendation: Dict) -> str:
        """Generate plain-Indonesian explanation for the recommendation."""
        code = recommendation["code"]
        name = recommendation["name"]
        conf = recommendation["confidence"]
        
        if conf >= 85:
            certainty = "Sangat cocok"
        elif conf >= 65:
            certainty = "Cocok"
        else:
            certainty = "Bisa dipertimbangkan"
        
        return (
            f"{certainty}: KBLI {code} ({name})\n\n"
            f"Mengapa: Berdasarkan aktivitas utama kamu, "
            f"kode ini paling sesuai dengan jenis kegiatan yang kamu lakukan.\n\n"
            f"Contoh pengguna: {', '.join(recommendation['examples'][:2])}.\n\n"
            f"Catatan: Jika kamu melakukan lebih dari satu jenis kegiatan, "
            f"pilih kode yang paling dominan (>=60% dari pendapatan). "
            f"Kamu bisa konsultasi dengan ahli pajak untuk kepastian lebih lanjut."
        )


# Example usage
if __name__ == "__main__":
    recommender = KBLIRecommender()
    
    # Case: YouTuber yang juga terima endorse
    result = recommender.recommend(
        primary_source=RevenueSource.VIDEO,
        has_endorsement=True,
        video_frequency="daily",
        audio_frequency="never",
        writing_frequency="never",
        sells_products=False,
        is_live_streamer=False,
    )
    
    print("Top 3 Recommendations:")
    for r in result[:3]:
        print(f"  KBLI {r['code']}: {r['name']} (confidence: {r['confidence']}%)")
        print(f"  -> {recommender.generate_explanation(r)}\n")
```

### 11.2. WhatsApp Flow Handler (Node.js)

```javascript
/**
 * WhatsApp conversation handler for Legal.in Aja bot.
 * Uses Twilio WhatsApp Business API + Dialogflow CX for NLU.
 */

const twilio = require('twilio');
const dialogflow = require('@google-cloud/dialogflow-cx');
const { ClaudeAPI } = require('./claude-client');
const { KBLIRecommender } = require('./kbli-engine');

// Initialize clients
const twilioClient = twilio(process.env.TWILIO_SID, process.env.TWILIO_AUTH);
const dfClient = new dialogflow.SessionsClient();
const kbliEngine = new KBLIRecommender();

// Session store (in production, use Redis)
const sessions = new Map();

/**
 * Main webhook handler for incoming WhatsApp messages.
 * Route by detected intent or conversation state.
 */
async function handleIncomingMessage(req, res) {
    const { Body: messageText, From: waNumber } = req.body;
    const sessionId = waNumber.replace('whatsapp:', '');
    
    // Get or create session
    if (!sessions.has(sessionId)) {
        sessions.set(sessionId, {
            state: 'welcome',
            data: {},
            history: []
        });
    }
    const session = sessions.get(sessionId);
    session.history.push({ role: 'user', text: messageText });
    
    // Route based on state and intent
    const response = await processMessage(session, messageText);
    
    session.history.push({ role: 'bot', text: response });
    
    // Send via Twilio
    await twilioClient.messages.create({
        from: 'whatsapp:+6281234567890',
        body: response.body,
        to: waNumber,
        ...(response.buttons ? {
            persistentAction: response.buttons.map(b => 
                `reply:${b.id}:${b.title}`
            ).join(';')
        } : {})
    });
    
    res.status(200).end();
}

/**
 * Process message based on conversation state machine.
 */
async function processMessage(session, text) {
    const state = session.state;
    const textLower = text.toLowerCase();
    
    // State machine transitions
    switch (state) {
        case 'welcome':
            if (textLower.includes('nib')) {
                session.state = 'kbli_wizard_q1';
                return {
                    body: 'Oke! Saya akan bantu pilih kode KBLI yang tepat.\n\n' +
                          'Pertanyaan 1: Apa sumber penghasilan utama kamu?\n' +
                          '1. Video (YouTube, TikTok, IG Reels)\n' +
                          '2. Audio (Podcast, voice over)\n' +
                          '3. Endorse/Sponsor dari brand\n' +
                          '4. Tulisan (Blog, copywriting)\n' +
                          '5. Jualan produk\n' +
                          '6. Live streaming\n\n' +
                          'Ketik angka 1-6:',
                    buttons: [
                        { id: '1', title: 'Video' },
                        { id: '2', title: 'Audio' },
                        { id: '3', title: 'Endorse' },
                    ]
                };
            } else if (textLower.includes('halal')) {
                session.state = 'halal_check_nib';
                return {
                    body: 'Baik! Saya bantu urus Sertifikasi Halal.\n\n' +
                          'Sebelum itu, kamu sudah punya NIB?\n' +
                          '(jawab: "Sudah" atau "Belum")'
                };
            } else if (textLower.includes('dua') || textLower.includes('semua')) {
                session.state = 'kbli_wizard_q1';
                session.data.needs_halal = true;
                return {
                    body: 'Kita urus satu per satu. Pertama NIB dulu, ya.\n\n' +
                          'Pertanyaan 1: Apa sumber penghasilan utama kamu?',
                    buttons: [
                        { id: '1', title: 'Video' },
                        { id: '2', title: 'Audio' },
                        { id: '3', title: 'Endorse' },
                    ]
                };
            } else {
                return {
                    body: 'Halo! Saya asisten legalitas digital.\n\n' +
                          'Saya bisa bantu:\n' +
                          '1. Cek KBLI & daftar NIB (wajib per 18 Juni 2026)\n' +
                          '2. Panduan Sertifikasi Halal (wajib Oktober 2026)\n' +
                          '3. Keduanya\n\n' +
                          'Ketik "NIB", "Halal", atau "Dua-duanya":',
                    buttons: [
                        { id: 'nib', title: 'NIB' },
                        { id: 'halal', title: 'Halal' },
                        { id: 'both', title: 'Dua-duanya' },
                    ]
                };
            }
        
        case 'kbli_wizard_q1': {
            const sourceMap = {
                '1': 'video', '2': 'audio', '3': 'endorse',
                '4': 'writing', '5': 'product', '6': 'streaming'
            };
            session.data.primary_source = sourceMap[text.trim()] || 'video';
            session.state = 'kbli_wizard_q2';
            return {
                body: 'Pertanyaan 2: Apakah kamu menerima endorsemen/sponsor dari brand?\n' +
                      '(jawab: "Ya" atau "Tidak")'
            };
        }
        
        case 'kbli_wizard_q2': {
            session.data.has_endorsement = textLower.includes('ya');
            session.state = 'kbli_wizard_q3';
            return {
                body: 'Pertanyaan 3: Seberapa sering kamu upload konten video?\n' +
                      '1. Setiap hari\n' +
                      '2. Seminggu sekali\n' +
                      '3. Sebulan sekali\n' +
                      '4. Jarang/tidak pernah\n\n' +
                      'Ketik angka 1-4:'
            };
        }
        
        // ... additional wizard steps ...
        
        case 'kbli_result': {
            // Generate recommendation using KBLI engine
            const recs = kbliEngine.recommend({
                primary_source: session.data.primary_source,
                has_endorsement: session.data.has_endorsement,
                video_frequency: session.data.video_frequency,
                audio_frequency: session.data.audio_frequency || 'never',
                writing_frequency: session.data.writing_frequency || 'never',
                sells_products: session.data.sells_products || false,
                is_live_streamer: session.data.is_live_streamer || false,
            });
            
            const top = recs[0];
            session.data.recommended_kbli = top.code;
            
            let response = `Rekomendasi KBLI untuk kamu:\n\n`;
            response += `1. KBLI ${top.code}: ${top.name} (confidence: ${top.confidence}%)\n`;
            response += `   ${top.description}\n\n`;
            
            if (recs.length > 1) {
                response += `Alternatif:\n`;
                response += `2. KBLI ${recs[1].code}: ${recs[1].name} (${recs[1].confidence}%)\n`;
            }
            
            response += `\nSetuju dengan rekomendasi ini? (jawab "Ya" atau "Pilih lain")`;
            
            session.state = 'kbli_confirm';
            return { body: response };
        }
        
        default:
            return {
                body: 'Maaf, saya tidak mengerti. Ketik "Menu" untuk kembali ke awal.'
            };
    }
}
```

### 11.3. OSS Status Scraper (Python, leveraging 01-crawler-scrapper)

```python
#!/usr/bin/env python3
"""
OSS-RBA NIB Status Checker.
Scrapes OSS portal to check NIB registration status and pre-fill guidance.

Leverages cookie persistence patterns from 01-crawler-scrapper/cookies-tokens/.

Requirements:
- playwright
- cryptography (for cookie encryption storage)
"""

import json
import time
from typing import Optional, Dict
from playwright.sync_api import sync_playwright, Page
from cryptography.fernet import Fernet

# Load encrypted cookie store (from 01-crawler-scrapper patterns)
COOKIE_STORE_PATH = "data/oss_cookies.encrypted"
COOKIE_KEY = Fernet.generate_key()  # in production, load from env

OSS_BASE_URL = "https://oss.go.id"
OSS_NIB_CHECK_URL = "https://oss.go.id/portal/cek-nib"


class OSSSession:
    """
    Manages OSS-RBA browser session with cookie persistence.
    Pattern borrowed from 01-crawler-scrapper/cookies-tokens/storage-safety.md
    
    Usage:
        session = OSSession()
        status = session.check_nib_status(nik="1234567890123456")
        print(f"NIB status for NIK: {status}")
    """
    
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.cipher = Fernet(COOKIE_KEY)
        self.browser = None
        self.context = None
        self.page = None
    
    def _load_cookies(self) -> Optional[list]:
        """Load encrypted cookies from local store."""
        try:
            with open(COOKIE_STORE_PATH, 'rb') as f:
                encrypted = f.read()
            decrypted = self.cipher.decrypt(encrypted)
            return json.loads(decrypted.decode())
        except (FileNotFoundError, Exception):
            return None
    
    def _save_cookies(self, cookies: list):
        """Encrypt and save cookies to local store."""
        encrypted = self.cipher.encrypt(json.dumps(cookies).encode())
        with open(COOKIE_STORE_PATH, 'wb') as f:
            f.write(encrypted)
    
    def _rotate_user_agent(self) -> str:
        """Rotate user agent to avoid detection."""
        agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        ]
        import random
        return random.choice(agents) + " Chrome/120.0.0.0 Safari/537.36"
    
    def start(self):
        """Launch browser and load saved cookies."""
        p = sync_playwright().start()
        self.browser = p.chromium.launch(headless=self.headless)
        self.context = self.browser.new_context(
            user_agent=self._rotate_user_agent(),
            viewport={"width": 1920, "height": 1080},
            locale="id-ID",
            timezone_id="Asia/Jakarta",
        )
        
        # Load saved cookies if available
        saved_cookies = self._load_cookies()
        if saved_cookies:
            self.context.add_cookies(saved_cookies)
            print(f"[OSS] Loaded {len(saved_cookies)} saved cookies")
        
        self.page = self.context.new_page()
        return self.page
    
    def check_nib_status(self, nik: str) -> Dict:
        """
        Check NIB status for a given NIK.
        
        Returns dict with:
        - has_nib: bool
        - nib_number: str or None
        - status: str (active, expired, not_found)
        - business_name: str or None
        - kbli_code: str or None
        - last_updated: str or None
        """
        if not self.page:
            self.start()
        
        page = self.page
        
        # Navigate to NIB check page
        page.goto(OSS_NIB_CHECK_URL, wait_until="networkidle")
        
        # Handle potential captcha or redirect
        if "captcha" in page.url.lower() or "recaptcha" in page.content().lower():
            print("[OSS] Captcha detected, using fallback method")
            return self._fallback_nib_check(nik)
        
        # Fill NIK in search field
        page.fill("input[name='nik']", nik)
        page.click("button[type='submit']")
        
        # Wait for results
        page.wait_for_selector(".result-card, .alert, .error-message", timeout=10000)
        
        # Parse result
        result = {"nik": nik, "has_nib": False}
        
        try:
            nib_element = page.query_selector(".nib-number")
            if nib_element:
                result["has_nib"] = True
                result["nib_number"] = nib_element.text_content().strip()
            
            status_element = page.query_selector(".status-badge")
            if status_element:
                result["status"] = status_element.text_content().strip()
            
            name_element = page.query_selector(".business-name")
            if name_element:
                result["business_name"] = name_element.text_content().strip()
            
            kbli_element = page.query_selector(".kbli-code")
            if kbli_element:
                result["kbli_code"] = kbli_element.text_content().strip()
        
        except Exception as e:
            print(f"[OSS] Error parsing result: {e}")
            result["error"] = str(e)
        
        # Save cookies for next use
        cookies = self.context.cookies()
        self._save_cookies(cookies)
        
        return result
    
    def _fallback_nib_check(self, nik: str) -> Dict:
        """
        Fallback: Use OSS public API endpoint directly (bypasses browser).
        This endpoint may be rate-limited.
        """
        import requests
        
        api_url = "https://api.oss.go.id/v1/nib/check"
        headers = {
            "User-Agent": self._rotate_user_agent(),
            "Origin": OSS_BASE_URL,
            "Referer": f"{OSS_BASE_URL}/portal/cek-nib",
            "Accept": "application/json",
        }
        
        response = requests.post(
            api_url,
            json={"nik": nik},
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            return {
                "nik": nik,
                "error": f"API returned {response.status_code}",
                "has_nib": None,
            }
    
    def get_nib_registration_guide(self, kbli_code: str) -> Dict:
        """
        Get step-by-step registration guide for specific KBLI code.
        
        Returns dict with fields that need to be filled in OSS:
        - required_documents: list
        - field_by_field_guide: list of (field_name, tips, example_value)
        - estimated_time: str
        - common_errors: list
        """
        # Static guide compiled from OSS documentation and user reports
        guide = {
            "59112": {
                "required_documents": [
                    "KTP (scan/foto)",
                    "NPWP (jika sudah punya)",
                    "Email aktif",
                    "Nomor telepon",
                ],
                "field_guide": [
                    {
                        "field": "Nama Usaha",
                        "tip": "Bisa pakai nama channel atau nama panggung",
                        "example": "KreatorTV Studio",
                    },
                    {
                        "field": "Jenis Usaha",
                        "tip": "Pilih 'Perorangan' bukan 'Badan Usaha'",
                        "example": "Perorangan",
                    },
                    {
                        "field": "KBLI",
                        "tip": "Ketik 59112, pastikan deskripsi sesuai",
                        "example": "59112 - Produksi Film, Video, TV",
                    },
                    {
                        "field": "Alamat Usaha",
                        "tip": "Bisa pakai alamat domisili (rumah/kos)",
                        "example": "Jl. Contoh No. 123, Jakarta Selatan",
                    },
                    {
                        "field": "Modal Usaha",
                        "tip": "Isi perkiraan modal awal (min Rp 10 juta untuk kreator konten)",
                        "example": "25.000.000",
                    },
                ],
                "estimated_time": "30-45 menit",
                "common_errors": [
                    "NIK tidak terdaftar di Dukcapil (solusi: hubungi Disdukcapil)",
                    "NPWP tidak valid (solusi: cek di djponline.pajak.go.id)",
                    "Email sudah terdaftar (solusi: gunakan email lain)",
                ],
            },
            # ... guides for other KBLI codes ...
        }
        
        return guide.get(kbli_code, {
            "required_documents": ["KTP", "NPWP", "Email", "No telepon"],
            "field_guide": [],
            "estimated_time": "30-60 menit",
            "common_errors": ["Verifikasi NIK gagal", "Email sudah digunakan"],
        })
    
    def close(self):
        """Close browser session."""
        if self.browser:
            self.browser.close()


# CLI entry point
if __name__ == "__main__":
    import sys
    nik = sys.argv[1] if len(sys.argv) > 1 else "1234567890123456"
    
    session = OSSession(headless=True)
    try:
        result = session.check_nib_status(nik)
        print(json.dumps(result, indent=2))
    finally:
        session.close()
```

### 11.4. SIHALAL Status Tracker (Playwright-based)

```python
#!/usr/bin/env python3
"""
SIHALAL Sertifikasi Halal Status Tracker.
Monitors self-declare and certification status for UMKM users.

Integrates with BPJPH SIHALAL system at https://sihalal.halal.go.id
"""

from typing import Optional, Dict
from dataclasses import dataclass
from enum import Enum
import json
from datetime import datetime


class HalalStatus(Enum):
    NOT_STARTED = "not_started"
    SELF_DECLARE_DRAFT = "self_declare_draft"
    SELF_DECLARE_SUBMITTED = "self_declare_submitted"
    PENDING_VERIFICATION = "pending_verification"
    P3H_ASSIGNED = "p3h_assigned"
    UNDER_REVIEW = "under_review"
    APPROVED = "approved"
    CERTIFIED = "certified"
    REJECTED = "rejected"
    EXPIRED = "expired"


@dataclass
class HalalCertification:
    """Data class for halal certification status."""
    user_id: str
    nib_number: str
    status: HalalStatus
    products: list
    submission_date: Optional[datetime]
    estimated_completion: Optional[datetime]
    certificate_number: Optional[str]
    p3h_name: Optional[str]
    queue_position: Optional[int]


class SIHALALTracker:
    """
    Tracks SIHALAL certification status by scraping the portal.
    
    Since SIHALAL does not provide webhook notifications,
    we poll the status page daily using Playwright.
    
    Cookie persistence and stealth patterns from 01-crawler-scrapper.
    """
    
    SIHALAL_BASE = "https://sihalal.halal.go.id"
    LOGIN_URL = f"{SIHALAL_BASE}/login"
    DASHBOARD_URL = f"{SIHALAL_BASE}/dashboard"
    STATUS_URL = f"{SIHALAL_BASE}/status-permohonan"
    
    def __init__(self):
        self.session = None
        self.page = None
    
    def login(self, email: str, password: str) -> bool:
        """Login to SIHALAL portal."""
        # Implementation using Playwright
        # Handles captcha by using 2captcha API or manual intervention
        pass
    
    def check_status(self, nomor_permohonan: str) -> HalalCertification:
        """Check certification status for a given application number."""
        pass
    
    def get_sehati_quota(self) -> Dict:
        """
        Check remaining SEHATI kuota.
        
        Returns dict:
        - total_quota: int
        - used: int
        - remaining: int
        - last_updated: str
        """
        pass
    
    def find_nearby_p3h(self, city: str) -> list:
        """
        Find nearby Pendamping P3H by city/kabupaten.
        
        Returns list of P3H with:
        - name
        - institution
        - city
        - contact (if public)
        - specialization
        """
        pass
```

---

## 12. Operational Plan

### 12.1. Team Requirements (First 6 Months)

| Role | Month 1-3 | Month 4-6 | Notes |
|------|-----------|-----------|-------|
| Full-stack developer | 2 | 3 | Node.js + Python + React |
| WhatsApp bot specialist | 1 | 1 | Dialogflow CX + Twilio |
| Legal/compliance officer | 1 | 2 | Monitor regulatory changes, handle escalations |
| Admin (customer service) | 2 | 5 | Handle full-service requests, answer questions |
| Content/marketing | 1 | 2 | SEO, TikTok content, community management |
| Data analyst | 0 | 1 | KBLI ML model, analytics, insights |
| **Total** | **7** | **14** | |

### 12.2. Monthly Cost Structure (Month 4-6 Steady State)

| Item | Monthly Cost (IDR) | Notes |
|------|--------------------|-------|
| Salaries (14 people) | Rp 250-350M | Competitive rates for Indonesian talent |
| WhatsApp API (Twilio/WATI) | Rp 15-30M | 500K-1M messages/month |
| Claude API / LLM | Rp 10-20M | 100K-200K API calls/month |
| Cloud infrastructure (GCP/AWS) | Rp 15-25M | PostgreSQL, app servers, CDN |
| Ads (Facebook, Google, IG) | Rp 50-100M | Customer acquisition |
| SEO/content production | Rp 10-20M | Freelance writers, video editors |
| Legal/compliance | Rp 5-10M | External counsel for regulatory monitoring |
| Office/overhead | Rp 15-25M | Co-working space, internet, etc. |
| **Total** | **Rp 370-580M** | **~USD 22K-35K/month** |

### 12.3. Revenue Projection (Conservative)

| Month | Free Users | Premium Users | Monthly Revenue | Cumulative Revenue |
|-------|-----------|---------------|-----------------|-------------------|
| M1 | 1,000 | 50 | Rp 4.9M | Rp 4.9M |
| M2 | 5,000 | 300 | Rp 29.7M | Rp 34.6M |
| M3 | 15,000 | 1,000 | Rp 99M | Rp 133.6M |
| M4 | 40,000 | 3,000 | Rp 297M | Rp 430.6M |
| M5 | 80,000 | 7,000 | Rp 693M | Rp 1.12B |
| M6 | 150,000 | 15,000 | Rp 1.48B | Rp 2.6B |
| M12 | 2,000,000 | 200,000 | Rp 19.8B | Rp ~60B |

---

## 13. Next Steps (Immediate Actions)

1. **Validate KBLI wizard with 20 kreator konten** -- Post in 3 Facebook/Telegram groups, offer free KBLI check, record accuracy and confusion points
2. **Scrape BPJPH P3H directory** -- Build database of 1,000+ Pendamping P3H across Indonesia with location mapping
3. **Test OSS API access** -- Request partner integration access from OSS team, or build Playwright-based fallback
4. **Set up WhatsApp Business API sandbox** -- Create test flow with Dialogflow CX, test with 10 users
5. **Create 10 SEO-optimized landing pages** -- Target "KBLI kreator konten", "daftar NIB online", "sertifikasi halal gratis 2026" keywords
6. **Publish first 5 TikTok/Reels** -- "Cek KBLI kamu gratis dalam 30 detik" series

---

## 14. New Gaps Discovered During Research

1. **KBLI code ambiguity tool needed** -- Selama riset, ditemukan bahwa banyak kreator konten yang bingung memilih antara KBLI 59112, 73100, dan 90200. Peluang untuk membuat "KBLI Ambiguity Detector" yang membandingkan 3 kode teratas dengan contoh kasus spesifik.

2. **P3H availability API/monitor** -- Pendamping P3H tidak memiliki API publik untuk cek ketersediaan. Scraper perlu dibangun untuk monitoring real-time jumlah P3H aktif per kabupaten/kota, karena distribusi tidak merata.

3. **OSS field-by-field video library** -- Banyak user OSS mengalami error di field yang sama (modal usaha, alamat, skala usaha). Peluang untuk membuat micro-video library (30 detik per field) yang bisa direferensi oleh platform regtech mana pun.

4. **Regulatory change monitor for kreator konten** -- Regulasi kreator konten masih sangat baru dan bisa berubah cepat. Kebutuhan akan automated monitor yang memindai Permendag, PMK, dan Peraturan Kemenekraf setiap hari, lalu mengirimkan ringkasan perubahan ke WhatsApp subscriber. Ini bisa menjadi produk standalone atau fitur premium.

5. **Cross-border regtech** -- Kreator konten Indonesia yang menerima pembayaran dari luar negeri (AdSense, Patreon, Stripe) menghadapi kompleksitas tambahan: pajak lintas negara, transfer valas, dan kepatuhan UU ITE. Peluang untuk layanan "Kreator Ekspor" yang mengurus legalitas ekspor jasa digital.

---

## 15. Sources

1. Kontan (2026-06-20). "Content Creator Komersial Wajib Punya NIB? Ini Syarat Daftar dan Aturan KBLI." https://lifestyle.kontan.co.id/news/content-creator-komersial-wajib-punya-nib-ini-syarat-daftar-dan-aturan-kbli

2. Kompas (2026-06-20). "NIB untuk Influencer: Negara Tak Boleh Kalah Cepat dari Algoritma." https://www.kompas.com/read/2026/06/20/11000081/nib-untuk-influencer-negara-tak-boleh-kalah-cepat-dari-algoritma

3. Tirto (2026-06-18). "Apa itu NIB Content Creator yang Wajib Dimiliki Pegiat Medsos?" https://tirto.id/apa-itu-nib-content-creator-yang-wajib-dimiliki-pegiat-medsos-g-ZZZ

4. Medcom (2026-06-18). "Kreator Konten Kini Wajib Punya NIB, Begini Penjelasannya." https://www.medcom.id/nasional/peristiara/YKgqjP3k-kreator-konten-kini-wajib-punya-nib-begini-penjelasannya

5. Yoursay.id (2026-06-19). "Wajib NIB bagi Kreator Konten per 18 Juni: Langkah Formalisasi atau Jerat Pajak Baru?" https://yoursay.id/wajib-nib-bagi-kreator-konten-per-18-juni-langkah-formalisasi-atau-jerat-pajak-baru/

6. Kompas.id (2026-06-22). "Kreator Konten Tak Bisa Gunakan PPh UMKM 0,5 Persen, Kok Bisa?" https://www.kompas.id/baca/riset/2026/06/22/kreator-konten-tak-bisa-gunakan-pph-umkm-05-persen (paywalled)

7. MediaKompeten (2026-06-20). "Kemenekraf Dialog dengan Asosiasi Tanggapi Wacana NIB Kreator Konten." https://mediakompeten.id/2026/06/20/kemenekraf-dialog-dengan-asosiasi-tanggapi-wacana-nib-kreator-konten/

8. BPJPH (2025-12-23). "Pemerintah Gratiskan 1,35 Juta Sertifikat Halal bagi Usaha Mikro dan Kecil di Tahun 2026." https://bpjph.halal.go.id/detail/pemerintah-gratiskan-1-35-juta-sertifikat-halal-bagi-usaha-mikro-dan-kecil-di-tahun-2026

9. Kontan (2026-06-19). "Wajib Sertifikasi Halal Berlaku Oktober 2026, UMKM Soroti Kendala Biaya." https://industri.kontan.co.id/news/wajib-sertifikasi-halal-berlaku-oktober-2026-umkm-soroti-kendala-biaya

10. LPPOM MUI (2025-12-17). "Sertifikat Halal UMKM Gratis 2026 (Panduan Lengkap)." https://halalmui.org/sertifikat-halal-umkm-gratis-panduan-2026/

11. Kementerian UMKM (2026-01-10). "Sertifikasi Halal Gratis 2026 Dimulai, Ini Kriteria UMKM yang Dapat." https://umkm.go.id/news/vofv7cb1omei09dao4bn8w8h

12. Pemerintah Kabupaten Cilacap (2026-05-31). "Jelang Wajib Halal, 300 UMKM Cilacap Disasar Sosialisasi." https://cilacapkab.go.id/v3/jelang-wajib-halal-300-umkm-cilacap-disasar-sosialisasi/

13. Money Glitch Vault (2026-06-23). "NIB Wajib bagi Kreator Konten dan Influencer." 03-id-business-trends/demand-mining/nib-wajib-kreator-konten-influencer.md

14. Money Glitch Vault (2026-06-23). "Sertifikasi Halal Wajib Oktober 2026: UMKM Terbebani Biaya dan Kerumitan Proses." 03-id-business-trends/demand-mining/sertifikasi-halal-wajib-oktober-2026-umkm-terbebani.md

15. Money Glitch Vault (2026-06-23). Weekly Gap Report 2026-06-23. 07-gaps-and-opportunities/weekly-gap-report-2026-06-23.md

---

*This document is a research one-pager for the Money Glitch Vault. It is not investment advice nor a business plan. Data points are sourced from public media, government announcements, and vault demand-mining files as of June 2026.*
