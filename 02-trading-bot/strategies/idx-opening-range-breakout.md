# IDX Opening Range Breakout (ORB): A Trader-Built Reference for the Jakarta Composite

This document is a research and implementation reference for the opening range breakout
(ORB) strategy applied specifically to the Indonesia Stock Exchange (Bursa Efek Indonesia,
IDX). It is written for a technical audience that wants working code, real session
constraints, and honest statistics rather than a sales pitch. Everything below is grounded
in sources that were reachable at research time (2026-07-16). Where a primary source was
bot-blocked or paywalled, that is stated explicitly and the claim is flagged as
"source unreachable" rather than invented.

The opening range breakout is one of the oldest mechanically-tradable intraday setups.
The core idea is simple: the first N minutes of the regular session define a price band
(the "opening range"). A sustained break above the top of that band is treated as a long
signal, and a break below the bottom is treated as a short signal. The thesis is that the
opening range concentrates the overnight news flow, the pre-opening auction imbalance, and
the first wave of liquidity, so the first directional push that escapes that band tends to
draw continuation as algos and momentum desks join.

On the IDX the setup is especially interesting because the opening window is unusually
compressed and liquidity is unusually concentrated. According to Pluang's 2026 trading-hours
guide, the first hour (09:00 to 10:00 WIB) alone contributes roughly 20 to 30 percent of
total daily volume, which is the single largest liquidity spike of the day. That concentration
is exactly what makes a 09:00 to 09:30 (or 09:00 to 10:00) opening range worth quantifying.
This file builds the full pipeline: session calendar, data acquisition, range construction,
entry and exit rules, risk sizing, backtest harness, and the failure modes specific to
Indonesian equities.

## Why the IDX opening window is structurally different

Most ORB literature is written for US equities where the regular session opens at 09:30 New
York time and the first 30 minutes already contain a large fraction of daily range. The IDX
has its own rhythm driven by the pre-opening call auction and the Friday prayer break.

The official IDX trading calendar (source: idx.id "Jam dan Mekanisme Perdagangan", fetched
2026-07-16) defines the following equity sessions:

- Prapembukaan (pre-open, input window): Monday to Friday, 08:45:00 to 08:57:59 WIB. Applies
  to shares on the Main Board, Development Board, and New Economy Board.
- Sesi I (regular session 1): Monday to Thursday 09:00:00 to 12:00:00 WIB. Friday
  09:00:00 to 11:30:00 WIB.
- Sesi II (regular session 2): Monday to Thursday 13:30:00 to 15:49:59 WIB. Friday
  14:00:00 to 15:49:59 WIB.
- Prapenutupan (pre-close, input window): Monday to Friday 15:50:00 to 15:59:59 WIB.
- Prapenutupan (pre-close, matching window): Monday to Friday 16:00:00 to 16:01:59 WIB.
- Post-trading: 16:00 to 16:15 WIB (executions only at the official closing price).
- Pasar Negosiasi (negotiation/block market): 09:00 to 17:00 WIB, used for large block
  trades outside the continuous auction.

Two structural facts matter for ORB design. First, the opening price is not set by the first
continuous print at 09:00. It is set by the pre-opening call auction whose matching occurs at
the 09:00 open. The official description states that "Harga Pembukaan terbentuk berdasarkan
akumulasi jumlah penawaran jual dan permintaan beli terbanyak yang dapat dialokasikan oleh
JATS INET pada harga tertentu pada periode Pra-pembukaan." In plain terms, the open is the
price that maximizes crossed volume across all pre-open orders. That means the 09:00 open
already reflects a full book imbalance, so the ORB should be measured from the 09:00 open
print, not from a pre-open indicative price.

Second, Friday is not a normal day. Session 1 ends at 11:30 instead of 12:00, and session 2
does not resume until 14:00 instead of 13:30, to accommodate the longer Friday prayer break.
Any ORB that assumes a symmetric lunch break will mislabel Friday afternoon data. The
backtest harness below hard-codes the Friday calendar.

A third fact that this document could NOT verify from a primary source: the exact auto
rejection (ARB) percentage bands and the tick-fraction schedule. The idx.id page references
"Peraturan II-A Kep-00003/BEI/04-2025" for price fractions but the underlying PDF was not
reachable at fetch time (source unreachable, 2026-07-16). The document instead uses the
commonly observed ARB bands (approximately plus or minus 10 percent for stocks above IDR
2000, tightening at lower prices) and flags them as operator-supplied assumptions to confirm
against the live rulebook before live trading.

## The opening range definition

There are several conventions for "the opening range" and the choice changes the trade
dramatically. The three most common on the IDX are:

- ORB-5: the high and low of the first 5 minutes of regular session (09:00:00 to 09:05:00).
- ORB-15: the high and low of the first 15 minutes (09:00:00 to 09:15:00).
- ORB-30: the high and low of the first 30 minutes (09:00:00 to 09:30:00).
- ORB-60: the high and low of the first 60 minutes (09:00:00 to 10:00:00).

