# Competitor Analysis: Indonesian Ride-Hailing Super-App Gaps 2025-2026

**File:** `03-id-business-trends/competitors/ride-hailing-super-app-gaps.md`
**Version:** 1.0
**Last updated:** 2026-06-24
**Audience:** Product strategists, founders, and engineers analyzing entry points in Indonesia's ride-hailing and super-app ecosystem.
**Purpose:** Map every major ride-hailing super-app's failure points, underserved segments, and structural weaknesses so we can identify where new entrants, specialized apps, or adjacent services can compete.

---

## Table of Contents

1. Market Structure Overview
2. Gojek (GoTo) -- The Super-App That Ate Itself
3. Grab -- The Regional Giant With Local Blind Spots
4. Gojek vs Grab Head-to-Head: The War That Never Ended
5. The Super-App Bloat Problem
6. Cross-Sell Category Breakdown and Failure Points
7. Driver Ecosystem and Two-Sided Market Failures
8. Merchant Pain Points and Platform Dependency
9. Payment Infrastructure and QRIS Integration Gaps
10. Food Delivery Deep Dive (GoFood vs GrabFood vs ShopeeFood)
11. Logistics and Courier Service Gaps
12. Financial Services and Lending Failures
13. Technical and API Weaknesses
14. Regulatory Exposure and Policy Risks
15. GoTo Post-IPO Financial Pressure
16. Grab Financial Trajectory and Market Expectations
17. Underserved Segments (Opportunity Map)
18. International Comparison: What Indonesian Super-Apps Can Learn
19. Conclusion: Top 12 Unserved Needs

---

## 1. Market Structure Overview

### 1.1 Current State of Indonesian Ride-Hailing and Super-Apps

Indonesia's ride-hailing and super-app market is projected to reach USD 35 billion GMV by 2026 (e-Conomy SEA 2025 by Google, Temasek, Bain). The market is a two-horse race between Gojek (now part of GoTo) and Grab, with a growing third force in ShopeeFood (ride-hailing-adjacent) and niche players in logistics.

**Market Share by GMV (2025-2026 estimates):**

| Metric | Gojek (GoTo) | Grab Indonesia | ShopeeFood | Others |
|--------|-------------|---------------|------------|--------|
| Ride-hailing GMV share | ~45% | ~42% | N/A | ~13% (Blue Bird, AnterAja, etc.) |
| Food delivery GMV share | ~40% | ~35% | ~20% | ~5% |
| Digital payments (e-wallet) | ~30% (GoPay) | ~28% (OVO/GrabPay) | ~15% (ShopeePay) | ~27% (DANA, LinkAja, etc.) |
| Total super-app users | ~170M (GoTo group) | ~180M (SEA-wide) | ~50M (ShopeePay) | N/A |

*Sources: Momentum Works 2025, DailySocial.id 2025, East Ventures Digital Competitiveness Index 2025, GoTo and Grab financial reports Q1 2026. Market share figures are consensus estimates; exact numbers vary by methodology.*

### 1.2 Key Trend: The Super-App Saturation

Both Gojek and Grab have pursued a super-app strategy, offering 20+ services per platform. However, the strategy is showing structural fatigue:

- User acquisition costs have risen 3x since 2022 as top-of-funnel growth plateaus (GoTo annual report 2025)
- Cross-sell conversion rates across non-core services remain below 15% (internal industry estimates)
- Bloat leads to app size exceeding 200MB, causing uninstall rates of 8-12% on low-end devices (Kompas Tekno 2025)
- Average session time per service outside ride-hailing/food is under 2 minutes (similarweb 2025 data)

## 2. Gojek (GoTo) -- The Super-App That Ate Itself

### 2.1 Corporate Structure and History

Gojek was founded in 2010 by Nadiem Makarim and Michaelangelo Moran, starting as a call center with 20 ojek drivers. It launched its app in January 2015 with 4 services: GoRide, GoSend, GoShop, and GoFood. By 2018 it had expanded to 20 services.

On 17 May 2021, Gojek merged with Tokopedia to form GoTo, Indonesia's largest tech group. The combined entity is valued at approximately USD 18-20 billion (as of mid-2026), down from a peak of USD 29.5 billion at its 2022 IPO on the IDX.

**Key Investors:** Google, Facebook (Meta), PayPal, Mitsubishi, Sequoia, Temasek Holdings, KKR, Warburg Pincus, Tencent, JD.com, Astra International.

**GoTo Key Financials (FY 2025):**

| Metric | Value | Year-over-Year |
|--------|-------|----------------|
| Gross Revenue | IDR 28.7 trillion (USD 1.8B) | +12% |
| Net Loss | IDR 15.3 trillion (USD 955M) | Narrowed 18% |
| Gross Transaction Value (GTV) | IDR 645 trillion (USD 40B) | +8% |
| Take Rate | 4.4% | +20 bps |
| Monthly Active Users (MAU) | 95 million | +2% |
| Average Revenue Per User (ARPU) | IDR 25,000/month | +5% |

*Source: GoTo Financial Report FY 2025, audited. Exchange rate: 1 USD = 16,000 IDR (average 2025).*

### 2.2 The GoTo Merger Integration Failure

The Gojek-Tokopedia merger was supposed to create synergies: ride-hailing drives foot traffic to Tokopedia's e-commerce, Tokopedia's logistics needs feed Gojek, and GoPay creates a closed-loop payment ecosystem.

**Reality check -- where integration failed:**

- **Cross-platform data sharing remains minimal.** Gojek user data and Tokopedia user data are siloed. A user ordering GoFood cannot seamlessly see Tokopedia promotions in the Gojek app without re-authentication. Source: DailySocial.id review 2025.

- **GoPay Tokopedia integration is surface-level.** Despite GoPay being the default payment on Tokopedia, checkout flows add 2-3 extra clicks compared to ShopeePay on Shopee. Conversion drops 12% at the payment step (internal GoTo data leaked via Tech in Asia 2025).

- **Logistics synergy was overpromised.** The plan was for Gojek drivers to handle Tokopedia last-mile delivery. In practice, only 8% of Tokopedia packages use GoSend. Most merchants prefer JNE, J&T, or SiCepat for reliability. Source: Populix survey 2025, 1,200 Tokopedia sellers.

- **Management turf wars.** Post-merger, Gojek and Tokopedia teams competed for control, leading to 3 rounds of layoffs (2022, 2023, 2024) eliminating 2,500+ positions. Morale remains low. Source: Katadata.co.id 2024.

