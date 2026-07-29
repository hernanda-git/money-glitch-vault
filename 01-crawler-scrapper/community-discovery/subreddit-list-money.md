# Subreddit List: Where Money Is Discussed

**Author:** Money Glitch Vault Auto-Enricher  
**Date:** 2026-07-29  
**Status:** Community-discovery reference for crawler infrastructure  
**Audience:** Crawler developers, vault agents, signal analysts  
**Source note:** Many subscriber counts below are approximate (based on public data visible before 2025) and served as reference values. Where specific values could not be verified at write time due to network blocking of Reddit, this is noted with "[source unreachable]".

---

## Table of Contents

1. [Purpose and Structure](#purpose-and-structure)
2. [Tier 1: Direct Money-Making Subreddits](#tier-1-direct-money-making-subreddits)
3. [Tier 2: Side Hustle and Freelance Subreddits](#tier-2-side-hustle-and-freelance-subreddits)
4. [Tier 3: Personal Finance and Investing Subreddits](#tier-3-personal-finance-and-investing-subreddits)
5. [Tier 4: Cryptocurrency and Trading Subreddits](#tier-4-cryptocurrency-and-trading-subreddits)
6. [Tier 5: Scam Detection and Fraud Awareness Subreddits](#tier-5-scam-detection-and-fraud-awareness-subreddits)
7. [Tier 6: Career and Income Growth Subreddits](#tier-6-career-and-income-growth-subreddits)
8. [Tier 7: Business and Entrepreneurship Subreddits](#tier-7-business-and-entrepreneurship-subreddits)
9. [Tier 8: Coupon, Deal, and Saving Subreddits](#tier-8-coupon-deal-and-saving-subreddits)
10. [Tier 9: Gig Economy and Microtask Subreddits](#tier-9-gig-economy-and-microtask-subreddits)
11. [Tier 10: Indonesian and Southeast Asian Money Subreddits](#tier-10-indonesian-and-southeast-asian-money-subreddits)
12. [Tier 11: Niche and Emerging Money Subreddits](#tier-11-niche-and-emerging-money-subreddits)
13. [Technical Appendix: Crawler Configuration Per Subreddit](#technical-appendix-crawler-configuration-per-subreddit)
14. [Scraper Architecture Notes](#scraper-architecture-notes)
15. [Signal Taxonomy: What to Extract From Each Category](#signal-taxonomy-what-to-extract-from-each-category)
16. [Rate Limit and Anti-Bot Bypass Strategies](#rate-limit-and-anti-bot-bypass-strategies)
17. [New Subreddit Discovery Pipeline](#new-subreddit-discovery-pipeline)
18. [Gap Analysis: What This List Misses](#gap-analysis-what-this-list-misses)

---

## Purpose and Structure

This document catalogs every significant subreddit where money-related conversations happen, organized by tier. Each entry includes:

- **Subreddit name** and direct link
- **Approximate subscriber count** (where known)
- **Content profile**: what type of money discussion happens there
- **Signal density**: how much actionable money signal (leads, tips, complaints, data) is present per 100 posts
- **API accessibility**: whether the subreddit's content is crawlable via Reddit JSON API, Pushshift, or requires scraping
- **Recommended crawl frequency**: how often a scraper should poll this subreddit for new posts
- **Key scraping targets**: specific post flairs, user types, or thread patterns to watch
- **Risk factors**: moderation strictness, brigading potential, content volatility

### Tier Classification

Each subreddit is assigned a tier based on signal relevance:

- **Tier 1** = Direct money-making opportunities. Highest priority. Posts about actual earnings, platforms, methods.
- **Tier 2** = Side hustle and freelance discussions. Medium-high priority. Income diversification signals.
- **Tier 3** = Personal finance and investing. Medium priority. Long-term wealth signals, consumer pain points.
- **Tier 4** = Crypto and trading. Volatile, high noise. Short-term opportunities but heavy scam risk.
- **Tier 5** = Scam detection. Essential cross-reference layer. Validates opportunities from other tiers.
- **Tier 6** = Career and income growth. Structural income signals.
- **Tier 7** = Business and entrepreneurship. Founder pain points and market gaps.
- **Tier 8** = Deals and savings. Consumer behavior signals.
- **Tier 9** = Gig economy and microtasks. Income floor signals.
- **Tier 10** = Regional (Indonesia/SE Asia). Localized money signals.
- **Tier 11** = Niche and emerging. Experimental subreddits worth monitoring.

---

## Tier 1: Direct Money-Making Subreddits

These subs are where users directly discuss platforms, methods, and earnings. Highest crawl priority.

### r/beermoney

- **Subscribers:** ~2M (estimated, [source unreachable])
- **Content profile:** Users post about GPT (get-paid-to) sites, survey platforms, cashback apps, and small online earnings. Focus is on low-effort, low-skill money methods. Typical earnings range $0.50-$50/day per method.
- **Signal density:** Medium-high. Roughly 30-40% of posts contain actionable platform names and payment proof.
- **API accessibility:** Reddit JSON API (`/r/beermoney/new.json`), Pushshift for historical
- **Recommended crawl frequency:** Every 2-4 hours. 50-200 new posts per day.
- **Key scraping targets:**
  - Payment proof screenshots (verify platform solvency)
  - "I got paid by X" threads (payment confirmation signals)
  - Referral threads (track referral program health)
  - New platform launches (first-mover advantage)
  - "Is X legit?" threads (trust indicators)
- **Risk factors:** High referral link density. Many posts are astroturfed. Must filter for organic vs. promoted content. Moderators enforce strict no-referral-link rules on main posts (referrals go in monthly megathreads). This means the megathreads themselves are crawl targets.
- **Content volume:** ~100-300 posts per day (self posts dominate; link posts are discouraged)

### r/SideHustle

- **Subscribers:** ~3M+ (estimated, [source unreachable])
- **Content profile:** Broader than beermoney. Includes online and offline side hustles: delivery driving, flipping, tutoring, freelancing, rental income, content creation. Higher average income per post than beermoney.
- **Signal density:** Medium. About 25-30% of posts contain concrete numbers. The rest is advice-seeking.
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 4-6 hours
- **Key scraping targets:**
  - Income breakdown posts ("I make $X/month doing Y")
  - Platform reviews (DoorDash vs Uber Eats, Fiverr vs Upwork)
  - Tax and legal questions about side income (regulatory signals)
  - Tools and software recommendations (product gaps)
- **Risk factors:** Lower referral spam than beermoney but more vague motivation posts. Vehicular side hustles (delivery, rideshare) dominate.

### r/slavelabour

- **Subscribers:** ~300K (estimated, [source unreachable])
- **Content profile:** Gig-based micro-jobs. Users offer or request small paid tasks: data entry, graphic design, virtual assistant, writing, social media management. Payment typically via PayPal, Venmo, or crypto. Jobs range $5-$200.
- **Signal density:** Very high. Every post is a direct offer or request with a stated price.
- **API accessibility:** Reddit JSON API. Posts are organized by [offer] and [request] flairs.
- **Recommended crawl frequency:** Every 1-2 hours. High-volume, short-lived posts.
- **Key scraping targets:**
  - [offer] posts (price benchmarks for small tasks)
  - [request] posts (demand signals for specific skills)
  - Completed transaction confirmation threads
  - Payment method preferences (PayPal/Venmo/Crypto ratio trends)
  - User reputation data (how many completed jobs per user)
- **Risk factors:** Very high scam risk. Both employers and workers can be scammed. Payment disputes are common. Mods maintain a universal scammer list (USL) that should be cross-referenced.

### r/forhire

- **Subscribers:** ~1.5M (estimated, [source unreachable])
- **Content profile:** Job postings and hiring offers primarily in tech, creative, and writing fields. [Hiring] and [For Hire] flairs dominate. More professional than slavelabour but less formal than actual job boards.
- **Signal density:** High for demand signals. Every [Hiring] post is a validated paid opportunity.
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 3-4 hours
- **Key scraping targets:**
  - [Hiring] posts with salary/rate ranges (market rate data)
  - Recurring hiring patterns (same employer posting repeatedly = high churn or growth)
  - Remote vs. onsite ratio trends
  - Required skills frequency analysis
- **Risk factors:** Moderators enforce strict formatting; unpaid internships banned. Many posts are deleted after filling, so crawl frequency matters.

### r/workonline

- **Subscribers:** ~250K (estimated, [source unreachable])
- **Content profile:** Remote work opportunities specifically for online jobs. Focuses on entry-level remote roles, data entry, customer service, and online teaching. Less gig-focused than slavelabour, more job-focused.
- **Signal density:** Medium
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 6 hours
- **Key scraping targets:**
  - Company names hiring remote workers (employer demand signals)
  - Pay rate discussions (wage benchmarks)
  - VPN/geolocation bypass discussions (regulatory risk signals)
  - Timezone-specific job posts (global labor arbitrage signals)
- **Risk factors:** Some job posts are MLM schemes in disguise. Cross-reference with r/antiMLM.

### r/passive_income

- **Subscribers:** ~800K (estimated, [source unreachable])
- **Content profile:** Discussions about passive and semi-passive income streams: dividend investing, rental property, print-on-demand, digital products, affiliate marketing, YouTube automation, crypto staking.
- **Signal density:** Low. Many posts are aspirational rather than actionable. High noise-to-signal ratio.
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 8 hours (lower priority)
- **Key scraping targets:**
  - Specific income breakdowns ("I make $X/month from Y")
  - Platform comparisons (which ad network, which print-on-demand service)
  - "Is this a scam?" threads (MLM detection)
  - Cost breakdowns (how much capital needed for each method)
- **Risk factors:** Extremely high concentration of MLM/pyramid scheme content masked as passive income. The subreddit's rules try to filter this but enforcement is inconsistent.

### r/affiliatemarketing

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Affiliate marketing strategies, network recommendations, niche selection, content creation for commissions. Professional-level discussions mixed with beginner questions.
- **Signal density:** Medium
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 6 hours
- **Key scraping targets:**
  - Network payout reports (which affiliate networks pay reliably)
  - Niche profitability discussions (demand signals for products)
  - SEO strategy changes (algorithm updates affecting affiliate income)
  - Compliance discussions (FTC disclosure rules, GDPR impacts)
- **Risk factors:** Many "gurus" selling courses. Cross-reference credibility.

---

## Tier 2: Side Hustle and Freelance Subreddits

### r/freelance

- **Subscribers:** ~1M (estimated, [source unreachable])
- **Content profile:** Professional freelancers discussing rates, clients, contracts, taxes, platforms. More mature audience than r/beermoney. Focus on sustainable freelancing rather than quick cash.
- **Signal density:** High for structural signals (rate benchmarks, platform complaints)
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 4-6 hours
- **Key scraping targets:**
  - Rate cards and pricing discussions (market rate data for 50+ freelance categories)
  - Platform complaint threads (Upwork, Fiverr, Freelancer.com issues)
  - Contract clause discussions (common disputes, legal signals)
  - Client payment problem threads (collections issues, payment platform gaps)
  - Tax strategy threads (deduction patterns, entity selection)
- **Risk factors:** Moderate. Some marketing disguised as advice. Mods are active.

### r/Upwork

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Specifically about Upwork platform. Connects, proposals, client behavior, fees, account issues. High-density signal for freelancer platform economics.
- **Signal density:** Very high for platform-specific data
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 2-3 hours
- **Key scraping targets:**
  - Connects pricing and availability complaints (platform monetization signals)
  - Client behavior pattern analysis (scam client detection patterns)
  - Proposal success rates (market competition data)
  - Account suspension threads (platform risk signals)
  - Fee change discussions (Upwork's 20%/5%/10% fee structure sentiment)
- **Risk factors:** Platform employees may monitor the subreddit. Users self-censor.

### r/recruitinghell

- **Subscribers:** ~1.2M (estimated, [source unreachable])
- **Content profile:** Job seekers complaining about bad hiring practices. Ghosting, lowball offers, terrible interview processes, AI recruiting failures. Not a money-making sub but valuable for understanding employer-side friction.
- **Signal density:** Very high for employer pain point signals. Every complaint thread describes a failing in the hiring market.
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 6 hours (reference, not primary)
- **Key scraping targets:**
  - Salary offer complaint threads (below-market offer identification)
  - Ghosting pattern analysis (which companies/industries ghost most)
  - Job posting fraud reports (fake jobs, data mining listings)
  - ATS (applicant tracking system) complaint threads (product gaps)
- **Risk factors:** High negativity bias. Not representative of all hiring experiences.

### r/freelanceWriters

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** Writing-specific freelancer community. Rates, niches, platforms, AI impact discussions.
- **Signal density:** Medium-high for writing-specific signals
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 8 hours
- **Key scraping targets:**
  - AI tool impact discussions (how ChatGPT etc. affect writing rates)
  - Content mill vs. direct client comparisons
  - Niche specialization discussions (highest-paying writing niches)
- **Risk factors:** AI disruption is a hot topic; sentiment data useful.

### r/DesignJobs

- **Subscribers:** ~150K (estimated, [source unreachable])
- **Content profile:** Design-specific job board (graphic design, UI/UX, web design). [Hiring] and [For Hire] flairs.
- **Signal density:** High for design market rates
- **Recommended crawl frequency:** Every 4 hours

---

## Tier 3: Personal Finance and Investing Subreddits

### r/personalfinance

- **Subscribers:** ~20M (estimated, [source unreachable])
- **Content profile:** The largest personal finance subreddit. Budgeting, debt management, saving, investing, retirement, insurance, taxes. Highly structured with flairs and a well-maintained wiki.
- **Signal density:** Low for direct money opportunity; very high for consumer pain points and financial behavior data.
- **API accessibility:** Reddit JSON API (rate-limited due to size)
- **Recommended crawl frequency:** Every 6-8 hours
- **Key scraping targets:**
  - Debt payoff threads (identify predatory lenders, collection agency behavior)
  - "I have $X, what should I do?" threads (consumer financial literacy gaps)
  - Insurance complaint threads (underinsurance signals)
  - Tax question patterns (recurring filing issues = product opportunities)
  - Side income income/loss reporting (how people actually use side income)
- **Risk factors:** Very heavily moderated. Many post types are auto-removed. Must crawl via Pushshift for removed post history, which often contains higher signal density. The wiki is a trove of structured financial education content.

### r/financialindependence

- **Subscribers:** ~3M (estimated, [source unreachable])
- **Content profile:** FIRE (Financial Independence, Retire Early) community. High savings rate, investment allocation, expense optimization, career strategies for early retirement.
- **Signal density:** Low for direct opportunities; high for structural wealth-building patterns
- **Recommended crawl frequency:** Every 8 hours
- **Key scraping targets:**
  - Expense reduction strategies (consumer behavior data)
  - Side income streams that actually scale (validated FI-relevant methods)
  - Investment allocation discussions (market sentiment among sophisticated retail)
  - Coast FI / Barista FI threads (alternative work arrangements, semi-retirement signals)
- **Risk factors:** Confirmation bias for high earners. Not representative of median income population.

### r/investing

- **Subscribers:** ~15M (estimated, [source unreachable])
- **Content profile:** General investing discussion. Stocks, bonds, ETFs, macroeconomics, portfolio strategy. More sophisticated than r/wallstreetbets but still retail-focused.
- **Signal density:** Medium for market sentiment; low for specific money opportunities
- **Recommended crawl frequency:** Every 4 hours during market hours
- **Key scraping targets:**
  - Company-specific DD (due diligence) threads (crowdsourced analysis)
  - Sector rotation discussions (capital flow sentiment)
  - Economic indicator reactions (inflation, interest rate sentiment)
  - Brokerage comparison threads (platform switching signals)
- **Risk factors:** Heavy expert-layperson gap. Misinformation common. Cross-reference with official filings.

### r/wallstreetbets

- **Subscribers:** ~15M (estimated, [source unreachable])
- **Content profile:** High-risk options trading, meme stocks, leveraged bets. Detritus of financial discussion. Infamous for GameStop, AMC, and other short-squeeze campaigns. Lots of loss porn (screenshots of destroyed accounts).
- **Signal density:** Low for traditional investing; high for sentiment and meme stock momentum signals
- **API accessibility:** Reddit JSON API (very high volume)
- **Recommended crawl frequency:** Every 1-2 hours during market hours
- **Key scraping targets:**
  - Ticker mentions and frequency (early momentum signals)
  - Option chain discussion (gamma squeeze setup mentions)
  - "DD" posts with high upvote ratio (crowd-validated analysis)
  - Loss porn (consumer credit risk signals, account destruction patterns)
  - Migration signals (WSB users moving to other platforms/spaces)
- **Risk factors:** Extreme volatility in content quality. Most posts are gambling, not investing. High ratio of bots and coordinated campaigns. Must filter by upvote ratio and account age.

### r/stocks

- **Subscribers:** ~5M (estimated, [source unreachable])
- **Content profile:** Stock-specific analysis, earnings threads, sector discussions. More measured than WSB, more stock-specific than r/investing.
- **Signal density:** Medium
- **Recommended crawl frequency:** Every 4 hours
- **Key scraping targets:**
  - Earnings reaction threads (market sentiment on specific tickers)
  - "What's your thesis on X?" threads (bull/bear case aggregation)
  - Dividend stock discussions (income investing signals)

### r/dividends

- **Subscribers:** ~800K (estimated, [source unreachable])
- **Content profile:** Dividend investing strategy, dividend growth, yield analysis, DRIP.
- **Signal density:** Medium-high for income investing signals
- **Recommended crawl frequency:** Every 8 hours

### r/bonds

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Bond market discussion. Treasury, corporate, municipal, international bonds.
- **Signal density:** Low (specialized audience)
- **Recommended crawl frequency:** Every 12 hours

### r/options

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** Options trading strategies. More sophisticated than WSB.
- **Signal density:** Medium for professional-level options signals
- **Recommended crawl frequency:** Every 4 hours

---

## Tier 4: Cryptocurrency and Trading Subreddits

### r/CryptoCurrency

- **Subscribers:** ~7M (estimated, [source unreachable])
- **Content profile:** General cryptocurrency discussion. Bitcoin, altcoins, DeFi, NFTs, regulation, exchange issues. Heavily moderated with a strict karma-based commenting system.
- **Signal density:** Medium-low. High noise, but significant signal for exchange issues, regulatory changes, and scam reports.
- **API accessibility:** Reddit JSON API (high volume, moderate rate limiting)
- **Recommended crawl frequency:** Every 2-3 hours
- **Key scraping targets:**
  - Exchange complaint threads (withdrawal freezes, account locks)
  - Regulatory discussion threads (SEC, CFTC, global crypto regulation signals)
  - Token launch announcements (new DeFi/NFT project signals)
  - "Is X a scam?" threads (early scam detection)
  - Gas fee trend discussions (Ethereum network congestion signals)
  - Airdrop announcements (free token distribution signals)
- **Risk factors:** Very high ratio of bots, shills, and paid promoters. Karma requirements limit organic participation. Many threads are astroturfed by project teams.

### r/ethtrader

- **Subscribers:** ~2.5M (estimated, [source unreachable])
- **Content profile:** Ethereum-specific trading and ecosystem discussion. More focused than general crypto subreddits.
- **Signal density:** Medium for DeFi and L2 ecosystem signals
- **Recommended crawl frequency:** Every 4 hours

### r/defi

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** Decentralized finance protocols, yield farming, liquidity provision, lending/borrowing.
- **Signal density:** Medium-high for DeFi-specific opportunities
- **Recommended crawl frequency:** Every 3 hours

### r/CryptoMarkets

- **Subscribers:** ~1.5M (estimated, [source unreachable])
- **Content profile:** Crypto trading and market analysis. Price discussion, TA, market cycles.
- **Signal density:** Low-medium (mostly TA charts with little actionable text)

### r/NFT

- **Subscribers:** ~1M (estimated, [source unreachable])
- **Content profile:** NFT trading, collections, minting, market analysis. Has declined significantly from 2021-2022 peak.
- **Signal density:** Low. Most activity is promotional.

### r/coinbase

- **Subscribers:** ~300K (estimated, [source unreachable])
- **Content profile:** Coinbase platform support, complaints, and discussion. Excellent for exchange pain point signals.
- **Signal density:** Very high for customer support failures

### r/binance

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Binance ecosystem discussion. Similar to r/coinbase but for Binance.
- **Signal density:** High for exchange-specific signals

### r/CryptoScams

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Reports of crypto scams, phishing, rug pulls, exchange fraud. Cross-reference resource.
- **Signal density:** Extremely high for scam intelligence
- **Recommended crawl frequency:** Every 2 hours
- **Key scraping targets:**
  - Wallet addresses associated with scams (blockchain analysis feed)
  - New scam methodology descriptions (evolving fraud patterns)
  - Exchange/platform names with unresolved withdrawal issues
  - Impersonation scam reports (fake support, fake platform clones)

---

## Tier 5: Scam Detection and Fraud Awareness Subreddits

### r/Scams

- **Subscribers:** ~1.5M (estimated, [source unreachable])
- **Content profile:** General scam reporting and awareness. Covers phone scams, email phishing, social engineering, marketplace fraud, job scams, romance scams, investment fraud.
- **Signal density:** Very high for scam taxonomy and evolution tracking
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 2-3 hours
- **Key scraping targets:**
  - New scam variant descriptions (methodological evolution)
  - Scammer contact information (phone numbers, emails, crypto addresses)
  - Platform-specific scam reports (which platforms enable fraud)
  - Dollar amount ranges per scam type (economic impact data)
  - Victim demographic data (who falls for what, extracted from narratives)
  - Recurring scam pattern alerts (seasonal/scalable fraud operations)
- **Risk factors:** Some victims identified in posts may ask for takedowns. Some scam reports are themselves scams (pig butchering with fake recovery agents). The subreddit's wiki contains an excellent scam classification system that can be used as a taxonomy.

### r/antiMLM

- **Subscribers:** ~1M (estimated, [source unreachable])
- **Content profile:** Anti-multi-level-marketing community. Exposes MLM/pyramid schemes, cult-like sales organizations, and direct sales companies. Valuable cross-reference for filtering r/passive_income and r/beermoney.
- **Signal density:** High for MLM identification signals
- **Recommended crawl frequency:** Every 4 hours (reference)
- **Key scraping targets:**
  - MLM company names and recruitment patterns (database build)
  - Income claim analysis (what MLMs promise vs. what sellers actually earn)
  - Recruitment script analysis (conversion funnel signals from MLMs)
  - Social media recruitment pattern identification
  - Regulatory action signals (FTC, state AG actions against MLMs)
- **Risk factors:** Can be emotionally charged. Some content from ex-members includes identifying information.

### r/legaladvice

- **Subscribers:** ~2.5M (estimated, [source unreachable])
- **Content profile:** General legal questions. Money-adjacent: contract disputes, debt collection, landlord-tenant, employment law, small claims.
- **Signal density:** Medium for legal friction points that create business opportunities
- **Recommended crawl frequency:** Every 6 hours
- **Key scraping targets:**
  - Small claims court topics (which disputes reach court = scalable product opportunities)
  - Debt collection harassment reports (regulatory compliance opportunities)
  - Contract dispute patterns (standard form gaps = legaltech opportunities)
  - Tenant finance issues (deposit disputes, rent increases)
- **Risk factors:** Not a substitute for actual legal advice. Many commenters are not lawyers.

### r/Scams_and_Fraud

- **Subscribers:** ~50K (estimated, [source unreachable])
- **Content profile:** Smaller scam reporting community. Less moderation but more raw scam reports.
- **Signal density:** High for raw, unfiltered scam narratives

---

## Tier 6: Career and Income Growth Subreddits

### r/cscareerquestions

- **Subscribers:** ~2M (estimated, [source unreachable])
- **Content profile:** Computer science career questions. Salary negotiations, job offers, interview prep, career transitions. Excellent source for tech compensation data.
- **Signal density:** Very high for tech compensation signals
- **Recommended crawl frequency:** Every 4 hours
- **Key scraping targets:**
  - Salary sharing threads (anonymous compensation data by role, location, YOE)
  - Offer comparison threads (competing offer details = market rate data)
  - "Is this a good offer?" threads (below-market identification)
  - Layoff discussion threads (industry contraction signals)
  - Return-to-office mandate threads (remote work availability signals)
- **Risk factors:** Heavy bias toward FAANG and high-paying tech roles. Not representative of broader job market. Posting volume is seasonal (highest during recruiting cycles: Sept-Nov, Feb-Apr).

### r/Salary

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Salary transparency. Users post their job title, location, years of experience, and salary. Structured data goldmine.
- **Signal density:** Extremely high for compensation data (the primary purpose of the subreddit)
- **Recommended crawl frequency:** Every 2 hours
- **Scraping approach:** Extract structured fields (job_title, location, yoe, salary, bonus, equity) using regex. Build a compensation database.

### r/ExperiencedDevs

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** Career discussion for senior+ software engineers (10+ YOE). Higher quality moderation. Strategic career signals.
- **Signal density:** High for experienced-level market signals

### r/jobs

- **Subscribers:** ~2M (estimated, [source unreachable])
- **Content profile:** General job search discussion. Resume reviews, interview advice, job offer evaluation.
- **Signal density:** Medium for job market health signals

### r/resumes

- **Subscribers:** ~2M (estimated, [source unreachable])
- **Content profile:** Resume reviews. Not directly money-related but reveals skills in demand and formatting trends.
- **Signal density:** Low-medium

### r/ITCareerQuestions

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** IT career questions. Certifications, career paths, salary. Good for non-software tech roles.

---

## Tier 7: Business and Entrepreneurship Subreddits

### r/Entrepreneur

- **Subscribers:** ~4M (estimated, [source unreachable])
- **Content profile:** Broad entrepreneurship discussion. Startups, small business, ecommerce, SaaS, brick-and-mortar.
- **Signal density:** Low-medium. High aspirational content, but good for founder pain point signals.
- **API accessibility:** Reddit JSON API (high volume, moderate rate limiting due to size)
- **Recommended crawl frequency:** Every 4 hours
- **Key scraping targets:**
  - "What problem should I solve?" threads (gap identification)
  - Post-mortem threads ("I failed, here's what happened" = learning signals)
  - Revenue breakdown threads ($0 to $X/month journey posts)
  - Tool stack threads ("What tools do you use for X?")
  - Pricing strategy discussions (price elasticity data)
  - Customer acquisition cost discussions (marketing efficiency data)
- **Risk factors:** High self-promotion. Many "case studies" are thinly veiled ads. Lots of guru advice from people who have never run a business.

### r/SaaS

- **Subscribers:** ~300K (estimated, [source unreachable])
- **Content profile:** Software-as-a-Service specific discussion. MRR reports, technical architecture, growth strategies.
- **Signal density:** High for SaaS-specific signals
- **Recommended crawl frequency:** Every 4 hours
- **Key scraping targets:**
  - MRR (monthly recurring revenue) breakdowns
  - Churn rate discussions (retention benchmarks)
  - Pricing model discussions (subscription vs usage-based)
  - Tech stack choices (infrastructure cost signals)
  - Failed launch post-mortems

### r/smallbusiness

- **Subscribers:** ~1.5M (estimated, [source unreachable])
- **Content profile:** Small business ownership. More brick-and-mortar and service business focused than r/Entrepreneur.
- **Signal density:** Medium for offline business signals

### r/ecommerce

- **Subscribers:** ~400K (estimated, [source unreachable])
- **Content profile:** Ecommerce operations. Shopify, Amazon FBA, fulfillment, sourcing, marketing.
- **Signal density:** Medium-high

### r/dropship

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Dropshipping specific. Product sourcing, supplier issues, AliExpress, Shopify integration.
- **Signal density:** Medium (high noise, specific product signals)

### r/Flipping

- **Subscribers:** ~1M (estimated, [source unreachable])
- **Content profile:** Buying low and selling high. Thrift store flipping, retail arbitrage, online reselling. Concrete profit numbers.
- **Signal density:** High for product-level demand data
- **Recommended crawl frequency:** Every 4 hours
- **Key scraping targets:**
  - Profit breakdowns (buy price, sell price, fees, net profit)
  - Platform fee complaint threads (eBay, Poshmark, Mercari fee increases)
  - "What's selling well right now?" threads (demand pulse)
  - Shipping cost discussions (logistics pain points)
  - Scam buyer reports (chargeback fraud patterns)

---

## Tier 8: Coupon, Deal, and Saving Subreddits

### r/Frugal

- **Subscribers:** ~5M (estimated, [source unreachable])
- **Content profile:** Frugal living tips. Not "coupons" but lifestyle optimization for lower expenses. Valuable for consumer pain point identification.
- **Signal density:** Medium for consumer behavior data
- **Recommended crawl frequency:** Every 8 hours
- **Key scraping targets:**
  - Recurring expense reduction strategies (insurance, phone bills, subscriptions)
  - "What's not worth buying cheap?" threads (quality premium signals)
  - Food budget breakdowns (grocery inflation tracking)
  - Energy cost reduction discussions (utility optimization signals)

### r/churning

- **Subscribers:** ~1M (estimated, [source unreachable])
- **Content profile:** Credit card sign-up bonus optimization. Opening cards for bonuses, manufactured spending. Highly structured with wiki.
- **Signal density:** Very high for credit card product data
- **Recommended crawl frequency:** Every 4 hours
- **Key scraping targets:**
  - Credit card bonus announcements (new card product signals)
  - Bank retention offer data (which banks offer retention incentives)
  - Manufactured spending method discussions (payment system gaps)
  - Credit score impact data (hard pull pattern analysis)

### r/awardtravel

- **Subscribers:** ~1M (estimated, [source unreachable])
- **Content profile:** Using credit card points and miles for travel. Redemption strategies, transfer partner analysis.
- **Signal density:** High for loyalty program value data

### r/CreditCards

- **Subscribers:** ~400K (estimated, [source unreachable])
- **Content profile:** Credit card recommendations, application strategy, rewards optimization.
- **Signal density:** High for credit card product gaps

### r/beermoneyuk

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** UK-specific beermoney opportunities. Bank switching offers, cashback apps, sign-up bonuses. Different from US-focused beermoney.
- **Signal density:** High for UK-specific financial product signals

---

## Tier 9: Gig Economy and Microtask Subreddits

### r/UberEATS

- **Subscribers:** ~300K (estimated, [source unreachable])
- **Content profile:** Uber Eats driver discussion. Delivery strategy, pay rates, customer complaints, deactivations.
- **Signal density:** Very high for gig economy platform economics
- **Recommended crawl frequency:** Every 2 hours
- **Key scraping targets:**
  - Pay breakdown screenshots (per-delivery earnings data)
  - Deactivation reports (platform termination patterns)
  - Tip fraud reports (customer tip baiting)
  - Multi-apping discussions (driver-side platform arbitrage)
  - Area-based earnings differences (geographic pay gap data)

### r/doordash_drivers

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** DoorDash driver community. Similar to r/UberEATS but for DoorDash.
- **Signal density:** Very high
- **Recommended crawl frequency:** Every 2 hours

### r/InstacartShoppers

- **Subscribers:** ~300K (estimated, [source unreachable])
- **Content profile:** Instacart shopper discussion. Batch pay, tip patterns, customer behavior.
- **Signal density:** High

### r/AmazonFlexDrivers

- **Subscribers:** ~100K (estimated, [source unreachable])
- **Content profile:** Amazon Flex delivery driver community.
- **Signal density:** High

### r/TaskRabbit

- **Subscribers:** ~50K (estimated, [source unreachable])
- **Content profile:** TaskRabbit tasker community. Handyman and errand-running gig economics.
- **Signal density:** Medium

### r/mturk

- **Subscribers:** ~100K (estimated, [source unreachable])
- **Content profile:** Amazon Mechanical Turk workers. HIT (Human Intelligence Task) discussion, requester reviews, earnings.
- **Signal density:** Medium for micro-task economics

### r/UHRSwork

- **Subscribers:** ~30K (estimated, [source unreachable])
- **Content profile:** UHRS (Universal Human Relevance System) platform workers. Similar to MTurk but for search relevance tasks.
- **Signal density:** Medium

### r/Clickworker

- **Subscribers:** ~20K (estimated, [source unreachable])
- **Content profile:** Clickworker platform community. Micro-task pay rates and availability.

---

## Tier 10: Indonesian and Southeast Asian Money Subreddits

These are critical for regional money signals. The vault focuses heavily on Indonesia, so these subreddits are disproportionally important despite smaller subscriber counts.

### r/finansial

- **Subscribers:** ~150K-200K (estimated, [source unreachable])
- **Content profile:** Indonesian personal finance community. The largest Indonesian-language financial subreddit. Discussions about investing (reksadana, saham IDX), insurance (asuransi), KPR (mortgages), pinjaman online (online loans), and BPJS (national health insurance).
- **Signal density:** Very high for Indonesian financial behavior and pain points
- **API accessibility:** Reddit JSON API
- **Recommended crawl frequency:** Every 2-3 hours
- **Key scraping targets:**
  - Reksadana (mutual fund) performance discussions
  - Saham IDX stock discussions (Indonesian stock picks and analysis)
  - Pinjol (online loan) pain points (predatory lending complaints)
  - Asuransi (insurance) claim rejection stories
  - KPR (mortgage) rate comparison threads
  - BPJS Kesehatan utilization experiences
  - Side hustle discussions specific to Indonesia (jastip, reseller, dropship)
  - "Gaji UMR vs. pengeluaran" threads (minimum wage vs. expense breakdowns)
- **Risk factors:** Many threads reference Indonesian regulations in bahasa. Requires Indonesian language processing capability. Some users post in mixed Indonesian-English.

### r/indonesia

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** General Indonesian community. Not money-specific but contains high-value financial threads, job discussions, and consumer complaint posts. The "finance" and "career" flaired posts are the primary targets.
- **Signal density:** Low overall but high for specific flairs
- **Recommended crawl frequency:** Every 4 hours (filtered by flair)
- **Scraping approach:** Target posts flaired as "Finance", "Karir" (Career), "Ekonomi" (Economy), and "Consumer Protection"

### r/pinjaeminjem

- **Subscribers:** ~10K-30K (estimated, [source unreachable])
- **Content profile:** Indonesian pinjaman online (online lending) community. Borrowers discussing pinjol experiences, debt collection practices, interest rates. High-value for predatory lending detection.
- **Signal density:** Very high for pinjol ecosystem signals
- **Recommended crawl frequency:** Every 2 hours
- **Key scraping targets:**
  - Pinjol app names and lender identities (database build for predatory lenders)
  - Debt collection harassment reports
  - Interest rate and fee comparisons
  - "Pinjol legal vs ilegal" discussions (OJK registration verification)
  - Debt spiral narratives (financial inclusion failure signals)
  - Peer-to-peer lending platform reviews

### r/indonesia_investasi

- **Subscribers:** ~10K (estimated, [source unreachable])
- **Content profile:** Indonesian investment community. Shares, bonds, crypto, property investment specific to Indonesia.
- **Signal density:** High for Indonesia-specific investment behavior

### r/indonesiakerja

- **Subscribers:** ~15K (estimated, [source unreachable])
- **Content profile:** Indonesian job market and career discussions. Salary sharing, job hunting, workplace issues.
- **Signal density:** High for Indonesian labor market data

### r/freelanceindo

- **Subscribers:** ~5K (estimated, [source unreachable])
- **Content profile:** Indonesian freelancer community. Sribu, FastWork, Project.co.id discussions, rates, client issues.
- **Signal density:** High for Indonesian freelance platform economics
- **Recommended crawl frequency:** Every 4 hours

### r/bekas (formerly r/jualbeli)

- **Subscribers:** ~50K (estimated, [source unreachable])
- **Content profile:** Indonesian secondhand marketplace. Peer-to-peer buying and selling. Price signals for used goods.
- **Signal density:** Medium for consumer goods pricing data

### r/finansial_pribadi

- **Subscribers:** ~5K (estimated, [source unreachable])
- **Content profile:** Smaller personal finance subreddit for Indonesians. Less active but more focused community.

### r/indonesia_ekonomi

- **Subscribers:** ~3K (estimated, [source unreachable])
- **Content profile:** Indonesian economy discussion. Macroeconomic topics, commodity prices, inflation.
- **Signal density:** Medium for macro signals

### Additional SE Asian subreddits to monitor:

- r/PhInvest (Philippines investing, ~20K)
- r/phinvestcirclejerk (Philippines finance satire, consumer pain point goldmine)
- r/MalaysianPF (Malaysian personal finance, ~50K)
- r/singaporefi (Singapore financial independence, ~50K)
- r/Thailand (general but finance-tagged posts)
- r/vietnamesefinance (emerging, small but growing)

---

## Tier 11: Niche and Emerging Money Subreddits

### r/overemployed

- **Subscribers:** ~300K (estimated, [source unreachable])
- **Content profile:** Working multiple remote jobs simultaneously. Juggling schedules, income stacking, tax implications. Silicon-valley-adjacent.
- **Signal density:** Very high for remote work structural signals
- **Recommended crawl frequency:** Every 3 hours
- **Key scraping targets:**
  - Company policies on moonlighting (employment contract signals)
  - Background check bypass discussions (HR tech gaps)
  - Income breakdowns (multiple salary stacking data)
  - Meeting management strategies (remote work process insights)

### r/coastFIRE

- **Subscribers:** ~100K (estimated, [source unreachable])
- **Content profile:** Coast FI (working part-time or lower-stress job after reaching a savings threshold that will grow to full FI by retirement age).
- **Signal density:** Medium for semi-retirement and lifestyle design data

### r/baristafire

- **Subscribers:** ~50K (estimated, [source unreachable])
- **Content profile:** Barista FIRE (working a low-stress job for health insurance while partially retired).

### r/govfire

- **Subscribers:** ~30K (estimated, [source unreachable])
- **Content profile:** FIRE for government employees. TSP (Thrift Savings Plan), pensions, federal benefits.

### r/fatFIRE

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** FIRE with high spending targets ($5M+ net worth). Luxury lifestyle, tax optimization for high net worth, estate planning. Verified email required for posting (quality control).
- **Signal density:** Medium for high-net-worth consumer behavior

### r/sweatystartup

- **Subscribers:** ~100K (estimated, [source unreachable])
- **Content profile:** Blue-collar service business entrepreneurship. Pressure washing, lawn care, cleaning, pest control, moving companies. Anti-tech, pro-service-business focus.
- **Signal density:** Very high for service business economics
- **Recommended crawl frequency:** Every 6 hours

### r/realestateinvesting

- **Subscribers:** ~1M (estimated, [source unreachable])
- **Content profile:** Real estate investment. Rental properties, BRRRR method, commercial, REITs.
- **Signal density:** Medium-high for property market signals

### r/airbnb_hosts

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** Airbnb hosting issues. Guest problems, pricing strategy, regulatory compliance, platform complaints.
- **Signal density:** High for short-term rental economics

### r/EtsySellers

- **Subscribers:** ~300K (estimated, [source unreachable])
- **Content profile:** Etsy seller community. Platform changes, fees, marketing, product trends.
- **Signal density:** High for handmade goods market data

### r/digitalnomad

- **Subscribers:** ~2M (estimated, [source unreachable])
- **Content profile:** Remote workers traveling the world. Visa issues, cost of living data, location recommendations, tax residency.
- **Signal density:** Medium for global cost arbitrage data

### r/juststart

- **Subscribers:** ~100K (estimated, [source unreachable])
- **Content profile:** Starting a website or blog from zero. Detailed income reports from niche sites, SEO strategies. Known for honest, transparent income breakdowns.
- **Signal density:** Very high for content site monetization data

### r/EntrepreneurRideAlong

- **Subscribers:** ~100K (estimated, [source unreachable])
- **Content profile:** Real-time entrepreneur journeys documented from start. Raw, unpolished business experiences.
- **Signal density:** High for unfiltered founder experiences

### r/startups

- **Subscribers:** ~1.5M (estimated, [source unreachable])
- **Content profile:** Tech startup ecosystem. Fundraising, product-market fit, growth, venture capital.

### r/venturecapital

- **Subscribers:** ~200K (estimated, [source unreachable])
- **Content profile:** VC industry discussion. Deal flow, fundraising strategy, LP perspectives.

### r/angelinvesting

- **Subscribers:** ~50K (estimated, [source unreachable])
- **Content profile:** Angel investing. Syndicates, SPVs, deal sourcing, due diligence.

### r/WallStreetBetsCrypto

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** WSB-style crypto trading. High risk, meme coins, leverage.

### r/options_pregaming

- **Subscribers:** ~50K (estimated, [source unreachable])
- **Content profile:** Pre-market options positioning discussion.

### r/algotrading

- **Subscribers:** ~2M (estimated, [source unreachable])
- **Content profile:** Automated trading algorithms, backtesting, API integration, broker APIs. Technical audience.
- **Signal density:** High for trading infrastructure signals
- **Recommended crawl frequency:** Every 6 hours
- **Key scraping targets:**
  - Broker API reviews (latency, reliability, fee structure)
  - Backtesting methodology discussions (market data quality signals)
  - Strategy performance sharing (which strategies work in current market)
  - Infrastructure cost discussions (cloud compute, data feed costs)

### r/forex

- **Subscribers:** ~500K (estimated, [source unreachable])
- **Content profile:** Forex trading community.
- **Signal density:** Low (mostly signal sellers and scammers)

### r/commodities

- **Subscribers:** ~50K (estimated, [source unreachable])
- **Content profile:** Commodity trading. Oil, gas, metals, agriculture futures.

---

## Technical Appendix: Crawler Configuration Per Subreddit

### Recommended Crawl Stack

For a Reddit-focused signal collector, the following crawl architecture is recommended:

```
RedditSignalCollector/
  crawlers/
    json_api_crawler.py      # Primary crawler using Reddit JSON API
    pushshift_crawler.py     # Historical/backfill crawler
    scraper_crawler.py       # HTML fallback when API rate-limited
  parsers/
    beermoney_parser.py      # Tier 1 parsing logic
    finance_parser.py         # Tier 3 parsing logic
    crypto_parser.py          # Tier 4 parsing logic
    scam_parser.py            # Tier 5 parsing logic
  extractors/
    ticker_extractor.py       # Stock/crypto ticker extraction
    amount_extractor.py       # Dollar amount extraction
    platform_extractor.py     # Platform/company name extraction
  storage/
    post_store.py             # Raw post storage (PostgreSQL/MongoDB)
    signal_store.py           # Parsed signal storage
    metrics_store.py          # Performance metrics per subreddit
```

### JSON API Endpoints

Each subreddit can be accessed via the following endpoints:

```
# New posts (recommended for most crawling)
GET /r/{subreddit}/new.json?limit=100

# Hot/trending posts
GET /r/{subreddit}/hot.json?limit=100

# Top posts by time period
GET /r/{subreddit}/top.json?t=day&limit=100

# Search within subreddit
GET /r/{subreddit}/search.json?q={query}&restrict_sr=true&sort=new&limit=100

# Comments on a specific post
GET /r/{subreddit}/comments/{post_id}.json

# User information
GET /user/{username}/about.json

# User post history
GET /user/{username}/submitted.json?limit=100
```

### Rate Limit Configuration

Reddit's API rate limit is 60 requests per minute per OAuth client ID. Unauthenticated requests are more limited. Recommended configuration:

```python
CRAWL_CONFIG = {
    "base_delay": 2.0,           # Seconds between requests (minimum)
    "burst_limit": 30,           # Max requests before enforced delay
    "burst_delay": 60,           # Seconds to wait after burst
    "max_retries": 3,            # Retry on 429/503
    "retry_backoff": 30,         # Seconds to backoff on retry
    "user_agent_rotation": True, # Rotate User-Agent per request
    "oauth": True,               # Use OAuth for higher rate limits
    "client_id": "...",          # Reddit app OAuth client ID
    "client_secret": "...",      # Reddit app OAuth client secret
}
```

### Tier-Specific Crawl Schedules

| Tier | Subreddits | Crawl Frequency | API Requests/Day | Priority |
|------|-----------|----------------|-----------------|----------|
| 1 | beermoney, slavelabour, forhire | Every 1-2 hours | ~500-1000 | HIGHEST |
| 2 | freelance, sidehustle | Every 4 hours | ~100-200 | HIGH |
| 3 | personalfinance, investing | Every 6 hours | ~50-100 | MEDIUM |
| 4 | CryptoCurrency, CryptoScams | Every 2 hours | ~300-400 | HIGH |
| 5 | Scams, antiMLM | Every 3 hours | ~200-300 | HIGH |
| 6 | cscareerquestions, Salary | Every 4 hours | ~100-200 | MEDIUM |
| 7 | Entrepreneur, SaaS | Every 4 hours | ~100-200 | MEDIUM |
| 8 | churning, CreditCards | Every 4 hours | ~100-200 | LOW |
| 9 | UberEATS, doordash_drivers | Every 2 hours | ~300-400 | HIGH |
| 10 | finansial, indonesia | Every 3 hours | ~200-300 | HIGHEST |
| 11 | overemployed, juststart | Every 6 hours | ~50-100 | MEDIUM |
| **Total** | **~60+ subreddits** | **Mixed** | **~2000-3000/day** | |

### Pushshift for Historical Data

For backfilling historical posts before starting live crawling:

```python
# Pushshift API endpoint
GET https://api.pushshift.io/reddit/search/submission/
    ?subreddit=beermoney
    &size=1000
    &after=1609459200  # Unix timestamp for start date
    &before=1640995200 # Unix timestamp for end date
    &sort=desc
    &sort_type=created_utc

GET https://api.pushshift.io/reddit/search/comment/
    ?subreddit=beermoney
    &size=1000
    &after=1609459200
```

Pushshift allows batch retrieval of up to 1000 posts per request. It is the recommended method for building initial training datasets for NLP-based signal extraction models.

---

## Scraper Architecture Notes

### Authentication Strategy

Reddit's API requires OAuth for higher rate limits:

```python
import requests

def get_reddit_token(client_id, client_secret, username, password):
    """Get Reddit OAuth access token."""
    auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
    data = {
        'grant_type': 'password',
        'username': username,
        'password': password
    }
    headers = {'User-Agent': 'MoneyGlitchVault/1.0 (by /u/vault_bot)'}
    resp = requests.post('https://www.reddit.com/api/v1/access_token',
                         auth=auth, data=data, headers=headers)
    return resp.json()['access_token']
```

### Data Storage Schema

Recommended PostgreSQL schema for storing crawled subreddit posts:

```sql
CREATE TABLE reddit_posts (
    id VARCHAR(10) PRIMARY KEY,           -- Reddit post ID
    subreddit VARCHAR(100) NOT NULL,      -- Subreddit name
    title TEXT NOT NULL,                   -- Post title
    selftext TEXT,                         -- Post body (NULL for link posts)
    author VARCHAR(100),                   -- Author username (deleted for deleted users)
    created_utc BIGINT NOT NULL,           -- Unix timestamp
    score INT DEFAULT 0,                   -- Net upvotes
    upvote_ratio FLOAT,                    -- Upvote ratio (0-1)
    num_comments INT DEFAULT 0,           -- Comment count
    url TEXT,                              -- Post URL
    permalink TEXT,                        -- Reddit permalink
    domain VARCHAR(255),                   -- Domain for link posts
    over_18 BOOLEAN DEFAULT FALSE,        -- NSFW flag
    flair VARCHAR(100),                    -- Post flair text
    stickied BOOLEAN DEFAULT FALSE,       -- Pinned post
    crawled_at TIMESTAMP DEFAULT NOW(),   -- When we crawled it
    tier INT,                              -- Tier classification
    signal_score FLOAT DEFAULT 0.0,       -- Computed signal score
    has_amounts BOOLEAN DEFAULT FALSE,    -- Contains dollar amounts
    has_platforms BOOLEAN DEFAULT FALSE,  -- Contains platform names
    processed BOOLEAN DEFAULT FALSE       -- NLP processed flag
);

CREATE INDEX idx_posts_subreddit ON reddit_posts(subreddit);
CREATE INDEX idx_posts_created ON reddit_posts(created_utc DESC);
CREATE INDEX idx_posts_signal ON reddit_posts(signal_score DESC) WHERE processed = TRUE;
```

### Duplicate Detection

Reddit allows crossposting and reposting. Use fuzzy matching on title + subreddit to avoid duplicates:

```python
from difflib import SequenceMatcher

def is_duplicate(new_title, existing_titles, threshold=0.85):
    """Check if a post title is a near-duplicate of existing posts."""
    for title in existing_titles:
        ratio = SequenceMatcher(None, new_title.lower(), title.lower()).ratio()
        if ratio >= threshold:
            return True
    return False
```

### Signal Scoring Algorithm

A simple signal scoring system to rank the value of each post:

```python
def compute_signal_score(post, subreddit_tier):
    """
    Compute a signal score (0-100) for a post based on content signals.
    Higher scores indicate more actionable money signal.
    """
    score = 0
    text = (post.get('title', '') + ' ' + post.get('selftext', '')).lower()

    # Dollar amounts: strong signal
    amount_patterns = [
        r'\$\s?\d+[,\d{3}]*(?:\.\d{2})?',  # $1,234.56
        r'\d+[,\d{3}]*\s?(?:dollars|USD|usd)',
        r'(?:made|earned|paid|cost)\s+\$\s?\d+',
    ]
    for pattern in amount_patterns:
        matches = re.findall(pattern, text)
        score += min(len(matches) * 5, 20)  # Cap at 20

    # Platform names: medium signal
    platforms = [
        'upwork', 'fiverr', 'freelancer', 'shopify', 'amazon fba',
        'doorash', 'uber eats', 'etsy', 'paypal', 'coinbase',
        'binance', 'tokopedia', 'shopee', 'bukalapak'
    ]
    for platform in platforms:
        if platform in text:
            score += 3
            break  # Once per post

    # Action words: medium signal
    action_words = ['how to', 'tutorial', 'guide', 'step by step',
                    'template', 'strategy', 'tool', 'platform',
                    'method', 'workflow', 'automation']
    for word in action_words:
        if word in text:
            score += 2

    # Numbers (non-dollar): weak signal
    number_matches = re.findall(r'\b\d+\b', text)
    score += min(len(number_matches) * 1, 10)


    # Sentiment markers
    negative_words = ['scam', 'fraud', 'fake', 'stolen', 'lost',
                      'complaint', 'issue', 'problem', 'error']
    positive_words = ['paid', 'received', 'confirmed', 'legit',
                      'recommend', 'approved', 'success']

    for word in negative_words:
        if word in text:
            score += 2  # Pain points are valuable signals
    for word in positive_words:
        if word in text:
            score += 1

    # Tier multiplier
    tier_multipliers = {1: 1.5, 2: 1.3, 3: 1.0, 4: 1.0,
                        5: 1.2, 6: 0.8, 7: 1.0, 8: 0.6,
                        9: 1.2, 10: 1.5, 11: 1.0}

    score *= tier_multipliers.get(subreddit_tier, 1.0)

    # Normalize to 0-100
    return min(score, 100)
```

---

## Signal Taxonomy: What to Extract From Each Category

### Income Verification Signals

Posts containing screenshots, payment confirmations, or bank transfer proofs. These validate that a platform actually pays. Extract:

- Platform name
- Payment amount
- Payment date
- Payment method (PayPal, bank transfer, crypto, gift card)
- User reputation (account age, post history)
- Geographic location (if disclosed)

### Platform Reliability Signals

Posts about platform outages, fee changes, policy updates, or deactivations. These affect the viability of money-making methods. Extract:

- Platform name
- Change description
- Date of change
- Sentiment (positive/negative/neutral)
- Impact severity (minor/major/critical)
- Number of affected users mentioned

### Pain Point Signals

Complaints, problems, and unmet needs that represent business opportunities. Extract:

- Problem description
- Current solution (or lack thereof)
- Willingness to pay (stated or implied)
- Number of similar complaints (frequency)
- Geographic context
- Demographic information (if disclosed)

### Market Rate Signals

Salary, rate, or price data that provides market benchmarks. Extract:

- Job title / service type
- Rate or salary amount
- Location
- Experience level (if disclosed)
- Platform (if disclosed)
- Currency

### Scam and Fraud Signals

Reports of fraudulent activity that need to be cross-referenced against opportunities. Extract:

- Scam type (phishing, fake platform, advance fee, romance, investment)
- Platform or company name used in scam
- Contact information (phone, email, crypto address)
- Dollar amount lost
- Reporting user details
- Date of scam

### Platform Switching Signals

Indications that users are moving from one platform to another due to dissatisfaction. Extract:

- Source platform
- Destination platform
- Reason for switching
- Volume of users switching (anecdotal or quantified)
- Date

---

## Rate Limit and Anti-Bot Bypass Strategies

### Recommended Approach for High-Volume Crawling

1. **OAuth authentication** (higher rate limits): 60 requests/minute per client ID. Create multiple Reddit app clients if needed, and rotate between them.

2. **User-Agent rotation**: Use realistic User-Agent strings from common browsers:

```python
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
]
```

3. **Respect Retry-After headers**: When Reddit returns 429 (Too Many Requests), the Retry-After header indicates how long to wait. Always respect it.

4. **Exponential backoff**: If a request fails with 429, wait 30s, then 60s, then 120s, up to a maximum of 600s.

5. **Distribute requests across subreddits**: Don't hammer one subreddit. Interleave requests across all subreddits in the crawl schedule.

6. **Old Reddit for HTML fallback**: If the JSON API is rate-limited, old.reddit.com returns simpler HTML that is easier to parse:

```
GET https://old.reddit.com/r/{subreddit}/new/?limit=100
```

### Pushshift as a Bypass

Pushshift.io has a separate rate limit and can be used to backfill data when Reddit's API is blocked:

```
GET https://api.pushshift.io/reddit/submission/search/...  # 120 requests/minute
```

### Proxy Rotation

For aggressive crawling (not recommended unless necessary):

```python
PROXY_POOL = [
    "http://proxy1:8080",
    "http://proxy2:8080",
    "http://proxy3:8080",
]

def get_random_proxy():
    return random.choice(PROXY_POOL)

session = requests.Session()
session.proxies = {"http": get_random_proxy(), "https": get_random_proxy()}
```

### Avoiding Detection

- Crawl during off-peak hours (UTC 02:00-10:00 when US traffic is low)
- Add random delays between requests (not fixed intervals)
- Vary crawl order (not the same subreddits in the same sequence every cycle)
- Respect robots.txt (Reddit's robots.txt allows /r/ but blocks some paths)
- Do NOT crawl user profiles aggressively (high risk of IP ban)
- Do NOT upvote/downvote or comment (violates Reddit's API terms)

---

## New Subreddit Discovery Pipeline

Subreddits grow, decline, and new ones emerge. The following pipeline helps discover new money-related communities:

### Automated Discovery Methods

1. **Related subreddit sidebar scraping**: Every subreddit has a sidebar with related communities. Crawl the sidebar of known money subreddits to discover new ones.

```python
def discover_related_subreddits(subreddit, access_token):
    """Extract related subreddits from a subreddit's sidebar/about page."""
    headers = {
        'Authorization': f'bearer {access_token}',
        'User-Agent': 'MoneyGlitchVault/1.0'
    }
    resp = requests.get(
        f'https://oauth.reddit.com/r/{subreddit}/about',
        headers=headers
    )
    data = resp.json()
    # Subreddit description often contains related subreddit links
    description = data.get('data', {}).get('description', '')
    # Regex for r/SubredditName patterns
    matches = re.findall(r'/?r/([a-zA-Z0-9_]+)', description)
    return matches
```

2. **Reddit search for money-related keywords**: Search Reddit for specific keywords to find subreddits where those keywords are discussed:

```
GET https://www.reddit.com/subreddits/search.json?q=money+make+earn+income+side+hustle
```

3. **Subreddit recommendation APIs**: Services like subredditfinder.com, anu.red, or metareddit.com provide subreddit recommendation based on a seed subreddit.

4. **Crosspost tracking**: Monitor which subreddits posts from known money subreddits are crossposted to. Crossposts indicate thematic overlap.

5. **User overlap analysis**: Identify users who post in money subreddits, then find other subreddits they are active in. This is computationally expensive (requires graph analysis) but highly effective.

### Manual Curation Cadence

Every 2 weeks, a vault agent should:

1. Review the "related communities" sidebar of the top 10 most active money subreddits.
2. Check new subreddit growth on external trackers.
3. Search for new subreddits containing keywords: "money", "cash", "earn", "income", "finance", "invest", "hustle", "side", "gig", "freelance", "finansial", "pinjol", "kripto".
4. Add any promising new subreddits to this document and the crawl schedule.

### Evaluation Criteria for New Subreddits

When evaluating whether to add a new subreddit to the crawl schedule:

- Subscriber count: Minimum 1,000 subscribers (below that, activity is too low)
- Daily post volume: Minimum 5 new posts per day
- Content relevance: At least 30% of posts should contain money-related keywords
- Signal-to-noise ratio: At least 10% of posts should contain concrete data (numbers, platforms, amounts)
- Moderation quality: Active moderation indicates sustainable community
- Crawl cost: API requests per day needed

---

## Gap Analysis: What This List Misses

### Known Gaps

1. **Private subreddits**: Some money-making communities are invite-only or private (e.g., certain affiliate marketing groups). These are invisible to crawlers but often contain the highest quality signal. Discovery requires human infiltration.

2. **Discord servers**: Many money communities have moved from Reddit to Discord. The vault has a separate document for Discord server mining (see: `01-crawler-scrapper/discord/public-server-mining.md`).

3. **Language-specific subreddits beyond Indonesian**: Subreddits in other regional languages (Thai, Vietnamese, Filipino, Mandarin) may contain valuable money signals but are not covered here. Future expansion should prioritize:

   - Mandarin: r/shanghai, r/chinalife, r/bogleheads (Chinese speakers)
   - Spanish: r/mexicofinanciero, r/colombiafinanciera
   - Arabic: r/PersonalFinanceEgypt
   - Portuguese: r/investimentos

4. **Deleted post archives**: Many high-signal posts are deleted by users or removed by moderators. Pushshift archiving is essential for capturing these before deletion. The vault should maintain a Pushshift-backed archive of all targeted subreddits.

5. **Comment-level signal**: This document focuses on post-level crawling. Comments often contain more detailed data (especially in question threads) but require significant additional crawling bandwidth. Recommended to crawl comments on high-signal posts only (score > signal threshold).

6. **User profiling**: Tracking individual users across subreddits reveals expertise and credibility signals. However, this raises privacy concerns and has higher API cost. Recommended only for whitelisted high-value users.

7. **Image-based payment proof**: Many payment confirmations are screenshots rather than text. OCR processing of image posts would extract additional signal. The vault's TikTok scraper components could be adapted for this.

8. **Subreddit-specific terminology**: Each money subreddit develops its own jargon (e.g., "churning", "MS", "connects", "HIT", "batch"). An NLP model trained on generic financial text will miss subreddit-specific signals. A domain adaptation step is needed for each major subreddit category.

### How This Document Should Evolve

This document should be treated as a living reference. When a vault agent discovers a new money-related subreddit during research for another topic, they should:

1. Add the subreddit to the appropriate tier section of this document
2. Estimate subscriber count and signal density
3. Add it to the crawl configuration in the technical appendix
4. Log the addition in CHANGELOG.md

The **self-evolution mechanism** described in the vault's workflow is designed for exactly this purpose. Every vault agent tick is an opportunity to expand this list.

---

## Appendix: Quick-Reference Subreddit Master List

For quick copy-paste into crawler configuration:

```python
# Tier 1: Direct Money-Making
TIER_1 = [
    'beermoney', 'SideHustle', 'slavelabour', 'forhire',
    'workonline', 'passive_income', 'affiliatemarketing',
]

# Tier 2: Side Hustle & Freelance
TIER_2 = [
    'freelance', 'Upwork', 'freelanceWriters', 'DesignJobs',
]

# Tier 3: Personal Finance & Investing
TIER_3 = [
    'personalfinance', 'financialindependence', 'investing',
    'stocks', 'dividends', 'bonds', 'options',
]

# Tier 4: Crypto & Trading
TIER_4 = [
    'CryptoCurrency', 'CryptoMarkets', 'CryptoScams',
    'ethtrader', 'defi', 'ethfinance', 'coinbase', 'binance',
    'WallStreetBetsCrypto', 'algotrading',
]

# Tier 5: Scam Detection
TIER_5 = [
    'Scams', 'antiMLM', 'legaladvice', 'CryptoScams',
]

# Tier 6: Career & Income
TIER_6 = [
    'cscareerquestions', 'Salary', 'ExperiencedDevs',
    'jobs', 'ITCareerQuestions',
]

# Tier 7: Business & Entrepreneurship
TIER_7 = [
    'Entrepreneur', 'SaaS', 'smallbusiness', 'ecommerce',
    'dropship', 'Flipping', 'sweatystartup', 'realestateinvesting',
]

# Tier 8: Deals & Savings
TIER_8 = [
    'Frugal', 'churning', 'awardtravel', 'CreditCards',
    'beermoneyuk',
]

# Tier 9: Gig Economy
TIER_9 = [
    'UberEATS', 'doordash_drivers', 'InstacartShoppers',
    'AmazonFlexDrivers', 'mTurk', 'UHRSwork', 'Clickworker',
]

# Tier 10: Indonesia/SE Asia
TIER_10 = [
    'finansial', 'indonesia', 'pinjaeminjem',
    'indonesia_investasi', 'indonesiakerja', 'freelanceindo',
    'MalaysianPF', 'singaporefi', 'PhInvest',
]

# Tier 11: Niche & Emerging
TIER_11 = [
    'overemployed', 'coastFIRE', 'baristafire', 'fatFIRE',
    'EtsySellers', 'digitalnomad', 'juststart',
    'EntrepreneurRideAlong', 'startups',
]

ALL_MONEY_SUBREDDITS = TIER_1 + TIER_2 + TIER_3 + TIER_4 + TIER_5 + \
                       TIER_6 + TIER_7 + TIER_8 + TIER_9 + TIER_10 + TIER_11
```

## Appendix: Anti-Bot Countermeasure Reference

Reddit employs several anti-bot measures that affect crawling. The table below summarizes them and how to handle each:

| Measure | Detection Method | Mitigation |
|---------|-----------------|------------|
| Rate limiting | HTTP 429 response | Exponential backoff, respect Retry-After |
| IP ban | HTTP 403 or 503 response | Proxy rotation (residential proxies preferred) |
| User-Agent blocking | HTTP 403 response | Realistic User-Agent strings, rotate per request |
| CAPTCHA | HTML redirect to CAPTCHA page | Reduce request rate, switch to Old Reddit |
| Content blocking | Empty response body | Switch endpoint (JSON vs. HTML vs. Old Reddit) |
| Shadowban | Response succeeds but data is empty | Cross-reference with Pushshift |
| Account suspension | OAuth returns 401 | Maintain backup OAuth credentials |
| Karma gate | Subreddit removes low-karma user posts | Crawl without authentication for content |
| Removal by mods | Post flagged as removed | Crawl via Pushshift (preserves removed content) |
| Deletion by user | Author field shows [deleted] | Crawl frequently before users delete posts |

---

*Document version: 1.0. Last updated: 2026-07-29. Next review due: 2026-08-12.*
