# Digital Credit Scoring for UMKM Unbankable: Turning QRIS Transaction Data into Agunan Digital

**Date observed:** 2026-06-29 (promoted from inbox)
**Signal strength:** 5 (Rp2,500T+ undisbursed credit, 64M UMKM unbankable, QRIS 119% growth, verified demand-mining files)
**Category:** cross (03-id-business-trends + 07-gaps-and-opportunities)
**Synthesis thesis type:** Fintech infrastructure play (credit scoring as a service)
**Cross-folders:** 03 (UMKM unbankable, 80% manual bookkeeping, QRIS settlement issues), 07 (opportunity one-pager)

---

## 1. Synthesis Thesis: The Rp2.500 Triliun Unlock

Indonesia has 64 juta UMKM contributing 60.5-61.7% to GDP and absorbing 97% of the workforce (BPS data, Antara May 2026). Yet Rp2.500 triliun in committed bank credit sits undistributed, while the majority of these businesses cannot access a single rupiah of formal financing. The reason is brutally simple: banks require physical collateral (sertifikat tanah, BPKB) that 75% of UMKM do not possess.

Meanwhile, QRIS (Quick Response Code Indonesian Standard) transaction volume grew 119% in Q1-2026 (Bank Indonesia data, cited Antara May 2026). Every QRIS transaction creates a digital footprint: amount, time of day, frequency, customer repeat rate, seasonal patterns, and growth trajectory. This data, currently sitting unused in payment processor databases, is the missing collateral. It is what the Antara editorial called "agunan masa depan" (future collateral).

**The wedge:** Build a credit scoring engine that ingests QRIS transaction data (with merchant consent) and outputs a risk score that banks can use to underwrite collateral-free micro-loans to UMKM. The platform sits between 64 juta UMKM and Rp2.500 triliun in undistributed credit, taking a 1-2% commission on loans originated.

**Why now:**
- BI Rate rose to 5.25% in May 2026, tightening credit further for risky borrowers (Antara, May 2026)
- KLM (Kebijakan Insentif Likuiditas Makroprudensial) incentivizes banks to lend to UMKM, but banks still need risk assessment tools (Antara, May 2026)
- QRIS adoption is at critical mass: the 119% Q1-2026 growth means millions of merchants now have 6-12 months of digital transaction history
- Permendag 19/2026 mandates NIB for e-commerce merchants, creating a legal identity layer that can be linked to credit scoring (Antara, June 2026)
- 80% of UMKM still do manual bookkeeping (OCBC Business Fitness Index 2023), so QRIS data is the ONLY digital financial record for most merchants

---

## 2. Problem Deep-Dive: The Unbankability Trap

### 2.1. Why 64 Juta UMKM Cannot Get Credit

The traditional banking credit assessment model requires five things that most UMKM lack:

**Physical collateral (agunan fisik).** Banks typically require sertifikat tanah (land certificate) or BPKB (vehicle ownership document) worth 120-150% of the loan amount. For a warung owner seeking Rp10 juta working capital, this means needing Rp12-15 juta in registered assets as collateral. Most micro-entrepreneurs rent their stall, use borrowed equipment, or operate from their home. Their "assets" are inventory and goodwill, neither of which banks accept. (Source: Antara, "Algoritma trotoar UMKM keliling", May 2026)

**Formal financial statements (laporan keuangan).** Banks require audited or at minimum internally prepared financial statements showing revenue, expenses, and profitability. 80% of UMKM record finances manually in buku tulis (notebooks), if at all (OCBC Business Fitness Index 2023, cited Fortune Indonesia January 2024). A warung owner who sells Rp500.000/day in cash cannot prove this to a bank officer.

**Registered business identity (legalitas usaha).** Until Permendag 19/2026, many e-commerce merchants operated without NIB. Even now, the transition is incomplete. Without NIB, banks cannot even begin the credit assessment process. (Source: Antara, "Mendag tegaskan NIB untuk pedagang e-commerce bukan untuk pajak", June 2026)

**Credit history (riwayat kredit).** First-time borrowers have no credit score at all. SLIK (Sistem Layanan Informasi Keuangan) under OJK shows blank records for the majority of micro-entrepreneurs. Without history, banks default to rejection.

**Digital footprint (jejak digital).** Traditional banks do not consider QRIS transaction data, marketplace sales data, or ride-hailing income as creditworthy evidence. The data exists but is not in the format banks need.

### 2.2. The Alternative: Predatory Lending

When formal banks reject them, UMKM turn to the only available alternatives:

