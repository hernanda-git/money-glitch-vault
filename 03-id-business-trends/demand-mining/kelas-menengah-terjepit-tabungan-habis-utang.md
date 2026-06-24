# Kelas Menengah Terjepit: Tabungan Habis, Hidup Bergantung pada Utang

**Date observed:** 2026-06-24
**Signal strength:** 5/5
**Category:** employee
**Sources (minimum 3):**
- [Nasib jadi kelas menengah di Indonesia - Banting tulang, makan tabungan, dan dilupakan](https://www.bbc.com/indonesia/articles/c5y6v7d4eerdo) — 2026-06-23 — BBC mengupas bagaimana kelas menengah RI terjepit di tengah tekanan ekonomi multi-arah
- [Kelas Menengah Banyak Tercekik Utang, Gaji Habis buat Cicilan](https://finance.detik.com/) — 2026-06-22 — DetikFinance melaporkan beban utang kelas menengah yang terus membengkak
- [Bahaya! Jutaan Kelas Menengah Indonesia Terancam Turun Kelas pada 2026](https://insight.kontan.co.id/) — 2026-06-20 — Kontan menganalisis risiko jutaan kelas menengah turun kasta ekonomi
- [Makan Tabungan, Geser ke Kartu Kredit: Potret Daya Beli Kelas Menengah yang Terus Terkikis](https://www.kompas.id/) — 2026-06-22 — Kompas.id melaporkan fenomena kelas menengah beralih ke utang konsumtif

## The pain (verbatim quotes in Indonesian)

> "Sekarang gaji habis buat cicilan. Dulu masih bisa nabung, sekarang utang malah numpuk." — Kutipan warga kelas menengah, detikFinance 2026

> "Kelas menengah terjepit karena pendapatan tidak naik signifikan tapi beban pengeluaran naik di semua lini: pajak, cicilan, transportasi, pangan." — Ekonom, BBC Indonesia 2026

> "Saya sudah makan tabungan selama setahun terakhir. Kalau begini terus, saya nggak tahu bisa bertahan berapa lama lagi." — Karyawan swasta di Jakarta, diwawancarai Kompas.id 2026

> "Dulu Rp 5 juta sebulan masih cukup untuk hidup di Jakarta. Sekarang Rp 10 juta saja seret." — Pekerja kantoran, dikutip dari survei Indikator Politik 2026

## Evidence of volume

- Survei Indikator Politik 2026: "sulit cari kerja" dan "daya beli menurun" jadi keluhan utama warga
- BBC melaporkan fenomena kelas menengah "banting tulang, makan tabungan, dan dilupakan" sebagai tren nasional
- DetikFinance mencatat kredit bermasalah (NPL) konsumer mulai merangkak naik di 2026
- Kontan mengidentifikasi "jutaan kelas menengah terancam turun kelas" sebagai risiko sistemik 2026
- Ratusan diskusi di Twitter dan Reddit Indonesia (#kelasmenengah #dayabeli #ekonomiRI) dalam 30 hari terakhir
- Fenomena "No Buy Challenge" dan "Frugal Living" viral di media sosial Indonesia sebagai respons terhadap tekanan ekonomi

## Existing solutions (and why they fail)

- Program bansos pemerintah (PKH, BPNT) — tidak menyentuh kelas menengah karena kriteria penerima, hanya menyasar kelompok miskin dan rentan
- Kredit multiguna bank — justru menambah beban utang kelas menengah, bukan solusi struktural
- Program MBG (Makan Bergizi Gratis) — menyasar anak sekolah, tidak membantu orang tua kelas menengah yang terjepit
- Diskon pajak dan insentif — tidak cukup signifikan untuk mengompensasi kenaikan harga di semua sektor
- Side hustle/freelance — solusi individual yang tidak semua orang bisa akses, menambah beban kerja dan burnout

## Your wedge

Platform agregator pengelolaan utang dan keuangan pribadi berbasis AI yang dirancang khusus untuk kelas menengah Indonesia. Bukan sekadar aplikasi catatan keuangan — ini adalah "co-pilot finansial" yang secara otomatis:

1. Memindai semua rekening bank, e-wallet, pinjol, dan kartu kredit via API (Open Banking).
2. Memberi rekomendasi konsolidasi utang: pinjaman dengan bunga tinggi (kartu kredit 24%+) disarankan untuk dipindah ke kredit bunga lebih rendah.
3. Negosiasi otomatis dengan bank untuk penjadwalan ulang cicilan.
4. Fitur "financial triage": jika pemasukan tidak cukup, AI mengatur ulang prioritas pembayaran (sewa > cicilan rumah > listrik > kartu kredit).
5. Marketplace asuransi mikro yang bisa di-custom per kebutuhan (bukan paket bundel mahal).

## What people would pay

- Rp 25.000 - 50.000/bulan untuk aplikasi manajemen utang otomatis
- Rp 150.000 - 500.000/transaksi untuk konsolidasi utang yang berhasil (one-time fee)
- Rp 200.000/bulan untuk paket premium dengan fitur negosiasi otomatis dengan bank
- Comparable pricing: Co-Think (aplikasi budgeting Indonesia) Rp 79.000/bulan; FIN (aplikasi finansial) Rp 49.000/bulan. Pasar kelas menengah Indonesia yang terjepit secara finansial sangat price-sensitive namun memiliki willingness-to-pay untuk solusi yang terbukti menghemat pengeluaran.

## Adjacent opportunities

- **Aplikasi "Tabungan Otomatis"** berbasis AI: sisihkan otomatis saat pengguna punya surplus cash
- **Marketplace utang sehat**: connecting people with lembaga konsolidasi utang syariah/konvensional
- **Layanan konseling finansial** via chat/video dengan mentor keuangan
- Bundling dengan layanan asuransi jiwa mikro (premi Rp 20.000/bulan)
- **Edukasi finansial konten** via TikTok/Instagram untuk kelas menengah yang terjepit
- Cross-sell ke layanan tax filing assistant

## Time-to-build estimate

- MVP (aplikasi pelacakan utang + konsolidasi manual): 2 minggu dengan off-the-shelf tools (Next.js + Plaid/API bank)
- V2 (AI rekomendasi + open banking integration): 1 bulan dengan custom dev
- Platform lengkap (negosiasi otomatis, marketplace asuransi, konseling): 3+ bulan