### 2.3 Gojek Service Portfolio (as of 2026)

| Category | Services | Cross-Sell Success | Notes |
|----------|----------|-------------------|-------|
| Ride-Hailing | GoRide, GoCar, GoBlueBird, GoCar Premium | High (core) | 70% of user sessions |
| Food Delivery | GoFood | High | 25% of GTV |
| Logistics | GoSend, GoBox | Medium | 5% of GTV |
| Payments | GoPay, GoTagihan, GoPayLater | Medium | 40M active wallets |
| Shopping | GoShop (personal shopper), GoMart, GoMed | Low | <2% of GTV |
| Entertainment | GoTix, GoPlay, GoGames | Very Low | GoPlay shut down 2024 |
| Services | GoClean, GoMassage, GoAuto, GoGlam | Very Low | <1% combined |
| Business | GoBiz, GoStore, GoPro | Low | Midsize merchant tool |

*Source: GoTo annual report 2025, App Annie data 2025.*

## 3. Grab -- The Regional Giant With Local Blind Spots

### 3.1 Corporate Structure

Grab Holdings Inc. (NASDAQ: GRAB) is a Singapore-headquartered super-app that went public via SPAC merger in December 2021 at a valuation of USD 40 billion. Its current market cap is approximately USD 12-14 billion (June 2026).

**Key Investors:** SoftBank Vision Fund, Mitsubishi UFJ Financial Group, Toyota, Microsoft, Oppenheimer Funds.

**Grab Key Financials (FY 2025):**

| Metric | Value | Year-over-Year |
|--------|-------|----------------|
| Revenue | USD 2.7 billion | +17% |
| Net Loss | USD 340 million | Narrowed 55% |
| GMV | USD 28 billion | +10% |
| Take Rate | 9.6% | Improved |
| Monthly Active Users | 40 million (SEA) | +5% |
| ARPU | USD 7/month (SEA avg) | +8% |

*Source: Grab Holdings FY 2025 Annual Report (SEC Filing).*

### 3.2 Grab's Indonesian Blind Spots

Grab's Indonesian operations contribute approximately 35-40% of its SEA GMV but only 25% of revenue. The Indonesian business consistently underperforms relative to market size because:

- **HQ-centric product decisions.** Grab's product and engineering teams are in Singapore. Features designed for the Singaporean market (high smartphone penetration, 100% credit card usage, English-first UX) translate poorly to Indonesia.

- **Local responsiveness is slow.** When Gojek rolled out GoPayLater (BNPL) in 2022, Grab took 8 months to launch GrabPayLater in Indonesia. By then, Gojek had 3M users locked in. Source: Tech in Asia 2023.

- **Driver community management is weaker.** Grab takes a 20-25% commission in Indonesia vs 15-20% for Gojek. Driver satisfaction surveys consistently rate Gojek higher (78% vs 62% satisfied). Source: Lembaga Demografi FEB UI 2025.

- **Merchant exclusivity is lower.** Only 40% of GrabFood merchants are exclusive to Grab, vs 55% for GoFood. Grab's multi-listing merchants (also on GoFood/ShopeeFood) tend to deprioritize Grab orders. Source: Populix merchant survey 2025.

### 3.3 Grab's Margin Improvement Strategy (and Its Costs)

Grab has been aggressively cutting incentives since 2023 to achieve profitability:

- Average consumer discount reduced from 18% (2022) to 6% (2025)
- Driver incentives cut from 12% to 4% of fare
- Minimum order thresholds increased for free delivery
- Subscription (GrabUnlimited) pricing raised 30% in 2025

**Result:** Take rate improved to 9.6%, but:
- Monthly active users in Indonesia declined 3% in 2025
- Average orders per user declined from 8.2/month to 6.9/month
- Net Promoter Score dropped from +32 to +18

*Sources: Grab Holdings SEC Filings, DailySocial.id consumer survey 2025 (n=2,000).*

## 4. Gojek vs Grab Head-to-Head: The War That Never Ended

### 4.1 Service Comparison Matrix

| Feature | Gojek | Grab | Who Wins |
|---------|-------|------|----------|
| Ride-hailing coverage | 500+ cities | 200+ cities | Gojek |
| Food delivery coverage | 300+ cities | 150+ cities | Gojek |
| E-wallet users | 40M (GoPay) | 35M (OVO/GrabPay) | Gojek |
| Driver fleet size | 2M+ | 1.2M+ | Gojek |
| App size | 185MB | 220MB | Neither (both bloated) |
| Average driver earnings | IDR 6.2M/month | IDR 5.1M/month | Gojek |
| Merchant commission | 15-20% | 20-25% | Gojek |
| BNPL penetration | 8M users | 4M users | Gojek |
| Cross-border readiness | Limited | Strong | Grab |
| Corporate travel | Basic | Grab for Business | Grab |
| Loyalty program | GoPay Points (weak) | GrabRewards (better) | Grab |

*Sources: Various -- company disclosures, DailySocial, Populix surveys, Q1 2026 reports.*

### 4.2 Pricing Wars and Subsidy Addiction

Between 2015-2022, both platforms burned an estimated USD 8 billion combined on subsidies in Indonesia. The war created:

- **Price-sensitive users who churn at 2% discount difference.** 63% of users have both apps installed and compare prices before ordering. Source: DailySocial 2025.

- **Driver multi-apping.** 71% of drivers work for both Gojek and Grab simultaneously. This means neither platform has a truly exclusive fleet. Source: Lembaga Demografi FEB UI 2025.

- **Merchant multi-listing.** 58% of food merchants list on both platforms plus ShopeeFood. Menu prices are adjusted per platform to account for commission differences.

- **No pricing power.** Both platforms lost the ability to raise prices meaningfully. Gojek's 2025 price increase of 8% in Jakarta led to a 14% volume decline within 2 months (reversed after 3 months).

## 5. The Super-App Bloat Problem

### 5.1 The Infinite Scroll of Mediocrity

Both Gojek and Grab suffer from what we call the "super-app bloat death spiral":

1. App gets too big (180-220MB)
2. Low-end Android phones (60% of Indonesian market) struggle to run it
3. Users uninstall and use Lite versions or competitors
4. Platforms add more features to retain users
5. App gets even bigger
6. Repeat

**Hardware mismatch:**

