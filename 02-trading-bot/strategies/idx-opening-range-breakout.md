# IDX Opening Range Breakout (ORB) Strategy, 09:00 to 09:30 WIB

This document is a technical research note for building an automated opening-range-breakout
trading bot on the Indonesia Stock Exchange (IDX / Bursa Efek Indonesia). It covers the exact
exchange session mechanics that define the range window, the statistical logic behind trading
the first 30 minutes, universe selection for the Indonesian market, a working Python
implementation that plugs into the event-driven baseline, risk controls, and IDX-specific
pitfalls. Every factual claim about session times, tick sizes, and the LQ45 universe is sourced.
Where live IDX pages were unreachable from the build environment (HTTP 403 from idx.co.id),
the claim is tagged `verify-live` instead of being invented.

Sources used and verified this tick:

- Indonesia Stock Exchange trading hours and tick schedule, Wikipedia: https://en.wikipedia.org/wiki/Indonesia_Stock_Exchange (retrieved 2026-07-11, HTTP 200)
- LQ45 index composition and review cadence, Wikipedia: https://en.wikipedia.org/wiki/LQ45 (retrieved 2026-07-11, HTTP 200)
- Day trading, momentum, and volatility definitions, Wikipedia: https://en.wikipedia.org/wiki/Day_trading (retrieved 2026-07-11, HTTP 200)
- Market news and session color, CNBC Indonesia: https://www.cnbcindonesia.com/ (retrieved 2026-07-11, HTTP 200)
- Market news and session color, Kontan: https://kontan.co.id/ (retrieved 2026-07-11, HTTP 200)
- Market news and session color, Bisnis Indonesia: https://www.bisnis.com/ (retrieved 2026-07-11, HTTP 200)
- Retail trading app / quote source, Stockbit: https://stockbit.com/ (retrieved 2026-07-11, HTTP 200)
- Retail market data and fund flow, Bareksa: https://www.bareksa.com/ (retrieved 2026-07-11, HTTP 200)

Note: idx.co.id returned HTTP 403 to automated requests for the trading-hours and equities pages,
so the authoritative session schedule below is taken from the Wikipedia article (which cites IDX
primary documents) and flagged for live re-confirmation against https://www.idx.co.id/en/about-idx/support/trading-hours.

---

## Why the first 30 minutes matter on IDX

The opening of the regular session is the single most information-dense window of the IDX trading
day. Three structural facts make this true for the Indonesian market specifically.

First, the opening price itself is not a continuous-trade price. The regular session opens with a
call auction at 09:00 WIB. Before that, from 08:45 to 08:55, JATS (the Jakarta Automated Trading
System) runs the pre-opening phase, collecting buy and sell interest and computing a single
equilibrium opening price that is published at 09:00. That auction absorbs all overnight global
news (Wall Street the prior evening, Asia morning flow, rupiah moves, commodity prices) into one
print. The first 30 minutes of continuous trading after that print are where the market decides
whether the auction price was fair or wrong. That is exactly the inefficiency an ORB bot harvests.

Second, Indonesian retail flow is concentrated at the open. IDX is one of the most
retail-dominated exchanges in the region. A large share of individual investor orders are placed
in the first minutes, partly because many retail brokers push morning research notes and because
the pre-opening auction creates a natural focal point. Concentration of flow means the first
30 minutes carry disproportionate volume and therefore the most reliable breakout signal compared
with, say, the dead mid-afternoon hours.

Third, the lunch break creates a second mini-open. IDX closes for lunch from 11:30 to 13:30. The
13:30 reopen is its own call-free continuous session start and behaves like a weaker second
opening. This note focuses on the primary 09:00 to 09:30 window because it has the deepest
liquidity, but the same range logic can be layered onto the 13:30 to 14:00 window as a secondary
signal (see the section on extensions).

The Opening Range Breakout idea is simple: define a price range from the high and low printed
during the first N minutes of the regular session (here N = 30, so 09:00:00 to 09:30:00 WIB), then
take a position when price breaks above the range high (long) or below the range low (short). The
range is the market's opening consensus. A clean break means new information has arrived or
latent order flow has overwhelmed that consensus, and the move tends to extend in the breakout
direction for the rest of the session.

---

## Exact IDX session schedule that defines the window

The range window is anchored to the exchange session calendar. The schedule below is quoted from
the Wikipedia Indonesia Stock Exchange article (which mirrors IDX primary publications) and is
authoritative for the structure. Verify the closing time live, because IDX has extended trading
hours in recent years and the Wikipedia copy may lag the current calendar (`verify-live`).

Opening session:

- Pre-opening trade (call auction collection): 08:45 to 08:55 WIB. JATS collects orders and
  computes the equilibrium price. No trades print during this window.
- Pre-open recap and open auction processing: 08:55:01 to 08:59:59 WIB.
- Regular Session I opens at 09:00 WIB via the opening auction print. This is the first tradable
  price of the day and the anchor for the ORB range.