| Source | Interest Rate (monthly) | Effective Annual | Risk |
|--------|------------------------|------------------|------|
| KUR (Kredit Usaha Rakyat) | 0.5% (6% p.a.) | 6% | Low, but hard to access |
| Fintech lending resmi (OJK) | 0.5-2% | 6-24% | Medium |
| Pinjol ilegal | 1-4% | 12-48% | Extreme (debt traps, harassment) |
| Rentenir / lintah darat | 10-30% | 120-360% | Extreme |

A warung owner who borrows Rp5 juta from a pinjol at 2% monthly pays Rp1.2 juta in interest over 6 months, eating 20% of the principal. At 4% monthly, the interest alone exceeds Rp2.4 juta. This is why OJK reported Rp23,7 triliun in pinjol outstanding to 32+ juta borrowers in 2024, with default rates climbing. (Source: OJK financial inclusion data, multiple reports)

The fundamental problem is not demand for credit (UMKM desperately need it) or supply of capital (Rp2.500 triliun sits undistributed). The problem is information asymmetry: banks cannot assess risk for businesses that operate entirely in cash.

### 2.3. QRIS as the Unlocks

QRIS transaction data contains exactly the signals banks need but cannot currently access:

**Revenue signal.** Total daily/weekly/monthly QRIS transaction volume directly proxies revenue. A warung that processes Rp300.000-500.000/day in QRIS payments has provable, auditable revenue that no buku tulis can provide.

**Consistency signal.** Transaction frequency and regularity indicate business stability. A merchant with daily QRIS transactions for 6+ months is fundamentally different from one with sporadic transactions.

**Growth signal.** Month-over-month transaction volume growth indicates expanding business. A merchant growing 10-15% monthly is a lower credit risk than one declining.

**Seasonality signal.** Transaction patterns reveal business cycles. A bakso vendor who spikes during Ramadan and school holidays has predictable cash flow that can inform repayment scheduling.

**Customer retention signal.** Repeat customer patterns (if the QRIS system captures device-level or account-level data) indicate business quality and customer satisfaction.

**Time-of-day signal.** Transaction timestamps reveal operational patterns: does the merchant open on time? Close on time? Are there gaps that suggest problems?

The Antara editorial (May 2026) captured this perfectly: "Setiap transaksi yang terekam secara digital menciptakan rekam jejak keuangan yang valid. Hal ini secara otomatis menyelesaikan kendala klasik UMKM, yaitu ketiadaan laporan keuangan resmi."

Translation: every digitally recorded transaction creates a valid financial trail, automatically solving UMKM's classic problem of having no official financial statements.

---

## 3. Market Sizing: Three Revenue Streams

### Segment A: Micro-Loans (KUR-Alternative)

**Target:** UMKM with Rp1-10 juta working capital need, 6+ months QRIS history
**Size:** ~20 juta active QRIS merchants (of 64M UMKM total, est. 30% active digital)
**Average loan size:** Rp5 juta
**Loan origination volume (Y1 at 5% capture):** 1M loans = Rp5T originated
**Commission (1-2%):** Rp50-100M revenue
**Comparison:** KUR disbursed Rp340T in 2024 to ~15 juta debitur (Kemenkeu data). A platform capturing even 1% of this market = Rp3.4T originated.

### Segment B: Credit Scoring as a Service (B2B)

**Target:** Banks, fintech lenders, cooperatives that want to lend to UMKM but lack risk assessment tools
**Size:** ~120 commercial banks + ~1.500 BPR (Bank Perkreditan Rakyat) + ~85.000 Koperasi Simpan Pinjam
**Revenue model:** SaaS subscription + per-score fee
**Average ASP:** Rp5-15 juta/bulan per bank institution
**Y1 target (10 institutions):** Rp600M - Rp1.8M revenue
**Comparison:** PEFINDO iRating charges Rp15-50 juta per credit rating for corporates. A micro-enterprise scoring service at Rp5 juta/month is 10x cheaper and 1000x more scalable.

### Segment C: Data Analytics and Insights

**Target:** FMCG companies, distributors, market researchers who want ground-truth data on micro-economy performance
**Size:** Unilever, Indofood, Mayora, and 50+ FMCG companies spend Rp50-200M/year on market research
**Revenue model:** Anonymized, aggregated QRIS transaction data sold as market intelligence
**Y1 target (5 clients):** Rp250M - Rp1B revenue
**Comparison:** Nielsen Indonesia charges Rp200-500M/year for retail panel data. QRIS-based data is more granular, more real-time, and covers the informal economy that Nielsen misses.

### Total Revenue Estimate

