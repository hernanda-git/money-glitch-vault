# Penipuan Lowongan Kerja Online Kian Makan Korban, Tabungan Pencari Kerja Melayang

**Date observed:** 2026-07-15
**Signal strength:** 5
**Category:** employee
**Sources (minimum 3):**
- [Cerita Yakobus Korban Penipuan Loker Mimika, Tabungan Rp 5 Juta Melayang demi Janji Palsu Grup WhatsApp](https://regional.kompas.com/read/2026/06/19/204500378/cerita-yakobus-korban-penipuan-loker-mimika-tabungan-rp-5-juta-melayang) — 2026-06-19 — 178 pencari kerja di Mimika tertipu janji kerja di Freeport lewat grup WA "Maret-April Job"
- [Bidan Puskemas di Serang Tipu Warga Modus Janjikan Kerja di BUMN, Korban Rugi Puluhan Juta](https://regional.kompas.com/read/2026/06/25/075826278/bidan-puskemas-di-serang-tipu-warga-modus-janjikan-kerja-di-bumn-korban) — 2026-06-25 — oknum bidan modus janji kerja BUMN, korban rugi puluhan juta
- [Calon ABK asal Garut jadi korban penipuan lowongan kerja di Muara Angke](https://www.antaranews.com/berita/5607840/calon-abk-asal-garut-jadi-korban-penipuan-lowongan-kerja-di-muara-angke) — 2026-01-29 — calon ABK tertipu perekrutan ilegal
- [Waspada Penipuan Modus Rekrutmen Kerja di Tambang Papua, Pria Ini Tipu Korban Puluhan Juta](https://www.merdeka.com/peristiwa/waspada-penipuan-modus-rekrutmen-kerja-di-tambang-papua-pria-ini-tipu-korban-puluhan-juta-584258-mvk.html) — 2026-06 — modus rekrutmen tambang Papua, korban puluhan juta
- [Nama Lesti Kejora Dicatut untuk Penipuan, Korban Rugi hingga Ratusan Juta Rupiah](https://celebrity.okezone.com/read/2026/05/30/33/3221550/nama-lesti-kejora-dicatut-untuk-penipuan-korban-rugi-hingga-ratusan-juta-rupiah) — 2026-05-30 — nama selebriti dicatut, korban rugi ratusan juta

## The pain (verbatim quotes in Indonesian)
> "Langkah kaki Yakobus Balubun terasa amat berat saat mendatangi Sentra Pelayanan Polres Mimika, Jumat (19/6/2026). Pria yang sudah berbulan-bulan berharap bisa mendapatkan pekerjaan layak ini harus menerima kenyataan pahit bahwa dirinya telah menjadi korban penipuan online." (Kompas)
> "Bagi Yakobus, penipuan ini bukan sekadar kehilangan uang, melainkan penghancuran harapan yang sudah dipupuknya sejak awal tahun." (Kompas)
> "Ada sekitar 178 pencari kerja (pencaker) lain di Kabupaten Mimika yang bernasib sama." (Kompas)

## Evidence of volume
- 178 pencari kerja tertipu dalam satu komplotan grup WhatsApp "Maret-April Job" di Mimika saja (Kompas, 19 Jun 2026)
- Kasus serupa meluas: Serang (BUMN), Garut/Muara Angke (ABK), tambang Papua, modus catut nama selebriti. Semua dalam Jun 2026
- Polri mencatat penipuan berkedok lowongan kerja sebagai salah satu modus digital yang naik signifikan setiap periode penerimaan kerja dan BUMN
- Facebook, TikTok, dan grup WhatsApp jadi kanal utama penyebaran iklan loker palsu yang meminta biaya "administrasi", "seragam", atau "tes kesehatan" di awal

## Existing solutions (and why they fail)
- SP2S / lapor.go.id dan patrolisiber.id: hanya untuk pelaporan pasca-kehilangan uang, tidak memverifikasi lowongan sebelum korban transfer
- Halaman "Lowongan Kerja" resmi BUMN (AFKAR, dll) dan situs Kemnaker: tersebar, tidak ada verifikasi pihak ketiga untuk iklan di medsos
- Fitur "laporkan iklan" di FB/TikTok: lambat, penipu ganti akun dalam hitungan jam
- Korban umumnya bukan "tech savvy" dan tidak punya referensi cepat untuk cek legalitas perusahaan (NIB, izin operasional) sebelum bayar

## Your wedge
Bangun layanan pengecekan lowongan kerja gratis dan instan sebelum korbannya transfer uang. Input: nama perusahaan, nomor WA, link postingan. Sistem menyeberangi data publik (AHU/OSS untuk NIB badan usaha, daftar resmi rekrutmen BUMN/Kemnaker, blacklist nomor/Rekening yang dilaporkan) lalu mengeluarkan "verifikasi hijau/kuning/merah" dalam 10 detik. Sisipkan edukasi: "lowongan resmi tidak pernah minta uang di awal". Kanal distribusi lewat bot WhatsApp/Telegram yang bisa diteruskan korban ke orang tua, agar viral secara organik di grup RT/RW dan keluarga.

## What people would pay
- Model: gratis untuk pengecekan dasar (viralitas), freemium Rp 15.000 - 25.000 per laporan mendalam atau langganan Rp 25.000/bulan untuk notifikasi penipuan di daerah tertentu
- Evidence willingness-to-pay: korban kehilangan Rp 5 juta - ratusan juta. Biaya Rp 25.000 untuk "jamin tidak ketipu" sangat murah dibanding kerugian
- Comparable: layanan cek rekening penipuan (ceklapak, TurnBackHoax) masih gratis tapi tidak spesifik loker; ruang untuk versi berbayar "asuransi verifikasi" untuk perusahaan yang ingin lowongannya bersertifikat aman

## Adjacent opportunities
- Cross-sell ke bot "cek rekening/link penipuan" yang sudah ada di gap inbox (scam-detection-tool)
- Bundling dengan layanan persiapan lamaran / CV untuk fresh graduate (karena target overlap)
- Data agregat "peta loker palsu per kota" bisa dijual ke pemda/Dinsos untuk edukasi

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: bot Telegram/WA + lookup sheet + API ceklapan + webhook ke dataset laporan
- 1 bulan dengan custom dev: koneksi ke OSS/AHU, scoring otomatis, dashboard blacklist publik
- 3+ bulan untuk produk penuh dengan kerjasama resmi Kemnaker/BSSN
