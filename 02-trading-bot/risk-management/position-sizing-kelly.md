# Position Sizing & Risk Management — Kelly / Drawdown

> Risk engine for the trading-bot wedge. Implements the **Kelly criterion** position sizing
> and a **drawdown cap** that the `idx-opening-range-breakout.md` strategy references but
> that did not exist. Consumed by the `04` signal-agent (R4) to emit "size at 0.5× Kelly,
> stop at −4%" alerts. Retail constraint: **shorting disabled**, so sizing is long-only.

**File:** `02-trading-bot/risk-management/position-sizing-kelly.md`
**Created:** 2026-07-12
**Category:** Risk engine (scaffold)
**Consumed by:** `04-freelancer-ai-agent/signal-agent/` (R4), `02/strategies/idx-opening-range-breakout.md`

---

## 1. Why this exists

The ORB strategy (`02/strategies/idx-opening-range-breakout.md`) defines the *signal*
(breakout + force-close) but not the *bet size*. Without a risk engine the agent would
either over-bet (blow up) or under-bet (no edge captured). This module closes that gap.

## 2. Kelly sizing (fractional)

For a trade with win probability `p`, win multiple `b` (net odds = payoff/risk), the full
Kelly fraction is `f* = p - (1-p)/b`. We use **fractional Kelly** (`k` ∈ [0.25, 0.5],
default 0.5) to avoid the variance of full Kelly.

```
f_actionable = k * f*          # k = 0.5 default
position_idr = capital * f_actionable
```

Guardrails:
- `f*` clamped to `[0, 0.95]` before applying `k` (never bet >95% on one trade).
- If `f* <= 0` (negative edge), **no position** — agent stays flat.
- Long-only: `f*` never negative (no shorts; retail IDX constraint from ORB doc).

## 3. Drawdown cap

A hard portfolio-level stop so a losing streak can't compound:

```
if drawdown_since_peak >= DD_MAX:        # DD_MAX default 0.15 (15%)
    flatten_all()
    reduce_k_to(0.25)                    # de-risk until recovered
```

## 4. Reference implementation

```python
# 02-trading-bot/risk-management/kelly.py
from dataclasses import dataclass

@dataclass
class RiskConfig:
    capital_idr: float
    kelly_fraction: float = 0.5          # fractional Kelly
    dd_max: float = 0.15                 # max drawdown before flatten
    stop_loss_pct: float = 0.04          # per-trade hard stop (e.g. -4%)
    long_only: bool = True

def kelly_fraction(p: float, b: float) -> float:
    """Full Kelly f* = p - (1-p)/b. b = net odds (payoff/risk)."""
    if b <= 0 or p <= 0 or p >= 1:
        return 0.0
    f = p - (1 - p) / b
    return max(0.0, min(f, 0.95))        # clamp, long-only (no negative)

def size_position(p: float, b: float, cfg: RiskConfig) -> dict:
    f_star = kelly_fraction(p, b)
    f_action = cfg.kelly_fraction * f_star
    pos = cfg.capital_idr * f_action
    risk_amt = pos * cfg.stop_loss_pct
    return {
        "edge": f_star > 0,
        "kelly_full": round(f_star, 4),
        "kelly_used": round(f_action, 4),
        "position_idr": round(pos),
        "risk_per_trade_idr": round(risk_amt),
        "stop_loss_pct": cfg.stop_loss_pct,
        "long_only": cfg.long_only,
    }

def check_drawdown(peak: float, now: float, cfg: RiskConfig) -> dict:
    dd = (peak - now) / peak if peak > 0 else 0.0
    breach = dd >= cfg.dd_max
    return {"drawdown_pct": round(dd, 4), "breached": breach,
            "action": "FLATTEN+DERISK" if breach else "ok"}
```

## 5. Worked example (from the ORB doc's volatility note)

Market gaps +4% on a high-volatility day, `p=0.55`, `b=1.8` (payoff/risk from historical
ORB win/loss):
- `f* = 0.55 - 0.45/1.8 = 0.30`
- `f_action = 0.5 * 0.30 = 0.15`
- On Rp 10jt capital → **Rp 1.5jt position**, risk Rp 60k at −4% stop.

This is exactly the "size at 0.5× Kelly, stop at −4%" message the signal-agent sends.

## 6. New gaps

- `02/signals/news-sentiment-scoring.md` (sibling, see that file) feeds `p` here from
  social sentiment ($BBRI $TLKM $BTC cashtag monitoring per `01` playbook).
- No broker integration module yet (the ORB doc notes shorting is disabled); the agent
  emits *advice*, doesn't place orders.
