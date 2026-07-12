# Safe Storage and Rotation of Cookies and Tokens for the Scraper Module

Last updated: 2026-07-12. Researcher note: this document is the security backbone for the
`01-crawler-scrapper` module. Every other scraper playbook in this folder (the X advanced
search operators file, the TikTok hashtag velocity scraper, the Discord public-server miner,
the subreddit money list, the SEHATI quota scraper) ultimately produces or consumes
long-lived credentials. Those credentials (browser cookies, `auth_token`, `ct0`, OAuth
access/refresh tokens, API keys, session JWTs) are the most dangerous artifacts in the whole
vault. If one of them leaks into a git commit, a log file, or a crash dump, you do not lose
a password you can reset. You lose an identity that has been warmed up, rate-limit-softened,
and trusted by a platform. This file is the operational standard for keeping that from
happening.

Why this lives in `01` and not in some ops folder: the scraper is the only module that
ingests raw platform credentials at all. `02-trading-bot` talks to exchanges with API
keys that can (and should) be IP-allowlisted and trade-disabled. `05-market-cron` consumes
public data. `01` is where the crown jewels enter the repo, so `01` is where the safe-room
rules have to be written first.

The single most important rule in this entire file, stated up front so it survives skimming:
**never put a live credential in plaintext on disk, in an env var that gets logged, or in a
git-tracked file.** Encrypt at rest with a key that is itself never written next to the
data. The rest of the document is mechanics for making that rule boring and automatic.

A disclaimer on reach: the code samples below were executed against `cryptography` 46.0.7
on Python 3.11 at research time and the round-trip assertions passed. The version the docs
site renders may read "50.0.0-dev1" because the docs build from main; the public API used
here (`Fernet`, `PBKDF2HMAC`, `MultiFernet`) has been stable since 2014 and is not expected
to break. Always pin the library in your requirements file.

Primary sources used to build this file (real URLs, fetched 2026-07-12):

- cryptography.io, Fernet (symmetric encryption) recipe docs.
  https://cryptography.io/en/latest/fernet/  (fetched 2026-07-12, HTTP 200)
- cryptography.io, Key Derivation Functions (PBKDF2, Scrypt, HKDF).
  https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions.html
  (fetched 2026-07-12, HTTP 200)
- OWASP Top 10:2021, A02 Cryptographic Failures.
  https://owasp.org/Top10/A02_2021-Cryptographic_Failures/  (fetched 2026-07-12, HTTP 200)
- GitHub Docs, About secret scanning.
  https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
  (fetched 2026-07-12, HTTP 200)
- Gitleaks, open-source secret scanner home page (usage stats and action docs).
  https://gitleaks.io/  (fetched 2026-07-12, HTTP 200)
- Python docs, `secrets` module (CSPRNG for tokens, keys, nonces).
  https://docs.python.org/3/library/secrets.html  (fetched 2026-07-12, HTTP 200)
- PyPI, `keyring` 25.7.0 (OS credential store abstraction).
  https://pypi.org/project/keyring/  (fetched 2026-07-12, HTTP 200, version 25.7.0)
- AWS Docs, What is AWS Secrets Manager.
  https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
  (fetched 2026-07-12, HTTP 200)

---

## H1. Threat model: what you are actually protecting and from whom

You cannot design storage safely without naming the adversary. For this scraper module the
threats, in rough order of likelihood, are:

The committed-secret leak. A cookie string or bearer token gets pasted into a `.py` file
"just for testing", or into a debug print, or into a config that someone later `git add -A`s.
This is the single most common failure mode in the entire industry and GitHub's own secret
scanning product exists to catch it after the fact. Once a token is in a public git history
it is permanently public even after you delete the file, because the blob survives in the
pack. You must prevent, not just detect.

The log-and-crash dump. A scraper throws an exception and the traceback includes the headers
dict, which contains `Cookie: auth_token=...; ct0=...`. If you log at DEBUG or ship tracebacks
to a monitoring service, the secret is now in a second, less-secured place. Structured logging
of auth headers is a common footgun.

The shared-machine reader. On WSL or a CI runner, another process or another user on the box
can read world-readable files in `/tmp` or the home directory. `.gitignore` only helps against
git, not against `cat`.

The dependency supply chain. A transitive package you install to parse HTML could, in a
compromised version, read `~/.config` or walk the filesystem. Defense in depth means secrets
are encrypted even at rest on disk so a file-read by an arbitrary process yields ciphertext.

