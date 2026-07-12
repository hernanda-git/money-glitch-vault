# <Server Name> MCP Server Spec

> <One-paragraph: what the MCP server wraps, which agent consumes it, and the highest-leverage tool it exposes.>

**File:** `04-freelancer-ai-agent/mcp-servers/<slug>.md`
**Created:** YYYY-MM-DD
**Category:** MCP server spec
**Consumed by:** <which agent / which one-pager>

---

## 1. Scope & positioning
<What real system this wraps (e.g. Fastwork, QRIS settlement, agri-input prices).>

## 2. Auth model
<Dual-auth / JWT / API key. Reference `config.json` fields by NAME ONLY — never paste tokens.>

## 3. Tool surface
| Tool | Args | Returns | Notes |
|------|------|---------|-------|
| `tool_name` | {arg: type} | type | idempotent? rate limit? |

## 4. Reference server code
<Minimal MCP server skeleton (FastMCP / official SDK).>

## 5. Reference client code
<How the agent calls it.>

## 6. Threat model & credential safety
<What must stay local; redaction rules before commit.>

## 7. New gaps / sibling specs
- `path/to/sibling-mcp.md` — why needed
