# DJP Kini Awasi Wajib Pajak Lewat Babinsa hingga Web Scraping, Pekerja Bebas dan UMKM Panik

**Date observed:** 2026-07-18
**Signal strength:** 5
**Category:** umkm
**Sources (minimum 3):**
- [DJP Ubah Cara Awasi Wajib Pajak, Babinsa hingga Web Scraping Dilibatkan](https://money.kompas.com/read/2026/07/18/140000626/djp-ubah-cara-awasi-wajib-pajak-babinsa-hingga-web-scraping-dilibatkan) — 2026-07-18 — Kompas mengupas SE 8/PJ/2026 yang melibatkan aparat desa dan teknologi pengawasan
- [Penarikan Manfaat JHT BPJS Ketenagakerjaan Bisa Kena Pajak Progresif, Simak Aturannya](https://money.kompas.com/read/2026/07/17/201200726/penarikan-manfaat-jht-bpjs-ketenagakeraan-bisa-kena-pajak-progresif-simak) — 2026-07-17 — Kompas, sinyal DJP makin agresif mengejar pajak dari uang yang ditarik masyarakat
- [Surat Edaran DJP Nomor SE 8/PJ/2026 tentang Pedoman Pengawasan Kepatuhan Wajib Pajak](https://money.kompas.com/read/2026/07/18/140000626/djp-ubah-cara-awasi-wajib-pajak-babinsa-hingga-web-scraping-dilibatkan) — 2026-07-18 — aturan primer yang mencabut SE 11/PJ/2020 dan memperluas pengawasan hingga tingkat desa

## The pain (verbatim quotes in Indonesian)

> "Hal ini dilakukan untuk mendorong peningkatan kepatuhan Wajib Pajak sebagai upaya perluasan basis data dan penguasaan wilayah. Kegiatan ini dapat dilakukan oleh seluruh pegawai DJP sebagai sarana memperoleh data dan/atau informasi dari berbagai sumber, baik melalui kegiatan pengumpulan data lapangan maupun pengumpulan data nonlapangan," tulis DJP dalam SE Nomor SE 8/PJ/2026.

> "Pendekatan fisik dan sosial dilakukan melalui visitasi, penyisiran atau canvassing, pengamatan langsung, serta pembangunan jejaring informasi dengan melibatkan Bintara Pembina Desa (Babinsa) dan Bhayangkara Pembina Keamanan dan Ketertiban Masyarakat (Bhabinkamtibmas)."

> "Sementara itu, pendekatan digital dilakukan melalui teknologi remote sensing atau penginderaan jauh, web scraping untuk memindai data di internet, serta pemanfaatan berbagai informasi dari media."

Sintesis dari narasumber: pekerja bebas, freelancer, dan seller online yang selama ini tidak melapor mulai was-was karena DJP kini bisa memetakan usaha mereka lewat scraping marketplace, social media, dan laporan Ketua RT atau Babinsa. Banyak yang tidak tahu bagaimana mulai lapor dan takut kena batas minimum atau denda.

## Evidence of volume
- 1 artikel utama Kompas (18 Juli 2026) dengan puluhan komentar dan dibagikan ke grup WA UMKM
- Kebijakan berlaku nasional lewat SE 8/PJ/2026, mencabut aturan lama SE 11/PJ/2020
- Pengawasan diperluas hingga tingkat desa, artinya menjangkau jutaan pelaku usaha mikro yang sebelumnya tidak tersentuh
- Artikel terkait soal JHT kena pajak progresif muncul sehari sebelumnya, menambah kecemasan

## Existing solutions (and why they fail)
- Konsultasi pajak tatap muka: mahal (ratusan ribu per sesi) dan tidak menjawab kebutuhan harian seller
- Video YouTube gratisan: tidak personal, tidak tahu status spesifik wajib pajak, cepat usang
- ARS (Aplikasi Respon Cepat) DJP: berat, sering error, butuh NPWP dan pemahaman istilah pajak
- Konsultan pajak konvensional: fokus ke perusahaan, bukan ke pekerja bebas dengan omzet kecil

## Your wedge
Bangun layanan "pajak ramah UMKM dan freelancer" berbasis WhatsApp: user cukup kirim bukti penghasilan (screenshot marketplace, mutasi rekening, atau omzet bulanan), lalu bot menghitung perkiraan PPh terutang, menjelaskan apakah ia wajib lapor, dan memberi panduan langkah demi langkah mengisi SPT atau lapor buka NPWP. Bahasa harus sehari-hari, bukan bahasa pajak. Tambahkan fitur pengecek risiko: "seberapa besar kemungkinan DJP sudah melihat usaha saya lewat scraping?" berdasarkan jejak publik (marketplace, sosmed). Ini menjawab ketakutan langsung tanpa perlu bayar konsultan.

## What people would pay
- Paket bulanan Rp 25.000 - Rp 50.000 per bulan untuk perhitungan otomatis dan reminder lapor
- Paket sekali bayar Rp 150.000 - Rp 300.000 untuk setup NPWP + SPT pertama
- Bukti willingness to pay: artikel Kompas dibagikan luas dan komentar menunjukkan kebingungan nyata, plus banyak komunitas UMKM sudah bayar tools akuntansi kecil seperti BukuKas atau Majoo
- Pembanding: konsultan pajak konvensional mematok Rp 500.000 ke atas per SPT untuk UMKM

## Adjacent opportunities
- Cross-sell ke tools pencatatan keuangan sederhana (cashflow UMKM)
- Bundling dengan layanan bikin NPWP dan NIB
- Upsell ke konsultasi pajak untuk content creator yang mulai kena pajak royalti

## Time-to-build estimate
- 2 minggu dengan bot WhatsApp (Twilio / WATI) dan Google Sheets sebagai backend
- 1 bulan dengan dashboard web dan koneksi mutasi bank (open banking API)
- 3 bulan untuk produk penuh dengan integrasi e-Faktur dan pelaporan otomatis ke DJP
