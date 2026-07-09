# Seller TikTok Shop dan Shopee Menjerit: Kewajiban NIB dan Komisi Dinamis Melonjak 15 Kali Lipat

**Date observed:** 2026-07-09
**Signal strength:** 5
**Category:** seller
**Sources (minimum 3):**
- [TikTok Shop naikkan biaya komisi dinamis per 18 Mei, seller menjerit](https://teknologi.bisnis.com/read/20260515/84/1974040/tiktok-shop-naikkan-biaya-komisi-dinamis-per-18-mei-seller-menjerit) — 2026-05-15 — Batas maksimum komisi naik dari Rp40.000 jadi Rp650.000 per item, melonjak 15 kali lipat
- [Tenggat singkat seller Shopee hingga TikTok Shop urus NIB](https://ekonomi.bisnis.com/read/20260619/12/1981890/tenggat-singkat-seller-shopee-tiktok-shop-cs-urus-nib) — 2026-06-19 — Permendag 19/2026 mewajibkan NIB, tenggat 6-18 bulan, berlaku 8 Juni 2026
- [Permendag 19/2026: Shopee, TikTok Shop cs wajib blokir seller tanpa NIB](https://teknologi.bisnis.com/read/20260609/84/1979590/permendag-192026-shopee-tiktok-shop-cs-wajib-blokir-seller-tanpa-nib) — 2026-06-09 — Platform harus menolak pendaftaran seller tanpa NIB
- [Mendag wajibkan Shopee, TikTok Shop cs tolak seller tanpa NIB](https://ekonomi.bisnis.com/read/20260617/12/1981337/mendag-wajibkan-shopee-tiktok-shop-cs-tolak-seller-tanpa-nib) — 2026-06-17 — Pengawasan lebih ketat dari pemerintah
- [Shopee-TikTok Shop cs dihantui penurunan jumlah seller aktif](https://premium.bisnis.com/read/20260613/658/1980632/shopee-tiktok-shop-cs-dihantui-penurunan-jumlah-seller-aktif) — 2026-06-13 — Kebijakan NIB berpotensi kurangi pedagang aktif

## The pain (verbatim quotes in Indonesian)
> "TikTok Shop diketahui akan memberlakukan perubahan skema Biaya Komisi Dinamis per 18 Mei 2026, dengan kenaikan batas maksimum komisi dari sebelumnya Rp40.000 menjadi hingga Rp650.000 per item atau meningkat 15 kali lipat." , tulis Bisnis.com merangkum pengumuman platform.
> "Biaya komisi dinamis akan dikenakan ke seluruh pesanan yang berhasil dikirim." , tulis TikTok Shop dalam websitenya.
> "Kewajiban Nomor Induk Berusaha (NIB) bagi seluruh seller marketplace seperti Shopee, TikTok Shop, hingga Lazada harus dilakukan dalam waktu singkat. Pemerintah memberi tenggat antara 6 bulan hingga 18 bulan hingga seluruh dokumen rampung." , kata laporan Bisnis.com.

## Evidence of volume
- Aturan berlaku nasional untuk seluruh seller Shopee, TikTok Shop, Tokopedia, Lazada sejak 8 Juni 2026
- Komisi dinamis TikTok Shop naik 15x lipat (Rp40.000 ke Rp650.000/item) per 18 Mei 2026
- Bisnis.com melaporkan platform dihantui penurunan jumlah seller aktif akibat kebijakan ini
- Jutaan UMKM seller online terdampak kewajiban NIB, banyak yang belum punya legalitas usaha
- Puluhan artikel panduan "cara urus NIB lewat OSS" muncul dalam sebulan terakhir, tanda permintaan tinggi

## Existing solutions (and why they fail)
- Portal OSS R/I (oss.go.id): sering error, UI berbelit, butuh login dan verifikasi yang membingungkan orang awam
- Jasa joki pendamping NIB: biayanya bervariasi dan tidak transparan, plus risiko data pribadi bocor
- Panduan YouTube/artikel: tidak lengkap, cepat kadaluarsa mengikuti perubahan aturan, tidak ada pengecekan status

## Your wedge
Bangun layanan "NIB dalam 1 hari" untuk seller online: asisten berbasis chatbot yang menuntun seller mengisi OSS langkah demi langkah, plus pengecekan otomatis apakah tokonya sudah memenuhi syarat agar tidak diblokir. Bisa dibundel dengan perhitung undangan margin otomatis yang memasukkan komisi dinamis + biaya iklan + ongkir, sehingga seller tahu harga jual minimum agar tidak rugi. Posisi sebagai "compliance + profit toolkit" untuk seller kecil yang panik karena tenggat NIB dan komisi membengkak.

## What people would pay
- Jasa pendampingan NIB sekali bayar: Rp 75.000 - Rp 250.000 per tokonya
- Langganan toolkit margin + alert komisi: Rp 49.000 - Rp 99.000 per bulan
- Bukti willingness to pay: seller rela bayar joki dan konsultan karena tokonya terancam diblokir dan margin menyusut. Kebutuhan mendesak karena tenggat 6-18 bulan sudah berjalan sejak Juni 2026

## Adjacent opportunities
- Bundling dengan jasa pembuatan PIRT/BPOM untuk seller makanan (lihat pain UMKM izin edar)
- Cross-sell ke agen perizinan daerah lain (NIB, Izin Lingkungan, NPWP)
- Alat hitung HPP dan harga jual untuk seller TikTok Shop/Shopee (pola sama, audiens sama)

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools: bot panduan OSS + kalkulator margin sederhana
- 1 bulan dengan custom dev: integrasi API OSS dan dashboard multi-toko
- 3+ bulan untuk produk penuh dengan kemitraan konsultan perizinan
