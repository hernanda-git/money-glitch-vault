# Changelog , money-glitch-vault

## 2026-06-18 , enrich(02): event-driven-trading-bot
- 3389-line deeply technical guide on event-driven trading bot architecture for Indonesian markets (IDX, crypto exchanges)
- Working Python code: EventBus (ZeroMQ PUB/SUB), MarketDataFeed (Binance + Indodax WebSocket), OrderBook, SignalGenerator (MA Crossover, RSI), RiskManager (Kelly Criterion, kill switch, max drawdown)
- IDX-specific: trading hours 09:00-15:00 WIB, T+2 settlement, lot sizes, OJK concentration limits
- Crypto-specific: WebSocket feeds from Binance/Indodax, rate limit management with sliding window
- Paper trading engine with slippage simulation (Almgren-Chriss model)
- Backtesting framework using yfinance for IDX stocks (BBCA.JK example)
- Prometheus metrics, Telegram alerts, Docker Compose deployment
- Full pytest suite for event bus, risk manager, order book, paper broker, IDX clock
- Files: 02-trading-bot/architectures/event-driven-baseline.md

## 2026-06-18 , id-miner round 3: 3 new pain points committed (employee, seller, other)
- Mined 3 new Indonesian business pain points from real 2026 sources (Warta Ekonomi, Celios, Kemen UMKM, Katadata, WebEkspor, PejuangKantoran, Cove, Kompas Money, Kompas Nasional, CNBC Indonesia, CNN Indonesia, Detik, Bisnis Finansial)
- Pain 7 (5/5, employee): Biaya Sewa Kos dan Properti di Kota Besar Tidak Terjangkau , Jakarta lebih mahal dari Paris/Tokyo, kos Kuningan 2x lipat Tebet, 73% milenial kesulitan beli rumah
- Pain 8 (5/5, seller): Biaya Platform Marketplace Makin Membebani Penjual Online , fee naik 20-25%, Menteri UMKM keluhkan biaya platform, Shopee tambah biaya pre-order 3% + SPayLater
- Pain 9 (4/5, other): Pekerja Informal dan Gig Workers Sulit Akses Jaminan Kesehatan , BPJS defisit Rp 20-30T, iuran akan naik 2026, klaim ditolak masalah administrasi
- Total: 9 pain points now in demand-mining across 8 categories (umkm, student, ojol, freelancer, farmer, employee, seller, other)
- Files: 03-id-business-trends/demand-mining/{biaya-sewa-kos-properti-kota-besar-tak-terjangkau-pekerja-muda,biaya-platform-marketplace-makin-membebani-umkm-penjual-online,pekerja-informal-gig-workers-sulit-akses-jaminan-kesehatan-layak}.md
- INDEX.md updated with all 3 new entries with categories employee, seller, other

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

## 2026-06-18 , enrich(01-crawler-scrapper): cookie-token-storage-safety
- 2824-line technical guide on cookie/token storage safety for web scraping in Indonesian context
- Covers Fernet encryption, SQLite vault, Playwright persistence, OAuth2/JWT refresh, UU ITE compliance
- Real-world examples for Tokopedia, Shopee, X/Twitter, Gojek session management

## 2026-06-19 , enrich(04): fastwork-mcp-server-spec
- 1778-line deeply technical MCP server specification for Fastwork.id, the #1 Indonesian freelance marketplace
- Reverse-engineered API surface (auth endpoints, Algolia search, chat WebSocket, wallet, job board)
- Complete MCP tool definitions: search_services, create_order, submit_job_proposal, send_message, and 12+ other tools
- TypeScript implementation walkthrough: MCP server setup, SessionManager with auto-refresh, encrypted SQLite token storage, token-bucket rate limiter, retry logic, error classification
- Prompt templates for proposal generation, market research, and order follow-up
- n8n integration patterns for auto-bidder and order monitor workflows
- Security considerations: AES-256-GCM encryption, OAuth2 flow, circuit breaker patterns
- Docker Compose deployment and Claude Desktop integration config
- Files: 04-freelancer-ai-agent/mcp-servers/fastwork-mcp-spec.md