| Stream | Y1 Revenue | Y2 Revenue | Y3 Revenue |
|--------|-----------|-----------|-----------|
| Loan origination commission | Rp50-100M | Rp500M-1B | Rp2-5B |
| B2B credit scoring SaaS | Rp600M-1.8B | Rp3-6B | Rp8-15B |
| Data analytics | Rp250M-1B | Rp1-3B | Rp3-8B |
| **Total** | **Rp900M-2.9B** | **Rp4.5-10B** | **Rp13-28B** |

---

## 4. Existing Solutions and Why They Fail

### 4.1. Government Programs

**KUR (Kredit Usaha Rakyat)**
- Pros: Low interest (6% p.a.), government-backed, Rp340T disbursed in 2024
- Cons: Requires physical collateral for loans above Rp10 juta, bureaucratic application process, limited branch coverage in rural areas, 2-4 week approval time
- Failure mode: Only 25% of UMKM have access to formal financial institutions (Wikipedia Indonesia, citing Detik Finance 2011 data)
- Coverage gap: Rp2.500 triliun committed but undistributed

**Lembaga Keuangan Mikro (LKM) / BPR**
- Pros: More accessible than commercial banks, local presence
- Cons: Often charge higher interest (12-24% p.a.), limited digital infrastructure, inconsistent risk assessment methods, some BPR have collapsed due to poor lending decisions
- Failure mode: BPR NPL (non-performing loans) ratio averages 3-5%, some reach 10%+ because they lack proper credit scoring tools

### 4.2. Fintech Lending

**Kominfo/OJK-registered P2P lending**
- Pros: Fast approval (hours), no physical collateral required, mobile-first
- Cons: High interest (0.5-2% monthly), short tenor (30-90 days), many target consumers not businesses, aggressive collection practices
- Failure mode: Only 32 juta of 64M UMKM are reached; average loan size Rp2-3 juta (too small for meaningful business investment); default rates 4-8%

**Akulaku, Kredivo, Modalku, Investree**
- Pros: Digital-first, some have QRIS integration
- Cons: Still require some form of digital footprint (salary slip, credit card history, marketplace seller data), which most micro-UMKM lack
- Failure mode: The "unbankable" 40M+ UMKM are precisely the ones these platforms also cannot serve because they have no digital financial trail BEYOND QRIS

### 4.3. QRIS-Native Players

**LinkAja, GoPay, OVO, DANA merchant data**
- Pros: Already have QRIS transaction data for millions of merchants
- Cons: Not in the business of credit scoring, regulatory restrictions on using payment data for lending (PSD2-like concerns), siloed data across multiple platforms
- Failure mode: Each wallet sees only its own QRIS transactions, not the full picture. A merchant accepting QRIS from GoPay, OVO, DANA, and ShopeePay has fragmented data across four platforms. No single platform has the complete picture.

### 4.4. Alternative Credit Scoring Startups

**Cicil, Pintek, Taralite**
- Pros: Some use alternative data for credit scoring
- Cons: Focused on education financing (Cicil) or invoice factoring (Pintek), not on micro-merchant QRIS-based scoring
- Failure mode: None of them specifically aggregate cross-platform QRIS data for credit scoring

**The gap:** No existing player aggregates QRIS data across multiple payment providers (GoPay, OVO, DANA, ShopeePay, LinkAja, bank QRIS) into a unified credit score that banks can use for underwriting. Each payment provider has its own data silo. The platform that breaks these silos captures the entire market.

---

## 5. Technical Architecture: How It Works

### 5.1. Data Ingestion Layer

The platform needs to aggregate QRIS transaction data from multiple sources. Three approaches:

**Approach A: Direct API integration with payment providers.**
- Each PJSP (Penyelenggara Jasa Sistem Pembayaran) has APIs for merchant transaction history
- GoPay, OVO, DANA, ShopeePay, LinkAja all offer merchant dashboards with transaction data
- Challenge: Each has different API formats, authentication, and rate limits
- Implementation: Build adapters for each PJSP, normalize data into unified schema

