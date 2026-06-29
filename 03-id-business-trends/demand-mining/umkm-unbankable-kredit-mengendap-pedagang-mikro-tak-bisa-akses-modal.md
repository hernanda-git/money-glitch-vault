# UMKM Unbankable: Rp2.500 Triliun Kredit Mengendap, Pedagang Mikro Tak Bisa Akses Modal

**Date observed:** 2026-06-29
**Signal strength:** 5/5
**Category:** umkm
**Sources (minimum 3):**
- [Denyut rupiah di nadi UMKM](https://www.antaranews.com/berita/5579744/denyut-rupiah-di-nadi-umkm) — 2026-05-23 — Lebih dari Rp2.500 triliun komitmen kredit mengendap, UMKM merasakan kesulitan kekurangan pasokan modal
- [Algoritma trotoar UMKM keliling](https://www.antaranews.com/berita/5552925/algoritma-trotoar-umkm-keliling) — 2026-05-04 — Tantangan terbesar penyaluran KUR adalah status unbankable mayoritas pedagang mikro
- [Mendag tegaskan NIB untuk pedagang e-commerce bukan untuk pajak](https://www.antaranews.com/berita/5617720/mendag-tegaskan-nib-untuk-pedagang-e-commerce-bukan-untuk-pajak) — 2026-06-22 — Kewajiban NIB untuk pedagang e-commerce, legalitas sebagai jalan akses perbankan
- [POPSI: Mandatori B50 perlu diiringi perhatian ke petani sawit](https://www.antaranews.com/berita/5624360/popsi-mandatori-b50-perlu-diiringi-dengan-perhatian-ke-petani-sawit) — 2026-06-26 — Petani sawit rakyat juga menghadapi kesulitan akses modal

## The pain (verbatim quotes in Indonesian)
> "Di satu sisi, UMKM merasakan kesulitan dalam pengembangan usahanya karena kekurangan pasokan modal, namun di sisi lain, triliunan rupiah hanya menjadi angka di pembukuan bank." — Artikel Antara, "Denyut rupiah di nadi UMKM" (Mei 2026)

> "Salah satu tantangan terbesar dalam penyaluran Kredit Usaha Rakyat (KUR) adalah status unbankable dari mayoritas pedagang mikro dan kecil. Tanpa aset fisik, seperti sertifikat tanah atau BPKB, akses terhadap modal sering kali tertutup." — Artikel Antara, "Algoritma trotoar UMKM keliling" (Mei 2026)

> "Kalau sudah mempunyai legalitas, maka dia akses ke perbankan, akses pembiayaan itu lebih mudah." — Mendag Budi Santoso tentang pentingnya NIB bagi UMKM (Antara, 22 Juni 2026)

## Evidence of volume
- Lebih dari Rp2.500 triliun komitmen kredit yang mengendap di perbankan nasional (data Antara, Mei 2026)
- 64 juta UMKM di Indonesia, mayoritas berstatus unbankable karena tidak memiliki agunan fisik
- Volume transaksi QRIS nasional Q1-2026 tumbuh 119%, menunjukkan potensi digital credit scoring
- Kewajiban NIB bagi pedagang e-commerce baru ditegaskan Juni 2026 (Permendag 19/2026), menunjukkan masih banyak yang belum memiliki legalitas usaha

## Existing solutions (and why they fail)
- Solution A: KUR (Kredit Usaha Rakyat) — gagal karena persyaratan agunan fisik (sertifikat tanah, BPKB) yang tidak dimiliki pedagang mikro, proses birokrasi rumit
- Solution B: Fintech lending (pinjol) — seringkali bunga tinggi dan praktik debt collector yang agresif, banyak yang ilegal
- Solution C: QRIS sebagai credit scoring — masih dalam tahap awal, belum semua bank mengadopsi data transaksi digital sebagai dasar penilaian kelayakan kredit

## Your wedge
Buat platform "digital credit scoring" untuk UMKM mikro yang menggabungkan data transaksi QRIS, riwayat penjualan harian, dan profil usaha untuk menghasilkan skor kelayakan kredit tanpa agunan fisik. Platform ini menghubungkan UMKM unbankable dengan bank mitra yang bersedia menyalurkan kredit berbasis data digital. UMKM tinggal hubungkan akun QRIS atau upload fotostruk transaksi harian, dan sistem otomatis menghitung skor kredit. Bank bisa menyalurkan kredit langsung ke rekening UMKM tanpa agunan, dengan bunga lebih rendah dari pinjol karena risiko lebih terukur.

## What people would pay
- Komisi 1-2% dari nilai kredit yang disalurkan untuk UMKM
- Bukti willingness-to-pay: UMKM saat ini membayar bunga pinjol 1-4% per bulan, sehingga bersedia bayar komisi satu kali 1-2% untuk akses kredit yang lebih murah dan aman
- Komparasi: KUR bunga 6% per tahun (sulit diakses), pinjol bunga 1-4% per bulan (berisiko), fintech lending resmi bunga 0,5-2% per bulan (masih mahal)

## Adjacent opportunities
- Cross-sell: asuransi mikro untuk UMKM (kesehatan, kerusakan barang, bencana alam)
- Bundling: layanan pembukuan digital sederhana yang otomatis menghasilkan data untuk credit scoring
- Data transaksi UMKM bisa dijual ke institusi riset atau perusahaan yang ingin memahami perilaku konsumen mikro

## Time-to-build estimate
- 2 minggu dengan MVP berbasis integrasi QRIS API + spreadsheet scoring
- 1 bulan dengan dashboard kredit sederhana untuk bank mitra
- 3+ bulan untuk full product dengan multi-bank integration dan credit scoring AI