| Phone Price Tier | Market Share | Can Run Gojek Full | Can Run Grab Full |
|-----------------|-------------|-------------------|-------------------|
| <IDR 2M (~$125) | 35% | No (frequent crashes) | No (crashes) |
| IDR 2-4M ($125-250) | 30% | With lag | With lag |
| IDR 4-8M ($250-500) | 20% | Yes | Yes |
| >IDR 8M ($500+) | 15% | Yes | Yes |

*Source: Counterpoint Indonesia 2025, combined with app performance testing by reviewer agnostik.org 2025.*

**Gojek Lite and Grab Lite** were launched but have been neglected -- Gojek Lite hasn't been updated since 2024 and lacks core features (GoFood, GoPayLater). Grab Lite has basic ride-hailing only.

### 5.2 Feature Bloat vs. User Needs

A 2025 survey by DailySocial.id (n=5,000) asked users to rank the importance of super-app features:

| Feature | % Rating "Very Important" | % Rating "Not Important" |
|---------|--------------------------|-------------------------|
| Ride-hailing | 92% | 1% |
| Food delivery | 78% | 5% |
| Bill payment | 55% | 15% |
| E-wallet transfer | 52% | 12% |
| Parcel delivery | 45% | 18% |
| Grocery delivery | 35% | 25% |
| BNPL / credit | 30% | 35% |
| Ticket booking | 22% | 40% |
| House cleaning | 8% | 72% |
| Massage booking | 6% | 78% |
| Car maintenance | 4% | 82% |
| Game top-up | 12% | 60% |

**Conclusion:** Services below bill payment (55%) are effectively noise for most users. Yet Gojek and Grab continue to invest in these low-importance services, burning engineering resources that could fix core experience issues.

### 5.3 The Hidden Cost: Engineering Tax

Every additional service a super-app adds creates an engineering tax:

- **QA matrix explosion:** Testing 20+ services x 3 platforms (iOS, Android, Web) x 1,000+ device models = combinatorial explosion
- **Payment integration:** Each service needs separate payment routing logic (cash, GoPay, OVO, QRIS, credit card, bank transfer, BNPL)
- **Customer support:** CSR agents need training on 20+ service-specific policies. Average resolution time for non-core services: 8+ hours vs 2 hours for ride-hailing
- **Regulatory compliance:** Each service category (payments, lending, health, logistics) has separate regulators (OJK, BI, Kominfo, BPOM, Kemendag)

**GoTo engineering team size:** ~4,500 engineers (2025). Estimated 40% work on non-core services that generate <10% of revenue. This is a structural inefficiency.

## 6. Cross-Sell Category Breakdown and Failure Points

### 6.1 Why Cross-Sell Works in China but Not Indonesia

The benchmark super-app is WeChat (Tencent), which achieves 80%+ cross-sell rates into payments, shopping, and services from its messaging base. Meituan achieves 45%+ cross-sell from food delivery to other local services.

**Why Indonesian super-apps fail at cross-sell:**

- **No social graph.** WeChat cross-sells through social interactions (red packets, group buying, friend recommendations). Gojek and Grab have no meaningful social layer.

- **Low ARPU ceilings.** Indonesian users spend IDR 100-200K/month on ride-hailing and food. Pushing additional services requires convincing users to increase total spend in a price-sensitive market.

- **Category adjacencies are weak.** A ride-hailing user is not naturally a massage-booking user. The behavioral link is tenuous.

- **UI/UX silos.** Despite being in one app, the experience of each service is isolated. Users must navigate separate menus, re-enter preferences, and manage separate order histories.

### 6.2 Service-by-Service Cross-Sell Failure Analysis

| Service Category | Core User Base | Cross-Sell Attempt | Conversion Rate | Why It Fails |
|-----------------|---------------|-------------------|-----------------|-------------|
| GoRide -> GoFood | Daily commuters | Push notification at lunchtime | 12% | Users who ride don't order food 2x/day |
| GoFood -> GoPayLater | Food orderers | Prominent payment option | 8% | Cash/GoPay users don't want credit |
| GoCar -> GoTix | Weekend travelers | Event recommendations near destination | 2% | Very context-dependent |
| GoPay -> GoInvestasi | Wallet users | Investment upsell in app | 0.5% | E-wallet users are transactional, not investors |
| GoFood -> GoMart | Lunch orderers | "Add grocery items" prompt | 3% | Different use case, different time |
| GoRide -> GoSend | Riders who carry parcels | "Send this for you" | 4% | WhatsApp forwarding easier |
| GoFood -> GoGames | Dinner orderers | Game top-up promo | 0.8% | No demographic overlap |

### 6.3 The BNPL Cross-Sell That Actually Worked

The one cross-sell success story: **GoPayLater (BNPL)** .

- Launched 2022 with frictionless enrollment (500K instant credit limit based on ride/food history)
- 8M active users as of Q1 2026
- Non-performing loan rate: 3.2% (manageable)
- Average credit limit: IDR 1.5M ($94)
- Cross-sell from ride/food users: 22% conversion

**Why it worked:**
- Behavioral data from ride/food history is directly predictive of creditworthiness
- Transactional users naturally need short-term credit
- Low friction (no paperwork, instant approval)
- Integrated into existing payment flow

**Lesson:** Cross-sell works when the new service shares the same behavioral context and payment moment as the core service. GoPayLater sits at the CHECKOUT step, the most natural upsell point.

## 7. Driver Ecosystem and Two-Sided Market Failures

### 7.1 The Driver Experience Decline

Both platforms face a structural problem: as they pursue profitability, driver income declines.

**Driver Income Trend (Gojek):**

| Year | Average Monthly Income | Hours Worked/Day | Platform Commission |
|------|----------------------|-----------------|-------------------|
| 2020 | IDR 7.5M | 8 | 10-12% |
| 2022 | IDR 6.8M | 9 | 15-18% |
| 2024 | IDR 6.0M | 10 | 18-20% |
| 2026 (est.) | IDR 5.5M | 11 | 20-22% |

*Source: Lembaga Demografi FEB UI 2025, combined with KBUMN survey of ojol drivers 2025. Note: Income before vehicle costs (fuel, maintenance, depreciation estimated at IDR 1.5-2M/month).*

**Driver Churn (2025):**

| Reason for Leaving | Gojek | Grab |
|-------------------|-------|------|
| Income too low | 38% | 45% |
| Platform commission too high | 25% | 30% |
| Safety concerns | 15% | 12% |
| Better opportunity elsewhere | 12% | 8% |
| Other | 10% | 5% |

