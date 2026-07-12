# Anchor-of-Trust Registry — one canonical `lookup_trust(entity)` for the whole vault

> The single biggest *unwritten* idea in the vault (flagged as **New gap #4** in the
> 2026-07-12 synthesis §4). Four independent products — judol-pinjol cross-detection, scam
> detection, desil/dormant checker, MBG compliance — each build their *own* isolated
> "is this safe/valid/compliant?" list. This doc plants the flag for **one shared registry
> service** (or one MCP `lookup_trust(entity)` tool) they should all consume, before they
> diverge into four incompatible silos.

**File:** `03-id-business-trends/bottlenecks/anchor-of-trust-registry.md`
**Created:** 2026-07-12
**Category:** Bottleneck analysis (cross-cutting infrastructure)
**Priority:** HIGH (R3 — last READY item)
**Consumed by (4 products):**
- `07/opportunities/judol-pinjol-cross-detection.md`
- `07/inbox/2026-07-07-scam-detection-tool.md`
- `07/opportunities/desil-dormant-checker-saas.md`
- `07/opportunities/mbg-compliance-saas.md`

---

## 1. The pattern nobody consolidated

Every trust/compliance product in the vault asks the same shape of question:

| Product | The question it asks | The list it builds today |
|---------|---------------------|--------------------------|
| judol-pinjol | "is this domain/phone/account/QRIS-MID a fraud entity?" | OJK whitelist + Satgas PASTI blocklist (its own) |
| scam-detection | "is this number/link a known scam?" | Kominfo blocklist + OSINT (its own) |
| desil/dormant | "is this citizen's desil status / account valid?" | SIKS-NG desil + bank dormant (its own) |
| MBG compliance | "is this SPPG dapur compliant / funded?" | BGN compliance status (its own) |

**Four products, four isolated lists, zero shared infrastructure.** The judol one-pager
already *names* the OJK whitelist as its "anchor of trust" — this doc generalizes that anchor
into a service all four call.

## 2. The registry: one interface, many sources

```
lookup_trust(entity_type, entity_value) -> {
    status:     "trusted" | "flagged" | "unknown",
    score:      0..100,          # 0 = safe, 100 = maximum risk/invalid
    band:       "green" | "amber" | "red",
    sources:    [ {registry, verdict, as_of, url} ],
    provenance: "...",           # which lists contributed (never hallucinate)
}
```

`entity_type ∈ { domain, phone, bank_account, ewallet_id, qris_mid, nik, sppg_id, lender_name }`

## 3. The five source registries (the "anchors")

| # | Registry | Kind | Feeds which product | Machine-readable today? |
|---|----------|------|---------------------|-------------------------|
| A | **OJK licensed-lender whitelist** | positive (allow) | judol-pinjol | published, not clean feed — *verify-live* |
| B | **Kominfo / OJK / PPATK / Satgas PASTI blocklists** | negative (deny) | judol-pinjol, scam | fragmented, not versioned — *verify-live* |
| C | **SIKS-NG desil status** | citizen status | desil/dormant | auth-gated — guided fallback |
| D | **BGN SPPG compliance** | compliance status | MBG compliance | dashboard, no API — *verify-live* |
| E | **Bank dormant / blokir status** | account status | desil/dormant | per-bank, no standard — guided fallback |

Positive registries answer "is this *licensed/valid*?"; negative registries answer "is this
*flagged*?". A complete verdict needs both — the judol doc's key insight (a whitelist only
covers the positive case; the negative case has no public query endpoint).

## 4. Reference interface (registry service + MCP tool)

