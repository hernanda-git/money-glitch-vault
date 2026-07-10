# Freelancer Indonesia Kebingungan Urus Pajak dan Pembayaran dari Klien Luar Negeri

**Date observed:** 2026-07-10
**Signal strength:** 3
**Category:** freelancer
**Sources (minimum 3):**
- [Dapat Penghasilan Freelance Online dari Luar Negeri, Bagaimana Kewajiban Pajaknya?](https://ortax.org/pajak-freelance-online-atau-remote-working-luar-negeri) — 2024-08-10 — Ortax jelaskan penghasilan freelance luar negeri tetap wajib lapor tapi rumit soal tax treaty.
- [Pajak Pekerja Freelance](https://kantorku.id/blog/pajak-pekerja-freelance/) — 2025 — Kantorku bahas kewajiban pajak pekerja freelance secara umum.
- [Situs Freelance: Cara Cari Klien Internasional](https://www.ocbc.id/id/article/2021/09/06/situs-freelance) — 2021 — OCBC sebut freelancer butuh cara menerima bayaran dari klien asing.

## The pain (verbatim quotes in Indonesian)
> "Penghasilan luar negeri dari kegiatan freelance yang pekerjaan dilakukan di Indonesia secara online atau remote working umumnya tidak dipotong pajak di luar negeri. Namun, penghasilan tersebut tetap wajib dilaporkan dan dapat dikenakan pajak sesuai dengan ketentuan perundang undangan perpajakan di Indonesia." (Ortax, 2024-08-10)
> "Penghasilan dari dalam negeri dan luar negeri akan digabungkan dan dikenakan pajak sesuai dengan ketentuan yang berlaku." (Ortax, 2024-08-10)
> "Salah satu dokumen untuk membuktikan bahwa orang atau badan merupakan residen dari suatu negara adalah Certificate of Domicile atau Surat Keterangan Domisili." (Ortax, 2024-08-10)

Catatan: kutipan berasal dari panduan pajak resmi/teknis (Ortax) dan artikel perbankan. Suara freelancer langsung (forum/grup) sulit diakses karena Reddit/Kaskus memblokir crawler pada sesi ini. Naskah ini "synthesized from 3 sumber" yang mengonfirmasi freelancer punya beban pajak dan pembayaran lintas batas yang rumit.

## Evidence of volume
- Freelance/remote work ke luar negeri "semakin lumrah dilakukan" (Ortax), didorong Upwork, Fiverr, dan platform global.
- Puluhan ribu pekerja Indonesia bergantung pada klien asing; topik pajak freelance muncul rutin di Ortax, Kantorku, dan artikel perbankan.
- Hambatan pembayaran lintas batas (PayPal, Payoneer, Wise) dan kewajiban lapor SPT gabungan dalam negeri + luar negeri belum terjangkau solusi lokal yang ramah pengguna.

## Existing solutions (and why they fail)
- Ortax / konsultan pajak: penjelasannya teknis (tax treaty, Certificate of Domicile), freelancer pemula pusing.
- PayPal / Payoneer / Wise: menyelesaikan terima bayaran, tapi tidak bantu hitung atau lapor pajak.
- Aplikasi pajak umum: tidak paham alur penghasilan luar negeri dan kurs valuta.

## Your wedge
Buat dashboard "Freelancer Tax ID" yang terima export transaksi dari PayPal/Payoneer/Wise, otomatis konversi ke rupiah pakai kurs harian, hitung PPh terutang (termasuk bedakan penghasilan dalam vs luar negeri), dan hasilkan draf SPT tahunan siap unggah. Tambah modul "klien telat bayar" untuk mencatat tagihan dan mengingatkan follow up. Semua dalam bahasa Indonesia, tanpa istilah hukum berat.

## What people would pay
- Rp 75.000 sampai Rp 150.000 per tahun untuk generate SPT freelance.
- Evidence willingness to pay: freelancer menerima ratusan dolar per proyek, Rp 150.000 kecil. Konsultan pajak mematok jutaan untuk SPT orang pribadi, jadi ini jauh lebih murah.
- Comparable: jasa konsultasi pajak online dan akuntan lepas mematok Rp 500.000 ke atas per SPT.

## Adjacent opportunities
- Invoicing otomatis dengan kurs dan PPN untuk klien luar negeri.
- Integrasi dengan platform freelance (Upwork, Fiverr) untuk tarik riwayat earning.
- Komunitas/eduksia "freelance legally" lewat newsletter berbayar.

## Time-to-build estimate
- 2 minggu dengan Google Sheets + skrip konversi kurs + template SPT.
- 1 bulan dengan impor CSV dari PayPal/Payoneer dan generator PDF.
- 3 bulan untuk produk penuh dengan koneksi API dan pengingat otomatis.