```python
# Pseudo-code: QRIS transaction ingestion
class QRISIngestion:
    def __init__(self):
        self.adapters = {
            'gopay': GoPayAdapter(),
            'ovo': OVOAdapter(),
            'dana': DANAAdapter(),
            'shopeepay': ShopeePayAdapter(),
            'linkaja': LinkAjaAdapter(),
            'bank_qris': BankQRISAdapter(),
        }
    
    def fetch_merchant_transactions(self, merchant_id, provider, months=6):
        """Fetch last N months of QRIS transactions for a merchant."""
        adapter = self.adapters[provider]
        raw_transactions = adapter.get_transactions(
            merchant_id=merchant_id,
            start_date=datetime.now() - timedelta(days=months*30),
            end_date=datetime.now()
        )
        return self.normalize(raw_transactions, provider)
    
    def normalize(self, transactions, provider):
        """Normalize transactions from different providers to common schema."""
        normalized = []
        for tx in transactions:
            normalized.append({
                'merchant_id': tx.merchant_id,
                'amount': tx.amount,  # in IDR
                'timestamp': tx.timestamp,
                'payment_method': tx.payment_method,  # QRIS sub-type
                'customer_hash': self.hash_customer(tx.customer_id),
                'status': tx.status,  # success, refund, pending
                'provider': provider,
            })
        return normalized
```

**Approach B: User-provided data via photo OCR.**
- Merchant photographs daily QRIS receipts/struk
- OCR extracts transaction amounts and timestamps
- Lower accuracy but works for merchants who don't have API access
- Good for MVP before API integrations are complete

```python
# Pseudo-code: Struk OCR processing
class StrukOCR:
    def process_receipt(self, image_path):
        """Process a photograph of a QRIS receipt."""
        # Use Tesseract or Google Vision API
        text = self.ocr_engine.extract_text(image_path)
        
        # Parse structured fields
        parsed = {
            'amount': self.extract_amount(text),
            'timestamp': self.extract_datetime(text),
            'merchant_name': self.extract_merchant(text),
            'transaction_id': self.extract_ref_number(text),
            'payment_method': self.extract_payment_type(text),
        }
        
        # Validate against known patterns
        if self.validate(parsed):
            return parsed
        else:
            return self.flag_for_review(parsed)
```

**Approach C: WhatsApp bot for manual entry.**
- Merchant sends daily sales summary via WhatsApp: "jualan hari ini 450rb, 23 transaksi"
- Chatbot parses and stores
- Lowest tech barrier, highest manual effort
- Good for Tier 3 cities where smartphone penetration is high but app usage is low

### 5.2. Feature Engineering Layer

Raw QRIS transactions must be transformed into credit scoring features. Key features:

```python
# Pseudo-code: Feature engineering for credit scoring
class QRISFeatureEngine:
    def compute_features(self, merchant_id, transactions):
        """Compute credit scoring features from QRIS transactions."""
        df = pd.DataFrame(transactions)
        df['date'] = pd.to_datetime(df['timestamp']).dt.date
        
        features = {}
        
        # Revenue features
        features['avg_daily_revenue'] = df.groupby('date')['amount'].sum().mean()
        features['median_daily_revenue'] = df.groupby('date')['amount'].sum().median()
        features['revenue_std'] = df.groupby('date')['amount'].sum().std()
        features['revenue_cv'] = features['revenue_std'] / features['avg_daily_revenue']
        
        # Growth features
        monthly_revenue = df.groupby(df['date'].apply(lambda x: x.strftime('%Y-%m')))['amount'].sum()
        if len(monthly_revenue) >= 2:
            features['mom_growth'] = (monthly_revenue.iloc[-1] / monthly_revenue.iloc[-2]) - 1
            features['3m_cagr'] = self.compute_cagr(monthly_revenue, periods=3)
        else:
            features['mom_growth'] = 0
            features['3m_cagr'] = 0
        
        # Consistency features
        active_days = df['date'].nunique()
        total_days = (df['date'].max() - df['date'].min()).days + 1
        features['active_day_ratio'] = active_days / max(total_days, 1)
        features['avg_transactions_per_day'] = len(df) / max(active_days, 1)
        
        # Customer retention features
        features['unique_customers'] = df['customer_hash'].nunique()
        features['repeat_customer_ratio'] = 1 - (features['unique_customers'] / len(df))
        
        # Time pattern features
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        features['peak_hour'] = df.groupby('hour')['amount'].sum().idxmax()
        features['business_hours_ratio'] = df[(df['hour'] >= 6) & (df['hour'] <= 21)].shape[0] / len(df)
        
        # Risk features
        features['refund_rate'] = df[df['status'] == 'refund'].shape[0] / len(df)
        features['avg_ticket_size'] = df['amount'].mean()
        features['max_single_transaction'] = df['amount'].max()
        features['revenue_concentration'] = df.nlargest(5, 'amount')['amount'].sum() / df['amount'].sum()
        
        # Streak features
        features['longest_active_streak'] = self.compute_longest_streak(df['date'].sort_values())
        features['current_streak'] = self.compute_current_streak(df['date'].sort_values())
        
        return features
```

