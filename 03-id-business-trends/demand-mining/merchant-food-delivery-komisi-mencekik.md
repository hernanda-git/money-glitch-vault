# Merchant Food Delivery Kepekik Potongan Komisi Platform

**Date observed:** 2026-07-13
**Signal strength:** 5
**Category:** seller
**Sources (minimum 3):**
- [Unikorn Food Platform Pungut Komisi 20 Persen ke Merchant, INDEF: UMKM Tak Berdaya](https://ekonomi.bisnis.com/read/20220506/12/1530431/unikorn-food-platform-pungut-komisi-20-persen-ke-merchant-indef-umkm-tak-berdaya) — 2022-05-06 — INDEF sebut potongan 20 persen sampai 30 persen membuat UMKM tidak berdaya.
- [Potongan ShopeeFood Berapa Persen? Merchant Wajib Cek!](https://tokpee.co/blog/potongan-shopeefood-berapa-persen/) — 2026-01-02 — ShopeeFood memotong merchant sekitar 20 persen, total bisa lebih dari itu.
- [Biaya Daftar ShopeeFood untuk Merchant 2026, Ini Rincian dan Cara Gabungnya](https://majoo.id/solusi/detail/biaya-daftar-shopee-food-untuk-merchant-2026-ini-rincian-dan-cara-gabungnya) — 2026-05-11 — rincian biaya admin dan komisi merchant food delivery 2026.
- [GOTO dan Grab Pangkas Komisi Ojol ke 8% per 1 Juli 2026](https://snips.stockbit.com/stockbit-research/goto-grab-pangkas-komisi-ojol-ke-8-per-1-juli-2026) — 2026-07-02 — catatan konteks: batas 8 persen hanya untuk ojol angkut penumpang, bukan merchant makanan.

## The pain (verbatim quotes in Indonesian)
> "UMKM akan perlahan-lahan bangkrut jika pemerintah tidak membuat regulasi khusus yang meringankan dalam pemotongan komisi." — Tauhid Ahmad, Direktur Eksekutif INDEF, dikutip Bisnis.com.
> "Kebijakan itu menyebabkan setiap merchant terpaksa menaikkan harga cukup tinggi agar menjaga keuntungan, komisi dan discount. Efek dari harga tinggi maka daya beli menurun dan mencekik merchant terutama UMKM." — bunyi petisi Change.org yang dikutip Bisnis.com.
> "Potongan 20 persen terhadap mitra tidak bisa diterima akal sehat." — Edwin Tejo, penulis petisi komisi food platform.
> "Selaku Pembina sekaligus mitra UMKM di daerah, saya setuju adanya evaluasi komisi 20%+Rp1k ini." — akun Choiruddin, pelaku UMKM di petisi.

## Evidence of volume
- Petisi Change.org menolak komisi food platform telah mengumpulkan hampir 4.700 tanda tangan dan terus bergulir.
- GrabFood di laporkan memotong hingga 30 persen di luar PPN menurut grabinaja.com, jauh di atas GoFood 20 persen + Rp 1.000.
- ShopeeFood menaikkan biaya admin per 1 Januari 2026 (dokumentasi di Instagram @ShopeeID dan tokpee.co), menekan margin merchant.
- Komisi 8 persen yang viral Juli 2026 hanya berlaku untuk driver ojol penumpang, bukan untuk merchant makanan, sehingga nyeri seller food delivery tetap utuh.

## Existing solutions (and why they fail)
- Naikkan harga jual di aplikasi: gagal karena daya beli turun dan orderan malah drop, seperti diakui di petisi.
- Promo dan iklan in app: justru nambah potongan baru (biaya iklan, diskon bersama), margin makin tipis.
- Pindah ke WhatsApp order mandiri: sulit dapat trafik baru tanpa biaya aquisisi pelanggan yang mahal.
- Regulasi pemerintah: INDEF bilang sampai sekarang belum ada aturan yang membatasi plafon komisi food merchant, berbeda dengan ojol yang sudah ada batas 8 persen.

## Your wedge
Bangun tools harga jual otomatis yang menghitung break even per item setelah semua potongan (komisi + admin + diskon + ongkir subsidised) supaya merchant tahu harga pasar minimal yang masih untung. Lalu tawarkan kanal order mandiri murah (landing page WhatsApp/website kecil dengan link pembayaran) sehingga merchant bisa pindahkan 20 persen sampai 30 persen pelanggan setia keluar dari komisi platform. Produk kedua: dashboard bandingkan net margin GoFood vs GrabFood vs ShopeeFood vs order langsung, dengan rekomendasi routinge mana yang dipakai per menu. Intip model group buying dan settlement harian yang sudah dipakai warung collective buying di vault ini.

## What people would pay
- Harga Rp 49.000 sampai Rp 99.000 per bulan untuk kalkulator net margin dan generator harga jual otomatis.
- Setup landing page order mandiri Rp 250.000 sekali bayar plus Rp 50.000 per bulan.
- Bukti willingness to pay: ribuan merchant sudah bayar tools majoo dan tools kasir lainnya, dan mereka rela ikut pelatihan hitung HPP GoFood gratis tapi butuh otomasi.
- pemain sejenis: majoo, olsera, cara kasir SaaS UMKM sudah charge Rp 50.000 sampai Rp 200.000 per bulan.

## Adjacent opportunities
- Cross sell ke UMKM seller marketplace yang juga terkena komisi dan ongkir (lihat file seller-marketplace-komisi-ongkir-meroket di vault).
- Bundling dengan layanan foto menu dan copywriting iklan makanan.
- Escrow atau settlement cepat untuk order mandiri supaya buyer percaya.

## Time-to-build estimate
- 2 minggu dengan off the shelf tools: spreadsheet otomatis + WhatsApp landing page generator no code.
- 1 bulan dengan custom dev: dashboard net margin multi platform dan routing rekomendasi.
- 3 bulan plus untuk produk penuh dengan integrasi API marketplace dan pembayaran.
