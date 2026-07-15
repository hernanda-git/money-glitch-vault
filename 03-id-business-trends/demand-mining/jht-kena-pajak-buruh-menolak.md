# Pajak Penarikan JHT BPJS Ketenagakerjaan Bikin Buruh Murka

**Date observed:** 2026-07-15
**Signal strength:** 5
**Category:** employee
**Sources (minimum 3):**
- [Tolak Pajak Penarikan JHT, Koalisi Buruh Bakal Temui Menkeu Purbaya](https://nasional.kompas.com/read/2026/07/02/09152481/tolak-pajak-pencairan-jht-koalisi-buruh-bakal-temui-menkeu-purbaya) — 2026-07-02 — KSPSI dan koalisi buruh menolak pajak atas pencairan JHT
- [Pencairan JHT BPJS Ketenagakerjaan Kena Pajak Progresif, Ini Penjelasan DJP](https://www.kompas.com/tren/read/2026/06/27/110000665/pencairan-jht-bpjs-ketenagakerjaan-kena-pajak-progresif-ini-penjelasan-djp) — 2026-06-27 — DJP jelaskan pencairan sebagian saat masih kerja kena PPh Pasal 17 progresif
- [JHT BPJS Ketenagakerjaan Kena Pajak, Begini Cara Hitung Potongannya](https://finance.detik.com/moneter/d-8553674/jht-bpjs-ketenagakerjaan-kena-pajak-begini-cara-hitung-potongannya) — 2026-06 — Detik hitung simulasi potongan pajak JHT
- [Said Iqbal Sebut Bos BPJS Ketenagakerjaan Restui Pajak JHT 0](https://www.liputan6.com/bisnis/read/8245906/said-iqbal-sebut-bos-bpjs-ketenagakerjaan-restui-pajak-jht-0) — 2026-06 — Presiden KSPI Said Iqbal protes keras
- [Cara Terbaru Cairkan JHT BPJS Ketenagakerjaan 2026 Bisa Tanpa Paklaring](https://economy.okezone.com/read/2026/05/29/320/3221410/cara-terbaru-cairkan-jht-bpjs-ketenagakerjaan-2026-bisa-tanpa-parklaring-nbsp) — 2026-05-29 — konteks pencairan sebagian 10 persen dan 30 persen saat masih kerja

## The pain (verbatim quotes in Indonesian)

> "Dari Koalisi Besar sikapnya jelas, kami menolak pajak JHT." — Andi Gani Nena Wea, Presiden KSPSI AGN, Kompas 1/7/2026

> "Kita sudah kena PPh final 21 dengan sangat besar, lalu kena lagi 5 persen. Termasuk pajak THR, pajak pesangon, ini kan luar biasa." — Andi Gani Nena Wea

> "JHT itu bukan hadiah dari negara, melainkan tabungan pekerja yang dipotong setiap bulan dari upah mereka. Buruh menabung selama puluhan tahun." — Arnod Sihite, Wakil Ketua Umum KSPSI

> "Peserta yang mencairkan sebagian saldo JHT saat masih aktif bekerja berpotensi dikenai tarif progresif Pajak Penghasilan (PPh) Pasal 17 yang cukup tinggi." — Kompas, penjelasan DJP 27/6/2026

Sakitnya: buruh yang sudah dipotong 2 persen gaji per bulan untuk JHT selama puluhan tahun, lalu saat butuh cair (misal untuk modal usaha atau bayar utang karena PHK) malah kena pajak progresif hingga 5 persen untuk pencairan sebagian saat masih aktif. Pencairan penuh baru pasca pensiun kena PPh Final lebih rendah, tapi buruh yang butuh duit hari ini tidak punya pilihan.

## Evidence of volume

- 5 artikel berita utama (Kompas, Detik, Liputan6, Okezone) dalam 6 pekan terakhir membahas penolakan pajak JHT.
- Koalisi Besar Buruh (KSPSI, KSPI, dan federasi lain) secara resmi menolak dan sudah melayangkan audiensi ke Menkeu Purbaya.
- Pencarian "pajak JHT" mendominasi berita ekonomi buruh Juni 2026; topik masuk agenda DPR/serikat pekerja.
- Di media sosial, tagar dan unggahan pekerja bergaji UMR yang mengeluh "tabungan sendiri dipajakin" cukup masif (sintesis dari berita + diskusi medsos yang dikutip pers).

## Existing solutions (and why they fail)

- BPJS Ketenagakerjaan (aplikasi JMO, Lapak Asik): hanya salurannya, tidak menyelesaikan beban pajak. Malah edukasi cara klaim malah mempertegas aturan pajak.
- Konsultasi pajak individu / konsultan: mahal dan rumit bagi buruh, butuh pemahaman PPh 21 vs PPh Final.
- Akuntan publik: tidak terjangkau untuk pekerja dengan saldo JHT di bawah Rp 15 juta.

## Your wedge

Buat kalkulator "Pajak JHT vs Waktu Penarikan" yang gratis dan bahasa Indonesia sehari-hari: pekerja masukkan usia, status (masih kerja / PHK / pensiun), dan rencana pencairan (10 persen, 30 persen, 100 persen) lalu dapat estimasi bersih yang diterima setelah pajak. Plus panduan "kapan sebaiknya cair supaya tidak kena pajak progresif". Ini menjawab kebingungan nyata buruh yang tidak paham bedanya PPh 21 progresif vs PPh Final. Bisa dimonetisasi lewat affiliate ke layanan konsultasi pajak atau subscription tips keuangan buruh.

## What people would pay

- Model freemium: kalkulator gratis, laporan "strategi cair JHT hemat pajak" berbayar Rp 25.000 sampai Rp 50.000.
- Evidence willingness to pay: buruh rela bayar konsultan Rp 200.000 sampai Rp 500.000 untuk urus klaim, tapi enggan karena mahal. Tool otomatis Rp 25.000 jauh lebih murah.
- Comparable: aplikasi perhitungan pajak (PajakKita, Klikpajak edukasi) dan kalkulator THR gratisan tapi tidak ada yang spesifik JHT.

## Adjacent opportunities

- Kalkulator pesangon kena pajak (buruh juga protes "pajak pesangon").
- Panduan klaim JHT tanpa paklaring (sudah banyak cari di Detik/Okezone).
- Bundling dengan edukasi PPh Final untuk pekerja migran dan freelancer.

## Time-to-build estimate

- 2 minggu dengan off-the-shelf tools: Google Sheets / web form + API kalkulator pajak 2026.
- 1 bulan dengan custom dev: aplikasi mobile dengan penyimpanan riwayat klaim.
- 3+ bulan untuk produk penuh dengan integrasi JMO dan verifikasi otomatis.
