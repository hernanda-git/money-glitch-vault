# Changelog , money-glitch-vault

## 2026-06-18 , id-miner round 2: 3 new pain points committed
- Mined 3 new Indonesian business pain points from real 2026 sources (CNBC Indonesia, Bisnis Tekno, Kompas, Kompas.id, ANTARA News, Patra Indonesia, Hukumonline, Kumparan)
- Pain 4 (5/5): Driver Ojol Potongan Tarif Gerus Pendapatan , persaingan makin ketat, Perpres 8% belum efektif
- Pain 5 (4/5): Freelancer Gagal Dibayar Klien Wanprestasi , 58% SEA freelancers unpaid, escrow masih mahal
- Pain 6 (5/5): Petani Tengkulak Margin Tidak Adil , harga anjlok saat panen, rantai distribusi 30-60% margin tengkulak
- Total: 6 pain points now in demand-mining across 5 categories (umkm, student, ojol, freelancer, farmer)
- Files: 03-id-business-trends/demand-mining/{driver-ojol-potongan-tarif-gerus-pendapatan,freelancer-gagal-dibayar-klien-wanprestasi,petani-tengkulak-margin-tidak-adil}.md
- INDEX.md updated with all 3 new entries

## 2026-06-16 , id-miner first run: 3 pain points committed
- Mined 3 distinct Indonesian business pain points from real 2026 sources (Kompas, CNBC Indonesia, OJK, Kontan, Suara, Jawa Pos, IMF via Viva)
- Pain 1 (5/5): UMKM Sulit Akses Modal , Kemen UMKM data 69.5% UMKM gagal dapat kredit bank, Celios research, IFC gender gap US$1.9T
- Pain 2 (5/5): Pinjol Ilegal Marak , 951 entitas ditutup Q1 2026, Rp585M dana korban diselamatkan, 68% korban perempuan
- Pain 3 (4/5): Fresh Grad Susah Kerja , TPT sarjana 5.18%, 20 bulan masa tunggu, IMF tsunami AI warning
- Cross-folder gap note dropped to /07-gaps-and-opportunities/inbox/ about "WhatsApp-first financial inclusion agent"
- Files: 03-id-business-trends/demand-mining/{umkm-sulit-akses-modal,pinjol-ilegal-menjebak-masyarakat-kurang-terlayani,fresh-graduate-susah-dapat-kerja-skill-mismatch}.md
- INDEX.md created with all 3 entries

## 2026-06-16 , Initial scaffold
- Repo created: `hernanda-git/money-glitch-vault` (private)
- 7 topic folders + README per folder
- `.gitignore` for secrets and raw data
- Folder layout modeled after `ai-knowledge-library`

## 2026-06-16 , Self-enriching cron pipeline (5 jobs)
- 3 no-agent data jobs: market-pulse, harga-pangan, auto-commit
- 2 LLM agents: id-miner, filler
- 1 weekly synthesizer
- All scripts tested end-to-end with real CoinGecko + Yahoo Finance data
- First market pulse captured: BTC $66,865, ETH $1,830, USD/IDR 16,848, IHSG pending Yahoo rate-limit recovery
- Data files (pulse-*.json, harga-*.json) committed and pushed

## 2026-06-16 , harga-pangan pipeline pivoted to SP2KP Kemendag
- Original PiJPS/Bapanas endpoints all dead (Cloudflare 522 on hargapangan.id, BPS firewall blocks, Bapanas subdomains unreachable)
- Discovered **SP2KP Kemendag** (https://sp2kp.kemendag.go.id/) is alive and serves live HNT (Harga Nasional Tertimbang) for 16 commodities x 514 kab/kota
- Converted `money-glitch-harga-pangan` cron from no_agent (HTTP scraper) to **agent-driven with browser MCP** (browser_navigate + browser_console extract)
- Deleted obsolete Python scraper + wrapper
- First successful capture: 26 records (16 commodities + 10 region sub-rows), top movers Cabai Merah Besar -2.21%, Bawang Merah -1.71%
- README updated to reflect SP2KP as primary source
- Data files: `sp2kp-2026-06-16.json`, `latest.json`, `INDEX.md`
