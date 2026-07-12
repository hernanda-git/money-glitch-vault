# CRON-SETUP — scheduled jobs for money-glitch-vault

> How the auto-enrich pipeline is actually scheduled on this machine. Both the **WSL Hermes**
> (real Python + `hermes` CLI) and the **Windows Hermes** (git-bash, no working `python`)
> run these as `no_agent` watchdogs. Reproduce with the commands at the bottom.

## Topology (why two schedulers?)

- **Windows git-bash has no working `python`** (the `python` command is a Microsoft Store
  stub). It *does* have `wsl.exe`.
- **WSL has `python3` (3.14) + the `hermes` CLI** and can see the repo at
  `/mnt/c/Workspace/money-glitch-vault`.

So: **WSL-side jobs run the Python directly.** **Windows-side jobs are thin wrappers that
delegate to WSL** via `wsl.exe bash -lc ".../mgv-*.sh"`. Both feed the same repo.

## Jobs

| Job (WSL / Windows) | Schedule | Script (WSL `scripts/`) | Deliver | Purpose |
|---|---|---|---|---|
| `mgv-pulse-heal` / `-win` | every 6h | `mgv-pulse-heal.sh` | local | Heal IHSG + IDX movers legs into `latest.json`, re-validate |
| `mgv-pulse-watch` / `-win` | daily 00:00 | `mgv-pulse-watch.sh` | **telegram** | Alert if pulse DEGRADED/DEAD (silent when healthy) |
| `mgv-archive` / `-win` | Sun 02:00 | `mgv-archive.sh` | local | Archive pulses >7d to `08-research-archive/market-pulses/` |
| `mgv-backlog` / `-win` | Sun 03:00 | `mgv-backlog.sh` | local | Synthesis "New gaps" → draft backlog (dedup) |
| `mgv-secret-scan` / `-win` | daily 06:00 | `mgv-secret-scan.sh` | **telegram** | Block-leak guard on tracked files |

## Files

- WSL wrappers: `/home/it26/.hermes/scripts/mgv-*.sh` (real, run Python on `/mnt/c/...`).
- Windows wrappers: `C:\Users\it26\AppData\Local\hermes\scripts\mgv-*-win.sh` (delegate to WSL).
- All call the vault's `_meta/*.py` + `05-market-cron/cron-configs/*.py`.

## Reproduce (WSL — the ones that actually do work)

```bash
# in WSL, as the it26 user:
hermes cron create --name mgv-pulse-heal   --no-agent --script mgv-pulse-heal.sh   "every 6h"
hermes cron create --name mgv-pulse-watch  --no-agent --script mgv-pulse-watch.sh  --deliver telegram "0 0 * * *"
hermes cron create --name mgv-archive      --no-agent --script mgv-archive.sh      "0 2 * * 0"
hermes cron create --name mgv-backlog      --no-agent --script mgv-backlog.sh      "0 3 * * 0"
hermes cron create --name mgv-secret-scan  --no-agent --script mgv-secret-scan.sh  --deliver telegram "0 6 * * *"
```

## Reproduce (Windows — delegates to WSL)

```bash
# in Windows git-bash, using the Windows Hermes CLI venv:
WH=C:/Users/it26/AppData/Local/hermes/hermes-agent/venv/Scripts/hermes.exe
$WH cron create --name mgv-pulse-heal-win   --no-agent --script mgv-pulse-heal-win.sh   "every 6h"
$WH cron create --name mgv-pulse-watch-win  --no-agent --script mgv-pulse-watch-win.sh  --deliver telegram "0 0 * * *"
$WH cron create --name mgv-archive-win      --no-agent --script mgv-archive-win.sh      "0 2 * * 0"
$WH cron create --name mgv-backlog-win     --no-agent --script mgv-backlog-win.sh      "0 3 * * 0"
$WH cron create --name mgv-secret-scan-win  --no-agent --script mgv-secret-scan-win.sh  --deliver telegram "0 6 * * *"
```

## Notes / gotchas

- Windows `python` is unusable → Windows jobs MUST delegate to WSL. If WSL isn't running,
  the `-win` jobs fail (and would alert via Telegram if wired — currently local).
- `hermes cron create --script` requires a **relative** name under `~/.hermes/scripts/`.
- Schedules accept `every Nh`/`every Nm` or a 5-field cron expression; `daily`/`weekly`
  word forms are NOT accepted.
- The watchdog uses `--quiet-ok` so healthy ticks are silent (empty stdout → no Telegram
  spam). Only DEGRADED/DEAD prints + exits non-zero.
- The WSL Hermes already runs a sibling job `money-glitch-harga-pangan` (workdir = this repo,
  `0 8 * * *`) — the pipeline shares one scheduler.
- Alert transport (`PULSE_ALERT_*`) is env-only; the cron `--deliver telegram` is the
  operational delivery path actually used here.
