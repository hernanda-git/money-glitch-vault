# Seller TikTok Shop Terbebani Biaya Kirim Gagal dan Retur Akibat Kebijakan Baru Juni 2026

**Date observed:** 2026-07-18
**Signal strength:** 4/5
**Category:** seller
**Sources (minimum 3):**
- [Aturan Baru TikTok Shop Berlaku Setelah Masa Tenggang 3 Bulan](https://ototekno.harianjogja.com/r-1257989/aturan-baru-tiktok-shop-berlaku-setelah-masa-tenggang-3-bulan) — 2026-05-31 — Platform wajibkan seller tanggung biaya logistik pengiriman gagal dan retur
- [Lagi rame banyak seller yang naikin harga dan perlahan banyak yang cabut dari e-commerce](https://finance.detik.com/berita-ekonomi-bisnis/d-8476747/ramai-seller-ngeluh-gegara-ongkir-toko-online-kemendag-buka-suara) — 2026-05-09 — Detik kutip keluhan seller soal beban ongkir yang dipindah ke penjual
- [Kontan: Tekanan Biaya E-Commerce 2026, Seller Mulai Cari Kanal Penjualan Alternatif](https://industri.kontan.co.id/news/tekanan-biaya-e-commerce-2026-seller-mulai-cari-kanal-penjualan-alternatif) — 2026-05-09 — Seller contoh laba Rp50.000 susut jadi Rp9.000 setelah potong ongkir dan platform
- [TikTok Shop Seller Wajib Waspada, kebijakan baru Mei-Juni 2026](https://www.instagram.com/p/DXoizP6Ex7D/) — 2026-05-31 — Seller individu mengeluh di Instagram

## The pain (verbatim quotes in Indonesian)
> "Platform TikTok Shop meluncurkan kebijakan baru pada Juni 2026. Aturan ini mewajibkan penjual ikut menanggung biaya logistik atas pengiriman gagal dan pengembalian barang yang disebabkan oleh pembeli, dengan total beban mencapai Rp10.000 per transaksi." (Harianjogja / ANTARA, 31 Mei 2026)
> "Kritik terhadap kebijakan ini juga datang dari pemerintah. Menteri UMKM Maman Abdurrahman menilai praktik tersebut berpotensi mengarah pada penyalahgunaan pasar (market abuse), terutama jika dilakukan oleh platform besar dengan posisi dominan." (Harianjogja / ANTARA, 31 Mei 2026)
> "Sekarang seller dapat untung kayak cuma hikmah aja. Dulu bisa untung 50%, sekarang tinggal 25%, bahkan pernah cuma 5%." (Bunga, seller Jakarta Barat, dikutip Kontan, 8 Mei 2026)
> "Lagi rame banyak seller yang naikin harga dan perlahan banyak yang cabut dari e-commerce dan beralih bikin web sendiri." (kutipan di artikel Detik, Mei 2026)

## Evidence of volume
- 3 artikel berita nasional (Detik, Kontan, Harianjogja/ANTARA) dalam Mei-Juni 2026 membahas beban ongkir dan retur yang dipindahkan ke seller
- Menteri UMKM secara terbuka mengkritik kebijakan platform (sinyal politis, bukan kasus tunggal)
- Puluhan unggahan Instagram dan TikTok dari seller individu mengeluhkan kebijakan retur dan kenaikan biaya admin sejak Mei 2026
- Kemendag membuka suara dan sedang menyusun aturan transparansi biaya PPMSE (Peraturan Pedagang Platform Semi Elektronik)

## Existing solutions (and why they fail)
- Beralih ke website mandiri / toko offline: butuh modal, traffic, dan skill teknis yang tidak dimiliki seller kecil. Tanpa iklan, website mandiri sepi pengunjung.
- Negotiasi dengan platform: tidak ada posisi tawar. Seller perorangan tidak bisa mengubah kebijakan TikTok Shop atau Shopee.
- Naikkan harga jual: langsung kalah saing dengan seller lain yang tetap harga murah, penjualan turun.
- Join agregator logistik lebih murah: hanya mengurangi biaya kirim awal, tidak menyelesaikan beban retur dan kirim gagal yang ditagih per transaksi.

## Your wedge
Bangun layanan "biaya tersembunyi calculator" dan alert harian untuk seller marketplace: input sku, harga, dan rate retur historis, lalu hitung margin bersih riil setelah ongkir, biaya platform, retur, dan kirim gagal. Gabungkan dengan rekomendasi otomatis (naikkan harga X, batasi gratis ongkir di produk margin tipis, pindah ke channel dengan biaya lebih rendah). Beri juga template protes / ajuan ke Kemendag dan ringkasan posisi tawar kolektif. Produk ini murah dibuat (sheet + bot WhatsApp + scraper harga komisi resmi) tapi langsung menjawab rasa "kok untung saya susah naik".

## What people would pay
- Paket dasar Rp50.000 - Rp99.000 per bulan untuk dashboard margin + alert
- Evidence: seller rela bayar jasa konsultan toko online dan iklan jutaan rupiah per bulan. Kontan mencatat seller kehilangan Rp41.000 dari laba Rp50.000 cuma dari potongan ongkir dan platform, jadi Rp50.000/bulan untuk alat pencegah kerugian sangat masuk akal.
- Comparable: Jurnal, BukuKas, Majoo mengenakan Rp100.000 - Rp300.000/bulan untuk fitur kasir dan pembukuan UMKM.

## Adjacent opportunities
- Cross-sell: bot balas otomatis untuk menekan rate retur akibat salah kirim
- Bundling dengan jasa pembuatan website mandiri (kanal alternatif yang sedang dicari seller)
- Data agregat margin per kategori produk bisa dijual ke brand sebagai riset pasar

## Time-to-build estimate
- 2 minggu dengan alat off-the-shelf: Google Sheet + Apps Script + bot WhatsApp (WATI/Fonnte) + scraper komisi resmi marketplace
- 1 bulan dengan dev kustom untuk dashboard web dan integrasi API marketplace
- 3+ bulan untuk produk penuh dengan ML prediksi retur