```python
# anchor_of_trust/registry.py — the shared service
from dataclasses import dataclass, field
from typing import Literal

EntityType = Literal["domain","phone","bank_account","ewallet_id","qris_mid",
                     "nik","sppg_id","lender_name"]

@dataclass
class Verdict:
    registry: str            # "OJK_whitelist" | "SatgasPASTI_blocklist" | ...
    verdict: str             # "trusted" | "flagged" | "unknown"
    as_of: str               # ISO date of the source list (provenance)
    url: str = ""            # citable source; verify-live

@dataclass
class TrustResult:
    entity_type: EntityType
    entity_value: str
    verdicts: list[Verdict] = field(default_factory=list)

    @property
    def status(self) -> str:
        if any(v.verdict == "flagged" for v in self.verdicts):
            return "flagged"
        if any(v.verdict == "trusted" for v in self.verdicts):
            return "trusted"
        return "unknown"

    @property
    def score(self) -> int:
        # negative (deny) list hit dominates; positive (allow) list lowers score
        if any(v.verdict == "flagged" for v in self.verdicts):
            return 90
        if any(v.verdict == "trusted" for v in self.verdicts):
            return 5
        return 50   # unknown = neutral-suspicious (absence of proof, not proof of absence)

    @property
    def band(self) -> str:
        s = self.score
        return "red" if s >= 70 else "amber" if s >= 40 else "green"


class Registry:
    """Aggregates the 5 anchor sources behind one lookup."""
    def __init__(self, adapters: dict):
        self.adapters = adapters      # {name: adapter with .check(etype, value)}

    def lookup_trust(self, entity_type: EntityType, entity_value: str) -> dict:
        verdicts = []
        for name, ad in self.adapters.items():
            v = ad.check(entity_type, entity_value)   # returns Verdict | None
            if v:
                verdicts.append(v)
        r = TrustResult(entity_type, entity_value, verdicts)
        return {
            "status": r.status, "score": r.score, "band": r.band,
            "sources": [vars(v) for v in verdicts],
            "provenance": ", ".join(v.registry for v in verdicts) or "no source matched",
            "verify_live": True,       # source lists must be re-confirmed before action
        }
```

MCP surface (one tool, mirrors the vault's MCP pattern — `fastwork-mcp-spec.md`):

```
lookup_trust        { entity_type, entity_value }         -> TrustResult
lookup_trust_batch  { entities: [{type,value}] }          -> [TrustResult]
registry_refresh    { source }                            -> { updated, as_of }
registry_sources    {}                                    -> [ {name, kind, as_of} ]
```

## 5. How the four products consume it (no more silos)

```
judol-pinjol  -> lookup_trust("qris_mid", mid)      # A + B anchors
scam-detect   -> lookup_trust("phone", number)      # B anchor + OSINT
desil-checker -> lookup_trust("nik", nik)           # C + E anchors
mbg-compliance-> lookup_trust("sppg_id", id)        # D anchor
```

The judol doc's entity-resolution graph (co-occurrence of a mule across judol_deposit and
pinjol_repay) becomes a **6th adaptive source** feeding negative verdicts back into the
registry — the registry gets smarter as any consumer reports.

## 6. Why build the registry, not four lists

- **Cost:** each source integration (OJK, Kominfo, SIKS-NG, BGN) is built once, not 4×.
- **Freshness:** one `registry_refresh` cron keeps all consumers current; today each rots
  independently (the exact failure mode the judol doc warns about — "one format-change away
  from useless").
- **Network effect:** every consumer's reports enrich the shared graph (§5), so the whole
  portfolio compounds instead of four isolated tools each starting from zero.
- **Trust:** one auditable provenance chain (`sources[].url` + `as_of`) instead of four
  opaque lists. Never returns a verdict without citing which registry produced it.

## 7. Credential & correctness safety

- Source API keys (OJK/SIKS-NG/BGN if any) by name only; `.gitignore` + D4 `check_secrets.py`.
- **`unknown` ≠ `safe`.** Absence from a blocklist is not proof of safety (score 50, not 0);
  the band logic encodes this so a consumer never green-lights an unverified entity.
- Every external figure and every source list tagged **`verify-live`** — re-confirm before
  any user-facing verdict.

## 8. New gaps discovered

- **`anchor-of-trust-mcp`** — the MCP server implementing §4 (sibling to `qris-settlement-mcp`).
- **Source adapters** (A–E) — five small ingest modules; OJK whitelist + Satgas PASTI
  blocklist are the highest-leverage first two (judol product needs them now).
- **Entity-resolution graph** — the co-occurrence graph from the judol doc, promoted to a
  shared registry input.

## 9. References

2026-07-12 synthesis §4 (new gap #4, "anchor-of-trust registry");
`07/opportunities/judol-pinjol-cross-detection.md` (OJK whitelist as anchor, risk-score model,
entity graph); `07/opportunities/desil-dormant-checker-saas.md` (C + E anchors);
`07/opportunities/mbg-compliance-saas.md` (D anchor); `07/inbox/2026-07-07-scam-detection-tool.md`.
