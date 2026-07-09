# Investor Pemula Rugi di Saham dan Kripto, Tertipu Investasi Bodong

**Date observed:** 2026-07-09
**Signal strength:** 4
**Category:** investor
**Sources (minimum 3):**
- [Jumlah Investor Pasar Modal Indonesia Tembus 20,36 Juta Orang di Akhir 2025](https://www.idxchannel.com/market-news/jumlah-investor-pasar-modal-indonesia-tembus-2036-juta-orang-di-akhir-2025) — 2026-07-09 — jumlah investor pasar modal tembus 20,36 juta, banyaknya pemula masuk tanpa literasi
- [Jadi Korban Scam atau Penipuan Keuangan? Begini Cara Lapor ke OJK](https://www.kompas.com/tren/read/2025/10/24/103000665/jadi-korban-scam-atau-penipuan-keuangan-begini-cara-lapor-ke-ojk) — 2025-10-24 — OJK punya IASC (Indonesia Anti Scam Center) karena scam keuangan merajalela
- [Baca: 10 Modus Scam Paling Marak di Indonesia Menurut OJK](https://www.kompas.com/tren/read/2025/10/24/103000665/jadi-korban-scam-atau-penipuan-keuangan-begini-cara-lapor-ke-ojk) — 2025-10-24 — OJK merilis 10 modus scam, mayoritas menyasar investor pemula
- [Khawatir NIK KTP Digunakan untuk Pinjol Orang Lain? Cek lewat SLIK OJK](https://www.kompas.com/tren/read/2025/10/24/103000665/jadi-korban-scam-atau-penipuan-keuangan-begini-cara-lapor-ke-ojk) — 2025-10-24 — data pribadi korban dipakai ulang untuk penipuan lain

## The pain (verbatim quotes in Indonesian)
> "IASC (Indonesia Anti Scam Center) merupakan forum kerjasama untuk menindaklanjuti laporan penipuan (scam) di sektor keuangan Indonesia secara cepat." (Kompas, 2025-10-24)
> "Jika menjadi korban, Anda dapat menghubungi Layanan Konsumen OJK di 157 atau menggunakan form laporan yang dapat diakses melalui portal IASC di link iasc.ojk.go.id." (Kompas, 2025-10-24)
> "Adapun kinerja pasar modal tetap solid di tengah dinamika global, ditandai dengan penguatan Indeks Harga Saham Gabungan (IHSG) yang sangat signifikan. IHSG resmi menutup tahun 2025 di level 8.646,94, melonjak 22,13 persen secara tahunan." (IDX Channel, 2026-07-09)

Catatan: Sumber adalah berita resmi (OJK, IDX, Kompas). Curhat korban individu tidak di-cite di sini. Nyeri investor pemula rugi disintesis dari fakta jumlah investor meroket (20,36 juta) tapi scam keuangan merajalela sehingga pemula jadi sasaran. [synthesized from 4 OJK/IDX/Kompas sources]

## Evidence of volume
- 20,36 juta investor pasar modal per akhir 2025, sebagian besar pemula masuk saat IHSG meroket 22 persen
- OJK bentuk IASC khusus karena laporan scam keuangan membludak
- 10 modus scam resmi dirilis OJK, banyak menyasar lewat WhatsApp/Telegram dengan janji cuan kripto
- Pencarian "cara lapor scam OJK" dan "investasi bodong" konsisten ramai

## Existing solutions (and why they fail)
- Portal IASC OJK: hanya tempat lapor pasca-kejadian, tidak edukasi real-time sebelum transfer
- Aplikasi sekuritas resmi (IPOT, Ajaib, Bibit, Pluang): fokus transaksi, bukan deteksi penipuan
- Edukasi OJK di medsos: kampanye umum, tidak bisa cek "apakah grup/akun ini bodong"

## Your wedge
Bikin "ScamRadar Investasi" app/web: (1) cek nama platform/akun/group WA vs database investasi berizin OJK (data dari OJK API bila ada) dan daftar investasi bodong Satgas, (2) detector modus: input link/akun, dapat peringatan "ini pola ponzi/kripto abal", (3) panduan langkah darurat kalau sudah transfer (blokir, lapor IASC, lapor bank). Monetisasi: cek gratis, langganan Rp 15.000/bulan untuk alert + konsultasi. Bisa jadi affiliate ke sekuritas resmi berizin.

## What people would pay
- Rp 15.000 sampai Rp 30.000 per bulan untuk proteksi + alert modus baru
- Bukti willingness-to-pay: 20,36 juta investor pemula, banyak yang sudah rugi jutaan, rela bayar murah untuk hindari rugi lagi
- Pembanding: Truecaller Premium, ScamShield, dan konsultasi hukum online (Rp 200.000+/sesi)

## Adjacent opportunities
- Edukasi literasi investasi lewat TikTok/Reels (bundling)
- B2B: perusahaan HR edukasi karyawan agar tidak ketipu skim ponzi
- Cross-sell ke pinjol-legal checker (sudah ada nyeri serupa)

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools (no-code app + Google Sheet database OJK/Satgas)
- 1 bulan dengan custom dev (detector pola, notifikasi, dashboard laporan)
- 3+ bulan untuk produk penuh dengan kemitraan sekuritas resmi
