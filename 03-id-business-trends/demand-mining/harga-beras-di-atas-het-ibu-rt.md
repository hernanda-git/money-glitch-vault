# Harga Beras Tembus di Atas HET, Ibu Rumah Tangga Kewalahan Atur RAB Makan

**Date observed:** 2026-07-09
**Signal strength:** 4
**Category:** parent
**Sources (minimum 3):**
- [Beras Dilanda Kenaikan Harga dan Ancaman Penurunan Produksi](https://www.kompas.id/artikel/beras-dilanda-kenaikan-harga-dan-ancaman-penurunan-produksi) — 2026-06-22 — harga beras medium Rp 14.402/kg dan premium Rp 16.230/kg, di atas HET
- [Harga Gabah Terus Naik dan Tembus Rp 7.300, Bulog Tetap Beli di HPP](https://ekonomi.bisnis.com/read/20260519/99/1974813/harga-gabah-terus-naik-dan-tembus-rp7300-bulog-tetap-beli-di-hpp) — 2026-05-19 — gabah meroket Rp 7.200-7.300/kg karena akhir musim panen, beras ikut mahal
- [BPS: Harga Beras Medium Naik 0,38 Persen per Juni 2026](https://www.kompas.id/artikel/beras-dilanda-kenaikan-harga-dan-ancaman-penurunan-produksi) — 2026-06-22 — 130 kabupaten/kota alami kenaikan harga beras, status waspada sampai tidak aman

## The pain (verbatim quotes in Indonesian)
> "Badan Pusat Statistik (BPS) mencatat, pada pekan ketiga Juni 2026, harga rerata nasional beras medium senilai Rp 14.402 per kilogram (kg). Harga beras tersebut naik 0,38 persen dibandingkan harga rerata pada Mei 2026." (Kompas.id, 2026-06-22)
> "Demikian juga dengan beras premium yang harga reratanya naik 0,46 persen menjadi Rp 16.230 per kg. Harga kedua jenis beras itu berada di atas rerata harga eceran tertinggi (HET) beras medium dan premium yang masing-masing dipatok Rp 13.500 per kg dan Rp 14.900 per kg." (Kompas.id, 2026-06-22)
> "Dalam periode perbandingan yang sama, jumlah kabupaten/kota yang mengalami kenaikan harga beras juga bertambah dari 110 daerah menjadi 130 daerah." (Deputi BPS Ateng Hartono, dikutip Kompas.id, 2026-06-22)
> "Kondisi ini karena masa panen sudah berlalu sehingga sudah mulai sedikit yang dipanen dan harganya melambung tinggi." (Dirut Bulog Ahmad Rizal, Bisnis.com, 2026-05-19)

Catatan: Sumber adalah berita resmi dan data BPS (bukan curhat ibu RT Reddit). Nyeri rumah tangga kesulitan beli beras disintesis dari fakta harga beras sudah di atas HET di 130 daerah. [synthesized from Kompas.id + Bisnis.com + BPS sources]

## Evidence of volume
- Harga beras medium Rp 14.402/kg (di atas HET Rp 13.500), premium Rp 16.230/kg (di atas HET Rp 14.900)
- 130 kabupaten/kota alami kenaikan harga beras, status "waspada" sampai "tidak aman"
- Gabah meroket ke Rp 7.300/kg pasca panen, artinya beras mahal berlanjut beberapa bulan
- Beras adalah komoditas paling dasar, kenaikan langsung tekan RAB makan keluarga miskin

## Existing solutions (and why they fail)
- Operasi pasar Bulog: titik terbatas, antre panjang, tidak menjangkau desa
- Pedoman HET Kemendag: ada aturan tapi pedagang jual di atas HET karena pasokan tipis
- Aplikasi belanja (Segari, Sayurbox): fokus kemudahan, bukan harga termurah beras
- Inflation dashboard pemerintah: hanya info, tidak bantu hemat

## Your wedge
Bikin "BerasHemat" untuk ibu RT: (1) panel harga beras harian per daerah (scrape data Bulog/Siskaperbako), (2) rekomendasi merek/toko termurah terdekat, (3) kalkulator RAB makan mingguan yang otomatis ganti komposisi kalau beras mahal, (4) alert saat operasi pasar Bulog buka di wilayahnya. Monetisasi: gratis untuk ibu RT, langganan Rp 15.000/bulan untuk fitur planning + cashback ewarung. Bisa jadi affiliate beras subsidi.

## What people would pay
- Ibu RT: gratis untuk cek harga, Rp 15.000/bulan untuk planner RAB + alert operasi pasar
- Warung/UMKM makanan: Rp 50.000/bulan untuk pantau harga beras grosir harian
- Bukti willingness-to-pay: beras tiap rumah beli mingguan, sensitif harga; ewarung cashback laku
- Pembanding: aplikasi belanja harian, price comparison, dan budget planner (MoneyLover, Finansialku)

## Adjacent opportunities
- Cross-sell ke pantauan harga telur, minyak, gula (paket sembako)
- Bundling dengan ewarung/warung langganan langganan
- Data harga pangan per daerah jadi produk untuk peneliti/NGO

## Time-to-build estimate
- 2 minggu dengan off-the-shelf tools (no-code app + Google Sheet harga harian)
- 1 bulan dengan custom dev (scraper harga, geolokasi toko, kalkulator RAB)
- 3+ bulan untuk produk penuh dengan kemitraan Bulog dan ewarung