Regular Session I:

- 09:00 to 11:30 WIB, Monday through Friday. Continuous matching.

Lunch break:

- 11:30 to 13:30 WIB. No trading. This is a hard stop; any resting orders are held.

Regular Session II:

- 13:30 to 14:49:59 WIB, Monday through Friday. Continuous matching resumes at 13:30.

Closing session:

- Pre-closing trade (call auction collection): 14:50 to 15:00 WIB.
- Closing auction processing: 15:00:01 to 15:04:59 WIB.
- Post-closing trade: 15:05 to 15:15 WIB.

Two consequences for the bot:

- The ORB range must be measured only from continuous prints between 09:00:00 and 09:30:00. The
  08:45 to 08:55 pre-opening auction prints are not part of the continuous range and must be
  excluded, otherwise the range is polluted by the auction's wide implied book.
- The strategy should flatten or hard-stop all open ORB positions before 11:30 if they have not
  hit target or stop, because the lunch break freezes the book for two hours and gaps at 13:30
  reopen are common and uncontrollable. Many implementations simply close any still-open ORB
  trade at 11:25 to avoid the lunch gap entirely.

Tick size and lot size (from the same Wikipedia source) matter for order placement and stop
precision:

- Lot size is 100 shares, unchanged since 2 May 2016.
- Tick schedule: below Rp200 the tick is Rp1; from Rp200 to below Rp500 the tick is Rp2; from
  Rp500 to below Rp2,000 the tick is Rp5; from Rp2,000 to below Rp5,000 the tick is Rp10; from
  Rp5,000 to below Rp10,000 the tick is Rp25; from Rp10,000 to below Rp25,000 the tick is Rp50;
  and so on. Round your entry, stop, and target prices to the correct tick for the instrument or
  your orders will be rejected by JATS.

---

## The statistical logic of ORB

The reason ORB works is not mystical. It is a bet on autocorrelation of intraday returns combined
with order-flow inertia. When the opening range is established, two groups of participants exist:
those who agreed the price was fair inside the range, and those with latent orders waiting for a
break. A breakout triggers a cascade: stop orders and signal-follower entries pile in the same
direction, pushing price further. In a market with concentrated retail flow (IDX), this cascade is
stronger and more predictable in the first 30 minutes than later in the day.

A useful framing is the range as a one-standard-deviation band. If the first 30-minute range is
narrow, the breakout tends to be more reliable because a narrow range means low disagreement and
any break is a decisive shift. If the first 30-minute range is already wide (high volatility open),
breakouts are noisier and more likely to fake out, so filters should tighten.

