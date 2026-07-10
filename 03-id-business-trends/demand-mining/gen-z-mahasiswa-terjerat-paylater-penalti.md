# Gen Z dan Mahasiswa Terjerat PayLater, Penalti Telat Bayar Makan Gaji Pertama

**Date observed:** 2026-07-10
**Signal strength:** 5/5
**Category:** student
**Sources (minimum 3):**
- [Kala Gen Z Dikepung Teror Pinjol dan Pay Later](https://mediaindonesia.com/forum-mahasiswa/906644/jebakan-manis-paylater-ketika-kemudahan-bertransaksi-mengancam-masa-depan-finansial-gen-z) — 2025-03-28 — OJK: PayLater tembus Rp31,55 triliun, 26,96 juta rekening per Juni 2025
- [Paylater: Kemudahan Finansial atau Bom Waktu untuk Mahasiswa?](https://mahasiswa.co.id/paylater-kemudahan-finansial-atau-bom-waktu-untuk-mahasiswa/10614/) — 2025-04-30 — Survei: 61 persen mahasiswa kota besar pakai paylater, 48 persen pakai lebih 3x sebulan
- [OJK: Anak Muda Kebanyakan Utang dari Paylater](https://www.liputan6.com/bisnis/read/5731700/ojk-anak-muda-kebanyakan-utang-dari-paylater) — 2026-01-07 — OJK sebut anak muda dominan berutang lewat paylater
- [Gen Z Hati-Hati! Tahun 2026 Jangan Sampai Tercekik Paylater](https://www.trenasia.id/tren-pasar/gen-z-hati-hati-tahun-2026-jangan-sampai-tercekik-paylater) — 2026-03-26 — Gen Z penyumbang tingkat kredit macet (TWP90) tertinggi

## The pain (verbatim quotes in Indonesian)

> "BAYANGKAN membeli sepatu seharga Rp800 ribu hanya dengan tiga ketukan jari, tanpa perlu mengecek saldo rekening. Itulah daya tarik utama layanan Buy Now Pay Later (BNPL) atau PayLater yang kini menjadi bagian tak terpisahkan dari gaya belanja generasi Z." — Media Indonesia

> "Survei OJK pada 2025 menunjukkan bahwa sekitar 61% mahasiswa di kota besar Indonesia telah menggunakan layanan paylater, dengan 48% di antaranya menggunakannya lebih dari tiga kali dalam sebulan." — Mahasiswa.co.id

> "Yang lebih mengkhawatirkan, diantara mayoritas tersebut menggunakan paylater bukan untuk kebutuhan akademik." — Mahasiswa.co.id

> "Gen Z tercatat menjadi penyumbang tingkat kredit macet (TWP90) tertinggi, akibat kombinasi pendapatan entry-level yang belum stabil dengan tekanan gaya hidup Fear of Missing Out (FOMO)." — Trenasia

PayLater (SPayLater, Kredivo, Akulaku, dll) menjebak Gen Z dan mahasiswa lewat kemudahan satu klik tanpa rasa "berutang". Promo, cashback, dan FOMO bikin mereka belanja bukan kebutuhan, lalu telat bayar kena penalti dan bunga berbunga. OJK mencatat total kredit paylater Rp31,55 triliun dengan 26,96 juta rekening per Juni 2025, dan Gen Z jadi penyumbang kredit macet tertinggi. Mahasiswa dengan penghasilan nol atau UMR entry-level kepleset ke spiral utang sejak kuliah.

## Evidence of volume

- OJK: paylater Rp31,55 triliun, 26,96 juta rekening per Juni 2025 (Media Indonesia), angka terus naik tiap kuartal.
- 61 persen mahasiswa kota besar pakai paylater, 48 persen pakai lebih 3x/bulan (survei OJK 2025 via Mahasiswa.co.id).
- Riset 57 mahasiswa USU: 82 persen tahu paylater, mayoritas pakai untuk gaya hidup bukan kebutuhan mendesak (JurnalPost).
- Gen Z penyumbang TWP90 (kredit macet) tertinggi secara nasional (Trenasia, 2026).

## Existing solutions (and why they fail)

- Edukasi OJK dan literasi keuangan kampus: gagal karena pesan moral tak sanggup lawan algoritma promo dan FOMO tiap hari.
- Fitur batas kredit dan reminder di app paylater: gagal karena justru mendorong pakai terus, bukan batasi.
- Aplikasi budgeting umum (Money Lover, Finansialku): gagal karena tak terhubung langsung ke saldo paylater, input manual, dan tak ada alarm telat bayar otomatis.

## Your wedge

Bangun pelindung utang digital khusus Gen Z: aggregator yang tarik semua saldo paylater (Shopee, Tokopedia, Kredivo, Akulaku, dll) ke satu dashboard, hitung total kewajiban vs pemasukan, dan kasih alarm H-3 sebelum jatuh tempo plus simulasi "kalau telat 5 hari denda berapa". Bedanya: ada mode "lock" yang blokir ajakan belanja saat sisa duit di bawah batas aman, dan konten edukasi singkat berbasis FOMO-buster. Model freemium: gratis untuk tracking, berbayar untuk fitur nego penalti dan rencana lunasi cicilan. Karena celahnya adalah kebiasaan, bukan ketidaktahuan, alat ini harus proaktif ngelindungin bukan cuma mengingatkan.

## What people would pay

- Model: gratis untuk 1 akun paylater, Rp19.000-Rp29.000/bulan untuk unlimited akun + alarm dan rencana lunasi.
- Evidence willingness-to-pay: mahasiswa rugi puluhan ribu rupiah denda tiap kali telat, jadi langganan Rp19.000/Bulan lebih murah dari satu kali penalti. Segmen pekerja baru dengan gaji UMR juga rela bayar untuk hindari macet.
- Comparable: aplikasi manajemen keuangan berlangganan Rp20.000-Rp50.000/bulan, dan konsultasi utang offline ratusan ribu per sesi.

## Adjacent opportunities

- Negosiasi tagihan dan restrukturisasi utang otomatis ke penyelenggara paylater.
- Bundling asuransi cicilan yang menanggung denda kalau telat gara-gara PHK.
- Komunitas tantangan "detoks paylater" berbasis gamifikasi untuk retensi.

## Time-to-build estimate

- 2 minggu dengan no-code dashboard + integration API publik (sebagian paylater punya open API) dan reminder WhatsApp.
- 1 bulan dengan scraper/aggregator multi-akun dan engine simulasi denda.
- 3+ bulan untuk fitur nego otomatis dan kemitraan resmi dengan fintech.
