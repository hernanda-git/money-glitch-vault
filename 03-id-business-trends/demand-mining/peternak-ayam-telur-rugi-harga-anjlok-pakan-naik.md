# Peternak Ayam dan Telur Merugi, Harga di Kandang Anjlok tapi Pakan Terus Naik

**Date observed:** 2026-07-10
**Signal strength:** 5
**Category:** farmer
**Sources (minimum 3):**
- [Peternak Ayam Gelar Aksi Mandi Telur di Solo Imbas Harga Anjlok](https://www.detik.com/jateng/bisnis/d-8563133/peternak-ayam-gelar-aksi-mandi-telur-di-solo-imbas-harga-anjlok) — 2026-07-07 — Peternak protes harga ayam broiler cuma Rp 12.500/kg, jauh di bawah HAP Rp 19.500
- [Peternak Teriak Rugi Ratusan Juta Gegara Harga Ayam di Kandang Anjlok](https://finance.detik.com/berita-ekonomi-bisnis/d-8530994/peternak-teriak-rugi-ratusan-juta-gegara-harga-ayam-di-kandang-anjlok) — 2026-06-13 — Per kg ayam rugi Rp 4.000, populasi besar rugi ratusan juta
- [Harga Telur Anjlok, Peternak di Kota Batu Kuras Tabungan untuk Bertahan](https://www.detik.com/jatim/bisnis/d-8555106/harga-telur-anjlok-peternak-di-kota-batu-kuras-tabungan-untuk-bertahan) — 2026-07-01 — Harga telur kandang Rp 19.000/kg, HPP Rp 23.000-Rp 24.000
- [Peternak Kota Batu Ketar-ketir Harga Telur Turun tapi Pakan Terus Naik](https://www.detik.com/jatim/berita/d-8526239/peternak-kota-batu-ketar-ketir-harga-telur-turun-tapi-pakan-terus-naik) — 2026-06 — Pakan naik karena rupiah melemah, peternak kuras tabungan

## The pain (verbatim quotes in Indonesian)
> "Harga telur hari ini bisa menyentuh Rp 16.500 di kalangan peternak, sedangkan harga acuan Rp 19.500. Bahkan kemarin ditetapkan harga acuan baru Rp 24.000, padahal sebelumnya Rp 26.500. Secara logika, kalau harga bahan baku naik, kenapa harga acuan penjualan telur justru diturunkan, kami butuh jawaban." (Chris Handrika Imannuel Raharjo, koordinator aksi, detikJateng 7/7/2026)

> "Kalau telur saja (saat mahal) dioperasi pasar, kenapa jagung (saat mahal) nggak dikerjakan, Ini ada ketimpangan dan ketidakadilan bagi kami." (Chris Handrika, peternak ayam, Solo)

> "Cuman kalau kita ambil di harga segitu (Rp 19 ribu), kita aslinya sudah enggak nutup biaya operasional dan lain-lain. Jadi kalau harga segitu bakul ambil, sudah rugi sekitar Rp 4 ribu-Rp 5 ribu rupiah per kilo. Kalau di bawah itu ya sudah, kerja bakti dan nguras tabungan yang ada." (Sotya Hanief, pemilik ASegg Farm Kota Batu, detikJatim 1/7/2026)

> "Harga masih ke tahan Rp 15.500-16.000/kg. Belum bisa naik lagi. (Kerugian) ratusan juta kalau yang punya populasi besar. Tapi kalau populasi kecil masih puluhan karena per kg-nya masih rugi Rp 4.000." (Asep Saepudin, Permindo, detikFinance 13/6/2026)

## Evidence of volume
- Aksi "mandi telur" massal di Solo (7/7/2026) dan bagi-bagi 1 juta telur gratis di Blitar , aksi protes terbuka peternak rakyat.
- ~70% populasi ayam pedaging dan petelur nasional terkonsentrasi di Pulau Jawa , memicu kelebihan pasokan dan tekanan harga.
- Permindo (Persatuan Peternak Rakyat Mandiri Indonesia) melaporkan HPP broiler meroket ke Rp 21.000-Rp 22.000/kg live bird , harga jual cuma Rp 15.500-Rp 16.000/kg.
- Peternak terpaksa afkir dini: ASegg Farm potong 200 dari 1.000 ayam , pasar kebanjiran daging afkiran.

## Existing solutions (and why they fail)
- Operasi pasar pemerintah: hanya aktif saat harga tinggi ke konsumen , "absen" saat harga jatuh di tingkat peternak (kutipan Chris). Tidak menyerap surplus produsen.
- Harga Acuan Pemerintah (HAP): ditetapkan tapi tidak mengikat pembeli , pengepul tetap beli di bawah HAP. Peternak bilang acuan malah diturunkan saat bahan baku naik.
- Impor pakan satu pintu: diharapkan turunkan harga, tapi bungkil kedelai justru naik Rp 2.000/setengah tahun (kutipan Chris).
- Koperasi/integrator: akses terbatas untuk peternak rakyat kecil, dominan dikuasai integrator besar.

## Your wedge
Bangun alat bantu harga dan manajemen pakan untuk peternak rakyat: (1) chatbot/WA "cek harga kandang harian" per daerah yang aggregasi harga pengepul real-time supaya peternak tahu kapan jual dan tidak rugi; (2) kalkulator HPP otomatis (pakan, DOC, listrik, vaksin) yang kasih alarm "harga jual di bawah HPP"; (3) marketplace langsung peternak ke ritel/warung lokal (potong tengkulak). Bisa dijalankan dengan Google Sheets + WhatsApp bot (WATI/Twilio) tanpa dev berat, lalu scale ke app. Cross-sell: grup beli pakan bareng (group buying) untuk dapat harga grosir.

## What people would pay
- WA bot + kalkulator HPP: Rp 25.000-Rp 50.000/bulan per peternak, atau Rp 500.000/bulan untuk paket kelompok kandang (10-20 peternak).
- Evidence willingness: peternak rela keluar uang untuk "konsultan" dan already bayar retribusi koperasi; satu stok 1.000 ayam rugi Rp 500.000/hari , jadi Rp 50.000/bulan untuk alat cegah rugi sangat murah.
- Comparable: aplikasi manajemen peternakan (eFarma, Si Petelur) ada berbayar tier UMKM, dan layanan info harga harian komoditas sudah jadi model berlangganan di sektor pertanian.

## Adjacent opportunities
- Group buying pakan (sudah ada gap inbox gas-UMKM, bisa diadaptasi ke pakan ternak).
- Asuransi ayam/ternak mikro (kaitan dengan AUTP petani yang kuota dipangkas, sudah ada file terpisah).
- Cold chain / cold storage mini untuk telur di daerah surplus.
- Integrasi ke Program Makan Bergizi Gratis (MBG) sebagai offtake stabil.

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: Google Sheets + WhatsApp bot + form input harga harian.
- 1 bulan dengan custom dev: app kalkulator HPP + peta harga + notifikasi.
- 3+ bulan untuk marketplace lengkap peternak ke ritel.
