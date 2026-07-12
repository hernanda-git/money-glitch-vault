# News & Social Sentiment Scoring

> Signal layer that turns `01-crawler-scrapper` X/Twitter cashtag chatter (`$BBRI $TLKM
> $BTC`) and headline sentiment into a **win-probability prior `p`** for the Kelly engine
> (`02/risk-management/position-sizing-kelly.md`). This is the `signals/` layer the ORB
> strategy references but that did not exist.

**File:** `02-trading-bot/signals/news-sentiment-scoring.md`
**Created:** 2026-07-12
**Category:** Signal layer (scaffold)
**Consumed by:** `04-freelancer-ai-agent/signal-agent/` (R4) → `position-sizing-kelly`

---

## 1. Why this exists

The `01` playbook already defines the highest-signal local query: cashtag monitoring
`($BBRI OR $TLKM OR $BTC ...)`. This module scores that firehose into a per-asset sentiment
signal in `[-1, +1]`, which is then mapped to a trade win-probability prior `p ∈ [0.4, 0.6]`
(the Kelly engine rejects edges outside that band as noise).

## 2. Scoring model (lexicon + volume)

```python
# 02-trading-bot/signals/sentiment.py
BEAR = ["jatuh","turun","rugj","bearish","profit taking","koreksi","panic","capit"]
BULL = ["naik","bullish","breakout","all time high","cuan","lonjak","rebound","green"]

def score_texts(texts: list[str]) -> float:
    """Return sentiment in [-1, +1] from a list of posts/headlines."""
    s = 0.0
    n = 0
    for t in texts:
        tl = t.lower()
        bull = sum(w in tl for w in BULL)
        bear = sum(w in tl for w in BEAR)
        if bull or bear:
            s += (bull - bear) / max(1, (bull + bear))
            n += 1
    return s / n if n else 0.0

def to_win_prob(sentiment: float) -> float:
    """Map [-1,1] -> [0.40, 0.60] (neutral=0.5). Kelly engine ignores edge<band."""
    return round(0.5 + 0.10 * max(-1.0, min(1.0, sentiment)), 4)
```

## 3. Volume weighting

Raw sentiment is noisy; weight by engagement (`min_faves`, retweets) using the `01` query
operator `min_faves:5`. High-volume bullish consensus → `p` nudges toward 0.58; lone posts
are discarded (n<3 → `p=0.5`, no edge).

## 4. Pipeline wiring

```
01 X cashtag query (cron, every 6h)
   -> 02/signals/sentiment.py  -> p per asset
   -> 02/risk-management/kelly.py -> position_idr + stop
   -> 04 signal-agent -> WhatsApp/Telegram alert
```

## 5. Caveats

- This is a **prior**, not a forecast. It is deliberately conservative (band 0.4–0.6) so the
  agent never over-bets on social noise.
- Indonesian retail sentiment is a *contrarian* sometimes; the signal-agent should log when
  sentiment diverges from price action (FOMO trap). Tag any external market figure
  `verify-live`.

## 6. New gaps

- No broker execution module — the agent advises, doesn't trade (retail constraint from ORB).
- Sentiment lexicon should be expanded per-asset; current list is a starter set.