*Source: Lembaga Demografi FEB UI 2025 (n=2,400 drivers).*

### 7.2 The Driver Multi-Appping Reality

The most significant structural weakness: drivers overwhelmingly work for multiple platforms.

```
Graph: Driver Multi-App Distribution (2025)
Gojek only:        18%
Grab only:         11%
Both Gojek+Grab:   58%
All 3 (+ShopeeFood): 13%
```

This means:
- Neither platform has "exclusive" capacity during peak hours
- Drivers prioritize higher-paying rides, creating supply shortages on the lower-paying platform
- Platforms cannot differentiate on driver quality (same drivers)

### 7.3 Safety and Trust Failures

Ride-hailing has an unresolved safety crisis:

- **Gojek:** 2,347 reported incidents (theft, harassment, accidents) in 2025 (Gojek Transparency Report 2025)
- **Grab:** 1,892 reported incidents in 2025 (Grab Safety Report 2025)
- **Panic button usage:** Only 2% of riders use the panic button during incidents
- **Criminal background checks:** Only 60% of driver applications go through thorough checks (the rest pass via incomplete data from partner screening agencies)
- **Insurance coverage:** Gojek provides accident insurance up to IDR 50M ($3,125) -- inadequate for serious incidents

**Regulatory threat:** In 2025, Kemenhub (Ministry of Transportation) proposed mandatory insurance of IDR 200M for ride-hailing passengers. Both platforms lobby against it. Source: Detik.com 2025.

## 8. Merchant Pain Points and Platform Dependency

### 8.1 The Commission Squeeze

Food merchants on both platforms face a take rate squeeze:

**Merchant Commission Comparison (2025):**

| Platform | Base Commission | +Promotion Costs | +Payment Fees | Total Effective Rate |
|----------|---------------|-----------------|--------------|-------------------|
| GoFood | 18-22% | 5-10% | 2% | 25-34% |
| GrabFood | 20-25% | 5-10% | 2% | 27-37% |
| ShopeeFood | 12-15% | 3-5% | 2% | 17-22% |

*Source: Populix merchant survey 2025 (n=1,500 food merchants across Jabodetabek, Surabaya, Bandung, Medan).*

**Merchant Profit Margin Impact:**

For a merchant with 50% COGS and 20% labor+rent cost:
- Direct sales margin: 30%
- GoFood margin: 5-11% (after subtracting 25-34% platform costs)
- GrabFood margin: 3-8% (after subtracting 27-37% platform costs)

**Many merchants report negative margins on platform orders** but continue because platform orders represent 40-60% of their volume. They cannot afford to leave the platform, but they cannot profitably serve it.

### 8.2 GoBiz and Merchant Tools Weaknesses

Gojek offers GoBiz for merchant management. Grab offers GrabMerchant. Both are inadequate:

| Feature | GoBiz | GrabMerchant | Ideal |
|---------|-------|-------------|-------|
| Real-time sales dashboard | Yes, 15-min delay | Yes, 10-min delay | Real-time |
| Menu management | Manual JSON upload | Manual form | API-based |
| Inventory sync | No | No | Essential |
| Multi-outlet management | Basic | Basic | Hierarchical |
| Promotions engine | Rule-based | Rule-based | AI-optimized |
| Customer data | Aggregate only | Aggregate only | Per-merchant analytics |
| Delivery zone control | Yes | Yes | Dynamic zone optimization |
| Payment reconciliation | Daily CSV | Daily CSV | Real-time API |
| Integration with POS | None (manual) | None (manual) | API integration with major POS |

The lack of POS integration is critical. Gojek and Grab do not offer APIs for major Indonesian POS systems (Moka, Pawoon, iReap, Olsera). Merchants must manually reconcile platform orders with their POS.

### 8.3 The Offline Merchant Opportunity

40% of Indonesian food merchants (estimated 4M outlets) are not on any platform. Reasons:

| Reason | % of Offline Merchants |
|--------|----------------------|
| Too complex / don't understand | 35% |
| Commission too high | 25% |
| No smartphone / data plan | 15% |
| Don't trust digital payments | 12% |
| Operating at full capacity anyway | 13% |

*Source: Populix merchant survey 2025, n=800 offline food sellers.*

This is a massive underserved segment. Competitors who can onboard these merchants with simpler tools, lower commissions, or offline-first approaches could capture significant market share.

## 9. Payment Infrastructure and QRIS Integration Gaps

### 9.1 The QRIS Mandate and Its Impact

BI (Bank Indonesia) mandated QRIS as the standard QR code for all payment providers in Indonesia. This was supposed to create interoperability. In practice:

- **QRIS settles in T+1 or T+2** (1-2 business days), while platform-owned wallets (GoPay, OVO) settle instantly
- **QRIS merchant fee** is 0-0.7% (depending on merchant category), lower than platform e-wallet fees of 2-3%
- **QRIS is increasingly mandated** for all electronic transactions in Indonesia (under BI regulation 24/2022)

**Impact on super-apps:**

| Aspect | Gojek | Grab |
|--------|-------|------|
| QRIS integration readiness | Partial (2025) | Partial (2025) |
| Own QR (GoPay/OVO) still pushed | Yes | Yes |
| QRIS acceptance on driver terminals | 45% of drivers | 30% of drivers |
| Merchant QRIS adoption | 65% | 55% |

### 9.2 The QRIS Settlement Crisis

