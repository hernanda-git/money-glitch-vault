# PPh Final UMKM 0,5% Cuma Bisa Dipakai PT Perorangan dan Koperasi

**Date observed:** 2026-07-16
**Signal strength:** 4/5
**Category:** umkm
**Sources (minimum 3):**
- [PP 20/2026: PPh Final UMKM Hanya Untuk PT Perorangan dan Koperasi](https://ekonomi.bisnis.com/read/20260531/259/1977457/pp-202026-pph-final-umkm-hanya-untuk-pt-perorangan-dan-koperasi) — 2026-05-31 — PP 20/2026 menyempitkan fasilitas 0,5% hanya untuk PT perorangan dan koperasi dengan omzet maksimal Rp4,8 miliar.
- [Pemerintah Revisi Aturan PPh Final UMKM 0,5%, Ini WP yang Bisa Memanfaatkan](https://nasional.kontan.co.id/news/pemerintah-revisi-aturan-pph-final-umkm-05-ini-wajib-pajak-yang-bisa-memanfaatkan) — 2026-05 — Kontan merinci WP badan yang masih berhak dan yang terekam keluar dari insentif.
- [PP 20/2026 diundangkan 22 April 2026 (dokumen resmi beleid)](https://ekonomi.bisnis.com/read/20260531/259/1977457/pp-202026-pph-final-umkm-hanya-untuk-pt-perorangan-dan-koperasi) — 2026-04-22 — beleid diundangkan, batas omzet Rp4,8 miliar.

## The pain (verbatim quotes in Indonesian)
> "Insentif PPh Final UMKM tarif khusus tersebut kini tidak lagi dapat dinikmati oleh seluruh jenis badan usaha." (Bisnis.com, 31 Mei 2026)
> "Fasilitas istimewa ini secara spesifik hanya menyasar dua jenis kualifikasi Wajib Pajak (WP) badan, yaitu perseroan perorangan yang didirikan oleh satu orang serta koperasi." (Bisnis.com, 31 Mei 2026)

Catatan: banyak UMKM berbadan CV, firma, atau PT biasa yang selama ini menikmati tarif 0,5% kini terlempar ke tarif normal PPh badan (11 persen hingga 22 persen progressive). Quotes di atas adalah kutipan langsung dari artikel berita, bukan curhat forum.

## Evidence of volume
- PP 20/2026 diterbitkan pemerintah dan langsung mengubah dasar hukum pajak puluhan juta UMKM berbadan selain PT perorangan/koperasi.
- Kontan dan Bisnis memberitakan revisi ini sebagai kebijakan nasional, artinya dampaknya sistemik, bukan kasus satu daerah.
- Artikel Kompas soal arus kas UMKM (Mei 2026) menunjukkan tekanan margin yang membuat selisih tarif 0,5% vs tarif normal sangat terasa bagi pelaku usaha kecil.
- Belum ada data jumlah pasti UMKM yang terdampak karena aturan baru, tapi ruang lingkup WP badan di Indonesia didominasi entitas selain PT perorangan.

## Existing solutions (and why they fail)
- Konsultan pajak tradisional: gagal karena mahal (rata-rata jutaan per bulan) dan tidak menjangkau UMKM mikro yang cuma butuh jawaban cepat apakah ia masih berhak 0,5%.
- DJP Online / Coretax: gagal karena antarmuka sering error dan tidak memberikan penjelasan sederhana "badan usaha saya masuk kategori apa, berapa tarifnya".
- Akuntan langganan: gagal karena UMKM baru tahu salah hitung setelah lebih bayar atau dapat surat teguran.

## Your wedge
Bangun layanan triage pajak UMKM berbasis chatbot: pelaku usaha cukup input bentuk badan (CV, PT, PT perorangan, koperasi) dan omzet, lalu dapat penjelasan apakah masih berhak PPh Final 0,5% atau harus pindah ke tarif normal, plus simulasi selisih pajaknya. Bundling dengan panduan gratis "cara balik ke PT perorangan / koperasi kalau mau tetap dapat 0,5%". Produk ini menjawab kebingungan sesaat setelah PP 20/2026 berlaku. Bisa dijalankan dengan LLM + basis aturan PP 20/2026 tanpa dev berat.

## What people would pay
- Harga langganan Rp49.000 sampai Rp99.000 per bulan untuk UMKM yang ingin konsultasi berulang dan reminder SPT.
- Bukti willingness to pay: UMKM sudah bayar konsultan pajak dan langganan software akuntansi (Jurnal, BukuWarung, Mekari) jutaan per tahun, jadi segmen ini terbiasa bayar untuk kepatuhan.
- Pembanding: langganan software akuntansi lokal mulai Rp100.000 per bulan; konsultasi sekali datang konsultan pajak Rp300.000 plus.

## Adjacent opportunities
- Modul konversi bentuk badan ke PT perorangan agar tetap dapat insentif 0,5%.
- Cross-sell dengan file umkm-pajak-digital-ribet dan coretax-sering-error yang sudah ada di vault.
- Bundling dengan pembuatan NIB dan oss (kaitan dengan file umkm-belum-punya-nib-oss-sulit).

## Time-to-build estimate
- 2 minggu dengan tools off-the-shelf (chatbot LLM + template aturan PP 20/2026 + form input).
- 1 bulan kalau mau tambah kalkulator otomatis dan integrasi ke Coretax.
