# Logistics Orchestrator MCP Server Specification

> An MCP server that wraps a **neutral multi-carrier B2B last-mile orchestration layer** —
> quote-all / book-best, idempotent event store, COD reconciliation, coverage telemetry —
> across Indonesian dedicated B2B carriers (Lalamove, AnterAja, etc.). This is the B2B
> last-mile sibling explicitly flagged as missing in
> `03-id-business-trends/competitors/lalamove-ankeraja-logistics-gaps.md` (Gap 5) and in the
> 2026-07-12 synthesis (P6). It reuses the settlement/netting pattern from
> `qris-settlement-mcp.md`.

**File:** `04-freelancer-ai-agent/mcp-servers/logistics-orchestrator-mcp.md`
**Created:** 2026-07-12
**Category:** MCP server spec
**Consumed by:** warung micro-fulfillment, COD settlement bottleneck, freelance delivery

---

## 1. Why this server exists

`lalamove-ankeraja-logistics-gaps.md` maps the missing **neutral multi-carrier orchestration
layer**: no unified quote-all/book-best, no idempotent event store, no COD reconciliation, no
coverage telemetry. Each carrier has its own HMAC auth + webhook contract (the doc ships
working Lalamove HMAC + AnterAja adapter code). This MCP server is the **unified surface**
over those adapters.

## 2. Carriers & auth (from the competitor doc)

- **Lalamove:** HMAC-SHA256 over the request body with an API key + secret.
- **AnterAja:** API key + secret, different signing scheme (see doc adapter code).
- Both sign per-request; the MCP server holds each carrier's creds **by name only** (env),
  never logs them (D4 redaction check applies).

## 3. Tool surface

| Tool | Args | Returns | Notes |
|------|------|---------|-------|
| `logi_quote_all` | `{ origin, destination, weight_kg, cod_idr?: int }` | `{ quotes: [{carrier, price_idr, eta_hours, covers_cod}] }` | Quote across all adapters. |
| `logi_book_best` | `{ quote_id, idempotency_key: str }` | `{ booking_id, carrier, status }` | Idempotent via key. |
| `logi_cod_reconcile` | `{ from_date, to_date }` | `{ matched, unmatched, float_idr }` | Shares netting engine w/ QRIS MCP. |
| `logi_webhook_ingest` | `{ carrier, payload }` | `{ event, booking_id, status, applied_to_cod? }` | Validates signature per carrier. |
| `logi_coverage` | `{ kabupaten }` | `{ carriers: [...], last_mile_ok: bool }` | Coverage telemetry (Gap: coverage-api). |
| `logi_setup` | `{ carrier, api_key, api_secret }` | `{ ok }` | Only sanctioned key-injection. |

## 4. Reference skeleton (adapter + idempotent store)

```python
# logistics_orchestrator_mcp/server.py  (stdio MCP)
import os, json, uuid
from mcp.server import Server

app = Server("logistics-orchestrator")
ADAPTERS = {}          # carrier -> adapter instance (Lalamove/AnterAja)
STORE = os.path.expanduser("~/.hermes/state/logi-events.json")  # idempotent event store

def load_store():
    return json.load(open(STORE)) if os.path.exists(STORE) else {"events": {}}

def save_store(s):
    tmp = STORE + ".tmp"
    json.dump(s, open(tmp, "w"))
    os.replace(tmp, STORE)

@app.tool()
def logi_quote_all(origin: str, destination: str, weight_kg: float,
                   cod_idr: int = 0) -> dict:
    quotes = []
    for name, ad in ADAPTERS.items():
        q = ad.quote(origin, destination, weight_kg, cod_idr)
        quotes.append({"carrier": name, "price_idr": q.price,
                        "eta_hours": q.eta, "covers_cod": q.cod})
    quotes.sort(key=lambda x: x["price_idr"])
    return {"quotes": quotes}

@app.tool()
def logi_book_best(quote_id: str, idempotency_key: str) -> dict:
    s = load_store()
    if idempotency_key in s["events"]:      # idempotent — never double-book
        return s["events"][idempotency_key]
    # ... call chosen carrier adapter book() ...
    result = {"booking_id": f"bk_{uuid.uuid4().hex[:8]}", "status": "booked"}
    s["events"][idempotency_key] = result
    save_store(s)
    return result
```

## 5. COD reconciliation (reuses QRIS netting)

COD collected by the courier sits in transit 7–14 days (see `cod-settlement-infrastructure.md`).
`logi_cod_reconcile` mirrors `qris_reconcile`: match courier remittance webhooks against
outstanding COD obligations, FIFO, idempotent. One netting engine, two rails.

## 6. New gaps

- **carrier-webhook-reliability** (Gap from doc): webhooks drop; the event store must
  reconcile against carrier polls, not trust webhooks alone.
- **coverage-api** (Gap): no neutral coverage telemetry exists; `logi_coverage` is a start.

## 7. Threat model & credential safety

- Per-carrier HMAC secrets by name only; `.gitignore` blocks them; D4 pre-commit scans docs.
- `idempotency_key` is mandatory on `logi_book_best` — prevents double-ship / double-charge.
- Reuses audit-log pattern from `fastwork-mcp-spec.md`.