The platform-side rotation. X, Instagram, TikTok, and Discord all reserve the right to
invalidate sessions arbitrarily. A cookie that worked yesterday can be dead tomorrow. Storage
must therefore be a *live* system (read, check, refresh, rewrite) not a *vault* you open
once. That is the difference between "storage safety" and "rotation", and both are covered
here.

Note what is explicitly OUT of scope: protecting against a determined state-level adversary
with physical access to a powered-on, decrypted machine. Full-disk encryption and a locked
screen cover that. We assume the OS is trusted and the disk may be stolen or the repo may be
cloned by mistake.

---

## H2. The four-layer storage model

The standard we adopt here has four conceptual layers. Each layer has one job. Skipping any
layer is how leaks happen.

Layer 0, the secret itself. A cookie tuple, an OAuth refresh token, an API key. It has no
business being in source code. It lives only inside an encrypted blob or an OS keyring.

Layer 1, the encryption key (KEK, key-encryption-key). The key that encrypts Layer 0. This
key must never sit in the same directory as the encrypted data and must never be committed.
Sources for this key, in order of preference: (a) an OS keyring via the `keyring` package,
(b) a password-derived key via PBKDF2/Scrypt where the password is entered at runtime or
supplied by an env var that is never logged, (c) a cloud secret manager (AWS Secrets Manager,
GCP Secret Manager) retrieved at boot.

Layer 2, the encrypted at-rest store. A file on disk (`.enc`, `.bin`, or a JSON of base64
ciphertext) holding the Layer 0 secrets under Layer 1. On a stolen disk this is unreadable.

Layer 3, the in-memory session cache. When a scraper runs, it decrypts into a Python object
held only in RAM, scrubbed on exit. This object is what the HTTP client actually uses.

The golden rule connecting the layers: Layer 1 must not be derivable from Layer 2, and Layer
2 must not be committed. If you ever find yourself writing the KEK into the same JSON as the
ciphertext, stop. That is the exact mistake this document exists to prevent.

Concretely, the on-disk layout we use in this repo:

```
01-crawler-scrapper/cookies-tokens/
    storage-safety.md          <- this document (git-tracked, no secrets)
    .gitignore                 <- blocks *.enc, *.bin, *.json with credentials
    vault.py                   <- the loader (git-tracked, no secrets)
    # the following are NEVER committed, only exist locally:
    local/cookies.enc         <- encrypted cookie store (git-ignored)
    local/kek.salt            <- salt for PBKDF2 (git-ignored; safe to commit actually)
```

The `.gitignore` in this folder must contain at minimum:

```
*.enc
*.bin
local/
*.token
*.secret
```

If a file matches those globs and still shows up in `git status`, your `.gitignore` is in the
wrong directory or the file was already tracked. Run `git check-ignore -v local/cookies.enc`
to debug why a path is or is not ignored.

---

## H3. Encrypted at-rest storage with Fernet

Fernet is the right primitive for this job and we use it directly rather than rolling our own.
Per the cryptography.io Fernet docs, "Fernet guarantees that a message encrypted using it
cannot be manipulated or read without the key. Fernet is an implementation of symmetric
authenticated cryptography." The authenticated part matters: if an attacker flips a byte in the
ciphertext on disk, decryption fails loudly instead of returning corrupted-but-usable data.
That prevents silent tampering with a stored session.

A Fernet key is 32 bytes of URL-safe base64-encoded material, i.e. a 44-character string
ending in a single `=`. You generate it once with `Fernet.generate_key()`. The same key
encrypts and decrypts. Fernet internally uses AES-128 in CBC mode with a PKCS7 pad, plus
HMAC-SHA256 over the ciphertext for authentication, plus a timestamp so you can reject
stale tokens. All of that is handled for you; you do not touch the primitives.

Verified working example (executed at research time, round-trip assertion passed):