## 2026-06-21 , enrich(03): umkm-digitalisasi-paksa-platform-ekosistem
- 800+ line deep technical analysis of UMKM forced digitization and platform ecosystem dependency in Indonesia
- The anatomy of platform lock-in: investment accumulation, algorithm control, predatory pricing, latent costs
- 10+ real data points from Kompas.id, Celios, LPEM FEB UI, Kemenkop UKM, OJK, and other sources
- 5 solution wedges: AI anti-dependency agent, multi-platform dashboard, koperasi marketplace, WhatsApp bot, class action advocacy
- Cross-referenced with 4 existing vault pain points (modal, biaya platform, pinjol, ojol)
- Files: 03-id-business-trends/demand-mining/umkm-digitalisasi-paksa-platform-ekosistem.md

## 2026-06-22 , enrich(03): competitors-tokopedia-shopee-gaps
- 955-line comprehensive competitor analysis covering Shopee, Tokopedia, TikTok Shop, Lazada, Bukalapak, and Blibli
- Detailed fee structure comparison for 2026 with working Python fee calculator (code included)
- 14 sections covering platform-specific gaps, cross-platform systemic gaps, underserved segments, regulatory weaknesses, API/technical gaps
- 10 unserved needs identified (premium marketplace, seller OS, escrow, services marketplace, refurbished electronics, rural commerce, cross-border sourcing, tax compliance, algorithm decoder, AI content factory)
- 20+ sources cited from WebEkspor, CNBC Indonesia, Bisnis.com, Katadata, Celios, LPEM FEB UI, OJK, and regulatory documents
- Created new subfolder: 03-id-business-trends/competitors/
- Files: 03-id-business-trends/competitors/tokopedia-shopee-gaps.md

## 2026-06-22 , SP2KP pipeline migrated from browser extraction to REST API
- Discovered public SP2KP REST API at https://api-sp2kp.kemendag.go.id/ (no auth required)
- Key endpoints: `average-price/export-area-daily-json` for national prices, `master/api/variant` for commodity list, `master/api/wilayah` for regions
- API returns 54 commodities (Barang Kebutuhan Pokok) vs browser's 17, at national level (no Region A/B/C breakdown)
- API is fast (under 5s) compared to browser navigation (5-15s + JS execution)
- Created fetch_sp2kp.py as the new fetcher script
- Updated prompt file with API-based workflow as primary, browser as fallback
- NOTE: Region A/B/C sub-row data is only available via browser extraction, not via the public API
- Data files: sp2kp-2026-06-19.json (54 commodities, API-derived)

## 2026-06-22 , enrich(03): fastwork-sribu-freelance-gaps
- 863-line competitor analysis of Fastwork vs Sribu vs Projects.co.id vs Upwork/Fiverr for the Indonesian freelance market
- Mapped technical architectures (Fastwork: Next.js + Algolia + Firebase; Sribu: Next.js + UpCloud + Freshworks; Projects.co.id: legacy PHP)
- Identified 10 specific gaps: no API/MCP, no cross-platform reputation, no WhatsApp-native workflow, no B2B procurement, no tax integration, no government program integration, no AI-native workflows, no regulated escrow, no skills verification, no offline-first mobile
- Detailed 10 commercial opportunities ranked by viability with market size estimates
- Coverage: payment structural weaknesses (regulated escrow gap, BI-FAST, FX problem), trust/reputation flaws, regulatory exposure (PSE, OJK, Kominfo, DJP), and AI agent integration failure points

## 2026-06-23 , enrich(07): regional-rice-arbitrage-aggregator
- 858-line opportunity one-pager for a B2B marketplace that exploits the 31.3% price gap for Beras Medium between SP2KP Region A and Region C
- Concrete transaction model: 8-ton FTL truckload from Sulawesi to Papua yields Rp33.4M gross arbitrage value at Rp4,171/kg gap, minus Rp2,500-4,000/kg logistics cost = Rp8-16M net margin
- Three-layer product architecture: (1) SP2KP API-powered price discovery, (2) FTL logistics aggregation via Kargo Technologies partnerships, (3) bank escrow trust infrastructure
- All 16 SP2KP commodities analyzed for regional gaps (cabai 53-68%, bawang merah 55%, telur 21%, daging sapi 13%)
- Year 3 revenue target Rp15.6B from transaction fees + subscriptions, Year 5 target Rp20-40B adding data licensing
- 6 new gaps discovered: logistics cost benchmarks, SNI quality lab coverage, pesantren procurement behavior, SP2KP API regional endpoint, cross-province trade docs, and API reliability monitoring