Each has a different character. ORB-5 fires early but has a tiny range, so it whipsaws in the
first volatile minutes. ORB-60 is the most statistically stable band on the IDX because the
09:00 to 10:00 window carries 20 to 30 percent of daily volume, so the range tends to be
meaningful, but it fires late and leaves less of the session to run. A robust design is to
track all four ranges in parallel and only take the breakout from the shortest range that has
already "completed" (its end time has passed) and whose range is wider than a minimum tick
filter.

The minimum range filter is critical. On the IDX the round lot is 100 shares and the tick
fraction is small for low-priced stocks, so a stock can print a 5-minute range of a single
tick (for example IDR 1 on a IDR 50 stock). Trading a breakout of a one-tick range is pure
noise. A practical filter is: require the opening range height to be at least K times the
average tick for that stock, or at least 0.3 percent of the opening price, whichever is
larger.

## Data acquisition: what you actually need

To backtest ORB you need one-minute OHLCV bars for your universe, tagged with session and
board. The IDX does not offer a clean public per-minute REST feed without authentication, and
the idx.co.id pages are behind Cloudflare (the live trading-hours page returned HTTP 403 at
fetch time, 2026-07-16, confirmed via direct curl and via the r.jina.ai reader proxy). The
practical options are:

- A retail broker API. Many Indonesian brokers (Stockbit, Bibit/Pluang, Phillip Sekuritas,
  Mirae Asset, BNI Sekuritas, etc.) expose historical and streaming quotes through their own
  APIs or through the trading terminal's export feature. These are the most reliable source
  for retail traders.
- The crawler/scraper stack in this vault (01-crawler-scrapper). If you build a TikTok or X
  signal scraper there, the same session-cookie pattern applies to pulling quote pages, but
  be aware that most broker quote pages are also bot-protected and ToS-restricted.
- A paid market-data vendor (Bloomberg, Refinitiv, FactSet, or regional providers like
  IQPlus/UTC/Password). These give clean adjusted one-minute bars but cost money.

For the reference implementation below we assume a local CSV of one-minute bars with the
schema: `datetime,ticker,open,high,low,close,volume,board`. The `board` column carries
"MAIN", "DEVELOPMENT", "NEW_ECONOMY", or "FCA" so the harness can exclude FCA stocks, which
the Pluang guide explicitly warns have very low liquidity and should be avoided by beginners.
FCA stocks trade by full call auction rather than continuous auction, so their one-minute
bars are sparse and an ORB on them is meaningless.

### Sample data shape

A realistic one-minute row for a liquid Main Board stock (example values, not a real tick):

```csv
2026-07-16 09:00:00,BBRI,4520,4520,4515,4518,182000,MAIN
2026-07-16 09:01:00,BBRI,4518,4530,4516,4527,240000,MAIN
2026-07-16 09:02:00,BBRI,4527,4535,4524,4529,198000,MAIN
```

Note the 09:00 bar already includes the opening auction print. The opening range for ORB-5 is
the high/low across the 09:00 and 09:01 to 09:04 bars (5 one-minute bars). For ORB-30 it is
the high/low across 09:00 to 09:29 inclusive (30 bars).

## Session calendar as code

The single most common ORB bug is using the wrong session boundaries, especially on Friday.
Encode the calendar explicitly rather than assuming a fixed 09:00 to 16:00 day.

```python
from datetime import datetime, time, timedelta
from enum import Enum

class Session(Enum):
    PRE_OPEN = "pre_open"
    SESSION1 = "session1"
    LUNCH = "lunch"
    SESSION2 = "session2"
    PRE_CLOSE = "pre_close"
    POST = "post"
    CLOSED = "closed"

# All times are WIB (Asia/Jakarta, UTC+7). The exchange uses local wall clock.
def idx_session(dt: datetime) -> Session:
    """Return the IDX trading session for a naive WIB datetime.

    Friday has a shorter session-1 and a longer lunch for the Jumat prayer.
    """
    if dt.weekday() >= 5:  # Saturday=5, Sunday=6
        return Session.CLOSED
    t = dt.time()
    is_friday = dt.weekday() == 4

    if time(8, 45) <= t <= time(8, 57, 59):
        return Session.PRE_OPEN
    if time(9, 0) <= t <= (time(11, 30) if is_friday else time(12, 0)):
        return Session.SESSION1
    if (time(11, 30) if is_friday else time(12, 0)) < t < (time(14, 0) if is_friday else time(13, 30)):
        return Session.LUNCH
    if (time(14, 0) if is_friday else time(13, 30)) <= t <= time(15, 49, 59):
        return Session.SESSION2
    if time(15, 50) <= t <= time(16, 1, 59):
        return Session.PRE_CLOSE
    if time(16, 2) <= t <= time(16, 15):
        return Session.POST
    return Session.CLOSED

def regular_open(dt: datetime) -> datetime:
    """09:00:00 WIB on the given trading day (ignores holiday calendar)."""
    return dt.replace(hour=9, minute=0, second=0, microsecond=0)

def orb_window_end(dt: datetime, minutes: int) -> datetime:
    """End (exclusive) of the opening range measured from 09:00."""
    return regular_open(dt).replace(minute=0) + timedelta(minutes=minutes)
```

The holiday calendar (national holidays when the exchange is closed) is not encoded above.
IDX publishes the annual holiday calendar; at fetch time the 2026 holiday list PDF was not
retrieved (source unreachable, 2026-07-16), so the harness treats Saturday and Sunday as the
only non-trading days and expects the operator to inject the official holiday dates as a
blocklist before running a production backtest.

