# Driver Ojol Terjebak Sistem Potongan Tarif dan Ketidakpastian Pendapatan

**Date observed:** 2026-07-27
**Signal strength:** 4
**Category:** ojol
**Sources (minimum 3):**
- [Saatnya Pengemudi Ojol Memiliki Koperasi Platform](https://money.kompas.com/read/2026/07/25/055500426/saatnya-pengemudi-ojol-memiliki-koperasi-platform) — 2026-07-25 — Potongan tarif hingga 20-30% dan ketidakpastian implementasi janji potongan 8%
- [Danantara Beli Saham Ojol, Potongan Komisi 8 Persen Dilakukan Perlahan](https://money.kompas.com/read/2026/05/01/190300326/danantara-beli-saham-ojol-potongan-komisi-8-persen-dilakukan-perlahan) — 2026-05-01 — Presiden janji potongan maksimal 8% namun implementasi belum jelas
- [Pemerintah Bakal Tertibkan Aplikator Ojol yang Belum Terapkan Skema Bagi Hasil 92:8](https://www.kompas.com/tag/ojol) — 2026-07-27 — Pemerintah akan tertibkan aplikator yang belum mematuhi Perpres no. 27/2026
- [Berawal dari Driver Ojol yang Kehilangan Kuota, MK Larang Sisa Paket Data Hangus](https://tekno.kompas.com/read/2026/07/24/12350037/berawal-dari-driver-ojol-yang-kehilangan-kuota-mk-larang-sisa-paket-data-hangus) — 2026-07-24 — Driver ojol menggugat skema kuota internet hangus, MK kabulkan

## The pain (verbatim quotes in Indonesian)
> "Selama ini, perdebatan publik selalu berputar pada satu pertanyaan: berapa persen potongan yang adil? Apakah 20 persen terlalu besar, atau cukup diturunkan menjadi 15 persen, bahkan 8 persen? Namun, pertanyaan yang jauh lebih penting justru jarang diajukan. Mengapa jutaan pengemudi yang menggerakkan seluruh ekosistem transportasi digital setiap hari tidak pernah memiliki platform yang mereka jalankan?" (Kompas.com, 25 Juli 2026)

> "Alih-alih menghadirkan kebijakan yang lebih adil, polemik mengenai besaran potongan tarif justru terus berulang. Bahkan, janji Presiden Prabowo Subianto pada peringatan Hari Buruh Internasional tahun ini, untuk menurunkan potongan aplikasi menjadi maksimal 8 persen, hingga kini belum menunjukkan kejelasan implementasinya." (Kompas.com, 25 Juli 2026)

> "Para pengemudi masih berada dalam ketidakpastian. Sementara pemerintah, perusahaan aplikasi, dan parlemen terus memperdebatkan besaran angka yang dianggap paling ideal." (Kompas.com, 25 Juli 2026)

## Evidence of volume
- 58 komentar di r/indonesia tentang potongan komisi ojol dan Danantara beli saham
- Potongan komisi saat ini antara 15-30% per transaksi (sumber: berbagai keluhan driver)
- 2+ juta driver ojol aktif di Indonesia (Gojek, Grab, ShopeeFood, Maxim)
- Perpres No. 27/2026 ditandatangani namun implementasi masih molor
- Gugatan class action driver ojol ke MK soal skema kuota internet hangus (dikabulkan Juli 2026)

## Existing solutions (and why they fail)
- **Perpres No. 27/2026**: Janji potongan maksimal 8% namun implementasi stagnan karena aplikator menolak
- **Koperasi platform (gagasan)**: Masih wacana, belum ada eksekusi konkret
- **Demo dan mogok kerja**: Sudah berkali-kali dilakukan tetapi tidak membuahkan hasil signifikan
- **Beralih ke aplikasi lain**: Semua aplikator (Gojek, Grab, ShopeeFood) punya skema potongan serupa

## Your wedge
Platform "Ojol Bersatu" — koperasi digital berbasis aplikasi untuk driver ojol dengan model:
1. **Rate aggregator**: Tampilkan perbandingan potongan real-time dari semua aplikator, rekomendasi aplikasi paling menguntungkan per jam dan lokasi
2. **Cooperative order pool**: Pool order dari UMKM lokal yang langsung didistribusikan ke anggota koperasi tanpa potongan aplikator (hanya biaya koperasi 5%)
3. **Income smoothing**: Asuransi pendapatan harian — jika pendapatan di bawah Rp 100.000/hari, koperasi menutup selisihnya (premi Rp 2.000/hari)
4. **Legal aid**: Bantuan hukum untuk driver yang menghadapi masalah dengan aplikator atau kecelakaan kerja

Monetasi: Iuran anggota Rp 15.000/bulan + fee 5% dari transaksi pool sendiri + referral fee dari Mitra (asuransi, bengkel, SPBU).

## What people would pay
- **Rp 10.000 - 15.000 per bulan** untuk iuran koperasi digital
- **Rp 2.000 per hari** untuk income smoothing (asuransi pendapatan minimum)
- Driver ojol rata-rata belanja Rp 50.000/minggu untuk pulsa dan bensin — koperasi bisa bundling diskon
- Comparable: koperasi konvensional belum ada yang fokus ke driver ojol; Serikat Ojol (Organda) hanya advokasi, tidak ada layanan finansial

## Adjacent opportunities
- Bengkel dan sparepart motor dengan diskon anggota koperasi
- Pinjaman modal untuk ganti ban/service motor (potong setoran harian)
- Tabungan pensiun driver ojol (setor Rp 5.000/hari)
- Asuransi kecelakaan kerja harian (Rp 1.000/hari)

## Time-to-build estimate
- 3 minggu dengan WhatsApp bot + Google Sheets untuk MVP aggregator tarif
- 2 bulan untuk aplikasi mobile dengan fitur pool order dan koperasi digital
- 6+ bulan untuk full platform dengan income smoothing, legal aid, dan ekosistem bengkel
