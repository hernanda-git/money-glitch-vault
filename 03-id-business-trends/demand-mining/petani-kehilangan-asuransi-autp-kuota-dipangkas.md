# Petani Padi Kehilangan Asuransi Gagal Panen karena Kuota AUTP Dipangkas

**Date observed:** 2026-07-10
**Signal strength:** 4/5
**Category:** farmer
**Sources (minimum 3):**
- [Efisiensi Anggaran Pusat, Perlindungan Asuransi Petani di Jombang Berkurang](https://kabarjombang.com/pertanian/efisiensi-anggaran-pusat-perlindungan-asuransi-petani-di-jombang-berkurang/) — 2026-01-27 — Kuota AUTP Jombang turun, premi Rp180 ribu/ha kini dibebankan ke provinsi dan kabupaten
- [Petani Gagal Panen Akibat Hama di Tabanan Dapat Bantuan Asuransi Penuh](https://bali.idntimes.com/news/bali/petani-gagal-panen-akibat-hama-di-tabanan-dapat-bantuan-asuransi-penuh-00-x4g41-t6q4dd) — 2026-02-16 — Bantuan pusat sudah habis sejak 2025, AUTP 2026 murni dari APBD dengan kuota cuma 5.000 hektare
- [Kementan Alokasikan AUTP untuk 100 Ribu Hektare Lahan Padi pada 2026](https://rri.co.id/nasional/2545546/kementerian-pertanian-alokasikan-autp-untuk-100-ribu-hektare-lahan-padi-pada-2026) — 2026-02-16 — Alokasi nasional terbatas padahal jutaan hektare sawah rawan gagal panen
- [Pemkab Jombang Tambah Kuota Asuransi Tani AUTP 2026](https://jatim.pikiran-rakyat.com/jawa-timur/pr-37410306137/pemkab-jombang-tambah-kuota-asuransi-petani-gagal-panen-akibat-banjir-hingga-serangan-hama) — 2026-07-04 — Daerah terpaksa nambah sendiri karena pusat pangkas

## The pain (verbatim quotes in Indonesian)

> "Terjadi efisiensi anggaran dari pemerintah pusat. Skema pembiayaan yang sebelumnya sepenuhnya ditanggung pusat kini dialihkan menjadi tanggung jawab bersama pemerintah provinsi dan kabupaten." — Rony, pejabat terkait, KabarJombang, 28/1/2026

> "Bantuan dari Pemerintah Pusat sudah tidak ada lagi. Pemkab Tabanan di tahun 2026 ini mengalokasikan anggaran untuk pembayaran premi yang dialokasikan ke 5000 hektare sawah." — I Made Utama, Kabid Sarpras Dinas Pertanian Tabanan, 16/2/2026

> "Skalanya memang kecil, sehingga dalam sosialisasi nanti akan kami tekankan prioritas bagi yang paling terdampak." — I Made Utama, terkait kuota AUTP yang terbatas di Tabanan

Petani padi yang dulu otomatis terlindung asuransi gagal panen (AUTP, premi Rp180.000/ha dengan subsidi pusat) kini kehilangan perlindungan karena efisiensi anggaran. Sejak 2025 bantuan premi dari pemerintah pusat dicabut dan dialihkan ke APBD provinsi/kabupaten yang tak punya cukup duit. Akibatnya kuota anjlok drastis: di Jombang kuota susut, di Tabanan cuma kebagian 5.000 hektare dari puluhan ribu hektare sawah. Petani kecil yang tak kebagian kuota, kalau sawahnya kena wereng, tikus, atau banjir, harus nanggung rugi sendiri.

## Evidence of volume

- Program AUTP nasional 2026 cuma mengalokasikan 100.000 hektare (RRi, 16/2/2026), padahal luas panen padi nasional puluhan juta hektare, artinya mayoritas petani tak ter-cover.
- Di Jombang, kuota peserta AUTP turun signifikan pada 2025 setelah pembiayaan dialihkan ke daerah (KabarJombang, 27/1/2026).
- Di Tabanan, kuota 5.000 hektare disebut "skala kecil" dan pakai skema prioritas karena tak semua petani kebagian (IDN Times Bali, 16/2/2026).
- Beberapa daerah (Jombang, Malangraya) terpaksa rilis berita "tambah kuota" sendiri karena pusat pangkas, tanda demand perlindungan tinggi tapi pasokan kurang.

## Existing solutions (and why they fail)

- AUTP resmi (Jasindo + Kementan): gagal karena premi subsidi dicabut dan kuota dipangkas, proses klaim masih manual lewat SIAP, sosialisasi lambat (baru mulai Maret di Tabanan).
- Asuransi pertanian swasta (Allianz, AXA, Prudential): gagal karena premi komersial jauh di atas kemampuan petani kecil, dan tak ada subsidi.
- KUR / pinjaman bank untuk petani: gagal karena sifatnya utang baru, bukan ganti rugi, dan butuh agunan yang tak dimiliki petani gurem.

## Your wedge

Bangun agregator dan asisten klaim asuransi pertanian berbasis WhatsApp yang murah untuk petani. Produk: (1) pengecek kelayakan AUTP per daerah (apakah kuota masih ada di kabupaten mereka), (2) panduan daftar dan lacak status klaim dalam bahasa lokal, (3) marketplace mini yang hubungkan petani ke asuransi mikro swasta atau koperasi tani bila AUTP penuh, dengan premi dicicil. Karena celah utamanya adalah info (petani tak tahu kuota habis, tak tahu cara klaim), alat ini menjawab lewat notifikasi musim tanam dan panduan bergambar. Bisa dijalankan tanpa izin asuransi dengan jadi perantara edukasi, bukan underwriter.

## What people would pay

- Model: gratis untuk cek kuota/info, berbayar Rp15.000-Rp25.000 per musim untuk layanan bantuan klaim end-to-end, atau komisi dari asuransi mikro koperasi.
- Evidence willingness-to-pay: petani rela bayar premi Rp180.000/ha untuk AUTP saat disubsidi, jadi Rp15.000-Rp25.000 untuk jasa bantu klaim masuk akal sebagai "asuransi atas asuransinya".
- Comparable: agen asuransi dan broker mikro di desa biasa patok fee Rp20.000-Rp50.000 per polis; aplikasi klaim digital akan lebih murah dan scalable.

## Adjacent opportunities

- Asuransi ternak dan perkebunan kecil yang juga kehilangan subsidi serupa.
- Layanan pendampingan subsidi pupuk dan solar yang prosesnya mirip.
- Bundling dengan marketplace jual hasil panen agar petani punya arus kas untuk bayar premi.

## Time-to-build estimate

- 2 minggu dengan WhatsApp Business API + Google Sheets sebagai backend pelacakan kuota per kabupaten.
- 1 bulan dengan custom app dan scraping data kuota AUTP tiap daerah.
- 3+ bulan untuk jadi marketplace asuransi mikro penuh dengan kerja sama koperasi.