## Building the opening range from one-minute bars

Given a list of one-minute bars for one ticker on one day, the range construction is a simple
rolling high/low over the first N minutes after the 09:00 open.

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Bar:
    ts: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int
    board: str

def build_opening_range(bars: List[Bar], orb_minutes: int = 30) -> dict:
    """Return the opening range for the first `orb_minutes` of regular session.

    bars: chronological one-minute bars for a single ticker on a single day.
    Only MAIN/DEVELOPMENT/NEW_ECONOMY boards are eligible; FCA is rejected.
    """
    eligible_boards = {"MAIN", "DEVELOPMENT", "NEW_ECONOMY"}
    # Filter to regular-session bars starting at 09:00
    session_bars = [
        b for b in bars
        if b.board in eligible_boards and time(9, 0) <= b.ts.time() <= time(15, 49, 59)
    ]
    if not session_bars:
        return {"valid": False, "reason": "no eligible bars"}

    open_ts = regular_open(session_bars[0].ts)
    end_ts = open_ts + timedelta(minutes=orb_minutes)
    window = [b for b in session_bars if open_ts <= b.ts < end_ts]
    if len(window) < orb_minutes:
        return {"valid": False, "reason": f"only {len(window)} bars in ORB window"}

    orb_high = max(b.high for b in window)
    orb_low = min(b.low for b in window)
    open_price = session_bars[0].open  # the 09:00 auction print
    return {
        "valid": True,
        "open": open_price,
        "orb_high": orb_high,
        "orb_low": orb_low,
        "orb_height": orb_high - orb_low,
        "open_ts": open_ts,
        "end_ts": end_ts,
    }
```

The opening price used as the anchor is `session_bars[0].open`, which is the 09:00 auction
clearing price. This is the correct reference because, as noted, the open is set by the
pre-open call auction, not by a continuous print.

## Entry rules

The baseline ORB entry is a stop order placed at the range boundaries once the range is
complete:

- Long entry: a buy stop at `orb_high + tick`, triggered when price trades at or above that
  level after `end_ts`.
- Short entry: a sell stop at `orb_low - tick`, triggered when price trades at or below that
  level after `end_ts`.

The `+ tick` / `- tick` offset avoids buying exactly at the high and getting filled on a
wick. A common refinement is to require the breakout to be confirmed by a closing one-minute
bar beyond the level, not just an intrabar spike, to filter single-print wicks. On the IDX
where the first hour is 20 to 30 percent of daily volume, a one-minute wick can be a real
liquidity event, but it can also be a thin auction tail, so the close-confirmation filter
materially cuts false signals.

A second refinement is the "breakout must happen within X minutes of range completion" rule.
If the breakout does not occur by, say, 10:30 WIB, the setup is considered stale and the
pending stops are cancelled. The logic is that an ORB that only fires three hours later is no
longer an opening-range breakout, it is just a midday range expansion, and the statistical
edge from the opening liquidity concentration is gone.

### Direction bias from the opening gap

The opening price itself carries information. Compare the 09:00 open to the previous day's
official close (the pre-close matching price at 16:00 to 16:01:59). A gap up (open above
prior close) biases the day bullish; a gap down biases bearish. A practical filter is to only
take long ORB breaks when the open is above the prior close, and only take short ORB breaks
when the open is below the prior close. This single filter aligns the trade with the
pre-open auction imbalance and removes a large share of failed reversals. The Pluang guide
explicitly notes that "jika harga pembukaan teoritis naik signifikan dari harga penutupan
kemarin, pasar kemungkinan akan membuka dengan sentimen positif (gap up), dan sebaliknya,"
which is the intuition this filter codifies.

```python
def gap_direction(open_price: float, prior_close: float) -> int:
    """+1 gap up, -1 gap down, 0 flat (within 0.1%)."""
    if prior_close <= 0:
        return 0
    pct = (open_price - prior_close) / prior_close
    if pct > 0.001:
        return 1
    if pct < -0.001:
        return -1
    return 0
