# Pedagang Daging Sapi dan Kuliner Tercekik Harga Daging Tembus Rp 130 Ribu/Kg

**Date observed:** 2026-07-18
**Signal strength:** 4
**Category:** seller
**Sources (minimum 3):**
- [Daging Sapi Tembus Rp 130 Ribu/Kg, Pedagang Pasar Porong Pilih Libur](https://www.detik.com/jatim/bisnis/d-8573882/daging-sapi-tembus-rp-130-ribu-kg-pedagang-pasar-porong-pilih-libur) — 2026-07-15 — Pedagang daging di Sidoarjo libur karena pembeli sepi dan takut rugi.
- [Keluh Pedagang Bakso di Lamongan Saat Harga Daging Sapi Terus Naik](https://www.detik.com/jatim/berita/d-8576084/keluh-pedagang-bakso-di-lamongan-saat-harga-daging-sapi-terus-naik) — 2026-07-16 — Pedagang bakso bingung naikkan harga takut pelanggan kabur.
- [Harga Daging Sapi Terus Naik, Pedagang di Lamongan Pilih Libur Jualan](https://www.detik.com/jatim/berita/d-8576068/harga-daging-sapi-terus-naik-pedagang-di-lamongan-pilih-libur-jualan) — 2026-07-16 — Paguyuban pedagang daging Lamongan mogok 3 hari.
- [Pedagang Daging Sapi Mau Mogok Jualan 5 Hari Mulai Senin Depan](https://finance.detik.com/berita-ekonomi-bisnis/d-5955599/pedagang-daging-sapi-mau-mogok-jualan-5-hari-mulai-senin-depan) — arsip pola mogok nasional saat harga melonjak.

## The pain (verbatim quotes in Indonesian)
> "Harga daging biasa sekarang Rp 130 ribu/kg. Kalau daging pilihan bisa mencapai Rp 135 ribu hingga Rp 140 ribu/kg. Pembeli sekarang sangat sepi." (Syaiful, pedagang daging Pasar Porong, detikJatim 15 Jul 2026)

> "Penjualan turun sangat jauh. Dulu ramai, sekarang pembeli berkurang terus. Modal naik, untung hampir tidak ada, bahkan kadang rugi." (Syaiful, pedagang daging Pasar Porong)

> "Kalau dipaksakan ambil banyak, nanti tidak habis terjual. Sekarang kami ambil sedikit saja karena harga sudah tinggi." (Ira, pedagang daging Pasar Porong)

> "Kami bingung. Mau menaikkan harga jual makanan takut pelanggan keberatan dan akhirnya warung jadi sepi. Tapi kalau tidak dinaikkan, pendapatan kami jelas berkurang dan tidak bisa menutup biaya operasional." (Khoirul, pedagang bakso Lamongan, detikJatim 16 Jul 2026)

Setelah Lebaran dan Idul Adha 2026, harga daging sapi justru kembali naik karena pasokan sapi siap potong menipis. Di Jawa Timur harga pasar tradisional kini Rp 120.000 sampai Rp 140.000/kg. Pedagang daging dan pelaku kuliner (bakso, soto, warung makan) terjepit di antara modal bahan baku naik dan ketakutan kehilangan pelanggan bila menaikkan harga jual.

## Evidence of volume
- 3 artikel detikJatim dalam 15 sampai 16 Juli 2026 membahas kenaikan harga daging sapi dan dampaknya ke pedagang.
- Paguyuban Pedagang Daging Sapi Lamongan memutuskan mogok berjualan 3 hari (15 sampai 17 Juli 2026), sinyal protes kolektif skala kabupaten.
- Menurut pedagang, kenaikan terjadi 3 kali dalam 3 bulan: dari Rp 100.000 ke Rp 130.000/kg, dan volume jual turun dari 3 sampai 4 ekor sapi/hari jadi belum tentu 1 ekor habis.
- Harga jeroan (hati, paru, limpa) ikut naik Rp 5.000/kg, menekan pelaku kuliner kecil secara menyeluruh.

## Existing solutions (and why they fail)
- Harapan pada Pemkab/Pemprov dan Dinas Perdagangan menstabilkan harga: lambat, bergantung pasokan sapi potong yang tak terkendali pedagang kecil.
- Pedagang menurunkan stok atau libur: menyelamatkan modal sebentar tapi kehilangan omzet dan pelanggan.
- Menaikkan harga jual: berisiko pelanggan pindah ke tempat lain, seperti dikeluhkan pedagang bakso.
- Membeli dari rumah potong hewan (RPH) langsung: tak semua pedagang kecil punya akses atau modal cash flow untuk stok panjang.

## Your wedge
Bangun "Koperasi Beli Bersama Daging & Bahan Pokok" berbasis WA/desktop: pedagang kuliner dan warung gabung pesan daging sapi (dan jeroan) dalam volume besar langsung dari RPH/feedlot terverifikasi, potong rantai tengkulak dan dapatkan harga grosir stabil. Tambahkan fitur "patokan harga jual" yang menghitung HPP + margin wajar agar pedagang berani naikkan harga tanpa kehilangan pelanggan, plus modul stok cerdas supaya tak over-beli. Monetisasi lewat margin grosir tipis (2 sampai 3 persen) dan iuran keanggotaan Rp 25.000 sampai Rp 50.000/bulan. Bisa diintegrasikan dengan gap inbox 2026-07-10-warung-collective-buying.md yang sudah ada.

## What people would pay
- Iuran keanggotaan: Rp 25.000 sampai Rp 50.000 per bulan per pedagang/warung.
- Margin grosir: 2 sampai 3 persen dari nilai belanja bersama (volume pedagang daging + kuliner di satu kabupaten bisa puluhan juta per hari).
- Evidence willingness-to-pay: konsep collective buying sudah masuk gap inbox (warung-collective-buying.md, gas-group-buying-umkm.md), dan pedagang secara eksplisit bilang "kami berharap pemerintah bisa membantu menstabilkan harga" artinya mereka terbuka pada solusi pihak ketiga yang lebih cepat.

## Adjacent opportunities
- Group buying untuk ayam potong, telur, minyak goreng (bahan kuliner lain yang ikut naik).
- Asuransi harga bahan baku mikro untuk warung (lindung margin saat harga loncat).
- SaaS HPP + penentu harga jual untuk UMKM kuliner (overlaps marketplace-net-margin-calc gap).

## Time-to-build estimate
- 2 minggu: grup WA + Google Sheet pemesanan bareng + daftar RPH mitra manual.
- 1 bulan: mini app web dengan kalkulator HPP dan manajemen stok otomatis.
- 3+ bulan: platform koperasi digital lintas kabupaten dengan logistik daging beku sendiri.
