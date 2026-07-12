# Agri-Input MCP Server Specification

> An MCP server that gives an agent **real-time sawit (TBS) price + pupuk subsidy eligibility**
> lookup for Indonesian smallholders — mirroring `fastwork-mcp-spec.md` but for the 2.7M
> smallholder agriculture vertical. Answers: *"today's TBS price at mill X in kabupaten Y"*
> and *"am I eligible for PSR/HGBT?"*

**File:** `04-freelancer-ai-agent/mcp-servers/agri-input-mcp.md`
**Created:** 2026-07-12
**Category:** MCP server spec
**Consumed by:** agriculture marketplace agent (Cluster F in synthesis), sawitpintar one-pager

---

## 1. Why this server exists

`07/opportunities/sawitpintar-platform.md` and `07/inbox/2026-07-06-pupuk-digital-platform.md`
both need a **price-discovery + GovData-validation** layer. The `fastwork-mcp-spec.md`
proves the agent pattern works for freelance; this ports it to agriculture so a smallholder
can ask a WA bot for today's TBS price and subsidy status without a browser.

## 2. Data sources (GovData, verify-live where unreachable)

- **TBS price:** Gapki / local mill price boards (per kabupaten, per mill). No single API;
  scrape or ingest from regional price bulletins. *Tag `verify-live` — figures not re-fetched this run.*
- **Pupuk subsidy (PSR/HGBT):** Kementan / BUMN pangan eligibility rules. Eligibility is a
  rules engine, not a live query.
- **Weather / harvest window:** BMKG for planning (optional).

## 3. Tool surface

| Tool | Args | Returns | Notes |
|------|------|---------|-------|
| `agri_tbs_price` | `{ kabupaten: str, mill_id?: str, date?: str }` | `{ price_idr_per_kg, mill, kabupaten, date, delta_vs_yesterday }` | Latest available; flag stale. |
| `agri_tbs_trend` | `{ kabupaten, days?: int=30 }` | `{ series: [...], min, max, avg }` | Feeds sawitpintar dashboard. |
| `agri_subsidy_eligibility` | `{ commodity: "sawit"\|"pupuk", area_ha?: float, status?: str }` | `{ program: "PSR"\|"HGBT", eligible: bool, reason, next_step }` | Rules engine, no external call. |
| `agri_input_price` | `{ input: "pupuk"\|"bibit", kabupaten }` | `{ price_idr, subsidized: bool, quota_left?: int }` | Pupuk double-squeeze monitoring. |
| `agri_setup` | `{ source_api_key?: str }` | `{ ok }` | Key by name only. |

## 4. Reference implementation (skeleton)

```python
# agri_input_mcp/server.py  (stdio MCP, mirrors fastwork/qris structure)
import os, json, time
from mcp.server import Server

app = Server("agri-input")

PRICE_DB = os.path.expanduser("~/.hermes/state/agri-tbs.json")  # local cache of ingested boards

@app.tool()
def agri_tbs_price(kabupaten: str, mill_id: str = None, date: str = None) -> dict:
    db = json.load(open(PRICE_DB)) if os.path.exists(PRICE_DB) else {}
    rows = db.get(kabupaten, [])
    if not rows:
        return {"error": "NO_DATA", "kabupaten": kabupaten, "verify_live": True}
    latest = rows[-1]
    prev = rows[-2]["price"] if len(rows) >= 2 else None
    delta = (latest["price"] - prev) if prev else None
    return {"price_idr_per_kg": latest["price"], "mill": latest.get("mill"),
            "kabupaten": kabupaten, "date": latest.get("date"),
            "delta_vs_yesterday": delta, "verify_live": True}

@app.tool()
def agri_subsidy_eligibility(commodity: str, area_ha: float = None,
                             status: str = None) -> dict:
    # PSR (Perkebunan Sawit Rakyat) rules — simplified; verify against Kementan
    if commodity == "sawit":
        eligible = bool(area_ha and area_ha < 25)  # smallholder threshold (verify-live)
        return {"program": "PSR", "eligible": eligible,
                "reason": "smallholder (<25 ha)" if eligible else "above smallholder threshold",
                "next_step": "daftar via dinas perkebunan", "verify_live": True}
    return {"program": None, "eligible": False, "reason": "unsupported commodity"}
```

## 5. Reuse

Shares the `fastwork-mcp-spec.md` server layout (`server.py` / `client.py` / `models.py` /
`state.py` / `audit.py`). The `agri_tbs_price` cache is ingested by a cron mirroring the
`05-market-cron` / `06-harga-pangan-papan` fetchers.

## 6. New gaps

- A **pupuk price + quota ingest cron** (sibling to `06`) — currently no live source wired.
- Integration with `sawitpintar-platform.md` as the UI layer.

## 7. Threat model & credential safety

- Source API keys (if any) by name only; `.gitignore` blocks them.
- `verify-live` on all prices — never present as fact without re-fetch.
