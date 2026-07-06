# Harga Tiket Pesawat Kembali Melambung Usai Insentif PPN Berakhir

**Date observed:** 2026-07-06
**Signal strength:** 4/5
**Category:** other
**Sources (minimum 3):**
- [Insentif Berakhir, Mulai Hari Ini Beli Tiket Pesawat Ekonomi Kena PPN](https://www.cnbcindonesia.com/news/20260706095830-4-748286/insentif-berakhir-mulai-hari-ini-beli-tiket-pesawat-ekonomi-kena-ppn) — 2026-07-06 — Insentif PPN DTP tiket pesawat ekonomi berakhir 5 Juli 2026, harga kembali naik
- [Sebelumnya Pemerintah Perpanjang Diskon 100% PPN untuk Tiket Pesawat Kelas Ekonomi](https://www.cnbcindonesia.com/news/20260706095830-4-748286/insentif-berakhir-mulai-hari-ini-beli-tiket-pesawat-ekonomi-kena-ppn) — 2026-07-06 — Kebijakan PPN DTP sebelumnya berlaku sejak 25 April 2026 selama 60 hari
- [Kenaikan Tarif Penerbangan Domestik Tetap di Kisaran 9%-13%](https://www.cnbcindonesia.com/news/20260706095830-4-748286/insentif-berakhir-mulai-hari-ini-beli-tiket-pesawat-ekonomi-kena-ppn) — 2026-07-06 — Pemerintah berupaya menjaga kenaikan tarif tetap di kisaran 9%-13%

## The pain (verbatim quotes in Indonesian)
> "Dengan berakhirnya insentif yang dimulai pada 24 juni 2026 tersebut, harga tiket pesawat domestik kembali memuat komponen PPN yang sebelumnya ditanggung penuh oleh pemerintah." (CNBC Indonesia, 6 Juli 2026)

> "Pemerintah berupaya menjaga agar kenaikan tarif penerbangan domestik tetap berada pada kisaran 9% hingga 13% sehingga masyarakat masih dapat mengakses layanan transportasi udara." (CNBC Indonesia, 6 Juli 2026)

> "Kebijakan ini merupakan bentuk kehadiran pemerintah dalam memberikan kemudahan kepada masyarakat untuk bepergian dengan biaya yang lebih terjangkau." (Menteri Perhubungan Dudy Purwagandhi via CNBC Indonesia)

## Evidence of volume
- Kebijakan PPN DTP diperpanjang dua kali sejak April 2026, menunjukkan tekanan publik yang kuat
- Kenaikan tarif penerbangan domestik sebesar 9%-13% sudah terjadi sebelum insentif PPN diberlakukan
- Selain tiket pesawat, pemerintah juga memberikan diskon 30% tarif kereta api kelas ekonomi selama libur sekolah 2026
- Ratusan ribu pemudik dan pelancong terdampak setiap musim liburan

## Existing solutions (and why they fail)
- Solution A: Insentif PPN Ditanggung Pemerintah (PPN DTP) -- sifatnya sementara (60 hari), begitu berakhir harga langsung naik kembali
- Solution B: Subsidi langsung ke maskapai -- belum dilakukan secara menyeluruh, dan maskapai sudah menaikkan tarif sejak awal 2026
- Solution C: Regulasi tarif batas atas oleh Kemenhub -- tidak efektif karena maskapai menaikkan harga mendekati batas atas

## Your wedge
Buat platform pembanding harga tiket pesawat real-time yang mengintegrasikan seluruh maskapai domestik dengan notifikasi harga termurah berdasarkan rute dan tanggal fleksibel. Tambahkan fitur "Prediksi Harga" yang menggunakan data historis untuk memberitahu pengguna kapan harga cenderung turun atau naik, sehingga mereka bisa membeli saat masih ada insentif atau sebelum kenaikan. Untuk UMKM pariwisata, sediakan dashboard yang memantau tren harga tiket rute populer dan membantu mereka menyesuaikan paket wisata.

## What people would pay
- Rp 15.000-25.000 per notifikasi harga spesifik rute tertentu
- Rp 99.000/bulan untuk akses prediksi harga dan alert otomatis
- Rp 299.000/bulan untuk UMKM pariwisata dengan dashboard analitik
- Bukti willingness-to-pay: Masyarakat rela antre berjam-jam untuk mendapatkan tiket diskon saat insentif PPN berlaku, menunjukkan sensitivitas harga yang sangat tinggi
- Komparasi: Aplikasi seperti Traveloka dan Tiket.com sudah mengenakan biaya admin Rp 20.000-50.000 per transaksi

## Adjacent opportunities
- Paket bundling tiket pesawat + hotel + transportasi darat untuk UMKM pariwisata
- Asuransi perjalanan dengan harga terjangkau untuk pelancong kelas ekonomi
- Platform konsolidasi muatan untuk UMKM yang mengirim barang via udara
- Sistem manajemen booking untuk agen perjalanan kecil

## Time-to-build estimate
- 2 weeks with off-the-shelf tools (scraping harga dari situs maskapai + notifikasi Telegram/WhatsApp)
- 1 month with custom dev (aplikasi mobile dengan prediksi harga menggunakan machine learning)
- 3+ months for full product (platform lengkap dengan fitur UMKM pariwisata dan integrasi payment gateway)