A critical gap that emerged in mid-2026 (documented in the vault's weekly gap report): QRIS settlement delays of T+1 to T+2 create cash flow problems for small merchants who need daily liquidity.

- **GoPay benefit:** Instant settlement within GoTo ecosystem
- **QRIS drawback:** Funds only available next business day (T+1) or later (T+2 for some banks)
- **For UMKM:** This means funds from Friday-Saturday transactions arrive on Tuesday. For a warung with IDR 500K/day revenue, this creates a working capital gap.

**The Wedge:** A settlement acceleration service (instant QRIS settlement at 0.5% fee) could capture UMKM merchants who cannot tolerate T+1 settlement.

### 9.3 GoPay vs OVO vs ShopeePay: The Fragmented Wallet War

Indonesia has 6 major e-wallets, none dominant:

| E-Wallet | Active Users (2025) | Part of Super-App | Can Pay On Rival Platform |
|----------|--------------------|-------------------|--------------------------|
| GoPay | 40M | Gojek, Tokopedia | No (GoPay not accepted on Grab) |
| OVO | 35M | Grab, Tokopedia (partial) | No (OVO not accepted on Gojek) |
| ShopeePay | 50M | Shopee, ShopeeFood | Yes (QRIS) |
| DANA | 30M | Standalone | Yes (QRIS) |
| LinkAja | 15M | Standalone (BUMN-backed) | Yes (QRIS) |
| QRIS (direct bank) | 25M | None | Yes (universal) |

**Fragmentation cost:** Merchants need 2-3 QR codes on their counter (GoPay, OVO/ShopeePay, QRIS). Each has different settlement timing, fee structure, and reconciliation.

**Estimated annual economic waste from payment fragmentation:** IDR 5-8 trillion ($312-500M) in operational inefficiency across the Indonesian merchant ecosystem.

## 10. Food Delivery Deep Dive (GoFood vs GrabFood vs ShopeeFood)

### 10.1 Market Share and Dynamics

| Platform | Monthly Orders (2025) | Avg Order Value | Merchant Count | Delivery Fee (avg) |
|----------|---------------------|-----------------|---------------|------------------|
| GoFood | 180M | IDR 45K ($2.80) | 500K+ | IDR 8K ($0.50) |
| GrabFood | 120M | IDR 52K ($3.25) | 350K+ | IDR 10K ($0.63) |
| ShopeeFood | 80M | IDR 35K ($2.20) | 200K+ | IDR 5K ($0.31) |

*Source: Momentum Works 2025, company disclosures.*

### 10.2 GoFood Strengths and Weaknesses

**Strengths:**
- Largest merchant network (500K+) with best coverage in tier 2/3 cities
- GoFood Points loyalty program has decent retention
- Integrated with GoPay (instant settlement for GoPay merchants)

**Weaknesses:**
- Commission structure is complex and unpredictable for merchants
- Delivery logistics in tier 2/3 cities use GoRide drivers who may reject food orders
- No dedicated food-only delivery fleet (unlike GrabFood which has GrabFood-only drivers in some areas)
- GoFood Unlimited subscription (IDR 20K/month) has poor value perception -- only 2M subscribers vs GrabFood's 5M

### 10.3 GrabFood Strengths and Weaknesses

**Strengths:**
- Higher AOV (IDR 52K vs 45K) suggests better merchant selection
- GrabRewards loyalty program is better structured
- GrabKitchen (cloud kitchen) strategy in 20+ locations

**Weaknesses:**
- Lower merchant count in tier 2/3 cities
- Higher delivery fees deter price-sensitive users
- GrabFood-only drivers are less available during peak hours
- Higher commission (20-25%) pushes merchants to prefer GoFood

### 10.4 The ShopeeFood Threat

ShopeeFood has grown from 0 to 20% market share in 3 years, primarily by:

- **Zero to low delivery fees** (IDR 5K or free with ShopeePay)
- **Lower commissions** (12-15%) for merchants
- **Cross-subsidy from Shopee e-commerce** (ShopeeFood is a loss leader to drive ShopeePay adoption)
- **Massive user base** (Shopee has 100M+ monthly users in Indonesia)

**Why Gojek and Grab should worry:** ShopeeFood is not trying to be profitable. It's a strategic play to increase ShopeePay usage. Shopee can afford to bleed money on food delivery for years, as the cost is offset by e-commerce GMV growth.

### 10.5 The Ghost Kitchen Opportunity

Both Gojek (GoKitchen) and Grab (GrabKitchen) have invested in cloud kitchens. Results are mixed:

| Metric | GoKitchen | GrabKitchen |
|--------|----------|-------------|
| Kitchens operational | 50+ | 25+ |
| Average orders/kitchen/day | 150 | 180 |
| Break-even achieved | No | Partial |
| Partner brand satisfaction | 65% | 72% |

**Gap:** Neither platform has cracked the unit economics of ghost kitchens in Indonesia. Rent in Jakarta is high (IDR 50-100M/month for prime locations), and the 15-20% commission on top of rent makes partner brands unprofitable.

## 11. Logistics and Courier Service Gaps

### 11.1 GoSend vs GrabExpress vs The Market

| Service | Same-Day Delivery | Instant Delivery | Price (Jakarta 10km) | Coverage | Avg Delivery Time |
|---------|------------------|-----------------|---------------------|----------|------------------|
| GoSend | Yes | Yes | IDR 25K ($1.56) | 500+ cities | 60 min (instantly) |
| GrabExpress | Yes | Yes | IDR 28K ($1.75) | 200+ cities | 55 min (instantly) |
| JNE YES | Yes | No | IDR 15K ($0.94) | Nationwide | 24 hours |
| J&T | Yes | No | IDR 12K ($0.75) | Nationwide | 24-48 hours |
| SiCepat Halu | Yes | Yes | IDR 18K ($1.13) | 50+ cities | 3-6 hours |

**Key gap:** GoSend and GrabExpress are priced 2x higher than dedicated logistics providers for non-instant delivery. The "instant" premium is valid for urgent documents, but for routine package delivery, users choose JNE/J&T.

**Market opportunity:** Neither platform has a "budget same-day" tier (IDR 12-15K, 3-6 hour delivery). This is a gap that niche logistics players (SiCepat, AnterAja) are filling.

### 11.2 The B2B Logistics Blind Spot

Neither Gojek nor Grab has meaningfully penetrated B2B logistics:

| Feature | GoSend Business | GrabExpress Business | Dedicated B2B (Lalamove, Kargo) |
|---------|---------------|--------------------|--------------------------------|
| Fleet API | No | No | Yes |
| Scheduled pickups | Basic | Basic | Yes |
| Route optimization | No | No | Yes |
| Real-time fleet tracking | No | No | Yes |
| Integration with WMS/ERP | No | No | Yes |
| Dedicated account manager | Yes (premium) | Yes (premium) | Yes |
| Temperature control | No | No | Yes (selected partners) |

Lalamove Indonesia operates in 15 cities and handles 50K+ B2B orders daily, but its coverage is limited. Kargo Technologies focuses on trucking, not last-mile. There is a gap for a last-mile B2B logistics platform that combines Gojek/Grab-like driver network with API-first infrastructure and scheduled pickup capability.

## 12. Financial Services and Lending Failures

### 12.1 GoTo Financial: The Ambitious Pivot That Hasn't Paid Off

GoTo Financial (the fintech arm) was supposed to be the monetization engine for GoTo. Results so far:

| Product | Launch Year | Active Users (2025) | Revenue Contribution |
|---------|------------|-------------------|---------------------|
| GoPayLater (BNPL) | 2022 | 8M | 15% of GoTo Financial revenue |
| GoTagihan (bill pay) | 2016 | 12M | 5% |
| GoInvestasi (mutual funds) | 2020 | 0.5M | <1% |
| Go Insurance | 2021 | 2M | 2% |
| GoPay (wallet) | 2016 | 40M | 60% (transaction fees) |
| GoPoint (loyalty) | 2015 | 10M | 0% (cost center) |
| GoModal (merchant lending) | 2023 | 0.1M | <1% |

*Source: GoTo Financial report 2025.*

### 12.2 Merchant Lending: The Biggest Missed Opportunity

Both platforms have failed at merchant lending:

**GoModal (Gojek):**
- Launched 2023, only 100K borrowers as of Q1 2026
- Total loan disbursed: IDR 1.2 trillion ($75M)
- Average loan size: IDR 12M ($750)
- NPL: 5.8% (high for secured merchant lending)

**GrabModal (Grab):**
- Launched 2022, 80K borrowers
- Total loan disbursed: IDR 0.8 trillion ($50M)
- Average loan size: IDR 10M ($625)
- NPL: 4.5%

**Why so small:** Both platforms have rich transaction data on merchants but cannot underwrite loans efficiently because:
- Merchant revenue data is noisy (depends on promotions, seasonal trends)
- Many merchants have no formal credit history (no BI Checking, no tax ID)
- Loan recovery is difficult (merchants can switch to the other platform)
- Regulatory constraints from OJK limit unsecured lending

**Market comparison:** Estimated UMKM credit gap in Indonesia is IDR 1,600 trillion ($100B). GoModal and GrabModal together address less than 0.01% of this gap.

### 12.3 The Digital Lending Regulatory Wall

OJK regulation POJK 2023 on digital lending tightened requirements:
- Maximum interest rate: 0.3% per day for BNPL
- Maximum late fee: 0.1% per day
- Mandatory registration of all digital lending products
- Credit limit capped at 2x monthly income for users under IDR 10M/month income

These regulations make BNPL and merchant lending less profitable, limiting the fintech upside that investors expected.

## 13. Technical and API Weaknesses

### 13.1 Developer Ecosystem

Neither platform has a healthy developer ecosystem:

| Feature | Gojek | Grab |
|---------|-------|------|
| Public API for third-party apps | Limited (GoPay API only) | Limited (Grab Platform API) |
| Sandbox environment | Yes (GoPay only) | Yes (limited) |
| Webhook/event system | No | No |
| Open source contributions | Few | Few |
| Developer documentation quality | C-grade | B-grade |
| API rate limits (public) | 100 req/min | 200 req/min |
| API authentication | OAuth 2.0 | OAuth 2.0 |
| SDK availability | Android, iOS, Web (GoPay) | Android, iOS, Web (limited) |

**Compare to:** Shopee has a comprehensive Open Platform with APIs for logistics, payments, and product management. Tokopedia has a better Open API than Gojek. Neither Gojek nor Grab treats developer platforms as a strategic priority.

### 13.2 The Dark Store / Mini-Warehouse Problem

Both platforms lack technical infrastructure for:
- **Dark store management** (dedicated fulfillment centers for quick commerce)
- **Real-time inventory tracking** across merchant locations
- **Dynamic delivery zone optimization** (adjusting radius based on driver availability and order volume)
- **AI-powered demand prediction for driver allocation**

Grab has some of these in Singapore but has not adapted them for Indonesia's unique geography (archipelago, varied road quality, traffic patterns that change by season).

### 13.3 The Map Problem

Both platforms rely on Google Maps for navigation. This creates issues in Indonesia:

- **Mapping gaps in tier 2/3 cities:** Google Maps has incomplete address data for 60% of Indonesian sub-districts (kelurahan)
- **No alley-level routing:** Indonesian cities have narrow alleys (gang) that Google Maps doesn't recognize as drivable
- **Pin-drop inaccuracy:** Users frequently drop pins at wrong locations in dense urban areas
- **No offline navigation:** Outside Java, data coverage is spotty. Neither platform has robust offline map support

Gojek invested in PetaJalan (a local mapping startup) in 2023, but integration is still in beta.

## 14. Regulatory Exposure and Policy Risks

### 14.1 The Tariff Regulation Debate

Kemenhub is considering regulating ride-hailing tariffs (similar to taxi tariffs). Proposed regulation (2025):

- Minimum fare per km: IDR 2,500 for GoRide, IDR 5,000 for GoCar
- Maximum platform commission: 15%
- Mandatory driver benefits: BPJS Ketenagakerjaan (employment insurance)
- Fleet age limits: Motorcycle max 10 years, car max 15 years

**Impact if passed:**
- Gojek/Grab revenue would drop 20-30% on commission cap
- Driver compliance costs would increase
- Low-end drivers would be pushed out (older vehicles)

Both platforms lobbied against this and succeeded in delaying it until 2027.

### 14.2 The QRIS Mandate Expansion

BI's QRIS mandate is expanding. By 2027, all electronic payment systems in Indonesia must use QRIS as the primary QR standard. This means:

- GoPay and OVO QR codes will be de-emphasized
- Platform-specific wallet benefits (points, cashback) will apply only to QRIS transactions
- Settlement will shift to T+1 by default (eliminating the instant settlement advantage of platform wallets)

**Strategic risk:** Gojek and Grab built their fintech strategies around proprietary wallet ecosystems. QRIS mandate erodes their moat.

### 14.3 Anti-Monopoly and Market Dominance

KPPU (Komisi Pengawas Persaingan Usaha) has flagged both platforms for potential anti-competitive practices:

| Issue | Gojek | Grab | Status |
|-------|-------|------|--------|
| Exclusive merchant agreements | Challenged 2023 | Not enforced | Gojek settled |
| Tiered pricing for exclusive merchants | Under review | Under review | Ongoing |
| Data hoarding (not sharing with regulators) | Noted | Noted | Awaiting regulation |
| Cross-subsidization (using ride profits to fund food delivery) | Possible | Possible | Under investigation |

## 15. GoTo Post-IPO Financial Pressure

### 15.1 The Stock Performance

GoTo (IDX: GOTO) IPO'd at IDR 338/share in April 2022. As of June 2026:

- Current price: IDR 68/share (down 80% from IPO)
- Market cap: IDR 108 trillion ($6.75B)
- Free float: 42%
- Majority shareholders: ByteDance (through Tokopedia control), SoftBank,阿里巴巴 (Alibaba)

**Pressure points:**
- IPO lock-up expirations continue to depress price
- ByteDance (TikTok parent) effectively controls Tokopedia and may push for further GoTo restructuring
- Retail investors (60% of free float) have lost 80% of their investment, creating political risk
- GoTo has been "net-cash positive" since Q4 2025 but still unprofitable on a GAAP basis

### 15.2 Cost-Cutting and Its Impact

GoTo's path to profitability has been brutal:

| Year | Layoffs | Services Shut | Market Spend |
|------|---------|--------------|-------------|
| 2022 | 1,300 | GoLife (cleaning/massage) | IDR 45T |
| 2023 | 600 | GoPlay (streaming) | IDR 28T |
| 2024 | 600 | GoGames (partial) | IDR 19T |
| 2025 | 0 | None (stabilization) | IDR 14T |

**Services still at risk:** GoTix, GoClean, GoMassage, GoAuto, GoGlam all have <2% revenue contribution and negative unit economics. They are likely candidates for shutdown in 2026-2027.

## 16. Grab Financial Trajectory and Market Expectations

### 16.1 Stock Performance

Grab Holdings (NASDAQ: GRAB) went public via SPAC at $13.13/share (Dec 2021). Current (June 2026): ~$3.80/share (down 71%).

**Investor sentiment:**
- Grab achieved GAAP profitability in Q1 2026 for the first time (net income: $8M)
- Revenue growth at 17% YoY is steady but below early projections of 30%+
- The market assigns Grab a P/S ratio of 4x vs Uber at 3.5x and DoorDash at 5x
- Short interest: 8% of float (moderate pessimism)

### 16.2 The Southeast Asia Expansion Trap

Grab operates in 8 countries but only 3 (Indonesia, Vietnam, Thailand) contribute meaningful revenue. The other 5 markets (Philippines, Malaysia, Singapore, Cambodia, Myanmar) are collectively unprofitable and represent 15% of revenue but 30% of operating costs.

**Indonesia's critical role:** If Grab cannot achieve sustainable profitability in Indonesia (its largest market), the entire thesis collapses. Yet Indonesian operations are structurally less profitable than Singapore operations due to lower AOV, higher subsidy expectations, and regulatory costs.

## 17. Underserved Segments (Opportunity Map)

### 17.1 Tier 2/3 City Ride-Hailing

Gojek claims 500+ city coverage, but quality is uneven:

| City Tier | Gojek Quality Score | Grab Quality Score | Population Served | Gap |
|-----------|-------------------|-------------------|-------------------|-----|
| Tier 1 (Jabodetabek, Surabaya, Bandung, Medan, Makassar) | A- | B+ | 50M | Minor |
| Tier 2 (Semarang, Palembang, Denpasar, Batam, Pekanbaru) | B | C+ | 40M | Moderate wait times |
| Tier 3 (Cirebon, Kediri, Palu, Ambon, etc.) | C | D | 30M | Long wait, minimum order |
| Non-covered cities | F | F | 100M+ | No service at all |

**The opportunity:** A lightweight ride-hailing app focused on tier 3+ cities with offline booking, SMS ordering, and lower commission rates could capture the 100M population that is currently unserved.

### 17.2 Merchant-First Platform

A platform designed from the merchant's perspective (vs. platform-first):

| Feature | Current Platforms | Opportunity |
|---------|-----------------|-------------|
| Commission | 15-25% | 8-12% flat |
| Settlement | T+1 (GoPay instant) | Real-time settlement via QRIS optimization |
| POS integration | None | Native integration with major POS |
| Customer data | Aggregated | Per-merchant analytics, customer attribution |
| Menu management | Manual/JSON | AI-powered photo-to-menu |
| Promotions | Platform-controlled | Merchant-controlled with ROI tracking |
| Offline mode | None | SMS/call ordering for non-smartphone users |

### 17.3 Driver Cooperative Model

The driver co-op model (similar to what happened in other markets):
- Drivers own the platform (profit-sharing model)
- Lower commission (5-10% for operating costs)
- Democratic governance (driver-elected board)
- Shared benefits (cooperative insurance, savings)

**Existing experiments:**
- **Koperasi Ojek:** Small-scale driver cooperatives exist in 5 cities but lack technology
- **Ojek on the Ground:** Community-organized rides via WhatsApp groups

**Why it could work now:** Technology (open-source dispatch software available via projects like SHARE, LibreTaxi, or OpenStreetMap routing) plus regulatory tailwinds (Kemenkop UKM supports cooperative models).

### 17.4 B2B Delivery and Logistics API

The gap between Gojek/Grab's instant premium delivery and JNE/J&T's 1-2 day economy delivery is a "same-day economy" segment:

- 3-6 hour delivery
- IDR 10-15K flat rate within city
- Scheduled pickup windows (10-12 AM, 12-2 PM, etc.)
- API-first for e-commerce integration
- Real-time tracking
- No minimum order

**Target:** E-commerce sellers who need faster-than-JNE but cheaper-than-GoSend. Estimated market: 500K+ small e-commerce sellers on TikTok Shop, Shopee, and Tokopedia who currently use JNE but lose customers who want same-day delivery.

### 17.5 Financial Inclusion for Drivers

Drivers are the platform's most loyal users but have terrible financial inclusion:

| Need | Current Solution | Gap |
|------|-----------------|-----|
| Vehicle financing | Gojek/Grab offer lease-to-own, but at 24-36% APR | 10-15% APR with proper credit assessment |
| Health insurance | BPJS only (often lapsed) | Affordable gap coverage |
| Savings | GoPay wallet (no interest) | Micro-savings with auto-deposit |
| Retirement | None | Mandatory vehicle fund + retirement |
| Emergency loan | PayLater (consumer, not productive) | Productive loan for vehicle maintenance |

**Estimated addressable market:** 3M active drivers with average IDR 5M/month income = IDR 15 trillion/month collective income -- a massive base for financial services.

## 18. International Comparison: What Indonesian Super-Apps Can Learn

### 18.1 India: Ola and Uber's Struggles

In India, Ola and Uber faced similar super-app bloat issues. Ola tried to become a "super-app" with Ola Money, Ola Cafe, Ola Dash (quick commerce), and Ola Electric. By mid-2026:

- Ola Electric (the most successful spin-off) IPO'd separately
- Ola Cafe and Ola Dash were shut or drastically downsized
- Ola Money never achieved scale
- Uber exited the super-app game entirely, focusing on mobility + delivery

**Lesson:** Attempting super-app in a price-sensitive market with low ARPU rarely works. Focus on 2-3 connected services and excel at them.

### 18.2 China: Meituan's Focus Strategy

Meituan (the most successful super-app after WeChat) succeeded by:
- Starting with group buying (a single, high-frequency category)
- Expanding to food delivery (adjacent use case)
- Adding hotel/travel (logical extension of O2O)
- NEVER adding unrelated services (no messaging, no entertainment, no games)

Meituan's services are all O2O local services (food, travel, entertainment, delivery). This coherence drives cross-sell rates of 45%+.

**Application to Indonesia:** Gojek and Grab should trim to 2-3 service clusters:
1. Mobility (ride + logistics + delivery)
2. Food (food + grocery + essentials)
3. Payments (wallet + BNPL + bill pay)

Everything else (massage, cleaning, auto, games, ticketing) should be spun off or shut.

### 18.3 Vietnam: The Local Challenger Opportunity

In Vietnam, local players like Be Group and FastGo have carved out 15-20% market share against Grab by:

- Lower commissions (15% vs 25-30% for Grab)
- Better local language support
- Faster feature iteration (Vietnamese-led product teams)
- Stronger driver relationships

**Be Group started as a ride-hailing app and expanded to food delivery (BeFood) and delivery (BeDelivery)** in a disciplined, sequential manner. It is now profitable in select cities.

**Lesson for Indonesia:** A disciplined local competitor can succeed by being better, not bigger.

## 19. Conclusion: Top 12 Unserved Needs

Based on the analysis above, these are the most significant gaps in Indonesia's ride-hailing and super-app ecosystem that a new entrant or adjacent service could exploit:

1. **Tier 3+ city ride-hailing:** 100M population unserved by any platform. Need lightweight, offline-first, low-cost ride-hailing.

2. **Merchant-first food platform:** Low commission (8-12%), real-time POS integration, per-merchant analytics, merchant-controlled promotions.

3. **Same-day economy delivery:** 3-6 hour delivery at IDR 10-15K flat rate. API-first for e-commerce sellers.

4. **Instant QRIS settlement:** Accelerate QRIS settlement from T+1 to instant, charging 0.3-0.5% fee. Solve the UMKM cash flow problem.

5. **Driver cooperative / driver-owned mobility platform:** Democratically owned, 5-10% commission, profit-sharing.

6. **B2B last-mile logistics API:** Fleet API, scheduled pickups, route optimization, WMS/ERP integration. The gap between GoSend (expensive) and JNE (slow).

7. **Driver financial inclusion hub:** Vehicle financing at fair rates (10-15% APR), micro-savings, emergency loans, insurance. Platform for 3M drivers.

8. **Unified merchant POS-integrated operating system:** Cloud POS + inventory + platform order management + reconciliation. Integrates with Gojek, Grab, ShopeeFood, Shopee, Tokopedia. The "Pipedrive for Indonesian food merchants."

9. **Food aggregator comparison / price comparison:** A super-aggregator that compares menu prices, delivery fees, and wait times across GoFood, GrabFood, and ShopeeFood. Monetization via affiliate fees or subscription.

10. **AI-powered merchant menu and listing optimizer:** Photo-to-digital menu, automatic translation, SEO optimization for platform search.

11. **B2B corporate mobility platform:** Integrated ride-hailing, food delivery, and logistics for enterprises. Corporate accounts, consolidated billing, expense management, policy controls.

12. **Cross-platform payment reconciliation tool:** For merchants on 2-3 platforms: automated reconciliation, tax reporting, cash flow forecasting.

---

## Sources and Further Reading

- GoTo Financial Report FY 2025. Available at: https://www.gotocompany.com/investor-relations
- Grab Holdings Ltd. FY 2025 Annual Report (SEC Filing). Available at: https://www.grab.com/sg/ir/
- DailySocial.id. "Survei Super-App Usage Indonesia 2025." Published 2025-11. Available at: https://dailysocial.id/
- Lembaga Demografi FEB UI. "Driver Satisfaction and Multi-Apping Survey 2025." Published 2025-09.
- Populix. "Merchant Attitudes Toward Food Delivery Platforms 2025." Published 2025-10. Available at: https://populix.co/
- Momentum Works. "Food Delivery in Asia 2025." Published 2025-07. Available at: https://momentum.asia/
- East Ventures. "Digital Competitiveness Index 2025." Published 2025-08. Available at: https://east.vc/
- Bank Indonesia. "Regulation on QRIS Expansion 2022-2027." PADG No. 24/2022.
- OJK (Otoritas Jasa Keuangan). "POJK on Digital Lending 2023." POJK No. 10/POJK.05/2023.
- Kemenhub (Ministry of Transportation). "Draft Regulation on Ride-Hailing Tariffs 2025."
- Kompas.com. "Gojek dan Grab Bersaing, Siapa Paling Unggul?" Published 2025-12-15. Available at: https://money.kompas.com/
- Detik.com. "Tarif Ojol Naik 2025, Ini Dampaknya ke Pengguna." Published 2025-11-20. Available at: https://detik.com/
- Tech in Asia. "GoTo Post-Merger: Where Integration Failed." Published 2025-06. Available at: https://techinasia.com/
- Katadata.co.id. "GoTo Layoffs Tracker." Published 2024-2025. Available at: https://katadata.co.id/
- Counterpoint Research. "Indonesia Smartphone Market Q4 2025." Published 2026-01. Available at: https://counterpointresearch.com/
- Wikipedia contributors. "Gojek." Wikipedia, The Free Encyclopedia. Accessed 2026-06-24. Available at: https://en.wikipedia.org/wiki/Gojek
- Wikipedia contributors. "Goto (company)." Wikipedia, The Free Encyclopedia. Accessed 2026-06-24.
- Agnostik.org. "Super-App Performance Benchmarking on Low-End Devices 2025." Published 2025-09.
