#!/usr/bin/env python3
"""pulse-health-watchdog.py — the alert transport (AUTO-ENRICH §2.4).

Runs `_meta/validate-pulse.py` against `latest.json` and, on DEGRADED/DEAD, delivers a
compact alert to a gateway channel. Delivery is **env-driven and never committed** — set one
of:

    PULSE_ALERT_TELEGRAM_TOKEN  + PULSE_ALERT_CHAT_ID   -> Telegram Bot API sendMessage
    PULSE_ALERT_WEBHOOK_URL                              -> generic POST (JSON)
    PULSE_ALERT_DISCORD_URL                              -> Discord webhook (JSON embed)

If none is set, the alert is printed to stdout (so a wrapping cron `deliver=` target, or the
Hermes notification system, can carry it). Exit code mirrors the validator (0 healthy,
1 degraded, 2 dead) so the cron itself can raise/notify on non-zero.

Idempotent and safe to run on a schedule (e.g. daily 07:00 WIB). Honest: it reports what the
validator says; if the validator says healthy, it sends nothing.

USAGE
-----
    python pulse-health-watchdog.py
    PULSE_ALERT_TELEGRAM_TOKEN=xxx PULSE_ALERT_CHAT_ID=-100.. python pulse-health-watchdog.py
"""
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
VALIDATOR = os.path.join(HERE, "validate-pulse.py")
DEFAULT_PULSE = os.path.join(ROOT, "05-market-cron", "data", "latest.json")


def run_validator(pulse_path: str) -> tuple[int, str]:
    """Return (exit_code, stdout). Non-zero exit = degraded/dead."""
    r = subprocess.run([sys.executable, VALIDATOR, pulse_path],
                       capture_output=True, text=True)
    return r.returncode, (r.stdout or r.stderr).strip()


def build_alert(stdout: str, status: str) -> str:
    head = "⚠️ MONEY-GLITCH-VAULT — market pulse DEGRADED" if status != "DEAD" \
        else "🛑 MONEY-GLITCH-VAULT — market pulse DEAD"
    # Keep it short: the validator already prints a clean summary.
    return f"{head}\n\n{stdout}"


def send_telegram(token: str, chat_id: str, text: str) -> bool:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = json.dumps({"chat_id": chat_id, "text": text,
                          "parse_mode": "Markdown"}).encode("utf-8")
    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status == 200
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError) as e:
        print(f"WARN: telegram send failed: {e}", file=sys.stderr)
        return False


def send_webhook(url: str, text: str, is_discord: bool) -> bool:
    if is_discord:
        payload = json.dumps({"content": text}).encode("utf-8")
    else:
        payload = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(url, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status in (200, 204)
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError) as e:
        print(f"WARN: webhook send failed: {e}", file=sys.stderr)
        return False


def deliver(alert: str) -> None:
    """Try configured transports in order; always also print to stdout."""
    print(alert)
    tok = os.environ.get("PULSE_ALERT_TELEGRAM_TOKEN")
    chat = os.environ.get("PULSE_ALERT_CHAT_ID")
    if tok and chat:
        if send_telegram(tok, chat, alert):
            print("-> delivered via Telegram", file=sys.stderr)
            return
    discord = os.environ.get("PULSE_ALERT_DISCORD_URL")
    if discord:
        if send_webhook(discord, alert, is_discord=True):
            print("-> delivered via Discord", file=sys.stderr)
            return
    hook = os.environ.get("PULSE_ALERT_WEBHOOK_URL")
    if hook:
        if send_webhook(hook, alert, is_discord=False):
            print("-> delivered via webhook", file=sys.stderr)
            return
    print("-> no gateway transport configured; alert on stdout only "
          "(set PULSE_ALERT_* env or wrap with a cron deliver target).", file=sys.stderr)


def main(argv) -> int:
    # crude flag parse so a wrapper can pass `--quiet-ok` (silent on healthy)
    quiet_ok = "--quiet-ok" in argv
    args = [a for a in argv if a != "--quiet-ok"]
    pulse = args[1] if len(args) > 1 else DEFAULT_PULSE
    code, out = run_validator(pulse)
    if code == 0:
        if not quiet_ok:
            print("pulse healthy — no alert")
        return 0
    status = "DEAD" if code >= 2 else "DEGRADED"
    alert = build_alert(out, status)
    deliver(alert)
    return code


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