### 5.3. Credit Scoring Model

The scoring model uses a hybrid approach:

**Layer 1: Rule-based scoring (for fast decisions)**
- Binary checks: minimum 3 months QRIS history, minimum Rp500.000/month volume, minimum 5 active days/week
- Automatic rejection: refund rate > 20%, revenue decline > 30% month-over-month
- Automatic approval: 12+ months history, consistent revenue growth, repeat customer ratio > 30%

**Layer 2: Machine learning model (for nuanced risk)**
- Algorithm: Gradient Boosted Trees (XGBoost/LightGBM) for interpretability
- Training data: Historical loan performance from partner banks (initially synthetic, then real)
- Features: All 25+ features from the feature engineering layer
- Output: Probability of default (PD) score, 0-1000 scale
- Explainability: SHAP values for each feature, so bank officers understand why a score was given

```python
# Pseudo-code: Credit scoring model
class UMKMCreditScorer:
    def __init__(self):
        self.rule_engine = RuleEngine()
        self.ml_model = self.load_model('umkm_credit_model.pkl')
        self.feature_engine = QRISFeatureEngine()
    
    def score(self, merchant_id, transactions):
        """Generate credit score for a UMKM merchant."""
        
        # Layer 1: Rule-based checks
        rule_result = self.rule_engine.evaluate(transactions)
        if rule_result.auto_reject:
            return CreditScore(
                score=0,
                decision='REJECT',
                reason=rule_result.rejection_reason,
                confidence=0.95
            )
        if rule_result.auto_approve:
            return CreditScore(
                score=900,
                decision='AUTO_APPROVE',
                reason='Meets all criteria',
                confidence=0.85
            )
        
        # Layer 2: ML scoring
        features = self.feature_engine.compute_features(merchant_id, transactions)
        feature_vector = self.prepare_feature_vector(features)
        
        pd_score = self.ml_model.predict_proba(feature_vector)[0][1]
        score_1000 = int(pd_score * 1000)
        
        # Risk categorization
        if score_1000 >= 700:
            decision = 'APPROVE'
            max_loan = self.compute_max_loan(features, score_1000)
        elif score_1000 >= 400:
            decision = 'MANUAL_REVIEW'
            max_loan = self.compute_max_loan(features, score_1000) * 0.5
        else:
            decision = 'REJECT'
            max_loan = 0
        
        # Explainability
        shap_values = self.explain(features)
        
        return CreditScore(
            score=score_1000,
            decision=decision,
            max_loan=max_loan,
            shap_explanation=shap_values,
            confidence=self.compute_confidence(transactions)
        )
    
    def compute_max_loan(self, features, score):
        """Compute maximum loan amount based on revenue and score."""
        monthly_revenue = features['avg_daily_revenue'] * 30
        max_loan_months = 3 + (score - 400) / 100  # 3-9 months of revenue
        max_loan = monthly_revenue * min(max_loan_months, 6)
        return min(max_loan, 50_000_000)  # Cap at Rp50 juta
```

### 5.4. Bank Integration Layer

The platform must deliver scores in a format banks can consume:

**API endpoint for real-time scoring:**
```python
# Bank calls this API when merchant applies for loan
@app.post("/api/v1/score")
async def score_merchant(request: ScoreRequest):
    # Authenticate bank API key
    bank = authenticate_bank(request.api_key)
    
    # Fetch QRIS data (merchant must have consented)
    transactions = await fetch_merchant_qris(
        merchant_id=request.merchant_id,
        consent_token=request.consent_token
    )
    
    # Generate score
    scorer = UMKMCreditScorer()
    score = scorer.score(request.merchant_id, transactions)
    
    # Log for audit trail
    await audit_log(bank, request.merchant_id, score)
    
    return ScoreResponse(
        merchant_id=request.merchant_id,
        score=score.score,
        decision=score.decision,
        max_loan=score.max_loan,
        explanation=score.shap_explanation,
        data_freshness=score.confidence,
        generated_at=datetime.now()
    )
```

**Batch scoring for portfolio review:**
```python
# Bank uploads list of existing merchants for batch scoring
@app.post("/api/v1/batch-score")
async def batch_score(request: BatchScoreRequest):
    results = []
    for merchant_id in request.merchant_ids:
        transactions = await fetch_merchant_qris(merchant_id)
        score = scorer.score(merchant_id, transactions)
        results.append(score)
    
    return BatchScoreResponse(
        results=results,
        summary={
            'total': len(results),
            'approve': sum(1 for r in results if r.decision == 'APPROVE'),
            'review': sum(1 for r in results if r.decision == 'MANUAL_REVIEW'),
            'reject': sum(1 for r in results if r.decision == 'REJECT'),
        }
    )
```

