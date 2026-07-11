# Warga Miskin Terblokir Layanan Kesehatan Gratis karena Status Desil Salah

**Date observed:** 2026-07-11
**Signal strength:** 4/5
**Category:** other
**Sources (minimum 3):**
- [Ubah Status Desil Demi Layanan Kesehatan Gratis, Warga Aceh Harus Tunggu 3 Bulan](https://regional.kompas.com/read/2026/05/05/223049778/ubah-status-desil-demi-layanan-kesehatan-gratis-warga-aceh-harus-tunggu-3) — 2026-05-05 — warga tak mampu kehilangan akses layanan gratis gara gara status desil 8-10
- [Kaget Desil Tak Sesuai Realita Berimbas ke BPJS, Warga Bener Meriah Ajukan Perubahan Data](https://regional.kompas.com/read/2026/05/04/122249578/rs-swasta-di-aceh-dilema-terapkan-layanan-kesehatan-gratis-berbasis-desil) — 2026-05-04 — warga ajukan perubahan data setelah desil tak sesuai kenyataan
- [RS Swasta di Aceh Dilema Terapkan Layanan Kesehatan Gratis Berbasis Desil](https://regional.kompas.com/read/2026/05/04/122249578/rs-swasta-di-aceh-dilema-terapkan-layanan-kesehatan-gratis-berbasis-desil) — 2026-05-04 — rumah sakit bingung jalankan aturan berbasis desil
- [Mau Kontrol Pakai BPJS Kesehatan? Cek Aturan Baru Juni 2026](https://www.beritasatu.com/nasional/3001071/mau-kontrol-pakai-bpjs-kesehatan-cek-aturan-baru-juni-2026) — 2026-06-01 — aturan baru kontrol BPJS semakin ketat

## The pain (verbatim quotes in Indonesian)
> "Syaratnya, dokumen kartu penduduk dan kartu keluarga, surat keterangan tidak mampu, permohonan perbaikan data ke kepala desa, setelah itu pemerintah desa akan membuat musyawarah khusus desa untuk memvalidasi data yang telah diberikan."

> "Pembaruan data SIKS-NG hanya bisa dilakukan tanggal 1-11 setiap bulannya. Setelah itu baru difinalisasi oleh operator Dinas Sosial, lalu dilakukan perangkingan oleh Kementerian Sosial RI dan Badan Pusat Statistik (BPS)."

> "Status bukan ditentukan daerah, nanti dari data yang diunggah ke aplikasi SIKS-NG, keluarlah status desil hasil finalisasi Kementerian Sosial dan Badan Pusat Statistik (BPS) RI. Sejauh ini, tiga bulan baru berubah status desilnya."

> "Kami harap masyarakat memahami kondisi ini."

## Evidence of volume
- Ratusan warga di Aceh (Lhokseumawe, Bener Meriah, Aceh Utara) sedang mengajukan perubahan status desil di tingkat desa sejak Mei 2026
- Pergub Aceh Nomor 2 Tahun 2026 mewajibkan pembiayaan JKA berbasis desil, desil 8-10 wajib bayar mandiri, berlaku sejak 1 Mei 2026
- Program Cek Kesehatan Gratis nasional ditargetkan jangkau 135 juta warga, artinya basis data desil makin menentukan akses
- Keluhan serupa muncul di media nasional soal "desil tak sesuai realita" berimbas ke BPJS di berbagai daerah

## Existing solutions (and why they fail)
- SIKS-NG (Sistem Informasi Kesejahteraan Sosial Next Generation): aplikasi resmi tapi pembaruan cuma boleh tanggal 1-11 tiap bulan dan butuh musyawarah desa, verifikasi BPS, jadi prosesnya 3 bulan
- Layanan Dinsos setempat: warga harus datang bawa KK, KTP, surat keterangan tidak mampu, belum tentu paham alur
- Konsultan administrasi desa: ada tapi tidak terdigitalisasi, tidak bisa dilacak status pengajuan

## Your wedge
Bangun asisten digital "Cek & Perbaiki Status Desil" yang membantu warga dan pendamping desa (PKH, kader) mengecek desil dari NIK, mendapat panduan dokumen yang tepat per kabupaten, dan melacak status pengajuan perubahan data secara real time. Produk ini bisa jadi chatbot WhatsApp berbasis bahasa daerah yang menarik data dari portal publik dan mengingatkan warga kapan jendela pengajuan (1-11) sudah buka. Sisi B2B: jual ke Dinsos atau opsir desa sebagai dashboard pelacakan perubahan data agar antrean tidak numpuk di akhir bulan. Ini menjawab friksi utama, yaitu warga tidak tahu statusnya salah sampai butuh berobat.

## What people would pay
- B2C: gratis untuk warga (model amal /CSR), monetisasi lewat referral asuransi murah atau donasi
- B2G/B2B: Rp 5 juta sampai Rp 15 juta per desa per tahun untuk dashboard pelacakan, atau kontrak Dinsos tingkat kabupaten
- Bukti willingness to pay: pemda sudah keluarkan anggaran sosialisasi dan bimbingan teknis SIKS-NG tiap tahun, artinya ada anggaran yang bisa dialihkan ke tools yang lebih efisien

## Adjacent opportunities
- Asuransi kesehatan mikro untuk warga desil 8-10 yang terpaksa bayar mandiri
- Navigasi BPJS untuk pekerja informal (lihat juga file bpjs-pbpu-beban-keluarga-informal)
- Layanan pendampingan administrasi kependudukan lain (KK, KIP, bansos) dalam satu chatbot

## Time-to-build estimate
- 2 minggu dengan WhatsApp API dan Google Sheets sebagai backend pelacakan
- 1 bulan dengan integrasi data portal publik dan dashboard desa
- 3 bulan lebih untuk produk SaaS lintas provinsi dengan kontrak pemda
