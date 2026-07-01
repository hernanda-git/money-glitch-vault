# Nelayan Untung di Atas Kertas, Tertekan di Lapangan: Biaya Produksi Makan Pendapatan

**Date observed:** 2026-07-01
**Signal strength:** 4/5
**Category:** farmer
**Sources (minimum 3):**
- [Nelayan Untung di Atas Kertas, Tertekan di Lapangan](https://suhana.web.id/2026/06/04/nelayan-untung-di-atas-kertas-tertekan-di-lapangan/) , 2026-06-04 , Analisis NTN bulanan: paradoks kesejahteraan nelayan di angka 107,48 tapi tekanan biaya terus meningkat
- [Biaya Naik Lebih Cepat, Nilai Tukar Petani Turun di Juni 2026](https://money.kompas.com/read/2026/07/01/140700426/biaya-naik-lebih-cepat-nilai-tukar-petani-turun-di-juni-2026) , 2026-07-01 , BPS: NTP turun tipis 0,06% di Juni 2026, biaya produksi naik lebih cepat dari harga jual
- [Nilai Tukar Petani Naik, Kesejahteraan Nelayan Justru Turun](https://money.kompas.com/read/2026/06/03/111200626/nilai-tukar-petani-naik-hampir-2-persen-pada-mei-2026-kesejahteraan-nelayan) , 2026-06-03 , NTN turun 0,47% di Mei 2026, biaya nelayan naik lebih cepat dari pendapatan

## The pain (verbatim quotes in Indonesian)
> "Di satu sisi, indikator makro menunjukkan bahwa kesejahteraan nelayan masih berada pada level yang relatif baik. Nilai Tukar Nelayan (NTN) tercatat sebesar 107,48, jauh di atas angka 100 yang secara teoritis menandakan bahwa pendapatan yang diterima nelayan masih lebih besar dibanding pengeluaran yang harus mereka tanggung. Namun di sisi lain, data juga memperlihatkan gejala yang perlu diwaspadai: kenaikan pendapatan nelayan mulai melambat, sementara biaya hidup dan biaya produksi terus meningkat." , Suhana/Analisis Ekonomi Kelautan, 4 Juni 2026

> "NTNP (Nilai Tukar Nelayan dan Pembudidaya Ikan) turun 0,64 persen, NTN turun 0,47 persen, dan NTPi turun lebih dalam sebesar 0,90 persen. Fenomena tersebut menunjukkan bahwa sektor perikanan sedang bergerak berlawanan arah dengan sebagian besar subsektor pertanian lainnya." , BPS via Suhana, 4 Juni 2026

> "Penurunan tersebut terjadi karena kenaikan indeks harga yang diterima nelayan hanya sebesar 0,03 persen, lebih rendah dibandingkan kenaikan indeks harga yang dibayar nelayan yang mencapai 0,51 persen. Dengan kata lain, biaya yang harus dikeluarkan nelayan meningkat lebih cepat dibandingkan tambahan pendapatan yang mereka peroleh dari hasil tangkapan." , BPS/Kompas, 3 Juni 2026

## Evidence of volume
- NTN bulanan menunjukkan tren penurunan sejak Maret 2026
- Biaya bahan bakar, es batu, dan peralatan tangkap terus naik
- Harga ikan di tingkat nelayan naik sangat lambat (0,03% di Mei 2026)
- Subsektor perikanan bergerak berlawanan arah dengan pertanian secara umum
- Data BPS menunjukkan hanya subsektor tanaman pangan yang mengalami kenaikan NTP di Juni

## Existing solutions (and why they fail)
- Subsidi BBM nelayak dari pemerintah , birokrasi rumit, nelayan kecil sering tidak terdaftar
- Program asuransi nelayan , klaim sulit, premi tidak terjangkau untuk nelayan tradisional
- Koperasi nelayan , banyak yang bermasalah tata kelola, some have collapsed (kasus Koperasi Desa Merah Putih)
- Harga acuan ikan dari KKP , tidak efektif karena tengkulak masih mendominasi rantai nilai

## Your wedge
Bangun sistem manajemen biaya operasional nelayan berbasis mobile yang sederhana. Nelayan tidak butuh spreadsheet rumit, mereka butuh: (1) tracking pengeluaran harian (BBM, es, umpan, sewa perahu) vs pendapatan dari hasil tangkapan, (2) alerts otomatis saat biaya mulai melebihi pendapatan, (3) data historis untuk negosiasi harga dengan tengkulak, (4) akses ke informasi harga pasar real-time. Model freemium: basic gratis, premium Rp25.000/bulan dengan fitur lengkap. initData dari 50 nelayan di pelabuhan Muara Angke.

## What people would pay
- Rp25.000-50.000/bulan untuk fitur premium (setara harga 1 kg ikan kembung)
- Nelayan tradisional sudah bayar Rp100.000-300.000/bulan untuk sewa perahu, jadi Rp25.000 sangat terjangkau
- Koperasi nelayan bisa jadi channel distribusi dengan potongan Rp5.000/nelayan/bulan
- Comparable: Aplikasi "Tangkapan" untuk nelayan di Filipina charge $2/bulan

## Adjacent opportunities
- Marketplace ikan langsung dari nelayan ke konsumen (hilangkan tengkulak)
- Sistem pemesanan es batu dan bahan bakar yang lebih efisien
- Jaringan informasi cuaca dan lokasi ikan untuk nelayan kecil
- Asuransi mikro berbasis komunitas nelayan

## Time-to-build estimate
- 2 minggu dengan MVP: form mobile sederhana untuk catat pengeluaran/pendapatan
- 1 bulan dengan custom dev: dashboard analytics, alerts, integrasi harga pasar
- 3+ bulan untuk full product: marketplace, asuransi mikro, jaringan informasi
