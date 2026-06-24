# Peternak Ayam Broiler dan Petelur Tersungkur: Harga Anjlok, Biaya Produksi Melonjak

**Date observed:** 2026-06-24
**Signal strength:** 5/5
**Category:** farmer
**Sources (minimum 3):**
- [Peternak Rakyat Menjerit, Harga Ayam Anjlok saat Biaya Produksi Naik](https://www.kompas.com/) — 2026-06-23 — Kompas melaporkan peternak ayam rakyat menjerit akibat harga jual anjlok di tengah biaya produksi yang terus naik
- [Saat harga ayam murah, peternak 'rugi' dan 'kalah saing' dengan perusahaan besar](https://www.bbc.com/indonesia/articles/c5y6v7d4eerdo) — 2026-06-22 — BBC mengungkap peternak kecil kalah saing dengan korporasi besar yang menguasai rantai pasok
- [Harga Ayam Hidup Anjlok Jadi Rp 17 Ribu Per Kg, Peternak Kelimpungan](https://www.detik.com/) — 2026-06-22 — DetikFinance melaporkan peternak ayam di Jateng kelimpungan harga ayam hidup anjlok
- [Guru Besar IPB: Industri Perunggasan Tak Baik-baik Saja](https://www.cnbcindonesia.com/) — 2026-06-20 — CNBC Indonesia mengutip Guru Besar IPB yang membongkar masalah struktural industri perunggasan RI

## The pain (verbatim quotes in Indonesian)

> "Sekarang harga jual ayam cuma Rp 17.000 per kg, padahal biaya produksi saja Rp 20.000 per kg. Berarti kami rugi Rp 3.000 per kg. Satu kandang isi 5.000 ekor, rugi sampai puluhan juta." — Peternak ayam broiler di Jawa Tengah, dikutip detikcom, Juni 2026

> "Peternak rakyat menjerit. Kami kalah saing dengan perusahaan besar yang punya pakan sendiri, DOC sendiri, dan rantai distribusi sendiri. Kami cuma bisa pasrah." — Ketua Perhimpunan Peternak Rakyat Mandiri Indonesia (PERMINDO), dikutip Akses.co.id

> "Dari modal nol, saya bangun usaha ini. Tapi sekarang harga pakan naik terus, jagung Rp 10.000 per kg. Kalau begini terus, saya akan berhenti beternak." — Peternak ayam petelur di Batu, Jawa Timur, dikutip detikcom

> "Oversupply terjadi karena korporasi besar terus membanjiri pasar, sementara peternak kecil tidak punya daya tawar. Ini bukan soal efisiensi, ini soal monopoli." — Guru Besar IPB University, dikutip Validnews.id

## Evidence of volume

- BBC Indonesia membuat laporan khusus tentang peternak kecil kalah saing dengan korporasi besar
- Detikcom memiliki lebih dari 15 artikel tentang krisis ayam dalam 30 hari terakhir
- CNBC Indonesia melaporkan temuan Guru Besar IPB tentang konsentrasi industri perunggasan
- Puluhan peternak di Tulungagung menggelar aksi bagi-bagi telur gratis sebagai protes harga anjlok (detikcom)
- Peternak di Solo Raya menggelar aksi "Mandi Jagung" memprotes harga pakan mahal
- PERMINDO (Perhimpunan Peternak Rakyat Mandiri Indonesia) melaporkan ribuan peternak rakyat merugi
- Pemerintah berencana impor 580.000 ayam CLQ dari AS, dikhawatirkan mematikan peternak lokal

## Existing solutions (and why they fail)

- Program MBG (Makan Bergizi Gratis) serap ayam/telur — kapasitas serap terbatas, tidak stabil, bergantung kontrak SPPG
- Pemerintah minta hotel/kafe serap ayam lokal — inisiatif ad-hoc, tidak ada mekanisme berkelanjutan
- Kementan stabilkan harga via pengaturan produksi DOC — tidak efektif karena produksi dikuasai korporasi besar (integrated)
- Pembatasan impor ayam — justru kontradiktif dengan rencana impor 580.000 ayam dari AS yang mengancam peternak lokal
- Subsidi pakan — tidak ada program subsidi pakan yang memadai, jagung pakan masih impor dan harganya fluktuatif

## Your wedge

Platform rantai pasok terintegrasi untuk peternak ayam rakyat yang memotong tengkulak dan korporasi besar. Modelnya:

1. **Koperasi digital**: peternak bergabung dalam koperasi daring untuk mendapatkan kekuatan tawar kolektif dalam membeli pakan (jagung, bungkil kedelai) langsung dari petani/importir, memotong margin distributor.
2. **Marketplace B2B**: menghubungkan peternak langsung ke pembeli (rumah potong, pedagang pasar, SPPG MBG, hotel, restoran) sehingga harga jual tidak dimonopoli tengkulak.
3. **Asuransi mikro berbasis cuaca dan harga**: jika harga ayam di bawah Harga Pokok Penjualan (HPP), peternak mendapat kompensasi otomatis. Premi dibayar per siklus panen (Rp 50.000 per 1.000 ekor).
4. **Dashboard prediksi harga**: AI memprediksi harga ayam 2-4 minggu ke depan berdasarkan data produksi DOC, permintaan musiman, dan tren harga, membantu peternak mengatur waktu panen.

## What people would pay

- Rp 150.000/bulan untuk akses ke platform koperasi digital (harga pakan lebih murah 10-15%)
- Rp 50.000 per siklus untuk asuransi mikro harga (setara 1-2% dari modal per siklus)
- 2-3% fee transaksi untuk marketplace B2B (lebih murah dari tengkulak yang ambil margin 10-20%)
- Komparasi: peternak saat ini kehilangan Rp 3.000-5.000/kg karena tengkulak; platform yang memotong rantai bahkan dengan fee 2% sudah sangat menguntungkan

## Adjacent opportunities

- **Agregator pakan ternak**: pembelian massal jagung, bungkil kedelai, tepung ikan untuk 100+ peternak sekaligus
- **Fintech syariah untuk peternak**: pembiayaan modal kerja dengan skema bagi hasil (bukan bunga), cocok untuk segmen mayoritas muslim
- **Aplikasi monitoring kandang IoT**: sensor suhu, kelembaban, dan pakan otomatis dengan notifikasi via WhatsApp
- **Marketplace DOC (bibit ayam)**: transparansi harga DOC yang selama ini dikendalikan perusahaan besar
- **Platform data industri perunggasan**: database real-time harga, produksi, dan permintaan yang bisa diakses publik

## Time-to-build estimate

- MVP (marketplace B2B + grup WA untuk koperasi digital): 2 minggu dengan off-the-shelf tools (Next.js + Twilio untuk notifikasi)
- V2 (dashboard prediksi harga + asuransi mikro): 1 bulan dengan custom dev
- Platform lengkap (semua fitur + integrasi IoT + fintech): 3+ bulan