### 5.5. Merchant-Facing Mobile App

The merchant experience must be ultra-simple:

1. **Onboarding (3 minutes):** WhatsApp chatbot guides merchant through consent flow. Merchant links QRIS accounts (GoPay, OVO, etc.) or starts uploading struk photos.

2. **Score dashboard:** Simple visual showing credit score, estimated loan amount, and what to improve. Color-coded: green (ready for loan), yellow (needs more data), red (too risky).

3. **Loan application:** One-tap application to partner bank. Platform pre-fills all data. Merchant just confirms.

4. **Repayment tracking:** Integrated with QRIS, so loan repayments are automatically deducted from daily QRIS settlements (with merchant consent).

```python
# Pseudo-code: WhatsApp bot for merchant onboarding
class MerchantOnboardingBot:
    def handle_message(self, phone, message):
        state = self.get_state(phone)
        
        if state == 'WELCOME':
            return self.send_welcome(phone)
        
        elif state == 'AWAITING_CONSENT':
            if message.lower() in ['ya', 'yes', 'setuju', 'consent']:
                return self.process_consent(phone)
            else:
                return self.send_consent_reminder(phone)
        
        elif state == 'AWAITING_QRIS_LINK':
            # Merchant sends screenshot of QRIS dashboard
            return self.process_qris_screenshot(phone, message)
        
        elif state == 'AWAITING_STRUK':
            # Merchant sends daily struk photos
            return self.process_struk_photo(phone, message)
        
        elif state == 'SCORE_READY':
            return self.send_score_result(phone)
```

---

## 6. Revenue Model and Unit Economics

### 6.1. Revenue Streams

**Stream 1: Loan origination commission (1-2% of loan amount)**
- Platform originates loan through partner bank
- Bank disburses directly to merchant
- Platform takes 1-2% as origination fee
- At Rp5 juta average loan, this is Rp50.000-100.000 per loan

**Stream 2: Credit scoring API (B2B SaaS)**
- Banks pay monthly subscription + per-score fee
- Monthly subscription: Rp5-15 juta per bank
- Per-score fee: Rp5.000-15.000 per query
- For a BPR doing 100 credit assessments/month: Rp5-15 juta + Rp500K-1.5M = Rp5.5-16.5 juta/month

**Stream 3: Data analytics (anonymized, aggregated)**
- FMCG companies, distributors, market researchers
- Monthly subscription: Rp20-50 juta per client
- Reports on merchant performance by region, category, and time period

**Stream 4: Premium merchant services**
- Score improvement coaching: Rp25.000-50.000/month
- Instant settlement guarantee: 0.1-0.3% fee on QRIS transactions
- Micro-insurance products: commission-based

### 6.2. Unit Economics

| Metric | Value |
|--------|-------|
| Customer acquisition cost (merchant) | Rp15.000-25.000 (WhatsApp marketing + onboarding support) |
| Customer lifetime value (merchant, 24 months) | Rp300.000-600.000 (fees from loan origination + services) |
| LTV/CAC ratio | 12-40x |
| Gross margin (B2B SaaS) | 80-90% |
| Gross margin (loan origination) | 70-80% (after partner bank share) |
| Break-even | Month 18-24 at 50.000 active merchants |

### 6.3. Comparison to Existing Pricing

| What merchant pays now | What merchant would pay platform |
|------------------------|----------------------------------|
| Pinjol: Rp1-4% monthly interest | Loan origination: 1-2% one-time |
| KUR: 6% p.a. but requires collateral | Platform: 1-2% origination, no collateral |
| Jasa konsultan: Rp500K-2M one-time for KUR application | Platform: Rp0 (embedded in loan fee) |
| Manual bookkeeper: Rp50-100K/month | Platform: Rp0 (QRIS data is automatic) |

---

## 7. Regulatory Landscape

### 7.1. Bank Indonesia (BI)

- QRIS is BI's national QR payment standard, launched August 2019
- BI encourages QRIS adoption for financial inclusion
- BI Rate at 5.25% (May 2026) and KLM policy incentivizes bank lending to UMKM
- BI has not yet issued specific regulations on using QRIS data for credit scoring, but the general framework under POJK 10/2022 (Financial Innovation) allows sandbox testing
- Risk: BI may restrict access to QRIS transaction data for non-payment purposes

