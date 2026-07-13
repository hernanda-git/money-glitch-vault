# Pekerja Koperasi Desa Merah Putih Gelisah Gaji dan Kontrak Tak Jelas

**Date observed:** 2026-07-13
**Signal strength:** 4/5
**Category:** employee
**Sources (minimum 3):**
- [Omzet harian Koperasi Merah Putih di Bojonegoro ditaksir Rp100.000, pengamat prediksi 'KDMP tidak akan bertahan lebih dari satu tahun'](https://www.bbc.com/indonesia/articles/cq51xj41j23o) — 2026-07-10 — puluhan gerai tutup protes ketidakjelasan upah dan kontrak
- [Bos Agrinas Tanggapi Isu Gaji Pengelola Koperasi Merah Putih](https://bisnis.tempo.co/read/2113159/bos-agrinas-tanggapi-isu-gaji-pengelola-koperasi-merah-putih) — 2026-07-11 — direktur PT Agrinas akui sedang evaluasi sistem pengupahan
- [ICW: Potensi Rente Pikap Koperasi Desa Setara Subsidi KPR](https://bisnis.tempo.co/read/2113133/icw-potensi-rente-pikap-koperasi-desa-setara-subsidi-kpr) — 2026-07-11 — pengamat soroti tata kelola KDMP

## The pain (verbatim quotes in Indonesian)
> "Pada malam hari sebelum penutupan [ada pertemuan], itu sebenarnya bukan tutup, hanya menggertak Agrinas untuk memberikan kejelasan."
> "Masalah lain, tambah Sugianto, para pekerja koperasi juga mengeluh belum mendapatkan kontrak kerja."
> "Awalnya saya sudah curiga, ini (pekerja) kok mudah diterima, terus tidak ada semacam kontrak kerja... Namanya kerja, biasanya ada semacam negosiasi soal gaji, jaminan BPJS, kan seperti itu."
> "Kalau saya enggak ikuti, tapi ini proyek strategis... Tapi kalau mengikuti, saya tahu alurnya enggak normal."

## Evidence of volume
- 54 gerai KDMP di Bojonegoro sempat tutup serentak pada Jumat pekan lalu sebagai protes atas upah dan kontrak (per BBC, diakui Ketua KDMP Bojonegoro)
- 1.061 gerai KDMP sudah beroperasi di Jawa Tengah dan Jawa Timur per Juli 2026, target 30.000 gerai pada Agustus 2026, artinya jutaan pekerja berpotensi terdampak pola pengupahan serupa
- Gaji pekerja dilaporkan bervariasi antara Rp76.000 hingga Rp1,9 juta per bulan, jauh di bawah UMK Bojonegoro 2026 sebesar Rp2.685.983
- Pengamat Ridwan Mahmudi (Strategy Cita Semesta) prediksi KDMP tidak akan bertahan lebih dari satu tahun karena tidak ada studi kelayakan

## Existing solutions (and why they fail)
- PT Agrinas Pangan Nusantara (BUMN pengelola): berjanji evaluasi sistem pengupahan, tapi per 11 Juli 2026 belum memberi kepastian kapan gaji disamakan UMK atau kapan kontrak kerja diterbitkan
- Kementerian Koperasi: hanya menyebut "ada target omset disesuaikan daerah" tanpa rincian, tidak menjawab keluhan pekerja secara langsung
- Serikat pekerja informal: tidak ada, karena pekerja KDMP direkrut via WhatsApp tanpa aturan formal dan tanpa BPJS

## Your wedge
Buat layanan "kalkulator hak kerja dan template kontrak" gratis untuk pekerja KDMP dan program padat karya pemerintah daerah: input lokasi, UMK setempat, hari kerja, lalu keluar estimasi gaji minimum yang wajib dibayar plus draf kontrak kerja standar (termasuk jaminan BPJS). Kembangkan juga bot WhatsApp pelaporan: pekerja cukup ketik "gaji saya RpX, hari kerja Y" maka bot memberi tahu apakah di bawah UMK dan cara mengadu ke Disnaker. Karena rekrutmen KDMP justru berjalan lewat WhatsApp, kanal yang sama adalah tempat paling masuk akal untuk edukasi dan pelaporan. Produk ini bisa di-white-label ke pemda atau serikat pekerja lain yang menampung program padat karya.

## What people would pay
- B2G (pemda / dinas tenaga kerja): Rp5 juta sampai Rp15 juta per bulan untuk dashboard pemantauan upah program padat karya
- B2B (koperasi / BUMDes): Rp200.000 sampai Rp500.000 per gerai per bulan untuk modul hitung gaji otomatis
- Evidence willingness to pay: pemda sudah mengalokasikan Dana Desa miliaran untuk KDMP, anggaran konsultansi tata kelola pasti tersedia. ICW dan pengamat sudah minta audit, artinya ada dorongan politik untuk transparansi
- Comparable: platform HR payroll lokal (Mekari, Talenta, Bob) mematok Rp50.000 sampai Rp100.000 per karyawan per bulan, tapi tidak menyasar pekerja informal program pemerintah

## Adjacent opportunities
- Modul BPJS Kesehatan otomatis untuk pekerja kontrak pendek (lihat gap inbox desil / dormant)
- Dashboard transparansi omzet koperasi desa untuk kepala desa (sudah ada keluhan stok barang susut)
- Escrow gaji untuk proyek pemerintah agar pekerja tidak mangkrak seperti kasus tukang bangunan (lihat inbox escrow-upah)

## Time-to-build estimate
- 2 minggu dengan tools off-the-shelf (bot WhatsApp + Google Sheets / Airtable sebagai backend hitung UMK)
- 1 bulan dengan custom dev (multi-gerai dashboard + pelaporan Disnaker)
- 3+ bulan untuk produk SaaS penuh dengan white-label pemda
