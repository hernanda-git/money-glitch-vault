# QRIS Settlement MCP Server Specification

> A Model Context Protocol server that wraps a **license-light, same-day QRIS settlement
> layer** so any agent (Fastwork freelancer agent, trading signal agent, warung bot) can
> offer merchants **same-day payout** on top of the mandated T+1 QRIS rail — without
> per-acquirer integration. This is the MCP sibling explicitly requested in
> `03-id-business-trends/bottlenecks/qris-settlement-speed-arbitrage.md §19` and is the
> literal "connective tissue" the vault is missing.

**File:** `04-freelancer-ai-agent/mcp-servers/qris-settlement-mcp.md`
**Created:** 2026-07-12
**Category:** MCP server spec
**Consumed by:** Fastwork agent (`04/.../fastwork-mcp-spec.md`), trading signal-agent (R4), warung collective-buying (`07/opportunities/warung-collective-buying-loyalty-toolkit.md`)

---

## 1. Why this server exists

`qris-settlement-speed-arbitrage.md` quantifies a **~Rp 16T systemic float** trapped in the
T+1 QRIS merchant payout rail (32.71M merchants). Three independent bottleneck docs
(COD settlement, QRIS float, logistics orchestration) all reinvent the *same* event-driven
settlement state machine. This MCP server is the **single reusable settlement primitive**
those products should share, exposing three tools:

- `advance_settlement` — advance a merchant's T+1 settlement to same-day for a 0.1% fee.
- `get_float` — report the systemic / merchant-level float being held.
- `reconcile` — idempotent webhook + netting engine that matches advances against the
  eventual T+1 clearing credit.

It deliberately mirrors the `fastwork-mcp-spec.md` architecture (stdio MCP, pydantic models,
audit log, token-by-name-only) so the two servers share tooling.

## 2. Auth model

Two surfaces, both credential-light by design:

- **Acquirer / PSP side** (where the advance capital lives): a licensed aggregator's API
  key. Referenced by **name only** (`QRIS_AGGREGATOR_API_KEY` env). Never committed; see
  `_meta/CONVENTIONS.md` and the D4 redaction check.
- **Merchant side** (the agent calling on behalf of a warung/freelancer): an OAuth or
  API-token issued by the aggregator after the merchant onboards via QRIS MID. Stored in the
  same secret store as Fastwork's token, never logged.

> No bank license is required for the *advance* product: it is a working-capital facility
> backed by the aggregator's balance sheet, settled against the mandated BI-FAST / SKNBI
> T+1 credit. Regulatory surface: BI PBI on QRIS, SKNBI batch architecture. Tag all figures
> `verify-live` — the float math is derived from the bottleneck doc, not re-fetched this run.

## 3. Tool surface

| Tool | Args | Returns | Notes |
|------|------|---------|-------|
| `qris_advance_settlement` | `{ merchant_mid: str, amount_idr: int, fee_bps?: int=10, dry_run?: bool=false }` | `{ advanced_id, gross, fee, net_disbursed, settle_on, status }` | Caps per-advance; requires `dry_run` first for any amount > Rp 5jt. |
| `qris_get_float` | `{ merchant_mid?: str, scope?: "merchant"\|"systemic" }` | `{ float_idr, days_held, daily_rate_bps, systemic_float_idr? }` | `systemic` aggregates across ledger; `verify-live` on totals. |
| `qris_reconcile` | `{ from_date: str, to_date: str }` | `{ matched: int, unmatched: int, net_position_idr, disputes: [...] }` | Idempotent; safe to re-run. |
| `qris_webhook_ingest` | `{ payload: dict }` | `{ event, merchant_mid, amount_idr, applied_to_advance?, status }` | Validates signature; updates netting ledger. |
| `qris_validate_merchant` | `{ merchant_mid: str }` | `{ valid, acquirer, onboarded_at, last_settle_at }` | Light probe, no mutation. |
| `qris_setup` | `{ aggregator_api_key: str }` | `{ ok }` | Only sanctioned key-injection path. |

## 4. Reference server skeleton