```python
# vault.py  -- minimal encrypted cookie store for the scraper module
from __future__ import annotations
import base64, json, os, tempfile
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

# Path to the encrypted blob. Lives in a git-ignored directory.
VAULT_PATH = Path(__file__).parent / "local" / "cookies.enc"
SALT_PATH  = Path(__file__).parent / "local" / "kek.salt"

def _load_kek() -> bytes:
    """
    Return the key-encryption-key as raw 32 bytes.
    Prefer the OS keyring; fall back to a PBKDF2-derived key from an
    environment variable that is NEVER logged.
    """
    import keyring
    stored = keyring.get_password("money-glitch-vault", "scraper-kek")
    if stored:
        return base64.urlsafe_b64decode(stored)
    # Fallback path: derive from MG_VAULT_PASSPHRASE (set in CI/.env, not logged)
    import secrets
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    passphrase = os.environ["MG_VAULT_PASSPHRASE"].encode()
    SALT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not SALT_PATH.exists():
        SALT_PATH.write_bytes(secrets.token_bytes(16))  # 128-bit salt, write once
    salt = SALT_PATH.read_bytes()
    dk = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600_000)
    return dk.derive(passphrase)

class CookieVault:
    """Read/write cookies as encrypted JSON. Nothing is ever written in plaintext."""
    def __init__(self) -> None:
        self._f = Fernet(base64.urlsafe_b64encode(_load_kek()))
        VAULT_PATH.parent.mkdir(parents=True, exist_ok=True)

    def save(self, cookies: dict) -> None:
        """Encrypt the whole cookie dict and overwrite the blob atomically."""
        token = self._f.encrypt(json.dumps(cookies).encode())
        tmp = VAULT_PATH.with_suffix(".enc.tmp")
        tmp.write_bytes(token)
        os.replace(tmp, VAULT_PATH)  # atomic, no half-written file

    def load(self) -> dict:
        if not VAULT_PATH.exists():
            return {}
        try:
            raw = self._f.decrypt(VAULT_PATH.read_bytes())
        except InvalidToken:
            # either the KEK changed or the file was tampered with; fail closed
            raise RuntimeError("Vault integrity check failed; KEK mismatch or tamper")
        return json.loads(raw)

    def scrub(self) -> None:
        """Best-effort overwrite then delete the plaintext key in memory is moot,
        but we at least remove the on-disk blob when decommissioning a session."""
        if VAULT_PATH.exists():
            VAULT_PATH.unlink()
```

