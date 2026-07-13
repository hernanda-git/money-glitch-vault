# Truk dan Bus Angkutan Barang Sulit Dapat Solar Bersubsidi, Logistik Terganggu

**Date observed:** 2026-07-13
**Signal strength:** 4/5
**Category:** other
**Sources (minimum 3):**
- [Mengapa Truk dan Bus Sulit Mendapatkan Solar](https://bisnis.tempo.co/read/2112987/mengapa-truk-dan-bus-sulit-mendapatkan-solar) — 2026-07-10 — antrean panjang di Sumatera, Kalimantan, Sulawesi
- [Pertamina Tanggapi Sinyal Kelangkaan Solar di Sumatera](https://bisnis.tempo.co/read/2113030/pertamina-tanggapi-sinyal-kelangkaan-solar-di-sumatera) — 2026-07-10 — Pertamina akui dugaan distribusi tak tepat sasaran
- [Nelayan Cilincing Keluhkan Sulitnya Dapat Solar Bersubsidi](https://www.tempo.co/foto/arsip/nelayan-cilincing-keluhkan-sulitnya-dapat-solar-bersubsidi-303191) — arsip Tempo — kelangkaan juga melanda nelayan

## The pain (verbatim quotes in Indonesian)
> "Bahkan hampir setiap jam ada video yang masuk ke grup percakapan kami terikat antrean solar."
> "Kelangkaan solar ini sebenarnya sudah berlangsung lama dan selalu berulang. Namun, kondisinya semakin parah dalam sebulan terakhir."
> "Adnan menilai kelangkaan solar atau biosolar bersubsidi semakin masif sejak diberlakukan sistem barcode melalui aplikasi MyPertamina. Menurut dia, penerapan sistem tersebut masih menyisakan banyak persoalan di lapangan sehingga belum berjalan efektif."
> "SPBU yang mengajukan pasokan sebanyak 32 kiloliter hanya menerima sekitar 18 kiloliter."

## Evidence of volume
- Organda terima laporan antrean hampir setiap hari dari Padang, Bukittinggi, Jambi, Medan, Palembang, hingga Lampung, plus wilayah Kalimantan dan Sulawesi
- ALFI (Asosiasi Logistik dan Forwarder Indonesia): masalah berlangsung bertahun-tahun di Kalimantan, Sulawesi, dan Indonesia timur, dibiarkan tanpa solusi konkret
- Sistem barcode MyPertamina disebut memperparah kelangkaan karena banyak persoalan di lapangan
- Pasokan SPBU sering dipotong (contoh: 32 kl diajukan, 18 kl diterima) sehingga stok cepat habis

## Existing solutions (and why they fail)
- Aplikasi MyPertamina (barcode subsidi): dimaksudkan tepat sasaran, tapi di lapangan justru memperlambat dan membingungkan pengemudi, menurut Sekjen Organda
- Pertamina Patra Niaga: hanya menjawab "dugaan distribusi tidak tepat sasaran" tanpa merinci penyebab atau langkah mitigasi (Tempo sudah kirim pertanyaan, tak dijawab rinci)
- SPBU kecil: kapasitas tangki dirancang untuk mobil penumpang, tidak cukup untuk truk logistik, sehingga antrean membludak

## Your wedge
Buat "peta stok solar real-time" yang mengumpulkan laporan sukarela dari supir truk dan kondektur bus lewat bot WhatsApp (ketik "SPBU X kosong/ada") lalu menampilkan peta ketersediaan dan perkiraan antrean. Karena distributor resmi tidak transparan, data dari pengemudi sendiri adalah satu-satunya sinyal real-time yang berguna. Tambahkan fitur navigasi rute irit BBM yang menghindari titik langka, serta modul klaim selisih pasokan untuk pengelola SPBU yang ingin buktikan pemotongan kuota ke Pertamina. Untuk UMKM logistik, berikan ringkasan harian "di mana solar ada" agar jadwal kirim tidak batal.

## What people would pay
- Perusahaan logistik / ekspedisi: Rp500.000 sampai Rp2 juta per armada per bulan untuk rute hindari-antrean dan pelaporan
- Koperasi angkutan / PO bus: Rp1 juta sampai Rp3 juta per bulan untuk dashboard stok wilayah
- Evidence willingness to pay: ALFI dan Organda sudah berkali-kali mengeluh ke publik, ada tekanan industri agar distribusi efisien. Biaya BBM adalah pos terbesar angkutan barang, jadi hemat rute sangat berharga
- Comparable: aplikasi navigasi macam Waze (gratis, tapi tak khusus BBM), dan platform manajemen armada (GPS tracking) seperti Gulir atau Traksi mematok puluhan ribu per kendaraan per bulan

## Adjacent opportunities
- Bot lapor kelangkaan BBM lain (Pertalite, elpiji 3 kg) terintegrasi satu dashboard warga
- Kalkulator biaya operasi angkutan saat subsidi dipangkas (lihat gap inbox takehomepay)
- Marketplace bill of lading untuk UMKM ekspor hindari telat kirim

## Time-to-build estimate
- 2 minggu dengan tools off-the-shelf (WhatsApp bot + peta Google Maps + spreadsheet sebagai backend laporan)
- 1 bulan dengan custom dev (peta agregat real-time + modul klaim SPBU)
- 3+ bulan untuk produk penuh dengan integrasi API logistik dan routing engine sendiri