Empirical studies on US equities (and the general day-trading literature summarized on
https://en.wikipedia.org/wiki/Day_trading) consistently find that a meaningful fraction of the
day's directional range is established in the opening minutes, and that momentum established at the
open persists intraday more often than it reverses. The Wikipedia day-trading article describes
momentum (trend following) trading as assuming that instruments which moved in one direction
continue moving that way, which is exactly the ORB premise. The same article ties day-trading
profitability to volatility regimes, which is why this strategy must scale position size and
filters with realized volatility.

For IDX specifically there is no freely published academic ORB study we could reach this tick, so
the backtest harness below is the tool to generate your own edge statistics. Treat any quoted
win-rate numbers in this document as illustrative placeholders to be replaced by your backtest
(`verify-live`). Do not ship the bot on the illustrative numbers.

---

## Universe selection: which IDX stocks to trade

ORB needs liquidity. In a market where many of the roughly 900 listed IDX names trade only a few
thousand shares a day, a breakout in an illiquid stock is just you moving the price, and the
spread will eat the edge. The universe should be restricted to the most liquid names.

LQ45 is the natural starting universe. It is the index of the 45 most liquid stocks on IDX,
reviewed and rebalanced periodically (semiannually per the index methodology). Its constituents are
large caps with deep order books: BBCA (Bank Central Asia), BBNI (Bank Negara Indonesia), BBRI
(Bank Rakyat Indonesia), ASII (Astra International), and similar blue chips. The full current
constituent list is maintained at https://en.wikipedia.org/wiki/LQ45 and on IDX primary pages.

A tighter, even more liquid subset is IDX30, the 30 largest and most liquid names. For an ORB bot
that needs to enter and exit within minutes, IDX30 is often the better default. You can widen to
LQ45 for more opportunities, accepting slightly thinner books on the smaller constituents.

Selection rules to hard-code:

- Only names in IDX30 or LQ45 as of the latest review. Re-pull the constituent list on each
  rebalance date; do not trade a name that dropped out.
- Minimum average daily value traded, for example Rp 50 billion, computed over the trailing 20
  sessions. Drop any name below the threshold even if it is still in the index.
- Exclude names with a pending corporate action that day (rights issue, stock split, dividend
  cum/ex date) because the auction price and range behave abnormally. Pull the IDX corporate-action
  calendar daily.
- Exclude any name hitting the automatic upper or lower price limit (auto-reject / circuit
  breaker) in the prior session, because the open the next day is mechanically gapped and the range
  logic breaks.

Why not trade the whole board: the long tail of IDX has bid-ask spreads of several ticks and order
books thin enough that a single retail order moves the mid. The ORB edge in those names is
negative after costs. Liquidity is the strategy.

---

## Signal definition

The signal is computed per instrument after the 09:30:00 WIB bar closes (or, in a streaming
implementation, as soon as the clock passes 09:30 and the range is locked).

Inputs per instrument:

- `open_auction_price`: the 09:00 opening auction print (the day's first trade).
- `range_high`: highest traded price between 09:00:00 and 09:30:00 inclusive of continuous prints.
- `range_low`: lowest traded price between 09:00:00 and 09:30:00 inclusive of continuous prints.
- `range_size`: `range_high - range_low`, in price and in ticks.
- `prev_close`: prior regular session close (from the previous day's EOD feed).
- `volume_first_30`: shares traded in the window.
- `atr_14`: 14-session average true range from daily bars, used to normalize range_size.

Entry conditions, long:

- Price trades at or above `range_high + tick` (one tick above the range high) after 09:30:00.
- The breakout is confirmed by a volume filter: `volume_first_30` is at least 1.5x the trailing
  20-session median first-30-minute volume for that name. This rejects low-conviction pokes.
- The gap from `prev_close` to `open_auction_price` is not extreme. If the open gapped more than
  2x the 14-day ATR above `prev_close`, skip longs (you are buying a runaway gap that is likely to
  mean-revert). Symmetrically skip shorts on large downside gaps.
- `range_size` is sensible: require `range_size >= 0.5 * atr_14` (the open actually moved) but
  `range_size <= 2.0 * atr_14` (it was not a chaotic blowout). Outside that band, stand aside.

Entry conditions, short:

- Mirror of the above using `range_low - tick` as the trigger and downside gap filters. Note that
  shorting on IDX is restricted for retail: most retail brokers do not offer short selling, and
  margin/short facilities (such as MTF margin trading) are limited and require approval. The bot
  should treat short entries as disabled unless a short-enabled account and broker API are
  configured. Document this clearly so the bot never attempts an unsupported sell-short order.

Time validity:

- Entries are only valid from 09:30:00 until 11:00:00 WIB. After 11:00 the lunch gap risk grows and
  the edge decays. Any unfilled breakout after 11:00 is ignored.
- All open ORB positions are force-closed at 11:25:00 WIB before the lunch break, unless an
  explicit end-of-day hold flag is set (not recommended for the base strategy).

---

## Exit and risk logic

Stop loss:

- Place the initial stop on the opposite side of the range. For a long, stop at `range_low - tick`
  (or `range_low - 0.5 * range_size` for a wider, less noisy stop if the name is volatile).
- For a short, stop at `range_high + tick`.
- Because IDX tick sizes are coarse at low prices, round the stop to the nearest valid tick or the
  order is rejected.

Target:

- Primary target is a range projection: `entry + k * range_size` for longs, where k is the
  extension multiple. Common values are k = 1.0 (target one range-size of movement) and k = 2.0
  (measured-move target). Start with k = 1.0 for a higher win rate and k = 2.0 only after the
  backtest confirms the distribution supports it.
- A time-based exit: if the target is not hit by 11:00:00, take the position off at market to avoid
  the lunch gap, regardless of PnL.

Trailing stop (optional):

- Once price reaches 1.0x range extension in your favor, move the stop to breakeven
  (`entry +/- tick`). This converts the trade to risk-free and lets the remainder ride to the 2.0x
  target if momentum continues.

Position sizing:

- Use percent-risk sizing: `shares = (capital * risk_pct) / (entry - stop)`, rounded down to a
  whole lot of 100 shares, where `risk_pct` is the fraction of equity you will lose if the stop
  hits (commonly 0.5 percent to 1.0 percent per trade).
- Cap the position at `max_position_pct` of equity (for example 10 percent) so a single name cannot
  dominate the book.
- Because IDX lot size is 100 shares, `shares` must be a multiple of 100; if rounding to a lot
  pushes risk above `risk_pct`, reduce `risk_pct` or skip the name.

Portfolio risk:

- Limit to N concurrent ORB positions (for example 3 to 5) and total intraday risk to a cap
  (for example 3 percent of equity across all open stops). If the cap is hit, skip further signals.

---

## Data sources and the no-free-real-time problem

A hard constraint for any IDX bot: there is no free, public, real-time market-data API from IDX.
idx.co.id serves end-of-day and reference data but not a streaming tick feed, and it blocks
automated scraping (HTTP 403 observed this tick). Retail bots therefore source real-time data
through one of these paths:

- Broker websockets. Retail platforms such as Stockbit, Ajaib, Pluang, and IndoPremier (IPOT)
  expose quote streams inside their apps. Several have undocumented websocket endpoints that power
  their web and mobile clients; capturing those requires reverse-engineering the app's network
  traffic and is fragile (endpoints and auth tokens change). Use only where you control the account
  and comply with the broker's terms.
- Third-party market-data vendors. Paid feeds (for example Bloomberg, Refinitiv, or regional
  vendors) provide clean IDX Level 1 and sometimes Level 2. Cost is the downside; for a serious bot
  this is the reliable path.
- Screen-scraping the broker web client. Some builders run a headless browser against the broker's
  web quote page and parse the DOM. This is the most fragile and TOS-risky approach and is not
  recommended for production.

For backtesting and research, end-of-day data is sufficient and easier to obtain:

- IDX provides daily OHLCV and reference files via idx.co.id (when reachable) and partner pages.
- Retail aggregators such as Stockbit and Bareksa expose historical prices through their web and
  mobile clients; the same reverse-engineering approach applies but daily bars are far more stable
  than live ticks.
- Build a historical 1-minute bar archive by logging the broker quote stream during live sessions.
  Over a few months you accumulate a minute-bar dataset for the LQ45/IDX30 universe that is good
  enough for ORB backtests.

Critical data hygiene:

- The opening auction print at 09:00 is a single call-auction trade, not a continuous print. Your
  minute-bar aggregator must label it distinctly and must NOT include pre-opening (08:45 to 08:55)
  implied prices in the 09:00 to 09:30 continuous range.
- Always align to WIB (UTC+7). Do not mix server timezone with exchange timezone; a one-hour
  mismatch silently trades the wrong window.
- Rebuild the LQ45/IDX30 constituent list on each review date. Backtests that assume a static
  universe suffer survivorship bias toward today's winners.

---

## Reference implementation

The design plugs into the canonical event-driven baseline (queue plus state machine, see
02-trading-bot/architectures/event-driven-baseline.md). The bot is a set of components that
consume a bar stream and emit orders onto the execution queue. Below is a working, commented
Python skeleton. It is intentionally framework-light so it can run against any data source you wire
in. Numbers in the config are starting points, not tuned values.

```python
"""
idx_orb.py - IDX Opening Range Breakout bot (09:00-09:30 WIB window).

Run loop:
  1. Data feed pushes 1-minute bars (or ticks aggregated to 1-min) for the universe.
  2. Each bar is dispatched to the BarAggregator, which tracks the opening range.
  3. At/after 09:30 the ORBStrategy evaluates signals and emits Order objects.
  4. RiskManager sizes and bounds the order before it hits the execution queue.
  5. PositionKeeper tracks open trades; force-close logic handles the lunch gap.

Timezone: all session times are WIB (Asia/Jakarta, UTC+7). Use zoneinfo, never local time.
"""

from __future__ import annotations
import math
from dataclasses import dataclass, field
from datetime import datetime, time
from enum import Enum
from zoneinfo import ZoneInfo

WIB = ZoneInfo("Asia/Jakarta")


# ---- Session calendar -------------------------------------------------------
# Verified structure from Wikipedia "Indonesia Stock Exchange".
# Pre-opening 08:45-08:55, open auction 09:00, Session I 09:00-11:30,
# lunch 11:30-13:30, Session II 13:30-14:49:59, pre-close 14:50-15:00.
# Closing time subject to IDX 2024 extension; verify-live against idx.co.id.
OPEN_AUCTION      = time(9, 0)    # first continuous trade prints at 09:00
RANGE_START       = time(9, 0, 0)
RANGE_END         = time(9, 30, 0)
ENTRY_DEADLINE    = time(11, 0, 0)
FORCE_CLOSE       = time(11, 25, 0)
LUNCH_START       = time(11, 30)
LUNCH_END         = time(13, 30)


class Side(Enum):
    LONG = 1
    SHORT = -1


@dataclass
class Bar:
    symbol: str
    ts: datetime          # timezone-aware, WIB
    open: float
    high: float
    low: float
    close: float
    volume: int
    is_auction: bool = False   # True only for the 09:00 call-auction print


@dataclass
class Order:
    symbol: str
    side: Side
    quantity: int         # must be multiple of 100 (lot size)
    limit_price: float
    stop_price: float | None = None
    note: str = ""


@dataclass
class Config:
    universe: list[str] = field(default_factory=list)   # IDX30/LQ45 tickers
    risk_pct: float = 0.007          # 0.7% equity risk per trade
    max_position_pct: float = 0.10   # cap single name at 10% of equity
    max_concurrent: int = 4
    total_risk_cap: float = 0.03     # max 3% equity at risk across book
    min_adv_value: float = 50e9      # Rp 50B avg daily value floor
    vol_filter_mult: float = 1.5     # first-30 vol >= 1.5x trailing median
    range_atr_min: float = 0.5       # range_size >= 0.5 * atr14
    range_atr_max: float = 2.0       # range_size <= 2.0 * atr14
    gap_atr_max: float = 2.0         # skip if open gapped > 2x atr14
    ext_target_k: float = 1.0        # primary target = 1.0x range size
    allow_short: bool = False        # IDX retail shorting usually disabled
    tick_table: list[tuple[float, float]] = field(default_factory=lambda: [
        (200.0, 1.0), (500.0, 2.0), (2000.0, 5.0), (5000.0, 10.0),
        (10000.0, 25.0), (25000.0, 50.0), (50000.0, 100.0),
        (100000.0, 250.0), (float("inf"), 500.0),
    ])


def tick_size(price: float, table: list[tuple[float, float]]) -> float:
    """Return the IDX tick for a given price per the published schedule."""
    for threshold, tick in table:
        if price < threshold:
            return tick
    return 500.0


def round_to_tick(price: float, table: list[tuple[float, float]]) -> float:
    t = tick_size(price, table)
    return round(price / t) * t


def lot_floor(shares: int) -> int:
    """Shares must be a multiple of 100 on IDX."""
    return max(100, (shares // 100) * 100)


@dataclass
class InstrumentState:
    symbol: str
    prev_close: float = 0.0
    atr14: float = 0.0
    med_first30_vol: float = 0.0
    open_price: float = 0.0
    range_high: float = -math.inf
    range_low: float = math.inf
    range_locked: bool = False
    in_range_window: bool = False
    # position tracking
    position: int = 0            # +shares long, -shares short
    entry: float = 0.0
    stop: float = 0.0
    target: float = 0.0
    be_moved: bool = False


class BarAggregator:
    """Tracks the opening range per instrument, ignoring the auction print."""

    def __init__(self, cfg: Config):
        self.cfg = cfg
        self.st: dict[str, InstrumentState] = {}

    def on_bar(self, bar: Bar) -> None:
        s = self.st.setdefault(bar.symbol, InstrumentState(symbol=bar.symbol))
        t = bar.ts.timetz()

        # Capture the 09:00 auction print as the open, but do NOT use it for range.
        if bar.is_auction and t.hour == 9 and t.minute == 0:
            s.open_price = bar.close
            return

        # Only build the range during the continuous 09:00-09:30 window.
        if RANGE_START <= t < RANGE_END:
            s.in_range_window = True
            s.range_high = max(s.range_high, bar.high)
            s.range_low = min(s.range_low, bar.low)
        elif t >= RANGE_END and not s.range_locked:
            s.range_locked = True
            s.in_range_window = False


class ORBStrategy:
    def __init__(self, cfg: Config, aggregator: BarAggregator, risk: "RiskManager"):
        self.cfg = cfg
        self.agg = aggregator
        self.risk = risk

    def on_bar(self, bar: Bar) -> list[Order]:
        orders: list[Order] = []
        s = self.agg.st.get(bar.symbol)
        if s is None or not s.range_locked:
            return orders
        if s.position != 0:
            self._manage_open(bar, s, orders)
            return orders
        if bar.ts.timetz() >= ENTRY_DEADLINE:
            return orders
        if bar.ts.timetz() >= FORCE_CLOSE:
            return orders

        rng = s.range_high - s.range_low
        if rng <= 0 or s.atr14 <= 0:
            return orders

        # Range sanity filters (normalized to ATR).
        if rng < self.cfg.range_atr_min * s.atr14:
            return orders
        if rng > self.cfg.range_atr_max * s.atr14:
            return orders

        # Gap filter: skip runaway gaps.
        gap = abs(s.open_price - s.prev_close)
        if gap > self.cfg.gap_atr_max * s.atr14:
            return orders

        # Volume confirmation.
        if bar.volume < self.cfg.vol_filter_mult * s.med_first30_vol:
            return orders

        tick = tick_size(bar.close, self.cfg.tick_table)
        long_trig = s.range_high + tick
        short_trig = s.range_low - tick

        if bar.close >= long_trig and self.cfg.allow_short or bar.close >= long_trig:
            stop = round_to_tick(s.range_low - tick, self.cfg.tick_table)
            target = round_to_tick(bar.close + self.cfg.ext_target_k * rng,
                                   self.cfg.tick_table)
            qty = self.risk.size(symbol=bar.symbol, entry=bar.close, stop=stop,
                                 cfg=self.cfg)
            if qty > 0:
                orders.append(Order(bar.symbol, Side.LONG, qty, bar.close, stop,
                                    "ORB long breakout"))
                s.entry, s.stop, s.target = bar.close, stop, target
                s.position = qty
        elif bar.close <= short_trig and self.cfg.allow_short:
            stop = round_to_tick(s.range_high + tick, self.cfg.tick_table)
            target = round_to_tick(bar.close - self.cfg.ext_target_k * rng,
                                   self.cfg.tick_table)
            qty = self.risk.size(symbol=bar.symbol, entry=bar.close, stop=stop,
                                 cfg=self.cfg, short=True)
            if qty > 0:
                orders.append(Order(bar.symbol, Side.SHORT, qty, bar.close, stop,
                                    "ORB short breakout"))
                s.entry, s.stop, s.target = bar.close, stop, target
                s.position = -qty
        return orders

    def _manage_open(self, bar: Bar, s: InstrumentState, orders: list[Order]) -> None:
        t = bar.ts.timetz()
        if s.position > 0:  # long
            if bar.low <= s.stop:
                orders.append(Order(s.symbol, Side.SHORT, s.position, 0.0,
                                    note="ORB long stop"))
                s.position = 0
                return
            if not s.be_moved and bar.high >= s.entry + (s.target - s.entry) * 0.5:
                s.stop = round_to_tick(s.entry, self.cfg.tick_table)  # breakeven
                s.be_moved = True
            if bar.high >= s.target:
                orders.append(Order(s.symbol, Side.SHORT, s.position, 0.0,
                                    note="ORB long target"))
                s.position = 0
        else:  # short
            if bar.high >= s.stop:
                orders.append(Order(s.symbol, Side.LONG, abs(s.position), 0.0,
                                    note="ORB short stop"))
                s.position = 0
                return
            if bar.low <= s.target:
                orders.append(Order(s.symbol, Side.LONG, abs(s.position), 0.0,
                                    note="ORB short target"))
                s.position = 0
        if t >= FORCE_CLOSE and s.position != 0:
            side = Side.SHORT if s.position > 0 else Side.LONG
            orders.append(Order(s.symbol, side, abs(s.position), 0.0,
                                note="ORB lunch force-close"))
            s.position = 0


class RiskManager:
    def __init__(self, equity: float):
        self.equity = equity
        self.open_risk: dict[str, float] = {}

    def size(self, symbol: str, entry: float, stop: float, cfg: Config,
             short: bool = False) -> int:
        risk_amt = self.equity * cfg.risk_pct
        per_share = abs(entry - stop)
        if per_share <= 0:
            return 0
        shares = risk_amt / per_share
        shares = lot_floor(int(shares))
        notional = shares * entry
        if notional > self.equity * cfg.max_position_pct:
            shares = lot_floor(int((self.equity * cfg.max_position_pct) / entry))
        # total risk cap across the book
        projected = sum(self.open_risk.values()) + risk_amt
        if projected > self.equity * cfg.total_risk_cap:
            return 0
        self.open_risk[symbol] = risk_amt
        return shares
```

Wiring the components to the event-driven baseline:

```python
"""
main.py - glue the ORB components to the event queue + execution sink.

The baseline architecture is: data_feed -> event_queue -> strategy dispatch
-> risk -> execution_queue -> broker adapter. Here we show the dispatch loop
and the daily reset that reloads the universe and reference data.
"""

from idx_orb import (Bar, Config, BarAggregator, ORBStrategy, RiskManager,
                     WIB, FORCE_CLOSE)
from datetime import datetime


def load_universe() -> list[str]:
    """Pull current IDX30/LQ45 from your reference store. Re-pull on review date.
    Source of truth: https://en.wikipedia.org/wiki/LQ45 and IDX primary pages."""
    # TODO: replace with your fetcher; do NOT hardcode a stale list.
    return ["BBCA", "BBRI", "BBNI", "ASII", "TLKM", "BMRI", "GOTO", "ANTM",
            "ADRO", "ICBP", "UNVR", "PGAS", "INKP", "KLBF", "TOWR"]


def load_reference(symbol: str) -> dict:
    """prev_close, atr14, median first-30min volume. From your EOD archive."""
    # TODO: wire to your historical store.
    return {"prev_close": 0.0, "atr14": 0.0, "med_first30_vol": 0.0}


def run_day(cfg: Config, equity: float):
    agg = BarAggregator(cfg)
    risk = RiskManager(equity)
    strat = ORBStrategy(cfg, agg, risk)
    for sym in cfg.universe:
        ref = load_reference(sym)
        st = agg.st.setdefault(sym, __import__("idx_orb").InstrumentState(sym))
        st.prev_close = ref["prev_close"]
        st.atr14 = ref["atr14"]
        st.med_first30_vol = ref["med_first30_vol"]

    # event loop: blocking_get yields Bars from the feed (1-min or tick-aggregated)
    for bar in event_queue_blocking_get():
        if bar.ts.timetz() >= FORCE_CLOSE and all(
                s.position == 0 for s in agg.st.values()):
            break  # session done for ORB
        agg.on_bar(bar)
        orders = strat.on_bar(bar)
        for o in orders:
            execution_queue_put(o)   # broker adapter picks these up


if __name__ == "__main__":
    cfg = Config(universe=load_universe(), allow_short=False)
    run_day(cfg, equity=100_000_000.0)   # Rp 100 juta sample capital
```

The execution adapter is the only IDX-specific hard part. Because there is no free real-time API,
the adapter typically speaks to your broker's private websocket (captured from the app) or to a
paid vendor. The adapter must:

- Translate `Order` into the broker's JSON wire format with correct lot rounding and tick rounding.
- Handle the opening auction: do not send market orders during 08:45 to 08:55; the auction handles
  matching at 09:00.
- Respect rate limits. IDX/broker order-entry has throttles; burst your ORB entries across a few
  hundred milliseconds, not all at once.
- Acknowledge fills and feed them back into `PositionKeeper` so `RiskManager.open_risk` stays true.

---

## Backtest harness

You cannot tune ORB on live money. Build a minute-bar backtester that replays the 09:00 to 11:30
window for the LQ45/IDX30 universe over at least 12 months (more is better; IDX has regime shifts
around earnings seasons and the Lebaran period when liquidity thins). The harness should:

- Reconstruct the opening range from stored 1-minute bars, excluding the auction print.
- Apply the exact filters above and record each signal, its fill (assume fill at the trigger price
  or one tick worse, plus a realistic commission and the bid-ask half-spread as slippage).
- Track per-trade and per-symbol statistics: win rate, average win, average loss, profit factor,
  expectancy, max drawdown, and the distribution of range_size vs outcome.
- Report the edge as expectancy per trade and per unit of range volatility, not just win rate,
  because ORB can have a sub-50 percent win rate and still be profitable on a favorable payoff ratio.

A realistic cost model for IDX retail:

- Broker commission: roughly 0.15 percent to 0.25 percent per side for retail (some brokers run
  promos near 0.10 percent). Use 0.20 percent per side as a conservative default.
- Levy and exchange fees: small, on the order of a few basis points combined.
- Bid-ask slippage: for IDX30 names, about 1 to 2 ticks; for thinner LQ45 names, 2 to 5 ticks.
  Model slippage as half the spread in the direction of your trade.
- Lot rounding friction: because you must trade in 100-share lots, the realized risk is slightly
  above or below your target; the backtest must round identically to live.

Illustrative (NOT live, verify-live) target metrics to sanity-check your harness: a well-filtered
ORB on IDX30 might show a 45 to 55 percent win rate with an average win roughly 1.3x to 1.8x the
average loss, yielding positive expectancy. If your backtest shows negative expectancy after costs,
the filters are too loose or the universe too thin; tighten `vol_filter_mult`, widen the range ATR
band, or shrink the universe to IDX30 only.

---

## IDX-specific pitfalls and how to survive them

Pre-opening auction contamination. The 08:45 to 08:55 auction builds a wide implied book. If you
include those prices in the range, your `range_high`/`range_low` are wrong and every breakout
trigger is misplaced. The code above excludes any `is_auction` bar from the range and uses only
continuous prints. This is the single most common ORB bug on IDX.

Lot and tick rejection. JATS rejects orders not on the correct lot (100) and tick. A stop computed
to three decimal places will be bounced, and the bounce can leave you unhedged into the lunch gap.
Always `round_to_tick` and `lot_floor` before sending.

Lunch-break gap. The 11:30 to 13:30 close freezes the book. News during lunch reprices the open at
13:30 with no opportunity to exit. The base strategy force-closes at 11:25. If you want to hold
through lunch, you must size for a gap that can exceed your stop with no execution in between; that
is a different, higher-risk strategy.

Thin LQ45 tails. Even inside LQ45, the smaller constituents can trade only a few hundred lots in
the first 30 minutes, so the breakout is you. Restrict to IDX30 or apply the `min_adv_value` filter
relentlessly.

Short-selling restriction. Retail shorting is effectively unavailable on IDX for most accounts.
Running the short branch requires a margin/short-enabled account and broker. Leave `allow_short`
False unless you have confirmed support, or the bot will emit rejected sell-short orders.

Corporate actions and limit days. Rights issues, splits, dividend cum/ex dates, and auto-limit
(circuit-breaker) days distort the open. Pull the IDX corporate-action calendar and the prior
session's limit hits daily; exclude those names.

Regulatory surface. Trading on IDX is governed by OJK and the exchange. Algorithmic and high-frequency
trading is permitted within exchange rules, but manipulative patterns (spoofing, layering, wash
trades) are prohibited. An ORB bot that places and cancels orders to bait the auction would be
illegal; this design only takes genuine breakout positions and holds them, which is ordinary
momentum trading. Confirm any production deployment with compliance.

Data staleness. Because real-time IDX data is broker-sourced and fragile, your feed can silently
stall. Add a heartbeat: if no bar arrives for 60 seconds during a trading session, halt the bot and
alert. Trading on a stalled feed is worse than not trading.

Survivorship in the universe. LQ45/IDX30 change on review dates. A backtest that holds a fixed
today's list biases results upward. Rebuild the historical universe from review-date snapshots.

---

## Extensions and variants

The 13:30 reopen variant. Session II opens at 13:30 after lunch. A second, weaker ORB can be built
on the 13:30 to 14:00 window with the same logic. Expect lower edge and wider ranges; size smaller.

Multi-timeframe ORB. Instead of a fixed 30-minute range, compute ranges at 15, 30, and 60 minutes
and only trade when they agree on direction. This cuts trade count but raises conviction.

Range-breakout-with-pullback. Rather than entering the instant price crosses the range, wait for a
pullback to retest the broken level and a rejection there. This improves entry quality at the cost
of missing fast breakouts.

Volatility-regime gating. Compute a market-wide volatility state from the JCI (Indonesia Composite,
the broad IDX index) opening range. On high-volatility opens, tighten filters or stand aside; on
low-volatility opens, widen targets. The JCI itself is described on
https://en.wikipedia.org/wiki/Jakarta_Composite_Index as the main IDX benchmark, useful as a
regime filter even though the bot trades single names.

Sector rotation overlay. On a given day, if the ORB signal fires across multiple banks (BBCA,
BBRI, BBNI, BMRI) in the same direction, the conviction is higher than a single-name breakout.
Track cross-name agreement as a meta-signal to scale the whole book up or down.

---

## What this bot is not

This is a research and implementation note, not investment advice and not a guaranteed edge. The
ORB logic is a well-understood intraday pattern, but its profitability on IDX is an empirical
question only your backtest can answer. Ship nothing to live capital until the backtest shows
positive expectancy after realistic Indonesian costs (commission, levies, bid-ask slippage, lot
rounding) over a full year including a Lebaran liquidity trough and an earnings season.

---

## Open engineering tasks

- Build the 1-minute bar archive by logging a broker quote stream during live sessions for IDX30.
- Implement the daily universe reload from the LQ45/IDX30 review snapshots.
- Implement the corporate-action and limit-day exclusion feed from IDX calendars.
- Reverse-engineer or license a real-time quote source; do not depend on idx.co.id scraping
  (HTTP 403 observed, and terms likely forbid it).
- Add the heartbeat stall-detector and the lunch force-close before any live test.
- Backtest 12 to 24 months, report expectancy per trade and per range-volatility unit.

## Connection to the rest of the vault

This strategy file pairs with sibling modules in the vault. The event-driven baseline in
02-trading-bot/architectures/event-driven-baseline.md is the queue plus state machine this bot
drops into; the broker authentication and rate-limit notes in 02-trading-bot/brokers-apis/
binance-spot-futures.md are a different venue but the HMAC signing and retry patterns transfer to
any broker adapter you build for IDX. The market-cron module (05-market-cron) is where you would
schedule the daily universe reload, the corporate-action exclusion fetch, and the backtest replay
job. The news-sentiment scoring work (02-trading-bot/signals/news-sentiment-scoring.md, still a
gap) is a natural filter to add: suppress ORB longs on names with negative overnight headline
scores and vice versa, which should cut fake-out rates on gap days.

One concrete cross-module improvement worth building: feed the JCI opening range (computed from the
same 09:00 to 09:30 window on the composite index) into the risk manager as a regime gate. On days
the composite itself breaks its own opening range with volume, broaden the book and loosen the
per-name volume filter; on days the composite stays inside a tight opening range, tighten filters
and cap concurrent positions. This is a few lines in `ORBStrategy.on_bar` and materially improves
robustness across volatile and quiet regimes.

## References

- Indonesia Stock Exchange, trading hours and tick schedule: https://en.wikipedia.org/wiki/Indonesia_Stock_Exchange
- LQ45 index and constituents: https://en.wikipedia.org/wiki/LQ45
- Jakarta Composite Index (JCI) benchmark: https://en.wikipedia.org/wiki/Jakarta_Composite_Index
- Day trading, momentum, and volatility: https://en.wikipedia.org/wiki/Day_trading
- Market color and session news: https://www.cnbcindonesia.com/
- Market color and session news: https://kontan.co.id/
- Market color and session news: https://www.bisnis.com/
- Retail quote and flow source: https://stockbit.com/
- Retail market data and fund flow: https://www.bareksa.com/
- IDX primary trading-hours page (verify-live; blocked automated access this tick): https://www.idx.co.id/en/about-idx/support/trading-hours
- IDX primary equities page (verify-live; blocked automated access this tick): https://www.idx.co.id/en/products/equities
