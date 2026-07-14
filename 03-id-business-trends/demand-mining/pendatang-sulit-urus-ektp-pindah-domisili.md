# Pendatang Antar-Daerah Tak Bisa Urus e-KTP dan Surat Pindah Domisili Online, Harus Datang ke Kantor

**Date observed:** 2026-07-15
**Signal strength:** 4
**Category:** employee
**Sources (minimum 3):**
- [Alasan Pendatang Luar Jakarta Tak Bisa Urus KTP-Surat Pindah Online](https://www.beritasatu.com/dki-jakarta/2939969/alasan-pendatang-luar-jakarta-tak-bisa-urus-ktp-surat-pindah-online) — 2024 — pengajuan KTP dan surat pindah bagi pendatang luar Jakarta tidak dapat dilakukan secara online maupun via aplikasi Alpukat Bet
- [Dukcapil DKI Buka Layanan 'Jumat Petang', Warga Bisa Urus e-KTP Sampai Malam](https://news.detik.com/berita/d-8437033/dukcapil-dki-buka-layanan-jumat-petang-warga-bisa-urus-e-ktp-sampai-malam) — 2026 — Dukcapil DKI harus buka layanan malam karena antrean urus e-KTP
- [Cara Urus SKPWNI untuk Pindah Domisili Pakai Aplikasi IKD](https://news.detik.com/berita/d-8483372/cara-urus-skpwni-untuk-pindah-domisili-pakai-aplikasi-ikd) — 2026 — panduan resmi pakai aplikasi IKD, bukti proses masih rumit butuh tutorial
- [Landen Marbun ke Rico Waas: Masyarakat Medan Utara Sulit Urus e-KTP!](https://medan.tribunnews.com/2025/07/09/landen-marbun-ke-rico-waas-masyarakat-medan-utara-sulit-urus-e-ktp) — 2025-07-09 — pelayanan adminduk di Medan Utara dikritik bobrok, warga kesulitan urus e-KTP
- [Diduga Kelelahan Urus Pindah Domisili, Lansia di Gowa Meninggal di Mal Pelayanan Publik](https://www.merdeka.com/peristiwa/diduga-kelelahan-urus-pindah-domisili-lansia-di-gowa-meninggal-di-mal-pelayanan-publik-530717-mvk.html) — 2025 — warga sampai meninggal antre urus pindah domisili

## The pain (verbatim quotes in Indonesian)
> "Pengajuan KTP dan surat pindah bagi pendatang dari luar Jakarta ternyata tidak dapat dilakukan secara online maupun melalui aplikasi Alpukat Bet." (Beritasatu)
> "Bobroknya pelayanan administrasi kependudukan kepada warga di Medan bagian Utara menjadi kritik DPRD Sumut kepada Wali Kota Medan." (Tribun-Medan)
> "Diduga karena kelelahan mengantre, seorang pria lanjut usia (lansia) bernama Nuntjik Isa S (71) meninggal dunia di Mal Pelayanan Publik (MPP) Kabupaten Gowa." (Merdeka)

## Evidence of volume
- Jutaan pendudak setiap tahun pindah domisili antar daerah (arus urbanisasi, kuli bangunan, buruh, mahasiswa); semua butuh surat pindah dan e-KTP baru
- Dukcapil DKI harus membuka layanan "Jumat Petang" hingga malam khusus untuk mengejar antrean e-KTP (detik, 2026)
- Aplikasi IKD dan Alpukat Bet ada, tapi fitur pindah domisili lintas daerah sering tidak berfungsi untuk pendatang, sehingga warga tetap harus pulang ke domisili asal
- Kasus ekstrem: lansia meninggal diduga kelelahan mengantre di MPP Gowa

## Existing solutions (and why they fail)
- Aplikasi IKD (Identitas Kependudukan Digital) dan Alpukat Bet: tidak mencover pindah domisili lintas kabupaten/kota secara penuh, sering error verifikasi
- Mal Pelayanan Publik (MPP): fisik, butuh datang, antrean panjang, jam kerja terbatas
- Layanan "Jumat Petang" Dukcapil DKI: hanya Jakarta, bukan solusi nasional
- Calo/admin desa: warga bayar untuk diuruskan, rawan pungli dan data bocor

## Your wedge
Layanan pendampingan adminduk "done-for-you" khusus pendatang: cek dokumen apa yang kurang (KK, surat pindah, bukti domisili), bantu isi form IKD/Alpukat Bet dengan benar, dan koordinasi Dukcapil asal-tujuan lewat agen lokal. Beri tracker status "surat pindah sudah sampai Dukcapil tujuan atau belum". Untuk pekerja migran domestik (buruh, ojol, kuli) yang pindah kota tiap proyek, ini hemat waktu dan cuti kerja. Bisa juga jadi SaaS untuk perusahaan yang mutasi karyawan lintas pulau.

## What people would pay
- Jasa bantu urus surat pindah + e-KTP: Rp 100.000 - 250.000 per proses (murah vs cuti kerja 1-2 hari hilang upah)
- Evidence: buruh harian lepas kehilangan Rp 100.000 - 200.000 per hari tidak masuk kerja; bayar jasa jauh lebih menguntungkan
- Comparable: jasa joki urus dokumen (SKCK, surat domisili) di marketplace laku Rp 75.000 - 200.000; pasar serupa untuk adminduk

## Adjacent opportunities
- Bundling dengan layanan urus NPWP, NIB, dan BPJS untuk pendatang yang pindah kota untuk kerja
- Cross-sell ke perusahhaan penyalur TKI domestik / agensi yang butuh dokumen rapi per karyawan
- Data "warga sulit adminduk" bisa jadi leads bagi layanan keuangan inklusif (rekening, KUR)

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: bot WA + checklist dokumen + agen manusia + grup koordinasi Dukcapil
- 1 bulan dengan custom dev: integrasi API IKD (jika terbuka), auto-fill, status tracker
- 3+ bulan untuk produk penuh dengan kerjasama resmi Ditjen Dukcapil per daerah
