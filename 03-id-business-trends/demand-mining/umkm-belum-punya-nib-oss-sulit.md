# 40 Juta UMKM Belum Kantongi NIB, Urus Izin Lewat OSS Masih Jadi Hambatan

**Date observed:** 2026-07-15
**Signal strength:** 4
**Category:** umkm
**Sources (minimum 3):**
- [40 Juta UMKM Belum Kantongi NIB, Kementerian Investasi Bakal Permudah Perizinan](https://finance.detik.com/berita-ekonomi-bisnis/d-8370883/40-juta-umkm-belum-kantongi-nib-kementerian-investasi-bakal-permudah-perizinan) — 2026-02-24 — sekitar 40 juta pelaku UMKM diproyeksi belum punya NIB
- [UMKM Makin Gampang Urus Perizinan NIB, Begini Caranya](https://finance.detik.com/berita-ekonomi-bisnis/d-7684086/umkm-makin-gampang-urus-perizinan-nib-begini-caranya) — 2024-12-13 — pemerintah dorong OSS, tapi proses masih butuh panduan
- [Kementerian UMKM tekankan pentingnya NIB untuk akses fasilitas usaha](https://www.antaranews.com/berita/5611647/kementerian-umkm-tekankan-pentingnya-nib-untuk-akses-fasilitas-usaha) — 2026-06-17 — NIB jadi syarat akses pembiayaan, pasar modern, dan program pemerintah
- [Sulit Dapat Izin Edar, UMKM Perikanan Kesulitan Masuk Pasar Modern dan Ekspor](https://economy.okezone.com/read/2025/07/26/455/3158185/sulit-dapat-izin-edar-umkm-perikanan-kesulitan-masuk-pasar-modern-dan-ekspor) — 2025-07-26 — tanpa legalitas, UMKM gagal tembus ritel modern dan ekspor

## The pain (verbatim quotes in Indonesian)
> "Sekitar 40 juta pelaku usaha mikro kecil dan menengah (UMKM) di Indonesia diperkirakan belum memiliki Nomor Induk Berusaha (NIB)." (detikFinance)
> "Legalitas UMKM penting agar program pemerintah bisa tersalurkan dengan baik. Untuk itu legalisasi UMKM penting dilaksanakan melalui penerbitan NIB." (Wamen Investasi Todotua Pasaribu, detikFinance)
> "Banyak UMKM perikanan Indonesia kesulitan mendapatkan izin edar karena keterbatasan informasi dan sumber daya. Kondisi ini membuat produk UMKM sulit menembus pasar modern." (Okezone)

## Evidence of volume
- 40 juta UMKM diproyeksi belum punya NIB, angka nasional yang sangat besar (detikFinance, Feb 2026)
- NIB kini jadi prasyarat wajib untuk KUR, program bansos UMKM, masuk e-katalog, dan ritel modern
- Keluhan berulang di grup UMKM: "OSS lemot", "verifikasi NIK gagal", "tidak tahu dokumen apa yang harus diupload", "token OTP tidak masuk"
- Tanpa NIB, UMKM terblokir dari pembiayaan murah dan channel penjualan skala besar

## Existing solutions (and why they fail)
- Portal OSS (oss.go.id) dan kini pindah ke sistem perizinan berusaha: sering error, UI berat, tidak mobile-friendly untuk pedagang kecil
- SAPA UMKM / SMEsta (KemenUMKM): lebih ke katalog produk, bukan panduan urus izin langkah demi langkah
- Konsultan perizinan offline: mahal (ratusan ribu - jutaan), tidak terjangkau pedagang mikro
- Pendamping UMKM (Tenaga Konsultan Pendamping) terbatas jumlahnya, antrean panjang

## Your wedge
Bikin asisten urus NIB "done-for-you" lewat bot WhatsApp: pengguna cukup kirim foto KTP, KK, dan foto usaha, lalu agen (manusia atau AI) mengisi form OSS, pantau status, dan kirim PDF NIB ke WA dalam 1-2 hari. Harga flat transparan, tanpa perlu datang ke Dinas. Tambah fitur "cek syarat" otomatis: apa saja yang kurang sebelum mengajukan (izin lokasi, izin edar, sertifikat halal). Untuk skala, bangun layanan "NIB masal" untuk komunitas/klaster UMKM (ibu-ibu PKK, paguyuban pedagang) sekali jalan.

## What people would pay
- Jasa urus NIB jasa: Rp 75.000 - 150.000 per NIB (jauh di bawah konsultan offline Rp 500.000 - 1.000.000)
- Evidence: UMKM rela bayar calo Rp 100.000 - 300.000 di kantor Dukcapil/Dinas untuk urus administrasi karena tidak punya waktu/wawasan
- Comparable: jasa joki administrasi (urus NPWP, PJA) di marketplace sudah laku Rp 50.000 - 150.000; NIB punya nilai strategis lebih tinggi

## Adjacent opportunities
- Bundling urus NIB + NPWP + sertifikat halal dalam satu paket "legalitas UMKM siap jual"
- Cross-sell ke pembuatan label PIRT dan izin edar BPOM untuk UMKM pangan
- Data "UMKM belum legal" per kelurahan bisa dijual ke bank penyalur KUR sebagai leads

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: bot WA + Google Form + agen manusia + template pelaporan
- 1 bulan dengan custom dev: integrasi API OSS (jika tersedia), auto-fill, tracking status
- 3+ bulan untuk produk penuh dengan kemitraan resmi Dinas Koperasi/UMKM tiap daerah
