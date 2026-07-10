# Karyawan Tak Dibayar THR, Perusahaan Pakai Modus Rumahkan atau Putus Kontrak Mendadak

**Date observed:** 2026-07-10
**Signal strength:** 5
**Category:** employee
**Sources (minimum 3):**
- [Terbongkar! Ternyata Begini Modus Perusahaan Tak Bayar THR Karyawan](https://www.cnbcindonesia.com/news/20260224123438-4-713400/terbongkar-ternyata-begini-modus-perusahaan-tak-bayar-thr-karyawan) — 2026-02-24 — CNBC ungkap modus pengusaha hindari THR dengan merumahkan atau memutus kontrak via WhatsApp.
- [Ini Modus Perusahaan Hindari Bayar THR Karyawan Jelang Lebaran 2026](https://lestari.kompas.com/read/2026/03/13/151100386/ini-modus-perusahaan-hindari-bayar-thr-karyawan-jelang-lebaran-2026?page=all) — 2026-03-13 — Kompas rangkum modus penghindaran THR jelang Lebaran.
- [Masalah Penghindaran Bayar THR Berulang](https://www.kompas.id/artikel/masalah-penghindaran-bayar-thr-berulang) — 2026 — Kompas.id catat masalah ini berulang tiap tahun.

## The pain (verbatim quotes in Indonesian)
> "Modus yang dilakukan oleh pengusaha pengusaha hitam ini untuk tidak bayar THR, dengan cara merumahkan, atau memutus kontrak tiba tiba melalui WhatsApp, modus modusnya." (Said Iqbal, Presiden KSPI, via CNBC 2026-02-24)
> "Terhadap buruh buruh atau karyawan, Mie Sedaap, sudah sekitar 20 an orang yang mengadu ke Posko Orange Partai Buruh di Gresik, mereka bilang, mereka belum dipanggil oleh perusahaan. Mereka tetap dirumahkan." (Said Iqbal, via CNBC 2026-02-24)
> "Secara administratif memang tidak ada pemutusan hubungan kerja (PHK). Namun, kondisi di lapangan menunjukkan buruh belum kembali bekerja meski kontrak masih berlaku." (CNBC 2026-02-24)

Catatan: kutipan berasal dari pernyataan serikat pekerja dan liputan langsung. Suara karyawan korban individual sulit diakses karena Reddit/Kaskus memblokir crawler pada sesi ini. Naskah ini "synthesized from 3 berita" yang mengonfirmasi pola penghindaran THR berulang.

## Evidence of volume
- CNBC melaporkan dugaan modus sistemik: sekitar 20-an buruh Mie Sedaap di Gresik mengadu tidak dipanggil kerja jelang Lebaran 2026.
- Kompas.id menyebut masalah penghindaran THR "berulang" tiap tahun, artinya bukan kasus satu perusahaan.
- THR diatur wajib oleh Permenaker, tapi pengawasan lapangan lemah sehingga modus terus muncul tiap Lebaran.

## Existing solutions (and why they fail)
- Lapor ke Posko Pengaduan THR Kemnaker: korban harus tahu ada posko, punya bukti, dan berani lapor (takut diPHK bila lapor).
- Serikat pekerja (KSPI): hanya menjangkau anggota, buruh kontrak informal tidak terorganisir.
- UU/Permenaker: aturan jelas tapi sanksi dan pengawasan lemah, pengusaha hitung risiko lebih murah dari bayar THR.

## Your wedge
Buat bot "Cek THR & Lapor" di WhatsApp: karyawan cukup isi nama perusahaan dan status (masih kerja, dirumahkan, kontrak diputus), bot langsung kasih tahu apakah perusahaan wajib bayar THR, estimasi nominal (persentase dari gaji), dan langkah lapor ke posko Kemnaker dalam bahasa sehari hari. Tambah fitur "anonim" supaya korban tidak takut balas dendam, dan kumpulkan laporan terpusat jadi peta perusahaan nakal tiap Lebaran. Bisa monetisasi lewat layanan konsultasi hukum kerja langganan.

## What people would pay
- Gratis untuk cek & panduan; upsell konsultasi hukum Rp 199.000 per kasus.
- Evidence willingness to pay: THR biasanya jutaan rupiah, Rp 199.000 murah untuk dapat hak. Kantor hukum patok jutaan per kasus.
- Comparable: jasa konsultasi hukum ketenagakerjaan online mematok Rp 250.000 ke atas per sesi.

## Adjacent opportunities
- Bot serupa untuk pesangon, lembur tidak dibayar, dan iuran JHT.
- Bundling asuransi perlindungan hukum bagi buruh kontrak.
- Data peta "perusahaan nakal" bisa dijual ke platform lowongan kerja sebagai warning.

## Time-to-build estimate
- 2 minggu dengan WhatsApp Business API + Google Sheets berisi aturan THR.
- 1 bulan dengan generator estimasi THR dan pengingat jadwal posko Kemnaker.
- 3 bulan untuk produk penuh dengan integrasi pelaporan resmi.
