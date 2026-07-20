# Koperasi Desa Merah Putih Simpang Siur Pengadaan, Rakyat Minta Dashboard

**Date observed:** 2026-07-20
**Signal strength:** 4
**Category:** umkm
**Sources (minimum 3):**
- [Beredar Kabar Pengadaan Kipas Angin Kopdes Rp1,8 T, Menkop Bilang Begini](https://finance.detik.com/berita-ekonomi-bisnis/d-8575449/beredar-kabar-pengadaan-kipas-angin-kopdes-rp-1-8-t-menkop-bilang-begini) — 2026-07-15 — DPR pertanyakan pengadaan 1,8 juta kipas angin senilai Rp1,8 triliun
- [Pekerja Koperasi Desa Merah Putih Gelisah Gaji dan Kontrak Tak Jelas](https://finance.detik.com/berita-ekonomi-bisnis) — 2026-07-13 — INDEX demand-mining existing pain soal nasib pekerja KDKMP
- [Rincian Utang Badan Gizi Nasional Rp1,6 Triliun](https://finance.detik.com/berita-ekonomi-bisnis/d-8579077/rincian-utang-badan-gizi-nasional-rp-1-6-triliun) — 2026-07-19 — pengadaan publik bermasalah beruntun, isu transparansi makin panas

## The pain (verbatim quotes in Indonesian)
> "Hari ini rakyat sedang dihebohkan dengan isu adanya pengadaan kipas angin 1,8 juta dengan nilainya Rp1,8 triliun. Lalu dari isu ini kami mencari informasi tapi kami tidak dapat satu informasi pun dari pemerintah adanya pengadaan ini." — Mufti Anam, Anggota Komisi VI DPR RI, 15 Juli 2026

> "Kipas angin cosmos di e-commerce official store milik Cosmos itu harganya Rp338 ribu. Lalu kemudian cek di Shopee, Tokopedia, harganya lebih murah lagi hanya Rp300 ribuan. Itu kalau beli satuan." — Mufti Anam, membandingkan harga pasar vs estimasi pengadaan

> "Kementerian Koperasi dan PT Agrinas Pangan yang selalu diam-diam dalam melakukan pengadaan barang untuk KDKMP. Untuk itu, ia meminta agar disediakan dashboard agar setiap rakyat dapat memantau setiap pengadaan." — Mufti Anam, menuntut transparansi

## Evidence of volume
- Program Koperasi Desa/Kelurahan Merah Putih (KDKMP) menyebar ke ribuan desa, anggaran pengadaan triliunan rupiah.
- DPR secara terbuka tidak dapat satu informasi pun soal pengadaan Rp1,8 triliun, menunjukkan ketiadaan akses data publik.
- Isu serupa muncul beruntun: utang BGN Rp1,6 triliun, 9 importir belum bayar utang malah dapat uang negara (detik, 19 Juli 2026).
- Anggota koperasi desa dan netizen ramai di X menuntut "dashboard KDKMP" pasca skandal kipas angin.

## Existing solutions (and why they fail)
- LPSE / Injourney e-procurement: hanya cover kementerian/lembaga, tidak cover pengadaan di bawah Kementerian Koperasi lewat PT Agrinas yang tertutup.
- Laporan tahunan koperasi: manual, terlambat, tidak real-time, dan sulit diakses anggota desa.
- Media investigasi: reaktif, baru angkat setelah viral di DPR.

## Your wedge
Bangun "KopDes Transparansi" , dashboard publik terbuka yang mengambil data pengadaan KDKMP/PT Agrinas (lewat FOI, web scraping, dan laporan anggota koperasi) lalu membandingkan otomatis dengan harga pasar e-commerce (Shopee/Tokopedia API) untuk mendeteksi markup. Anggota koperasi bisa input pengadaan desanya lewat WA bot, sehingga terbangun peta pengadaan nasional dari bawah. Wedge: crowdsource + auto price-check vs pasar, sesuatu yang tidak dilakukan pemerintah. Bisa dimonetisasi lewat langganan DPR/NGO/LSM (transparansi watchdog) dan fitur alert untuk anggota koperasi.

## What people would pay
- Price point: gratis untuk anggota koperasi (crowdsource data); Rp2-10 juta/tahun untuk LSM/NGO/watchdog dan DPRD.
- Evidence willingness-to-pay: DPR sendiri minta dashboard resmi. LSM seperti Indonesia Corruption Watch dan kawan-kawan siap pakai alat pantau anggaran.
- Comparable: platform seperti Kawal Dana, Aplikasi SiTepat, dan ayodonasi punya model serupa (grant/instansi funded).

## Adjacent opportunities
- Bundling dengan umkm-compliance-dashboard (sudah ada di gaps inbox) untuk pelaporan koperasi.
- Alert bot untuk anggota koperasi soal hak dan dana desa (mirip PBI-guard WA bot).
- Cross-sell ke tools pemantauan dana desa (DDT, Siskeudes) yang sudah ada.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: WA bot input + sheet dashboard + scraper harga e-commerce.
- 1 bulan dengan custom dev: auto price-check engine dan peta nasional.
- 3+ bulan untuk produk penuh dengan integrasi FOI otomatis dan API pemerintah.
