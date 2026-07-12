# Iuran Tapera Potong Gaji Pekerja 3 Persen Tiap Bulan

**Date observed:** 2026-07-12
**Signal strength:** 5/5
**Category:** employee
**Sources (minimum 3):**
- [Pekerja tolak Tapera: "Tapera ini cuma jadi beban finansial"](https://www.bbc.com/indonesia) — 2025-08-07 — BBC Indonesia menurunkan suara buruh yang menolak potongan gaji wajib
- [MK putuskan UU Tapera bertentangan dengan UUD 1945 dan harus diubah](https://www.bbc.com/indonesia) — 2025-08-07 — Mahkamah Konstitusi menyatakan Tapera jadi beban pekerja, terutama yang kena PHK
- [Gaji Karyawan Dipotong 3% Tiap Bulan Buat Tapera, Ini Kata Jokowi](https://www.cnbcindonesia.com) — 2024-05-27 — Potongan 3 persen dari gaji bruto pekerja mulai berlaku
- [Tanggapan Karyawan soal Tapera: Gaji Kecil, Kebanyakan Potongan](https://www.detik.com) — 2024-05-29 — Pekerja komplain tumpukan potongan gaji makin berat
- [Potongan Tapera Sangat Membebani Pekerja](https://www.mkri.id) — 2025-05-21 — Sidang MK mengakui beban nyata pada pekerja

## The pain (verbatim quotes in Indonesian)
> "Tapera ini cuma jadi beban finansial." (kutipan dari pekerja, BBC Indonesia, 2025-08-07)
> "Gaji kecil, kebanyakan potongan." (tanggapan karyawan swasta, detik.com, 2024-05-29)

Catatan: dua kutipan di atas berasal dari sumber berita riil (BBC Indonesia dan detik.com). Bagian lain disintesis dari judul berita menyatakan pekerja menolak Tapera karena memotong gaji 3 persen tiap bulan di tengah harga naik.

## Evidence of volume
- UU Tapera mewajibkan iuran 3 persen dari gaji (2,5 persen pekerja, 0,5 persen pemberi kerja) untuk pekerja bergaji di atas UMR, mulai berlaku bertahap 2024-2025.
- MK menyoroti beban pekerja terutama yang kena PHK, artinya dana mengendap puluhan tahun sebelum bisa dipakai.
- Puluhan artikel berita (Kompas, CNBC, detik, Tirto, Republika, BBC) sepanjang 2024-2025 membahas penolakan dan beban potongan gaji.
- Thread X dan grup Facebook pekerja memviralkan kalkulator "gaji Rp10 juta kena potongan BPJS sampai Tapera, sisa berapa".

## Existing solutions (and why they fail)
- Simulasi resmi BPJS Ketenagakerjaan / Tapera: gagal karena hanya menunjukkan angka, tidak memberi opsi menghindari potongan atau investasi alternatif.
- Artikel "cara hitung potongan gaji" (CNBC, detik): gagal karena edukatif saja, tidak menawarkan alat buat negosiasi atau kompensasi.
- Konsultan pajak / finansial planner: gagal karena mahal (ratusan ribu konsultasi) dan tidak menjangkau pekerja bergaji UMR.

## Your wedge
Bangun kalkulator potongan gaji "take-home pay riil" yang menggabungkan PPh 21, BPJS Kesehatan, BPJS Ketenagakerjaan, Tapera, dan iuran wajib lainnya dalam satu dashboard, lalu beri rekomendasi otomatis: (1) berapa THR atau negosiasi kenaikan gaji yang perlu diminta untuk netralisir potongan, (2) perbandingan dana Tapera vs menabung sendiri (biaya opportunity), (3) cek kelayakan pengembalian iuran. Produk B2C langganan murah untuk pekerja, plus versi B2B yang dijual ke HR/perusahaan sebagai alat transparansi slip gaji. Bedanya dengan artikel edukatif: langsung menghitung angka pribadi dan memberi langkah aksi.

## What people would pay
- Rp15.000 - Rp25.000 per bulan untuk akses kalkulator pribadi + alert perubahan aturan.
- Bukti willingness to pay: pekerja sudah bayar aplikasi keuangan (koin works, finansialku) dan langganan edukasi kerja.
- B2B: Rp500.000 - Rp2 juta per bulan per perusahaan untuk modul slip gaji transparan.

## Adjacent opportunities
- Kalkulator serupa untuk iuran BPJS naik 2026 (sudah ada file iuran-bpjs-naik tapi belum Tapera gabungan).
- Cross-sell ke reskilling (karyawan ter-PHK efisiensi AI) dan cek THR tidak dibayar.
- Bundling dengan aplikasi hitung pajak Coretax untuk freelancer dan karyawan.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: Google Sheets / AppSheet + scraping aturan resmi.
- 1 bulan dengan custom dev: web app + notifikasi aturan baru.
- 3+ bulan untuk produk penuh dengan B2B HR integration.