### 7.2. OJK (Otoritas Jasa Keuangan)

- OJK regulates fintech lending (P2P) under POJK 10/2022
- OJK requires credit scoring for all lending decisions
- OJK encourages alternative data for credit scoring (circular letter on responsible lending)
- OJK's SLIK system provides credit history but only for borrowers who already have formal credit
- Risk: OJK may require specific licensing for credit scoring as a service

### 7.3. PDP Law (Personal Data Protection)

- UU PDP (Law No. 27/2022) requires explicit consent for processing personal data
- QRIS transaction data contains personal data (customer IDs, transaction amounts, timestamps)
- Platform must obtain merchant consent AND customer anonymization
- Risk: Non-compliance penalties up to 2% of annual revenue

### 7.4. Risk Mitigation

- Register with OJK sandbox for fintech innovation
- Implement privacy-by-design: all customer data anonymized at ingestion
- Obtain ISO 27001 certification for data security
- Partner with established bank (BRI, BNI, or Mandiri) as primary lending partner to reduce regulatory friction
- Maintain data processing within Indonesia (no cross-border data transfer)

---

## 8. Competitive Moat and Defensibility

### 8.1. Data Network Effects

Every merchant that joins the platform improves the credit scoring model. More data = better predictions = more banks trust the scores = more merchants want to join = more data. This creates a flywheel that is nearly impossible for competitors to replicate once the platform reaches critical mass.

### 8.2. Cross-Platform Aggregation Advantage

The platform aggregates QRIS data across ALL payment providers (GoPay, OVO, DANA, ShopeePay, LinkAja, bank QRIS). No single payment provider has this cross-platform view. A GoPay merchant might also accept OVO and DANA. Only the aggregation platform sees the complete picture.

### 8.3. Bank Trust and Integration

Once a major bank (e.g., BRI, which has the largest UMKM lending portfolio through KUR) integrates the scoring API, switching costs are high. Bank risk departments build their decision trees around the scoring model. Replacing it means rebuilding risk frameworks.

### 8.4. Merchant Lock-in

Merchants who build credit history on the platform have an incentive to stay: their score improves over time. Leaving the platform means starting from zero with a new provider. This is similar to how credit card users stay with issuers to maintain their credit score.

---

## 9. Implementation Roadmap

### Phase 1: MVP (Months 1-3)

**Goal:** 1.000 merchants onboarded, scoring model operational
- WhatsApp bot for merchant onboarding and struk photo upload
- Basic OCR for struk processing
- Rule-based scoring engine (no ML yet)
- Partnership with 1 BPR (Bank Perkreditan Rakyat) for pilot lending
- Estimated cost: Rp200-300 juta

### Phase 2: API Integration (Months 4-6)

**Goal:** 10.000 merchants, 3 bank partners
- Direct API integration with GoPay and OVO (largest QRIS providers)
- ML credit scoring model trained on pilot data
- Bank dashboard for score visualization and loan decision
- Estimated cost: Rp500M-1B

### Phase 3: Scale (Months 7-12)

**Goal:** 100.000 merchants, 10+ bank partners
- Full QRIS provider coverage (all 5 major e-wallets + bank QRIS)
- B2B credit scoring API launch
- Data analytics product for FMCG clients
- Mobile app launch (replacing WhatsApp bot)
- Estimated cost: Rp2-3B

### Phase 4: Ecosystem (Months 13-24)

**Goal:** 1M merchants, 50+ bank partners, regional expansion
- Micro-insurance integration
- Instant settlement guarantee product
- Cross-border QRIS data sharing (Singapore, Thailand, Malaysia)
- IPO preparation or Series B fundraise

---

## 10. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| QRIS data access restricted by BI | Medium | High | Register in OJK fintech sandbox, build relationships with BI officials, demonstrate financial inclusion benefits |
| Banks refuse to use alternative scoring | Medium | High | Start with BPR (smaller, more agile), prove default rates are lower than traditional scoring, then approach major banks |
| Merchant consent rates too low | Low | Medium | WhatsApp onboarding is frictionless, demonstrate clear value (access to credit), offer incentive (free score report) |
| ML model accuracy insufficient | Medium | Medium | Start with rule-based scoring, use ML only for edge cases, continuously retrain with loan performance data |
| Competition from GoPay/OVO building their own scoring | Medium | High | Cross-platform aggregation is the moat. GoPay cannot score an OVO merchant. Only the aggregator sees the full picture |
| Regulatory crackdown on fintech lending | Low | Medium | Position as credit scoring service (B2B), not as direct lender. Banks do the lending, platform does the scoring |