```python
# qris_settlement_mcp/server.py  (stdio MCP, mirrors fastwork-mcp structure)
import os, json, time, hmac, hashlib
from mcp.server import Server

app = Server("qris-settlement")

AGG_KEY = os.environ.get("QRIS_AGGREGATOR_API_KEY", "")
LEDGER_PATH = os.path.expanduser("~/.hermes/state/qris-ledger.json")
FEE_BPS_DEFAULT = 10          # 0.1%
ADVANCE_CAP_IDR = 5_000_000   # require dry_run above this

def load_ledger():
    if not os.path.exists(LEDGER_PATH):
        return {"advances": {}, "webhooks": []}
    with open(LEDGER_PATH) as f:
        return json.load(f)

def save_ledger(l):
    # atomic write-through (see fastwork-mcp state design)
    tmp = LEDGER_PATH + ".tmp"
    with open(tmp, "w") as f:
        json.dump(l, f, indent=2)
    os.replace(tmp, LEDGER_PATH)

@app.tool()
def qris_advance_settlement(merchant_mid: str, amount_idr: int,
                            fee_bps: int = FEE_BPS_DEFAULT,
                            dry_run: bool = False) -> dict:
    if amount_idr <= 0:
        return {"error": "INVALID_AMOUNT"}
    if amount_idr > ADVANCE_CAP_IDR and not dry_run:
        return {"error": "DRY_RUN_REQUIRED", "cap_idr": ADVANCE_CAP_IDR}
    fee = int(amount_idr * fee_bps / 10_000)
    net = amount_idr - fee
    if dry_run:
        return {"dry_run": True, "gross": amount_idr, "fee": fee,
                "net_disbursed": net, "settle_on": "T+0 (same day)"}
    # call aggregator disbursement API here (key by name only)
    adv_id = f"adv_{int(time.time()*1000)}"
    l = load_ledger()
    l["advances"][adv_id] = {
        "merchant_mid": merchant_mid, "gross": amount_idr, "fee": fee,
        "net": net, "status": "advanced", "created_at": time.time(),
    }
    save_ledger(l)
    return {"advanced_id": adv_id, "gross": amount_idr, "fee": fee,
            "net_disbursed": net, "settle_on": "T+0", "status": "advanced"}

@app.tool()
def qris_get_float(merchant_mid: str = None, scope: str = "merchant") -> dict:
    l = load_ledger()
    if scope == "systemic":
        # sum of outstanding advances = float we are carrying
        out = sum(a["net"] for a in l["advances"].values()
                  if a["status"] == "advanced")
        # NOTE: full systemic Rp16T figure is verify-live from bottleneck doc
        return {"scope": "systemic", "outstanding_advanced_idr": out,
                "systemic_float_idr": 16_300_000_000_000, "verify_live": True}
    # per-merchant float = outstanding advances for that MID
    out = sum(a["net"] for a in l["advances"].values()
              if a["merchant_mid"] == merchant_mid and a["status"] == "advanced")
    return {"merchant_mid": merchant_mid, "float_idr": out}

@app.tool()
def qris_reconcile(from_date: str, to_date: str) -> dict:
    l = load_ledger()
    # match webhook clears against advances; idempotent
    matched = sum(1 for a in l["advances"].values() if a["status"] == "reconciled")
    return {"matched": matched, "unmatched": len(l["advances"]) - matched,
            "idempotent": True}

if __name__ == "__main__":
    app.run()
```

## 5. Netting / reconciliation model

The advance is a *loan against* the T+1 clearing credit. When the aggregator receives the
mandated T+1 settlement from BI-SKNBI, a webhook (`qris_webhook_ingest`) closes the advance:

```
advance (T+0 disburse, fee 0.1%)  --collateralized by-->  T+1 clearing credit
   on T+1 webhook: mark reconciled, release float
```

Edge cases handled (from `qris-settlement-speed-arbitrage.md` §netting engine):
- **Webhook never arrives** → `qris_reconcile` flags `unmatched`; escalate after 2 business days.
- **Partial clear** → prorate against outstanding advances FIFO.
- **Dispute / chargeback** → freeze merchant float, open `disputes[]` entry.

## 6. Reuse across the vault

| Consumer | How it uses this MCP |
|----------|---------------------|
| Fastwork agent | `qris_advance_settlement` to pay freelancers same-day instead of waiting on platform payout. |
| Trading signal-agent (R4) | `qris_get_float` as a macro indicator; `qris_advance_settlement` for copy-fee payouts. |
| Warung collective-buying | `qris_advance_settlement` so warungs get pooled-buy proceeds same-day (zero-MDR QRIS). |

## 7. Threat model & credential safety

- `QRIS_AGGREGATOR_API_KEY` is the only secret; loaded from env, never logged, never in git
  (`.gitignore` blocks `config.json` / `.env`). The D4 pre-commit check scans committed docs
  for leaked token shapes.
- `qris_advance_settlement` is the money tool: enforce `dry_run` above the cap, per-merchant
  daily limits, and an audit log of every call.
- The `verify-live` systemic float (Rp 16.3T) is cited from the bottleneck doc; re-verify
  before any external claim.

## 8. New gaps / sibling specs

- `logistics-orchestrator-mcp` (**P6**) — the B2B last-mile sibling; shares this netting pattern.
- `agri-input-mcp` (**P5**) — sawit/pupuk price + subsidy lookup, same MCP shape.
- `settlement-float-convergence` (**P1**) — the unifying research doc this server implements.