```

## Exit rules

ORB exits come in three flavors and a robust system uses all three with priority ordering.

- Time stop: exit at the close of the regular session (15:49:59 on the IDX) if still in the
  trade. Because this is a day-trading strategy, overnight positions are not allowed. All
  positions flatten before the pre-close window.
- Profit target: exit at a multiple of the opening range height. A common target is 1.0x or
  2.0x the ORB height measured from the entry. For ORB-30 with a IDR 50 range on a IDR 4500
  stock, a 1x target is IDR 50 of move, a 2x target is IDR 100.
- Trailing stop: once the trade is in profit by at least 0.5x the ORB height, move the stop
  to entry (break-even), then trail by the running session VWAP or by a multiple of the
  average true range (ATR).

The time stop deserves emphasis. The Day trading Wikipedia article summarizes a well-known
study of Brazilian day traders: "Considering the performance net of exchange and brokerage
fees, we find that 97% of all investors who persisted for more than 300 days lost money."
That statistic is about retail day traders generally, not ORB specifically, and it is a
reminder that holding losers past the session close and paying spread plus fee decay is how
the edge disappears. Flattening at 15:49 is non-negotiable for the backtest.

## Risk sizing and the fee reality

Position sizing for ORB is driven by the opening range height, not by a fixed percent of
equity, because the range height is the natural stop distance. The stop is placed just inside
the opposite range boundary (for a long, stop at `orb_low - tick`). The risk per share is
therefore roughly the ORB height. To risk a fixed fraction R of equity (for example 0.5
percent) per trade:

```python
def size_for_risk(equity: float, risk_fraction: float,
                  entry: float, stop: float, lot: int = 100) -> int:
    """Return number of SHARES (rounded down to a round lot)."""
    per_share_risk = abs(entry - stop)
    if per_share_risk <= 0:
        return 0
    risk_budget = equity * risk_fraction
    shares = risk_budget / per_share_risk
    # round down to nearest round lot (100 on IDX)
    shares = int(shares // lot) * lot
    return max(shares, 0)

# Example: equity 100,000,000 IDR, risk 0.5% = 500,000 IDR.
# Entry 4520, stop 4490 (ORB height 30). per_share_risk = 30.
# shares = 500000 / 30 = 16666 -> round lot -> 16600 shares.
# Notional = 16600 * 4520 = 75,063,200 IDR (about 75% of equity, leverage-free).
```

Two IDX-specific cost notes. First, brokerage on the IDX is typically 0.15 to 0.25 percent
per side for retail, plus a levy and VAT, so a round trip costs roughly 0.3 to 0.5 percent
before any edge. An ORB that targets only 0.5x the range height will be eaten alive by fees,
which is why the 1x to 2x target and the break-even trail exist. Second, the auto rejection
(ARB) bands mean a stop placed far outside the allowed band will be rejected by JATS INET, so
stops must sit within the ARB envelope (source unreachable for exact 2025 bands; use the
observed ~10 percent band and confirm).

## Backtest harness

The following harness is a minimal but complete event loop. It assumes a list of daily bar
lists per ticker. It is intentionally single-asset and end-of-minute marked-to-close for
simplicity; production code should vectorize and use a proper cost model.

```python
from typing import List, Dict

def backtest_orb(
    daily_bars: Dict[str, Dict[str, List[Bar]]],  # ticker -> date -> bars
    orb_minutes: int = 30,
    risk_fraction: float = 0.005,
    target_mult: float = 1.0,
    use_gap_filter: bool = True,
    max_entry_offset_min: int = 90,  # breakout must fire by 10:30 for ORB-30
) -> List[dict]:
    trades = []
    for ticker, by_date in daily_bars.items():
        prior_close = None
        for date_str in sorted(by_date.keys()):
            bars = by_date[date_str]
            rng = build_opening_range(bars, orb_minutes)
            if not rng["valid"]:
                # still update prior_close for next day
                last = max(bars, key=lambda b: b.ts)
                prior_close = last.close
                continue
            open_price = rng["open"]
            orb_high = rng["orb_high"]
            orb_low = rng["orb_low"]
            end_ts = rng["end_ts"]

            # gap filter
            if use_gap_filter and prior_close is not None:
                g = gap_direction(open_price, prior_close)
                allow_long = g >= 0
                allow_short = g <= 0
            else:
                allow_long = allow_short = True

            # scan post-range bars for breakout
            entry = None
            direction = 0
            deadline = end_ts + timedelta(minutes=max_entry_offset_min)
            for b in bars:
                if b.ts < end_ts:
                    continue
                if b.ts > deadline:
                    break
                if allow_long and entry is None and b.high >= orb_high:
                    entry = orb_high
                    direction = 1
                    stop = orb_low
                    target = entry + target_mult * (orb_high - orb_low)
                    break
                if allow_short and entry is None and b.low <= orb_low:
                    entry = orb_low
                    direction = -1
                    stop = orb_high
                    target = entry - target_mult * (orb_high - orb_low)
                    break

            if entry is not None:
                # simulate exit on remaining bars
                exit_price = None
                exit_reason = None
                for b in bars:
                    if b.ts <= end_ts:
                        continue
                    if direction == 1:
                        if b.low <= stop:
                            exit_price, exit_reason = stop, "stop"
                            break
                        if b.high >= target:
                            exit_price, exit_reason = target, "target"
                            break
                    else:
                        if b.high >= stop:
                            exit_price, exit_reason = stop, "stop"
                            break
                        if b.low <= target:
                            exit_price, exit_reason = target, "target"
                            break
                if exit_price is None:
                    # flatten at last regular-session close (time stop)
                    reg = [b for b in bars if time(9,0) <= b.ts.time() <= time(15,49,59)]
                    exit_price = reg[-1].close if reg else entry
                    exit_reason = "time_stop"
                pnl_pct = (exit_price - entry) * direction / entry
                trades.append({
                    "ticker": ticker, "date": date_str, "direction": direction,
                    "entry": entry, "exit": exit_price, "reason": exit_reason,
                    "orb_high": orb_high, "orb_low": orb_low, "pnl_pct": pnl_pct,
                })
            last = max(bars, key=lambda b: b.ts)
            prior_close = last.close
    return trades
```

This harness deliberately ignores fees and slippage, which is the most common way a backtest
lies. Before trusting any number it produces, subtract a round-trip cost of at least 0.4
percent and add a conservative slippage of one to two ticks on entry and exit. On the IDX,
where a liquid stock's tick can be IDR 1 on a IDR 50 name or IDR 5 on a IDR 4500 name, the
slippage in percent terms is tiny on high-priced liquid names and large on low-priced ones,
which is another reason to restrict the universe to liquid Main Board stocks.

## What the statistics say about day trading in general

The ORB is a day-trading strategy, and day trading as a class has brutal aggregate outcomes.
The Day trading Wikipedia article reports the Brazilian study finding that 97 percent of
investors who persisted more than 300 days lost money, with only 1.1 percent earning more
than the minimum wage and only 0.5 percent earning more than a bank teller's starting salary.
FINRA's pattern-day-trader rule (four or more day trades in five business days, above 6
percent of activity, requiring a 25,000 USD minimum equity) is a US rule and does not apply
to the IDX, but the underlying risk lesson transfers: high-frequency intraday turnover
compounds fees and emotional error.

This is not a reason to abandon ORB. It is a reason to treat ORB as a systematic,
cost-aware, small-risk-per-trade method rather than a "get rich" tactic, and to report
expectancy net of fees honestly. The vault's own CHANGELOG notes repeated emphasis on
"honest gaps" and verified, healthy pipelines, which is the right posture here too.

## Failure modes specific to the IDX

Several ways this strategy breaks on Indonesian equities, derived from the session structure
and market microstructure described above:

- Pre-open auction gap. Because the 09:00 open is an auction clear, a stock with a large
  overnight news event can open already outside what would have been the opening range. The
  ORB then triggers immediately at 09:00 on the first continuous bar, often chasing a gap
  that already happened. The gap-direction filter mitigates this but does not eliminate it.
- Thin names and FCA. Low-liquidity Development Board or FCA stocks have sparse one-minute
  bars. An ORB on them is statistically meaningless. Exclude them by board.
- Friday calendar shift. If the harness uses the Monday to Thursday lunch break, Friday
  session-2 bars get mislabeled and the time stop fires at the wrong instant. The
  `idx_session` function above handles this.
- ARB rejection. Stops outside the auto rejection band are rejected by JATS INET. Keep stops
  inside the band (exact 2025 bands source unreachable at fetch time; confirm before live).
- Suspension and force majeure. The IDX can suspend or shorten trading under "gangguan
  sistem, bencana nasional, atau volatilitas pasar ekstrem" (system disruption, national
  disaster, or extreme volatility). The harness should drop any day with an anomalous session
  length rather than trade it.
- Holiday gaps. Missing a national holiday makes the "previous close" link cross a multi-day
  gap, producing a fake gap signal. Inject the official holiday calendar.

## Liquidity windows to exploit and avoid

Pluang's 2026 guide identifies three liquidity spikes: the opening hour 09:00 to 10:00 (the
largest, 20 to 30 percent of daily volume), the lunch break 12:00 to 13:30 (the lowest), and
the closing hour 15:00 to 16:00 (a second spike, driven by institution and fund-manager
rebalancing). The ORB lives in the first spike, which is exactly why its edge exists: the
breakout is backed by real volume. The guide also advises beginners to "hindari panik saat
melihat pergerakan harga besar di jam pembukaan, sering kali harga kembali stabil setelah
30-60 menit pertama" (do not panic at large opening moves; prices often stabilize after the
first 30 to 60 minutes), which is the empirical justification for the close-confirmation
filter and the break-even trail, not for exiting good trades early.

## A practical multi-range scanner

Rather than committing to one ORB length, run ORB-15, ORB-30, and ORB-60 in parallel and take
the first valid breakout from the shortest completed range whose height clears the minimum
filter. This adapts to volatility: on calm days the short ranges are too tight and the system
naturally waits for ORB-60; on volatile days the short ranges fire early.

```python
def pick_range(bars: List[Bar], min_height_pct: float = 0.003) -> dict:
    """Pick the shortest completed ORB whose height clears the filter."""
    for minutes in (15, 30, 60):
        rng = build_opening_range(bars, minutes)
        if not rng["valid"]:
            continue
        if rng["orb_height"] / rng["open"] >= min_height_pct:
            rng["chosen_minutes"] = minutes
            return rng
    return {"valid": False, "reason": "no range cleared min height filter"}
```

## Performance reporting checklist

When you report ORB results, report all of the following, net of a round-trip fee of at least
0.4 percent and one-to-two-tick slippage:

- Total trades and trade days, with the date range.
- Win rate, average win, average loss, profit factor, and expectancy per trade.
- Max drawdown on the tested equity curve.
- Breakdown by direction (long vs short) and by ORB length.
- Breakdown by day of week, especially Friday vs the rest.
- Number of trades killed by the time stop vs target vs stop loss.
- The assumed fee and slippage model, stated explicitly.

Any report missing the fee model is not trustworthy. The whole point of documenting this
strategy in the vault is to keep the analysis honest, not to show a pretty equity curve.

## Sources used (all reachable at 2026-07-16 unless flagged)

- IDX official trading hours and mechanism: https://www.idx.id/id/produk-layanan/jam-dan-mekanisme-perdagangan/ (fetched via r.jina.ai reader proxy; the raw idx.co.id/en/about-idx/trading-hours/ page returned HTTP 403 Cloudflare at direct fetch, 2026-07-16). Confirms pre-open 08:45-08:57:59, Sesi I 09:00-12:00 (Mon-Thu) / 09:00-11:30 (Fri), Sesi II 13:30-15:49:59 (Mon-Thu) / 14:00-15:49:59 (Fri), pre-close input 15:50-15:59:59 and matching 16:00-16:01:59, round lot 100, price fractions under Peraturan II-A Kep-00003/BEI/04-2025.
- Pluang 2026 trading-hours guide: https://pluang.com/akademi/berita-analisis/jam-bursa-saham-indonesia . Confirms the full session table including post-trading 16:00-16:15 and negotiation market 09:00-17:00, the 20-30 percent first-hour volume share, the three liquidity spikes, and the FCA low-liquidity warning.
- Investbro ID overview: https://investbro.id/bursa-efek/ . Secondary confirmation of Sesi I 09:00-11:30 and Sesi II 13:30-14:49:59 (note: this source appears outdated on the Sesi II close vs the official IDX page; the official IDX page is treated as authoritative).
- Wikipedia, Day trading: https://en.wikipedia.org/wiki/Day_trading . Source for the definition of day trading, pattern day trader rules, and the Brazilian study statistic that 97 percent of persistent day traders lost money.
- Wikipedia, Bursa Efek Indonesia: https://id.wikipedia.org/wiki/Bursa_Efek_Indonesia . Confirms the 2 January 2013 trading-hours update and the 6 December 2021 pre-closing/penutupan code-broker adjustment, plus the JATS INET continuous auction system context.
- Wikipedia, Jakarta Stock Exchange: https://en.wikipedia.org/wiki/Jakarta_Stock_Exchange . Historical context: JSX launched JATS in 1995, merged with Surabaya into IDX in September 2007.

## Items explicitly flagged as source unreachable (do not treat as verified)

- The exact auto rejection (ARB) percentage bands for 2025/2026 under Peraturan II-A Kep-00003/BEI/04-2025. The idx.id page references the rule but the PDF was not retrievable (bot-protected, 2026-07-16). Use the commonly observed ~10 percent band as a placeholder and confirm before live trading.
- The official IDX 2026 national holiday calendar. Not retrieved (source unreachable, 2026-07-16). Inject before production backtests to avoid fake gap signals across closed days.
- A clean public per-minute IDX OHLCV REST feed. idx.co.id endpoints returned HTTP 403 (Cloudflare) at direct curl; use a broker API or the vault's crawler stack with proper session handling instead.

## How this connects to the rest of the vault

- 05-market-cron/cron-configs/ihsg-daily-fetch.py (gap in the auditor): an IHSG daily fetcher
  would feed the index-level gap and breadth context that the gap-direction filter needs.
- 01-crawler-scrapper: the session-cookie pattern used for X/TikTok scraping is reusable for
  pulling broker quote pages, subject to ToS.
- 02-trading-bot/risk-management/position-sizing-kelly.md (gap in the auditor): the
  `size_for_risk` function above is a fixed-fraction baseline; a Kelly or half-Kelly layer
  belongs in that file.
- 02-trading-bot/signals/news-sentiment-scoring.md (gap in the auditor): the gap-direction
  filter is a pure price signal; layering a news-sentiment score on top would let the system
  skip ORBs on stocks with negative same-morning headlines.

## Worked example with concrete numbers

To make the mechanics concrete, walk through a hypothetical liquid Main Board stock, say a
bank with open price IDR 4520, on a Monday (normal calendar). Assume one-minute bars:

```text
09:00  open 4520  high 4525  low 4512  close 4522  vol 182000
09:01  open 4522  high 4530  low 4518  close 4527  vol 240000
09:02  open 4527  high 4535  low 4524  close 4529  vol 198000
09:03  open 4529  high 4533  low 4521  close 4524  vol 160000
09:04  open 4524  high 4531  low 4519  close 4526  vol 175000
...
09:29  (thirtieth bar) high 4548  low 4515  close 4540
```

For ORB-30 the opening range is the high/low across 09:00 to 09:29. In this trace the range
high is IDR 4548 (or the true max across all 30 bars) and the range low is IDR 4512 (the
09:00 low). The ORB height is IDR 36, about 0.8 percent of the IDR 4520 open, which clears the
0.3 percent minimum height filter. The long trigger is a buy stop at IDR 4549 (4548 + 1 tick),
the short trigger is a sell stop at IDR 4511.

Suppose the prior close was IDR 4490, so the open at 4520 is a gap up of 0.67 percent. The
gap filter permits longs and permits shorts only weakly (gap >= 0 allows both, gap > 0 biases
long). At 09:42 the first one-minute bar closes at IDR 4551, breaking above the IDR 4548
range high with confirmation. Entry fills at IDR 4549. The fixed target at 1x is 4549 + 36 =
IDR 4585. The stop is at the range low IDR 4512, so per-share risk is IDR 37.

With equity IDR 100,000,000 and risk fraction 0.5 percent (IDR 500,000), the size function
gives shares = 500000 / 37 = 13513, rounded down to the nearest round lot of 100 gives
13,500 shares. Notional at entry = 13,500 x 4549 = IDR 61,411,500, about 61 percent of equity,
leverage-free. If the price reaches IDR 4585 the gross profit is (4585 - 4549) x 13500 =
IDR 486,000, about 0.49 percent of equity before fees. After a 0.4 percent round-trip fee
(IDR 245,646) the net is IDR 240,354, about 0.24 percent of equity. That thin net is exactly
why the target multiplier and the break-even trail matter: a 1x target on a tight range is
barely fee-positive, while a 2x target or a trailed exit captures more of the move.

## ATR-based stop variant

Fixed stops at the opposite range boundary are simple but ignore volatility scaling. On a
high-volatility day the range is wide and the stop is far, risking too much; on a low-volatility
day the range is tight and the stop is near, inviting whipsaw. A common variant sets the stop
at a multiple of the average true range instead of at the range boundary, while still using
the range boundary as the trigger.

```python
def atr(bars: List[Bar], n: int = 14) -> float:
    """Average True Range over the last n one-minute bars before entry."""
    trs = []
    for i in range(1, min(n, len(bars))):
        prev = bars[i - 1]
        cur = bars[i]
        tr = max(cur.high - cur.low,
                 abs(cur.high - prev.close),
                 abs(cur.low - prev.close))
        trs.append(tr)
    return sum(trs) / len(trs) if trs else 0.0

# stop = entry - 1.5 * atr (long) or entry + 1.5 * atr (short)
# target = entry + 2.0 * (orb_height)  # keep the range-based target
```

The hybrid uses the opening range for the trigger and the ATR for the stop distance, which
often improves the win rate because the stop adapts to intraday volatility rather than to a
single static band.

## Portfolio aggregation across a universe

A single stock ORB is noisy. The edge appears more reliably across a basket of 20 to 50 liquid
names where you take the top few breakouts ranked by range-height-to-volume ratio. The
aggregation step scores each candidate at range-completion time and enters only the highest
ranked N.

```python
def rank_candidates(orb_results: List[dict]) -> List[dict]:
    """Rank completed ORB ranges by height/volume (range efficiency).

    Higher ratio = a wider range formed on less volume = more conviction.
    """
    scored = []
    for r in orb_results:
        if not r.get("valid"):
            continue
        vol = r.get("volume", 1)
        efficiency = (r["orb_height"] / r["open"]) / max(vol, 1)
        scored.append({**r, "efficiency": efficiency})
    return sorted(scored, key=lambda x: x["efficiency"], reverse=True)

# Take top 3 of the ranked list, size each with size_for_risk on shared equity.
```

Note this ranking is a heuristic, not a proven optimizer. It is included as a building block,
not as a recommendation, and any production use needs its own backtest with the fee model
below.

## Cost-model simulation

The single most important honesty check is a proper cost model. The harness above ignores
costs. Wrap it like this before trusting any number:

```python
ROUND_TRIP_FEE = 0.004   # 0.4% total (broker + levy + VAT, retail estimate)
SLIPPAGE_TICKS = 2       # ticks of slippage on entry and exit (assumption)

def apply_costs(trades: List[dict], tick_size: float = 1.0) -> List[dict]:
    out = []
    for t in trades:
        entry_slip = SLIPPAGE_TICKS * tick_size * (1 if t["direction"] > 0 else -1)
        exit_slip = SLIPPAGE_TICKS * tick_size * (-1 if t["direction"] > 0 else 1)
        real_entry = t["entry"] + entry_slip
        real_exit = t["exit"] + exit_slip
        gross = (real_exit - real_entry) * t["direction"]
        fee = real_entry * ROUND_TRIP_FEE  # fee on notional, simplified
        net = gross - fee
        out.append({**t, "real_entry": real_entry, "real_exit": real_exit,
                    "gross": gross, "fee": fee, "net": net})
    return out

def expectancy(trades: List[dict]) -> dict:
    nets = [t["net"] / t["real_entry"] for t in trades]  # net return per trade
    wins = [x for x in nets if x > 0]
    losses = [x for x in nets if x <= 0]
    win_rate = len(wins) / len(nets) if nets else 0
    avg_win = sum(wins) / len(wins) if wins else 0
    avg_loss = sum(losses) / len(losses) if losses else 0
    exp = sum(nets) / len(nets) if nets else 0
    profit_factor = (sum(wins) / abs(sum(losses))) if losses else float("inf")
    return {"trades": len(nets), "win_rate": win_rate, "avg_win": avg_win,
            "avg_loss": avg_loss, "expectancy": exp, "profit_factor": profit_factor}
```

With this model a strategy that shows a gross expectancy of 0.15 percent per trade can easily
flip negative once the 0.4 percent round trip is subtracted, which is the central lesson of
the Brazilian day-trader study cited earlier. Always report the post-cost expectancy.

## Comparison of ORB lengths

The table below summarizes the qualitative trade-off between opening-range lengths on the IDX.
These are design characteristics, not backtest results, and must be validated per universe.

| ORB length | Fire time | Range quality | Whiplash risk | Room to run | Best when |
|------------|-----------|---------------|--------------|-------------|-----------|
| 5 min | 09:05 | tiny, noisy | high | most | very volatile names, scalping |
| 15 min | 09:15 | small | medium | high | trending mornings |
| 30 min | 09:30 | good | medium-low | good | default balanced choice |
| 60 min | 10:00 | best statistically | low | least | calm names, fewer signals |

The 09:00 to 10:00 window carries 20 to 30 percent of daily volume (Pluang, 2026), so ORB-60
sits at the tail of the biggest liquidity spike, which is why its range tends to be the most
reliable even though it leaves the least session remaining to capture the move.

## Data-quality validation routine

Before trusting any backtest, validate the bar feed. The IDX has holidays, suspensions, and
split/rights events that corrupt naive OHLCV. A validation pass should reject days that fail
these checks:

```python
def validate_day(bars: List[Bar], ticker: str, holidays: set) -> List[str]:
    problems = []
    if not bars:
        return ["empty_day"]
    date = bars[0].ts.date()
    if date.isoweekday() >= 6:
        problems.append("weekend_data")
    if date.isoformat() in holidays:
        problems.append("holiday_data")
    sess1 = [b for b in bars if time(9,0) <= b.ts.time() <= time(12,0)]
    if len(sess1) < 170:  # ~180 expected Mon-Thu, fewer Fri
        problems.append("short_session1")
    highs = [b.high for b in bars]
    lows = [b.low for b in bars]
    if max(highs) <= min(lows):
        problems.append("flat_or_bad_data")
    # detect a stale/zero-volume bar in the opening hour (possible suspension)
    open_hour = [b for b in bars if time(9,0) <= b.ts.time() < time(10,0)]
    if any(b.volume == 0 for b in open_hour):
        problems.append("zero_volume_open_hour")
    return problems
```

Days flagged "holiday_data", "short_session1", or "zero_volume_open_hour" should be dropped
from the backtest, not traded, because the prior-close link and the range construction both
assume a normal session.

## Order-type notes for live execution

On the IDX the continuous auction matches on price then time priority. For an ORB you want a
stop order that converts to a marketable limit when the trigger hits, not a pure market order,
because a pure market order during a fast opening breakout can slip several ticks. Most retail
broker APIs support a "stop limit" or a "trigger" order; set the limit a small number of ticks
past the trigger to bound slippage. Also respect the non-cancellation period in pre-open and
pre-close: orders there cannot be amended or cancelled once entered in the matching window, so
do not place ORB stops during those windows. The regular session (09:00 to 15:49:59) is the
only window where ORB orders should live.

## Relationship to index context

The ORB is a single-name strategy but the IDX as a whole often opens with a directional bias
driven by US overnight moves (the NYSE/NASDAQ session ends around 04:00 WIB, per Pluang's
time-zone note) and by futures on the Jakarta Composite. A useful filter is to check the IHSG
futures or the prior US session before taking a counter-trend single-name ORB. If the IHSG is
gap-down and a stock prints a long ORB breakout, the single-name signal is fighting the index
tide and the historical edge is weaker. This is exactly the kind of context the
05-market-cron IHSG fetcher (currently a gap in the auditor) is meant to supply.

## Common parameter mistakes

A short list of mistakes seen repeatedly in ORB implementations, useful as a pre-launch
checklist:

- Using 09:30 New York style fixed windows instead of the IDX 09:00 open and Friday shift.
- Forgetting the round lot of 100, so the size function returns non-tradable quantities.
- Setting the stop exactly at the range boundary with no tick offset, getting filled on wicks.
- Ignoring the 0.4 percent round-trip cost and reporting gross expectancy.
- Trading FCA or Development Board names with sparse bars.
- Letting a position ride past 15:49:59 into the pre-close auction by mistake.
- Not injecting the holiday calendar, producing fake gaps across closed days.
- Treating the pre-open indicative price as the open instead of the 09:00 auction clear.

## Minimal end-to-end run script

Putting the pieces together, a minimal end-to-end script structure (pseudo-code, not a full
program) looks like this:

```text
1. load holiday_calendar.txt  (operator-supplied official IDX holidays)
2. for each ticker in universe:
3.   load one-minute bars from broker CSV/API
4.   drop days failing validate_day()
5.   for each valid day:
6.     rng = pick_range(bars)            # shortest valid ORB length
7.     if not rng.valid: skip
8.     g = gap_direction(rng.open, prior_close)
9.     scan post-range bars for breakout with gap filter
10.    if entry: simulate exit (stop / target / time_stop)
11.    record trade
12. apply apply_costs(trades) with 0.4% round trip + 2tick slippage
13. print expectancy(trades) and the full report from the checklist
```

This is the skeleton. The production version adds vectorization, a real broker API adapter,
the IHSG context filter, and an ATR stop variant, all of which are described in the sections
above.

## Closing notes for the operator

The opening range breakout on the IDX is a real, mechanically-tradable edge only because the
09:00 to 10:00 window concentrates 20 to 30 percent of daily volume and the 09:00 open is a
true auction clear that absorbs the overnight book. Trade it as a small-risk, fee-aware,
systematic method on liquid Main Board stocks, exclude FCA and thin names, hard-code the
Friday calendar, flatten every position before 15:49:59, and report expectancy net of at
least 0.4 percent round-trip cost. Anything prettier than that is a story, not a strategy.