---

## 11. New Gaps Discovered During Research

While researching this opportunity, the following gaps surfaced that the vault does not yet cover:

1. **QRIS settlement speed arbitrage.** Merchants lose 1-3 days of float when QRIS settlements are delayed (as documented in dana-qris-tertahan.md). A platform that guarantees same-day settlement for a 0.1% fee could generate significant recurring revenue. This is adjacent to but distinct from the credit scoring play. Add to `03-id-business-trends/bottlenecks/` as `qris-settlement-speed-arbitrage.md`.

2. **Cross-border QRIS credit scoring.** BI is expanding QRIS cross-border to Singapore, Thailand, Malaysia, and the Philippines. Indonesian merchants receiving cross-border QRIS payments have a unique credit profile (foreign customer base, forex exposure). No one is building credit scoring for cross-border micro-merchants. Add to `07-gaps-and-opportunities/inbox/` as `cross-border-qris-credit-scoring.md`.

3. **BPR digital transformation gap.** 1.500+ BPR (Bank Perkreditan Rakyat) in Indonesia lack modern core banking systems, let alone credit scoring tools. Many still use Excel for loan assessment. A SaaS platform that modernizes BPR operations (not just credit scoring but also loan origination, CRM, and regulatory reporting) is a much larger market than credit scoring alone. Add to `07-gaps-and-opportunities/inbox/` as `bpr-digital-transformation-saas.md`.

---

## 12. Sources

1. Antara News, "Denyut rupiah di nadi UMKM" (May 23, 2026). Rp2.500 triliun undisbursed credit, KLM policy, BI Rate 5.25%, UMKM contribution to GDP. URL: https://www.antaranews.com/berita/5579744/denyut-rupiah-di-nadi-umkm

2. Antara News, "Algoritma trotoar UMKM keliling" (May 4, 2026). QRIS 119% growth Q1-2026, digital credit scoring concept, "agunan masa depan", UMKM formalization via QRIS. URL: https://www.antaranews.com/berita/5552925/algoritma-trotoar-umkm-keliling

3. Fortune Indonesia, "80% UMKM RI Masih Catat Keuangan Manual" (January 8, 2024). OCBC Business Fitness Index: 80% manual bookkeeping, only 32% digital adoption. URL: https://www.fortuneidn.com/finance/80-umkm-ri-masih-catat-keuangan-manual-pahami-fungsi-digitalisasi-00-ccw2k-3cjmgn

4. Wikipedia Indonesia, "Usaha mikro, kecil, dan menengah". 64 juta UMKM, 60% PDB, 97% tenaga kerja, 25% akses keuangan formal. URL: https://id.wikipedia.org/wiki/Usaha_mikro,_kecil,_dan_menengah

5. Antara News, "Mendag tegaskan NIB untuk pedagang e-commerce bukan untuk pajak" (June 22, 2026). NIB wajib untuk pedagang e-commerce, akses perbankan. URL: https://www.antaranews.com/berita/5617720/mendag-tegaskan-nib-untuk-pedagang-e-commerce-bukan-untuk-pajak

6. Media Konsumen, "Keluhan Pengusaha UMKM: Dana QRIS Shopee Rp10 Juta Tertahan" (February 1, 2026). QRIS settlement issues, merchant pain. URL: https://mediakonsumen.com/2026/02/01/surat-pembaca/keluhan-pengusaha-umkm-dana-qris-shopee-rp10-juta-tertahan-modal-saya-macet-total

7. CNN Indonesia, "Melihat Aturan Biaya Admin QRIS" (January 14, 2026). MDR QRIS regulations, merchant cost burden. URL: https://www.cnnindonesia.com/ekonomi/20260114131228-85-1187122/melihat-aturan-biaya-admin-qris

8. Liputan6, "QRIS UMKM Bermasalah, Menteri Maman Jamin Tak Rugikan Pelaku Usaha" (November 7, 2024). Puluhan ribu UMKM terdampak InterActive QRIS. URL: https://www.liputan6.com/bisnis/read/5773859/qris-umkm-bermasalah-menteri-maman-jamin-tak-rugikan-pelaku-usaha

9. Bank Indonesia, QRIS Transaction Statistics (Q1-2026). 119% growth in QRIS transaction volume. Source cited in Antara May 2026.

10. Vault files: umkm-unbankable-kredit-mengendap-pedagang-mikro-tak-bisa-akses-modal.md, umkm-80-persen-pembukuan-manual-literasi-keuangan-minim.md, dana-qris-tertahan-umkm-kehilangan-modal.md