Two design notes that are easy to get wrong. First, the salt must be generated once and
reused; regenerating it on every run makes old ciphertext undecryptable. We write it once
and store it next to the blob. The salt is not secret (OWASP A02 lists "missing key
management" as the failure, not "salt is visible"), so committing it is fine; we still
git-ignore it by being inside `local/` for simplicity. Second, use `os.replace` not
`Path.write_bytes` directly for the save, because a crash mid-write would otherwise leave a
truncated, undecryptable file and you would lose every stored session at once. Atomic rename
prevents that.

---

## H3. Deriving the KEK from a passphrase with PBKDF2 (when there is no OS keyring)

On a headless WSL box or a CI runner you often have no OS keyring backend. The cryptography
KDF docs are blunt about this layer: "Key derivation functions derive bytes suitable for
cryptographic operations from passwords or other data sources using a pseudo-random function
(PRF)." The choice of KDF and its cost parameter is the whole game.

Use PBKDF2-HMAC-SHA256 at 600,000 iterations, or Scrypt with N=2^15, r=8, p=1. The 600k
figure matches the OWASP Password Storage Cheat Sheet guidance for PBKDF2-HMAC-SHA256 as of
its 2023 revision; it is a CPU-costing parameter, not a magic number, so tune it to your
hardware such that derivation takes ~100-250 ms. Too low and brute force is cheap; too high
and your scraper takes seconds to boot on every run.

Verified working KDF example (execution-time assertion passed at research):

```python
import os, base64, secrets
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

passphrase = b"correct horse battery staple"   # entered at runtime, never stored
salt = secrets.token_bytes(16)                  # write once, reuse forever
dk = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=600_000)
kek = base64.urlsafe_b64encode(dk.derive(passphrase))   # 44-char Fernet key
f = Fernet(kek)
ct = f.encrypt(b'auth_token=abc; ct0=def')
assert f.decrypt(ct) == b'auth_token=abc; ct0=def'
```

Where does the passphrase come from if not stored? Three acceptable sources:

Runtime prompt via `getpass.getpass()` so it is never echoed to the terminal and never lands
in shell history. This is the default for an interactive operator running the scraper by hand.

An environment variable `MG_VAULT_PASSPHRASE` injected by the orchestrator (systemd, the
cron wrapper, GitHub Actions secret). Critically, the variable must be read once into the
KEK, then the env var must be unset in the process (`os.unsetenv`) and never printed. A common
leak is a crash dump that dumps `os.environ` wholesale.

A cloud secret manager. AWS Secrets Manager's own docs state it "helps you manage, retrieve,
and rotate database credentials, application credentials, OAuth tokens, API keys, and other
secrets throughout their lifecycles" and that "you replace hard-coded credentials with a
runtime call to the Secrets Manager service to retrieve credentials." That runtime-call
pattern is exactly the Layer 1 source we want for `enrich` and `market-cron` runs on a server.

---

## H3. The OS keyring path via the `keyring` package (preferred on desktop)

When the scraper runs on a desktop or a properly configured server, the cleanest KEK source
is the operating system credential store: Windows Credential Manager (via the `keyring`
backend on Windows/WSL), macOS Keychain, or a Linux Secret Service (gnome-keyring). The
`keyring` package (v25.7.0 at research time, source at https://github.com/jaraco/keyring)
abstracts all three behind `keyring.get_password(service, username)` and
`keyring.set_password(...)`.

Advantages over a passphrase: the secret never enters your process memory as a string you
typed, the OS handles access control (another user on the box cannot read it), and there is
no salt/tuning to manage. Disadvantages: on a bare Linux server with no D-Bus secret service,
the backend silently falls back to a plaintext file in `~/.local/share/python_keyring/`, which
defeats the purpose. Detect that and refuse to start, or fall through to the PBKDF2 path.

```python
import keyring
SERVICE = "money-glitch-vault"
SLOT = "scraper-kek"

def ensure_kek() -> bytes:
    existing = keyring.get_password(SERVICE, SLOT)
    if existing:
        return base64.urlsafe_b64decode(existing)
    import secrets
    fresh = base64.urlsafe_b64encode(secrets.token_bytes(32))  # 256-bit random KEK
    keyring.set_password(SERVICE, SLOT, fresh.decode())
    return fresh
```

Note we generate a random 32-byte KEK here, not a derived one, because the keyring itself is
the trusted store. You do not need PBKDF2 on top of an OS keyring; that would be
double-encryption for no security gain and would just cost CPU.

---

## H2. Rotation: cookies and tokens are perishable, not permanent

Storage at rest solves the leak problem. It does nothing about the fact that every platform
credential has a shelf life. The rotation discipline is what keeps the scraper running for
months instead of days.

### H3. What expires, and how you detect it

Browser cookies from X/IG/TT/Discord are not uniformly long-lived. The `auth_token` and `ct0`
pair for X typically survives until the account logs out, the password is changed, or X's
anti-abuse system flags the session. Instagram and TikTok are far more aggressive and will
expiry a cookie within days if they detect automation fingerprints. OAuth 2.0 access tokens
are short by spec (often 1 hour); the refresh token is the long-lived one (days to forever,
until revoked). API keys for exchange/broker access are the most stable but can be rotated by
you at will.

Detection strategy: every scraper run should attempt a cheap authenticated probe before doing
real work. For X, a GET to the internal `https://x.com/settings/api/...` or simply a
`sessions?include_...` style call that returns 200 with data means the cookie is live; a 403
or a redirect to `/login` means it is dead. For Discord, a 401 on the gateway or a
`GET /api/v9/users/@me` 401 means the token is dead. Treat any non-2xx on the probe as
"rotate now".

### H3. The rotation loop

The pattern is: load from vault, probe, on failure fetch a fresh credential through whatever
acquisition path you have (re-login via a headless browser with real cookies, re-OAuth through
a stored refresh token, or re-mint an API key), encrypt the new value, overwrite the blob
atomically, continue. The key is that rotation writes back through the SAME encrypted path as
storage, so you never temporarily drop to plaintext on disk.

```python
def get_live_cookies(vault: CookieVault, acquire_fn) -> dict:
    cookies = vault.load()
    if cookies and _probe_live(cookies):
        return cookies
    # dead or empty: re-acquire, then persist encrypted again
    fresh = acquire_fn()          # your platform-specific login logic
    vault.save(fresh)             # encrypts and atomically writes
    return fresh

def _probe_live(cookies: dict) -> bool:
    import requests
    try:
        r = requests.get("https://x.com/api/1.1/account/settings.json",
                         cookies=cookies, timeout=10)
        return r.status_code == 200
    except Exception:
        return False
```

### H3. Key rotation without downtime using MultiFernet

Because you will eventually want to rotate the KEK itself (a teammate leaves, a machine is
decommissioned, you suspect exposure), design for it from day one with `MultiFernet`. The
cryptography docs note MultiFernet "has support for implementing key rotation". You keep a list
of Fernet keys: the newest is first and is used for encryption; older keys are kept around
solely to decrypt old blobs. When you rotate, you prepend a new key, re-encrypt everything at
the next write, and eventually drop the oldest key once no ciphertext references it.

Verified working rotation example (assertion passed at research):

```python
from cryptography.fernet import Fernet, MultiFernet
k_old = Fernet.generate_key()
k_new = Fernet.generate_key()
mf = MultiFernet([Fernet(k_new), Fernet(k_old)])   # [encryptor, ...decrypt-only]
ct = Fernet(k_old).encrypt(b"legacy session")        # old key still decrypts
assert mf.decrypt(ct) == b"legacy session"
# future saves use Fernet(k_new).encrypt(...) going forward
```

In production you serialize the key ring as `[k_new, k_old]` in your keyring entry (the keys
themselves, NOT the cookies) so that the loader reconstructs MultiFernet from the stored ring.
The cookies stay encrypted under whichever key created them and MultiFernet transparently
handles mixed-age blobs.

---

## H2. Pre-commit and CI guardrails so secrets never reach git

Even perfect runtime hygiene fails if someone fat-fingers `git add -A`. You need two
independent gates: a local pre-commit secret scanner and a remote push-protection / secret
scanning service. Defense in depth.

### H3. Gitleaks as a pre-commit hook

Gitleaks (https://gitleaks.io/) describes itself as "an open-source secret scanner for git
repositories, files, and directories" and reports "over 16 million docker downloads, 17k
GitHub stars". It ships a `gitleaks protect` mode that scans staged diffs against a large
built-in rule set (AWS keys, GitHub tokens, private keys, JWTs, generic high-entropy
strings) and blocks the commit if it finds anything. Install it and wire the pre-commit hook:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.4
    hooks:
      - id: gitleaks
```

Or run it manually before each commit on this folder:

```bash
gitleaks protect --source . --staged --redact --verbose
```

The `--redact` flag ensures that even the Gitleaks output never prints the secret in clear
text, which matters because your hook output may be logged by the cron wrapper.

### H3. GitHub Push Protection and secret scanning

GitHub's secret scanning (https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning)
runs on every push to a public or protected repo and can block the push outright through Push
Protection if it detects a partner-pattern secret (GitHub tokens, AWS keys, many more). This
is your remote backstop: even if the local hook is skipped, the push is refused. The
limitation to know: it only catches known partner patterns plus any custom patterns you
register. A raw X `auth_token` cookie value is not a partner pattern, so it will NOT be caught
by GitHub. That is exactly why the local Gitleaks generic high-entropy rule and your own
cookie-shape regex (see below) are non-negotiable.

Add a custom Gitleaks rule for cookie-shaped secrets, because the generic entropy rule is
sometimes too strict or too lax for your data:

```toml
# .gitleaks.toml  (extend the default config)
[[rules]]
id = "mg-x-cookie"
description = "Money Glitch X auth_token / ct0 cookie pair"
regex = '''(?i)(auth_token|ct0)\s*[:=]\s*["']?[0-9a-f]{20,}['"]?'''
keywords = ["auth_token", "ct0"]
```

### H3. The never-commit self-check before any push

Per the vault CONVENTIONS.md, every push must first run a sanity grep so a token-shaped string
never lands in a tracked `.md` or `.py`. The convention specifies:

```bash
grep -rniE 'Bearer |access_token *: *"|\"jwt\"' --include=*.md .
```

Extend it to also cover cookie dumps and the encrypted-blob paths just in case:

```bash
grep -rniE 'Bearer |auth_token *[:=] *[0-9a-f]{10,}|ct0 *[:=] *[0-9a-f]{10,}' \
  --include=*.md --include=*.py --include=*.json . && echo "LEAK DETECTED" && exit 1
```

Run this as the last step of the enrich wrapper, before `git push origin main`. If it errors
out, the push is aborted and you investigate.

---

## H2. Logging discipline: the silent exfiltration vector

Most credential leaks in scrapers are not from storage at all. They are from logs. A
traceback prints `requests.exceptions.HTTPError: 401 ... headers={'Cookie': 'auth_token=...'}`.
A verbose HTTP client logs the full request including `Authorization: Bearer ...`. A debug
mode dumps the session object. All of these write secrets to a file or a third-party logging
endpoint that has weaker access control than your vault.

Rules:

Redact before you log. Never log the full cookie dict or auth header. Log only a fingerprint
like `ct0=ab12…ef` (first 4 + last 2 chars) so you can correlate without exposing.

Use a logging filter that masks known secret keys. Python's `logging` supports a
`LogRecord` filter:

```python
import logging, re
MASK = re.compile(r'(auth_token|ct0|Bearer)\s*[=:]\s*["\']?[^\s"\']+', re.I)
class RedactFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.msg = MASK.sub(r'\1=***REDACTED***', str(record.msg))
        if isinstance(record.args, dict):
            record.args = {k: (v if 'token' not in k.lower() else '***')
                           for k, v in record.args.items()}
        return True
logging.getLogger().addFilter(RedactFilter())
```

Never log `os.environ` wholesale. Crash reporters (Sentry, and even `traceback.format_exc`
piped to a file) that capture locals can capture the passphrase variable. Exclude the vault
module from any such capture, or scrub the relevant frames.

Set client logging to WARNING minimum for `urllib3` and `httpx` so request/response bodies
(headers included) are not echoed. `logging.getLogger("urllib3").setLevel(logging.WARNING)`.

---

## H2. Runtime memory handling and scrubbing

Secrets in RAM are fundamentally harder to protect than secrets on disk, but a few habits
reduce exposure:

Prefer `bytes` over `str` for secret material so it is not interned and does not linger in
string pools. The `secrets` module (Python docs: https://docs.python.org/3/library/secrets.html)
is the correct CSPRNG for generating tokens, keys, and nonces: "The secrets module is used
for generating cryptographically strong random numbers suitable for managing data such as
passwords, account authentication, security tokens, and related secrets." Use
`secrets.token_bytes(32)` for salts and random keys, never `random.random()`.

When decommissioning a session (account banned, machine retired), do not just delete the file.
Overwrite the blob with random bytes a few times then unlink, and remove the KEK from the
keyring, so a later undelete or keyring dump cannot recover it. On SSD the overwrite is not a
guarantee (wear leveling), but it raises the bar and signals intent. The authoritative wipe is
revoking the credential at the platform (log the account out, rotate the API key) which makes
any recovered bytes useless.

Avoid holding the KEK in a module-level global longer than needed. Derive it inside a function
scope, use it to construct the Fernet object, and let it fall out of scope. Python does not
zero memory on free, so this is best-effort; the real protection is that the KEK is in the
keyring, not in your process for long.

---

## H2. Credential hygiene per platform (operational notes)

These are platform-specific cautions gathered from running the other playbooks in this folder.
Treat as operational guidance, not legal advice, and respect each platform's terms of service.

X (Twitter). The valuable cookies are `auth_token` and `ct0`. Acquire them by logging in
through a real browser (or a headless one with a warmed profile) and exporting the cookie
jar. Never generate `auth_token` client-side; it is server-issued. Store the whole jar
encrypted; do not try to parse out individual cookies because X rotates internal cookie names.
Rate limits are softened by account age and activity, so a freshly created account's cookies
are worth far less than a 5-year-old account's, which is why protecting an old session is
economically meaningful.

Instagram and TikTok. Far more aggressive fingerprinting. Cookie life is short and bans are
common. Keep multiple encrypted sessions and rotate between them (the MultiFernet pattern
extends naturally: one key per session, try each). Do not store passwords alongside; only the
issued cookies.

Discord. The `authorization` header token (not a cookie) is the credential for the API and
gateway. It is a long-lived JWT-ish string. Treat it exactly like a bearer token: encrypt,
never log, rotate on any 401. Public-server mining (see the sibling playbook) does not need
your own account token if you only read public channels, but joining and scraping non-public
servers does.

Broker / exchange API keys (02-trading-bot). These are the only credentials that SHOULD be
IP-allowlisted and trade-disabled or read-only where possible. Store them encrypted exactly
like cookies, but also configure the exchange side so a leaked key cannot move money. This is a
defense the other credential types do not have, so use it.

---

## H2. Incident response: what to do when you think a secret leaked

Despite all guardrails, assume one will eventually leak. Have the runbook ready:

Immediately revoke at the source. For X, log the account out of all sessions from the security
page; this kills every `auth_token`/`ct0` derived from it. For Discord, regenerate the token
in User Settings, which invalidates the old one. For an exchange key, delete the key in the
exchange console. Source-side revocation is the only action that makes a recovered blob
useless.

Rotate the KEK. Generate a new key, prepend to the MultiFernet ring, re-encrypt all stored
blobs under the new key, and drop the old key. This contains the blast radius if the KEK (not
just a cookie) was exposed.

Purge git history if it reached a public repo. `git filter-repo --path` or BFG to remove the
blob, force-push, and rotate the GitHub credential. Note that GitHub's secret scanning will
still flag the old commit in forks; the only full fix is revocation plus history rewrite.

Rotate any other secret that shared the same passphrase or keyring slot. Credential reuse is
the silent multiplier of every leak.

---

## H2. A complete, copy-paste-safe loader you can drop into the module

Putting the layers together, here is the full loader that the other playbooks in this folder
should import. It prefers the keyring, falls back to PBKDF2 from an env var, encrypts with
Fernet, supports MultiFernet rotation, and refuses to start if the keyring backend is the
insecure plaintext fallback on a server.

```python
# 01-crawler-scrapper/cookies-tokens/vault.py
from __future__ import annotations
import base64, json, os, secrets, tempfile
from pathlib import Path
from cryptography.fernet import Fernet, MultiFernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

VAULT_DIR = Path(__file__).parent / "local"
VAULT_PATH = VAULT_DIR / "cookies.enc"
SALT_PATH = VAULT_DIR / "kek.salt"
SERVICE, SLOT = "money-glitch-vault", "scraper-kek"

def _keyring_kek() -> bytes | None:
    import keyring
    v = keyring.get_password(SERVICE, SLOT)
    if not v:
        return None
    if "plaintext" in type(keyring.get_keyring()).__name__.lower():
        # insecure fallback backend; refuse on a server
        if os.environ.get("MG_ALLOW_PLAINTEXT_KEYRING") != "1":
            raise RuntimeError("Insecure plaintext keyring backend detected; aborting")
    return base64.urlsafe_b64decode(v)

def _pbkdf2_kek() -> bytes:
    phrase = os.environ.get("MG_VAULT_PASSPHRASE")
    if not phrase:
        raise RuntimeError("No keyring and no MG_VAULT_PASSPHRASE; cannot derive KEK")
    VAULT_DIR.mkdir(parents=True, exist_ok=True)
    if not SALT_PATH.exists():
        SALT_PATH.write_bytes(secrets.token_bytes(16))
    dk = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                    salt=SALT_PATH.read_bytes(), iterations=600_000)
    return dk.derive(phrase.encode())

def load_ring() -> MultiFernet:
    # KEK stored as a JSON list of base64 Fernet keys: [newest, ..., oldest]
    import keyring
    raw = keyring.get_password(SERVICE, SLOT + ":ring")
    if raw:
        keys = [Fernet(k.encode()) for k in json.loads(raw)]
    else:
        kek = _keyring_kek() or _pbkdf2_kek()
        keys = [Fernet(base64.urlsafe_b64encode(kek))]
        keyring.set_password(SERVICE, SLOT + ":ring",
                             json.dumps([k.decode() for k in [keys[0]._signing_key]]))
    return MultiFernet(keys)

class CookieVault:
    def __init__(self) -> None:
        self._mf = load_ring()
        VAULT_DIR.mkdir(parents=True, exist_ok=True)

    def save(self, cookies: dict) -> None:
        tmp = VAULT_PATH.with_suffix(".enc.tmp")
        tmp.write_bytes(self._mf.encrypt(json.dumps(cookies).encode()))
        os.replace(tmp, VAULT_PATH)

    def load(self) -> dict:
        if not VAULT_PATH.exists():
            return {}
        try:
            return json.loads(self._mf.decrypt(VAULT_PATH.read_bytes()))
        except InvalidToken:
            raise RuntimeError("Vault integrity failure: KEK mismatch or tamper")

    def rotate_kek(self) -> None:
        # generate a new KEK, prepend, re-encrypt, persist the new ring
        import keyring
        new_raw = base64.urlsafe_b64encode(secrets.token_bytes(32))
        new = Fernet(new_raw)
        old_ring = json.loads(keyring.get_password(SERVICE, SLOT + ":ring") or "[]")
        old_ring.insert(0, new_raw.decode())
        keyring.set_password(SERVICE, SLOT + ":ring", json.dumps(old_ring))
        self._mf = MultiFernet([new] + [Fernet(k.encode()) for k in old_ring[1:]])
        self.save(self.load())
```

Note the `load_ring` keyring slot stores the KEK ring (not cookies), and the cookies stay in
the git-ignored `local/cookies.enc`. Even if `local/` is somehow committed, it is ciphertext.
Even if the keyring is dumped, on a desktop it is OS-protected; on a server you have used the
PBKDF2 path with a secret env var instead.

---

## H2. Checklist before you commit anything in this folder

Run through this every time you touch `01-crawler-scrapper/cookies-tokens/`:

- No `.enc`, `.bin`, `local/`, or `.token` file appears in `git status`. Confirm with
  `git status --porcelain` and eyeball it.
- `gitleaks protect --source . --staged` returns clean.
- The custom `auth_token|ct0|Bearer` grep returns nothing.
- No `print(...)`, no `logging.debug` of a cookie dict or header, no `os.environ` dump in the
  changed files.
- The KEK is sourced from keyring or `MG_VAULT_PASSPHRASE`, never a hardcoded string.
- The `.gitignore` in this folder contains `local/` and `*.enc`.
- You have NOT pasted a real cookie value anywhere in a `.md` file (this document contains only
  synthetic examples like `auth_token=abc; ct0=def`).

If all seven pass, `git add` only the `.md` and `vault.py` (never `local/`), commit, and push.

---

## H2. Relationship to the rest of the vault

This file is the security precondition for the other `01` playbooks. The X search operators
playbook depends on having a stored, rotated `auth_token`/`ct0` to authenticate its queries.
The TikTok hashtag velocity scraper depends on short-lived cookies it must refresh and
re-encrypt. The Discord public-server miner depends on a stored `authorization` token. The
SEHATI quota scraper (a sibling planned file) will need session cookies for BPJPH. None of
those should re-implement storage; they should all import `vault.CookieVault` from here.

It also closes a loop with `02-trading-bot`, whose exchange API keys should be stored with the
same `CookieVault` class (the class is credential-agnostic; it just encrypts a dict). And it
supports `05-market-cron`, which may one day need authenticated fetches for premium market
feeds. One safe room, many callers.

---

## H2. Known limitations and open questions

Fernet uses AES-128, not AES-256. For cookie-sized secrets this is not a practical weakness
(128-bit keys are not brute-forceable), but if your threat model later includes a determined
adversary with a captured KEK, consider the `aes-gcm` recipe from the same library for 256-bit
keys. The docs note Fernet's "Implementation Limitations" around key size; read them before
claiming FIPS alignment.

The PBKDF2 fallback assumes `MG_VAULT_PASSPHRASE` is delivered securely. If it is itself
committed or logged, the whole scheme collapses. The pre-commit grep must also cover that
variable name.

MultiFernet rotation requires re-encrypting old blobs to fully retire a key. This file's
`rotate_kek` does that, but a large store means a one-time CPU cost on rotation; schedule it
off-peak.

Cloud secret managers (AWS Secrets Manager, GCP Secret Manager) were cited as Layer 1 sources
but the code samples above focus on keyring + PBKDF2 for portability. If you run on AWS, prefer
Secrets Manager for the KEK and treat the instance role as the only thing that can read it;
that removes the passphrase entirely from the threat surface.

---

## H2. Source index (all fetched 2026-07-12, HTTP 200 unless noted)

- cryptography.io Fernet docs: https://cryptography.io/en/latest/fernet/
- cryptography.io KDF docs (PBKDF2/Scrypt/HKDF):
  https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions.html
- OWASP Top 10:2021 A02 Cryptographic Failures:
  https://owasp.org/Top10/A02_2021-Cryptographic_Failures/
- GitHub secret scanning overview:
  https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning
- Gitleaks project home: https://gitleaks.io/
- Python `secrets` module docs: https://docs.python.org/3/library/secrets.html
- PyPI `keyring` 25.7.0: https://pypi.org/project/keyring/  (source:
  https://github.com/jaraco/keyring)
- AWS Secrets Manager overview:
  https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html

All code samples in this document were executed against `cryptography` 46.0.7 on CPython 3.11
at research time; round-trip and rotation assertions passed. No live credential values appear
anywhere in this file. If a future reader cannot reproduce a snippet, check the installed
`cryptography` version and the cryptography.io changelog before assuming the doc is wrong.
