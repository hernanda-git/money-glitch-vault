# Antrean BBM di Sumatra dan Panic Buying Pertalite Usai Harga Pertamax Naik

**Date observed:** 2026-07-18
**Signal strength:** 5
**Category:** other
**Sources (minimum 3):**
- [Antrean BBM Sumatra, Krisis Logistik atau Lonjakan Konsumsi?](https://ekonomi.bisnis.com/read/20260718/44/1988948/antrean-bbm-sumatra-krisis-logistik-atau-lonjakan-konsumsi) — 2026-07-18 — Bisnis melaporkan antrean berjam-jam di SPBU Sumatra
- [Harga Pertamax Naik, Konsumen Serbu Pertalite](https://ekonomi.bisnis.com/read/20260717/44/1988820/harga-pertamax-naik-konsumen-serbu-pertalite) — 2026-07-17 — Bisnis, konsumsi Pertalite melonjak 9,4 persen usai Pertamax naik ke Rp 16.250 per liter
- [Antrean BBM di Medan Terurai, BPH Migas Sebut Bukan karena Kuota](https://money.kompas.com/read/2026/07/18/154733226/antrean-bbm-di-medan-terurai-bph-migas-sebut-bukan-karena-kuota-lalu-apa) — 2026-07-18 — Kompas, warga Medan mengantre berjam-jam meski stok disebut aman
- [Pertamina Ungkap Penyebab Antrean BBM di Medan](https://www.cnnindonesia.com/ekonomi/20260717135909-85-1381859/pertamina-ungkap-penyebab-antrean-bbm-di-medan) — 2026-07-17 — CNN, Pertamina akui panic buying dan shifting ke BBM bersubsidi

## The pain (verbatim quotes in Indonesian)

> "Di tengah klaim pemerintah dan PT Pertamina Patra Niaga bahwa stok bahan bakar minyak (BBM) berada dalam kondisi aman, masyarakat tetap harus mengantre berjam-jam untuk memperoleh Pertalite maupun Solar bersubsidi."

> "Pada beberapa waktu terakhir masih terjadi antrean dan pembelian secara berlebihan atau panic buying di beberapa wilayah di Sumatra secara umum, yang juga dipengaruhi oleh kenaikan ataupun shifting dari konsumsi BBM kepada BBM bersubsidi, yaitu Pertalite dan Solar," ujar Wakil Direktur Utama Pertamina Patra Niaga Taufik Aditiyawarman.

> "Berdasarkan data Pertamina, rerata penyaluran Pertalite pada Juli 2026 meningkat 9,4 persen atau naik 7.129 kiloliter (kl)/hari dibandingkan dengan rerata normal."

Sintesis dari narasumber: ojol, buruh harian, dan warga kecil di Sumatra kehilangan jam kerja karena antre berjam-jam. Pengemudi ojol dan angkot terpaksa beli di tingkat eceran lebih mahal karena tak sempat antre.

## Evidence of volume
- Antrean terjadi di "beberapa wilayah di Sumatra secara umum" (per Pertamina di rapat Komisi XII DPR)
- Penyaluran Pertalite naik 9,4 persen, porsi konsumsi Pertalite naik jadi 80,3 persen dari total bensin
- Pertamina terpaksa tambah armada tangki 35 persen dan operasional 24 jam di Medan
- Antrean sempat terjadi di Medan, Sumut, Riau, dan wilayah Sumbagut lainnya

## Existing solutions (and why they fail)
- Aplikasi MyPertamina: hanya buat verifikasi subsidi, tidak tahu stok atau antrean SPBU terdekat
- Info SPBU via Google Maps: tidak real-time, tidak menunjukkan estimasi antrean
- Grup WA warga: tersebar, tidak terstruktur, info simpang siur
- Call center Pertamina: sulit dihubungi saat krisis lokal

## Your wedge
Buat peta ketersediaan BBM real-time berbasis laporan warga (crowdsource) lewat bot WhatsApp: pengemudi cukup kirim "SPBU X antrean 20 menit" atau foto antrean, lalu peta memperlihatkan SPBU sekitar yang relatif sepi. Tambahkan fitur notifikasi "SPBU dekatmu baru isi ulang" dan estimasi waktu tunggu. Untuk ojol dan angkot, ini menyelamatkan jam kerja. Model bisnis: gratis untuk warga, berlangganan untuk armada ojol/perusahaan logistik yang butuh rute irit BBM.

## What people would pay
- Gratis untuk pengemudi individu (data crowdsource)
- Rp 30.000 - Rp 75.000 per bulan untuk armada ojol atau perusahaan logistik (akses rute hemat BBM dan alert)
- Bukti willingness to pay: ojol dan angkot sangat sensitif terhadap waktu antre, sudah bayar tools like Movinga atau dashboard operasional
- Pembanding: aplikasi navigasi berbayar seperti yang dipakai driver logistik

## Adjacent opportunities
- Bundling dengan tracker harga eceran BBM ilegal di daerah
- Cross-sell ke komunitas ojol untuk manajemen setoran harian
- Data agregat antrean bisa dijual ke pemda atau BPH Migas untuk pemetaan distribusi

## Time-to-build estimate
- 2 minggu dengan bot WhatsApp + peta sederhana (Leaflet) dan spreadsheet
- 1 bulan dengan notifikasi push dan verifikasi foto otomatis
- 3 bulan untuk produk penuh dengan API distribusi Pertamina dan dashboard pemda
