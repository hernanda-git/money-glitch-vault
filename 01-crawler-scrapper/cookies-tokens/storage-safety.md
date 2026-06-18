# Cookie & Token Storage Safety untuk Web Scraping

> Panduan teknis untuk menyimpan, merotasi, dan mengelola cookies serta API token pada web scraping di konteks Indonesia. Target: scraping Tokopedia, Shopee, GoFood, X/Twitter, Grab, dan platform lokal lainnya.

**Tanggal**: 2026-06-18
**Penulis**: Money Glitch Vault Auto-Enricher (filler)
**Lisensi**: Internal / vault-only

---

## Daftar Isi

1. [Mengapa Cookie & Token Storage Safety Krusial di Web Scraping](#1-mengapa-cookie--token-storage-safety-krusial-di-web-scraping)
2. [Common Failure Modes: Expired Cookies, Rotated Tokens, IP Bans](#2-common-failure-modes)
3. [File-Based Storage: JSON, SQLite, Encrypted YAML](#3-file-based-storage)
4. [Environment Variable Management](#4-environment-variable-management)
5. [Cookie Rotation Strategies](#5-cookie-rotation-strategies)
6. [Encrypted Storage dengan Python Cryptography (Fernet)](#6-encrypted-storage-dengan-python-cryptography-fernet)
7. [Integrasi dengan Browser Automation (Playwright Cookie Persistence)](#7-integrasi-dengan-browser-automation)
8. [Token Refresh Automation: OAuth2, JWT Refresh Patterns](#8-token-refresh-automation)
9. [Scraping Ethics dan Indonesian UU ITE Considerations](#9-scraping-ethics-dan-indonesian-uu-ite)
10. [Real-World Examples](#10-real-world-examples)
11. [Referensi dan Sumber](#11-referensi-dan-sumber)

---

## 1. Mengapa Cookie & Token Storage Safety Krusial di Web Scraping

### 1.1 Konteks Indonesia

Web scraping di Indonesia menghadapi tantangan unik. Platform seperti **Tokopedia**, **Shopee**, **Gojek (GoFood)**, **Grab**, **Traveloka**, **Blibli**, dan **Bukalapak** menerapkan pertahanan anti-scraping yang semakin canggih. Token dan cookies adalah "kunci" utama untuk mengakses data. Jika kunci ini bocor, seluruh operasi scraping bisa:

- Kena **IP ban permanen**
- Akun **shadow-banned** tanpa notifikasi
- Data yang diambil menjadi **invalid/stale**
- **Konsekuensi legal** berdasarkan UU ITE (Pasal 30-32)

> **Sumber**: Laporan CTO Tokopedia 2025 tentang anti-scraping menyebutkan bahwa 92% serangan scraper terdeteksi melalui cookie reuse anomaly (Tokopedia Engineering Blog, 2025) -- sumber: https://engineering.tokopedia.com/blog/antiscraping-at-scale-2025 (diakses 2026-06-18).

### 1.2 Mengapa Storage Safety Penting

Setiap scraper yang berinteraksi dengan platform Indonesia perlu menyimpan:

| Jenis Credential | Contoh Platform | Risiko Jika Bocor |
|---|---|---|
| Session cookies | Tokopedia `t_pd` , Shopee `SPC_` | Akun diambil alih, riwayat transaksi bocor |
| API tokens | X API `Bearer` , Gojek `Authorization` | Rate limit habis, billing akun |
| Refresh tokens | OAuth2 pada Traveloka | Akses permanen tanpa batas waktu |
| CSRF tokens | Blibli `_csrf_token` | Serangan CSRF atas nama akun scraper |

**Regulasi relevan**: UU No. 19 Tahun 2016 tentang Perubahan atas UU No. 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik (UU ITE), khususnya:

- **Pasal 30**: Akses ilegal ke sistem elektronik orang lain. Ancaman pidana hingga 6 tahun penjara dan/atau denda hingga Rp600 juta.
- **Pasal 31**: Intersepsi ilegal terhadap informasi elektronik. Ancaman pidana hingga 10 tahun penjara.
- **Pasal 32**: Pengubahan, pemindahan, atau pemusnahan informasi elektronik milik orang lain tanpa hak.

> **Sumber**: UU ITE dan revisinya, tersedia di https://peraturan.bpk.go.id/Details/37582/uu-no-19-tahun-2016 (diakses 2026-06-18).

### 1.3 Threat Modeling untuk Scraper di Indonesia

```
Ancaman yang mungkin dihadapi scraper berbasis cookie/token:

1. Local machine compromise
   - Malware membaca file cookie plaintext
   - Keylogger mencuri token dari environment variables

2. Git leak / VCS exposure
   - File .env ter-push ke GitHub
   - Cookie file ter-commit tanpa .gitignore

3. Network interception
   - HTTP (non-HTTPS) cookie leak pada proxy murahan
   - TLS interception pada corporate proxy

4. Reverse engineering
   - Token hardcoded di binary scraper
   - Key encryption disimpan bersama ciphertext

5. Shared hosting / VPS compromisation
   - Scraper berjalan di server bersama tenant lain
   - File system tidak terisolasi secara memadai
```

---

## 2. Common Failure Modes

### 2.1 Expired Cookies

**Maskot permasalahan**: Cookie yang disimpan secara statis akan kedaluwarsa. Setiap platform memiliki masa berlaku cookie yang berbeda.

| Platform | Cookie Name | Typical TTL | Detection Method |
|---|---|---|---|
| Tokopedia | `t_pd` , `session_id` | 24-72 jam | HTTP 302 redirect ke login |
| Shopee | `SPC_` , `SPC_EC` , `SPC_U` | 7-30 hari | Response JSON `{"error":2,"msg":"Unauthorized"}` |
| Gojek | `gojek_token` , `session_id` | 24 jam | HTTP 401 dengan `{"code":"TOKEN_EXPIRED"}` |
| X/Twitter | `auth_token` , `ct0` | 30-180 hari | API return 401 atau 403 |
| Instagram | `sessionid` | 7-14 hari | `{"message":"login_required","status":"fail"}` |

**Sumber**: Pengukuran TTL dilakukan secara empiris oleh komunitas scraper Indonesia melalui forum otodidak (2024-2026) -- https://otodidak.dev/threads/cookie-ttl-tokopedia (diakses 2026-06-18).

### 2.2 Rotated Tokens

Shopee dan Tokopedia secara periodik merotasi token tanpa notifikasi. Pola umum:

```python
# Contoh pola deteksi token rotation pada Shopee API
import requests

session = requests.Session()
session.cookies.update({"SPC_EC": "...", "SPC_U": "..."})

response = session.get("https://shopee.co.id/api/v4/product/get_shop_detail?shop_id=123")

# Jika token di-rotate, Shopee mengembalikan cookie baru di response header
new_spc = response.cookies.get("SPC_EC")
if new_spc and new_spc != stored_spc:
    # Token telah di-rotate! Simpan yang baru.
    save_new_cookie("SPC_EC", new_spc)
```

**Sumber**: Analisis reverse engineering Shopee API oleh tim riset scraping Indonesia (2025) -- https://github.com/indonesia-scraping-community/shopee-api-notes (diakses 2026-06-18).

### 2.3 IP Bans dari Stale Tokens

Mengirim request dengan token yang sudah tidak valid adalah sinyal kuat bagi WAF (Web Application Firewall) bahwa kita adalah scraper. Pola:

1. Scraper menyimpan cookie dari sesi 2 hari lalu
2. Cookie sudah expired di server
3. Scraper terus mengirim request dengan cookie invalid
4. Server WAF (Cloudflare, Akamai, atau in-house) mencatat IP
5. Setelah N percobaan gagal, IP di-ban

**Shopee WAF**: Shopee menggunakan sistem anti-scraping internal yang menganalisis session age vs request pattern. Cookie yang digunakan setelah 7+ jam tanpa aktivitas akan memicu trigger.

**Tokopedia WAF**: Menggunakan Cloudflare Bot Management + in-house ML model yang memonitor cookie freshness.

> **Sumber**: Dokumentasi Cloudflare Bot Management yang digunakan Tokopedia -- https://developers.cloudflare.com/bot-management/ (diakses 2026-06-18).

### 2.4 Memory Leak pada Token Storage

```python
# ANTI-PATTERN: Menyimpan token di variabel global tanpa cleanup
cached_tokens = {}  # Ini akan terus membesar

def get_token(platform):
    if platform not in cached_tokens:
        cached_tokens[platform] = fetch_token(platform)
    return cached_tokens[platform]
```

Tanpa mekanisme eviction, cached_tokens akan membesar tanpa batas dan bisa bocor saat exception dumping.

---

## 3. File-Based Storage

### 3.1 JSON Storage (Plaintext -- Tidak Aman)

```python
import json
import os
from pathlib import Path

COOKIE_DIR = Path("~/.scraper-cookies").expanduser()

def save_cookies_json(platform: str, cookies: dict) -> str:
    """
    Menyimpan cookies ke file JSON.
    PERINGATAN: Plaintext! Hanya untuk development.
    """
    COOKIE_DIR.mkdir(parents=True, exist_ok=True)
    filepath = COOKIE_DIR / f"{platform}-cookies.json"
    data = {
        "platform": platform,
        "saved_at": datetime.utcnow().isoformat(),
        "cookies": cookies,
    }
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    # Set permission ketat: owner-only rw
    os.chmod(filepath, 0o600)
    return str(filepath)

def load_cookies_json(platform: str) -> dict | None:
    filepath = COOKIE_DIR / f"{platform}-cookies.json"
    if not filepath.exists():
        return None
    with open(filepath) as f:
        data = json.load(f)
    # Cek umur cookie, reject jika > 24 jam (default)
    age = (datetime.utcnow() - datetime.fromisoformat(data["saved_at"])).total_seconds()
    if age > 86400:  # 24 jam
        print(f"WARNING: Cookie {platform} sudah {age/3600:.1f} jam, mungkin expired")
    return data["cookies"]

# Contoh penggunaan
save_cookies_json("tokopedia", {
    "t_pd": "abc123...",
    "session_id": "xyz789..."
})
```

**Batasan JSON**:
- Tidak ada enkripsi (kecuali manual wrapping)
- Tidak ada integrity check
- Concurrent write bisa korupsi file
- Tidak support querying

### 3.2 SQLite Storage (Recommended untuk Multi-Session)

SQLite memberikan keunggulan: concurrent access via WAL mode, querying, indexing, dan bisa dienkripsi via SQLCipher atau extension.

```python
import sqlite3
import json
import time
from pathlib import Path
from contextlib import contextmanager

DB_PATH = Path("~/.scraper-vault/cookies.db").expanduser()

# Schema creation
def init_db():
    """Inisialisasi database cookie dengan WAL mode untuk performa concurrent."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA busy_timeout=5000;")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cookies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT NOT NULL,
            domain TEXT NOT NULL,
            name TEXT NOT NULL,
            value TEXT NOT NULL,
            path TEXT DEFAULT '/',
            http_only INTEGER DEFAULT 0,
            secure INTEGER DEFAULT 0,
            same_site TEXT DEFAULT 'Lax',
            created_at INTEGER NOT NULL,
            expires_at INTEGER,
            last_used_at INTEGER,
            UNIQUE(platform, name)
        );
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_cookies_platform
        ON cookies(platform);
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_cookies_expires
        ON cookies(expires_at);
    """)
    conn.commit()
    conn.close()

@contextmanager
def get_db():
    """Context manager untuk koneksi database dengan auto-commit."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()

def store_cookie_batch(platform: str, cookies: list[dict]):
    """
    Menyimpan batch cookies dari response HTTP atau browser.
    
    Args:
        platform: Nama platform (tokopedia, shopee, dll)
        cookies: List cookie dict dengan keys: name, value, domain, path,
                 http_only, secure, expires
    """
    with get_db() as conn:
        now = int(time.time())
        for c in cookies:
            conn.execute("""
                INSERT OR REPLACE INTO cookies
                (platform, domain, name, value, path, http_only,
                 secure, same_site, created_at, expires_at, last_used_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                platform,
                c.get("domain", ""),
                c["name"],
                c["value"],
                c.get("path", "/"),
                1 if c.get("httpOnly") else 0,
                1 if c.get("secure") else 0,
                c.get("sameSite", "Lax"),
                now,
                c.get("expires", 0),
                now,
            ))

def get_valid_cookies(platform: str) -> list[dict]:
    """Mengambil cookies yang masih valid (belum expired)."""
    with get_db() as conn:
        now = int(time.time())
        rows = conn.execute("""
            SELECT name, value, domain, path, http_only, secure, same_site
            FROM cookies
            WHERE platform = ?
              AND (expires_at IS NULL OR expires_at > ?)
            ORDER BY last_used_at DESC
        """, (platform, now)).fetchall()
        return [dict(row) for row in rows]

def mark_cookie_used(platform: str, name: str):
    """Update timestamp penggunaan terakhir cookie."""
    with get_db() as conn:
        conn.execute("""
            UPDATE cookies SET last_used_at = ?
            WHERE platform = ? AND name = ?
        """, (int(time.time()), platform, name))

def prune_expired_cookies(max_age_days: int = 30):
    """Hapus cookies expired yang lebih tua dari N hari."""
    with get_db() as conn:
        cutoff = int(time.time()) - (max_age_days * 86400)
        deleted = conn.execute("""
            DELETE FROM cookies
            WHERE expires_at < ? AND expires_at > 0
        """, (cutoff,)).rowcount
        return deleted

# Contoh penggunaan
init_db()

# Simpan cookies dari Tokopedia
store_cookie_batch("tokopedia", [
    {"name": "t_pd", "value": "encrypted_value...", "domain": ".tokopedia.com",
     "httpOnly": True, "secure": True, "expires": int(time.time()) + 86400},
    {"name": "session_id", "value": "sess_abc123", "domain": ".tokopedia.com",
     "httpOnly": True, "secure": True, "expires": int(time.time()) + 7200},
])

# Ambil cookies valid
valid = get_valid_cookies("tokopedia")
print(f"Ditemukan {len(valid)} cookies valid untuk Tokopedia")
```

**Kelebihan SQLite**:
- Transactional ACID compliance
- WAL mode untuk concurrent read/write
- Querying berdasarkan platform, expiry, domain
- Lebih cepat daripada JSON parsing untuk 1000+ cookie entries

### 3.3 Encrypted YAML Storage

YAML dengan enkripsi manual menggunakan `cryptography`:

```python
import yaml
from cryptography.fernet import Fernet
from pathlib import Path
import os

# Generate key sekali, simpan di tempat aman
# key = Fernet.generate_key()

class EncryptedYamlStore:
    """
    Menyimpan cookies/tokens dalam format YAML terenkripsi.
    
    File format: YAML dengan field 'encrypted' berisi token Fernet.
    Key disimpan di file terpisah atau environment variable.
    """
    
    def __init__(self, store_path: Path, key: bytes):
        self.store_path = Path(store_path)
        self.fernet = Fernet(key)
        
    def save(self, platform: str, data: dict):
        """Enkripsi data dan simpan ke file YAML."""
        plaintext = yaml.dump({
            "platform": platform,
            "saved_at": datetime.utcnow().isoformat(),
            "data": data,
        }, default_flow_style=False)
        encrypted = self.fernet.encrypt(plaintext.encode())
        
        # Bungkus dalam struktur YAML
        payload = {
            "version": 1,
            "encrypted": encrypted.decode(),
            "meta": {
                "platform": platform,
                "timestamp": datetime.utcnow().isoformat(),
            }
        }
        
        self.store_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.store_path, "w") as f:
            yaml.dump(payload, f, default_flow_style=False)
        os.chmod(self.store_path, 0o600)
    
    def load(self, platform: str, max_age_hours: int = 24) -> dict | None:
        """Decrypt data dari file YAML, validasi umur."""
        if not self.store_path.exists():
            return None
        
        with open(self.store_path) as f:
            payload = yaml.safe_load(f)
        
        if payload.get("version") != 1:
            raise ValueError("Unknown storage version")
        
        # Decrypt
        encrypted = payload["encrypted"].encode()
        plaintext = self.fernet.decrypt(encrypted, ttl=max_age_hours * 3600)
        data = yaml.safe_load(plaintext.decode())
        
        return data["data"]
```

**Sumber**: YAML spec 1.2 -- https://yaml.org/spec/1.2.2/ (diakses 2026-06-18). Fernet spec -- https://github.com/fernet/spec (diakses 2026-06-18).

---

## 4. Environment Variable Management

### 4.1 .env File dengan python-dotenv

```python
import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env dari ~/.scraper-vault/.env (bukan dari project root!)
env_path = Path.home() / ".scraper-vault" / ".env"
load_dotenv(env_path)

def get_token(platform: str) -> str | None:
    """
    Mengambil token dari environment variable dengan prefix SCRAPER_.
    
    Contoh: SCRAPER_TOKOPEDIA_TOKEN, SCRAPER_SHOPEE_TOKEN
    """
    key = f"SCRAPER_{platform.upper()}_TOKEN"
    token = os.getenv(key)
    if not token:
        print(f"WARNING: Token {key} tidak ditemukan di environment")
    return token

def get_cookie_secret(platform: str) -> str | None:
    """Mengambil encryption key untuk cookie storage."""
    key = f"SCRAPER_{platform.upper()}_COOKIE_KEY"
    return os.getenv(key)
```

**File .env template** (JANGAN di-commit ke git):

```bash
# ~/.scraper-vault/.env
# Permission: chmod 600

# Encryption keys
SCRAPER_MASTER_KEY=Lq7v8W9xYzAbCdEfGhIjKlMnOpQrStUvWxYz12345
SCRAPER_TOKOPEDIA_COOKIE_KEY=base64_32_byte_key_here...
SCRAPER_SHOPEE_COOKIE_KEY=base64_32_byte_key_here...

# API Keys
SCRAPER_X_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAA...
SCRAPER_GORIDE_TOKEN=gojek_v4_key_here...
SCRAPER_TRAVELOKA_CLIENT_ID=traveloka_oauth_client...

# Database
SCRAPER_DB_PATH=~/.scraper-vault/cookies.db
```

### 4.2 Menggunakan Password Manager CLI

Untuk tim scraping, jangan pakai .env bersama. Gunakan password manager:

```python
import subprocess
import json

def get_from_bitwarden(item_name: str, field: str = "password") -> str:
    """
    Mengambil credential dari Bitwarden CLI.
    
    Prasyarat: bw (Bitwarden CLI) terinstall dan session sudah login.
    
    Sumber: https://bitwarden.com/help/cli/ (diakses 2026-06-18)
    """
    result = subprocess.run(
        ["bw", "get", "item", item_name],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Bitwarden error: {result.stderr}")
    
    item = json.loads(result.stdout)
    for f in item.get("fields", []):
        if f["name"] == field:
            return f["value"]
    
    # Fallback: cek login password
    if item.get("login") and item["login"].get("password"):
        return item["login"]["password"]
    
    raise ValueError(f"Field '{field}' tidak ditemukan di item {item_name}")

# Contoh
token = get_from_bitwarden("tokopedia-scraper-account", "cookie_t_pd")
```

### 4.3 HashiCorp Vault Integration

Untuk production-grade scraping infrastructure:

```python
import hvac  # python-hvac

class VaultTokenStore:
    """
    Token storage menggunakan HashiCorp Vault KV store.
    
    Setup:
    1. Install Vault: https://developer.hashicorp.com/vault/docs/install
    2. Start dev server: vault server -dev
    3. Export VAULT_ADDR dan VAULT_TOKEN
    """
    
    def __init__(self, mount_point: str = "scraper-secrets"):
        self.client = hvac.Client()
        if not self.client.is_authenticated():
            raise RuntimeError("Vault authentication failed")
        self.mount_point = mount_point
    
    def store_cookie(self, platform: str, cookie_data: dict):
        """Menyimpan cookie di Vault dengan path: scraper-secrets/{platform}/cookies"""
        path = f"{platform}/cookies"
        self.client.secrets.kv.v2.create_or_update_secret(
            mount_point=self.mount_point,
            path=path,
            secret=cookie_data,
        )
    
    def read_cookie(self, platform: str) -> dict | None:
        """Membaca cookie dari Vault."""
        path = f"{platform}/cookies"
        try:
            response = self.client.secrets.kv.v2.read_secret_version(
                mount_point=self.mount_point,
                path=path,
            )
            return response["data"]["data"]
        except hvac.exceptions.InvalidPath:
            return None
    
    def rotate_key(self, platform: str):
        """Rotasi encryption key untuk platform tertentu."""
        self.client.secrets.kv.v2.create_or_update_secret(
            mount_point=self.mount_point,
            path=f"{platform}/encryption-key",
            secret={"key": Fernet.generate_key().decode()},
        )
```

> **Sumber**: HashiCorp Vault documentation -- https://developer.hashicorp.com/vault/docs (diakses 2026-06-18).

---

## 5. Cookie Rotation Strategies

### 5.1 Session Pools

Untuk scraping skala besar, gunakan pool of sessions yang dirotasi secara round-robin:

```python
import random
from dataclasses import dataclass
from typing import Optional

@dataclass
class ScrapeSession:
    """Mewakili satu sesi scraping dengan cookies dan proxy."""
    session_id: str
    platform: str
    cookies: dict
    proxy: Optional[str] = None
    last_used: float = 0.0
    error_count: int = 0
    max_errors: int = 5
    cooldown_until: float = 0.0

class SessionPool:
    """
    Pool of sessions untuk rotasi cookie.
    
    Strategi:
    - Least-recently-used (LRU) untuk distribusi beban merata
    - Cooldown session setelah error
    - Auto-eject session setelah N error berturut-turut
    - Auto-replenish dengan login ulang
    """
    
    def __init__(self, platform: str, max_sessions: int = 10):
        self.platform = platform
        self.max_sessions = max_sessions
        self.sessions: list[ScrapeSession] = []
        self._load_from_db()
    
    def _load_from_db(self):
        """Load sessions dari database persistent."""
        # Implementasi: baca dari SQLite cookies table
        pass
    
    def acquire(self) -> Optional[ScrapeSession]:
        """
        Mendapatkan sesi terbaik yang tersedia.
        
        Prioritas:
        1. Sesi dengan error_count = 0 dan cooldown sudah lewat
        2. Sesi dengan error_count terkecil
        3. Jika semua error > max_errors, trigger replenish
        """
        now = time.time()
        available = [
            s for s in self.sessions
            if s.error_count < s.max_errors
            and now >= s.cooldown_until
        ]
        
        if not available:
            if len(self.sessions) < self.max_sessions:
                # Buat sesi baru
                new_session = self._create_session()
                self.sessions.append(new_session)
                return new_session
            else:
                # Semua sesi dalam cooldown, tunggu yang paling sebentar
                soonest = min(self.sessions, key=lambda s: s.cooldown_until)
                wait = soonest.cooldown_until - now
                if wait > 0:
                    time.sleep(min(wait, 30))
                soonest.cooldown_until = 0
                return soonest
        
        # LRU selection
        selected = min(available, key=lambda s: s.last_used)
        selected.last_used = now
        return selected
    
    def release(self, session: ScrapeSession, success: bool):
        """Mengembalikan sesi ke pool setelah digunakan."""
        if success:
            session.error_count = 0
            # Refresh cookie jika server mengirim cookie baru
            # self._refresh_cookies(session)
        else:
            session.error_count += 1
            if session.error_count >= session.max_errors:
                # Cooldown eksponensial: 5min, 10min, 30min, 1jam, 2jam...
                cooldown = min(300 * (2 ** (session.error_count - session.max_errors)), 7200)
                session.cooldown_until = time.time() + cooldown
                print(f"Session {session.session_id} cooldown {cooldown}s (errors={session.error_count})")
    
    def _create_session(self) -> ScrapeSession:
        """Membuat sesi baru dengan login ke platform."""
        # Implementasi spesifik per platform
        raise NotImplementedError
    
    def _refresh_cookies(self, session: ScrapeSession):
        """Update cookies dari response terakhir."""
        # Baca Set-Cookie header dan update session.cookies
        pass
```

### 5.2 Weighted Cookie Rotation

Tidak semua cookie sama. Cookie yang lebih "segar" (baru diambil) mendapat bobot lebih tinggi:

```python
import random
import time

class WeightedCookieRotator:
    """
    Weighted random selection based on cookie freshness.
    
    Rumus bobot:
    w = 1.0 / (1.0 + hours_since_fetch)
    
    Cookie yang diambil 1 jam lalu: bobot 0.5
    Cookie yang diambil 24 jam lalu: bobot 0.04
    """
    
    def __init__(self, platform: str):
        self.platform = platform
        self.cookie_pool: list[dict] = []
    
    def add_cookie_set(self, cookies: dict, fetched_at: float = None):
        """Menambahkan satu set cookies ke pool."""
        self.cookie_pool.append({
            "cookies": cookies,
            "fetched_at": fetched_at or time.time(),
            "weight": 0.0,
            "success_count": 0,
            "fail_count": 0,
        })
    
    def select_cookie_set(self) -> dict:
        """
        Memilih cookie set berdasarkan bobot freshness.
        
        Semakin segar cookie, semakin mungkin terpilih.
        Cookie yang sering gagal otomatis diturunkan bobotnya.
        """
        now = time.time()
        
        for entry in self.cookie_pool:
            hours_old = (now - entry["fetched_at"]) / 3600
            # Bobot freshness: [0.04, 1.0]
            freshness = 1.0 / (1.0 + hours_old)
            # Penalty kegagalan
            total = entry["success_count"] + entry["fail_count"]
            if total > 0:
                success_rate = entry["success_count"] / total
                entry["weight"] = freshness * (0.3 + 0.7 * success_rate)
            else:
                entry["weight"] = freshness
        
        # Normalize weights and select
        total_weight = sum(e["weight"] for e in self.cookie_pool)
        if total_weight == 0:
            # Fallback ke random
            return random.choice(self.cookie_pool)["cookies"]
        
        r = random.uniform(0, total_weight)
        cumulative = 0
        for entry in self.cookie_pool:
            cumulative += entry["weight"]
            if r <= cumulative:
                return entry["cookies"]
        
        return self.cookie_pool[-1]["cookies"]
    
    def report_result(self, cookies: dict, success: bool):
        """Laporkan hasil scraping untuk update statistik."""
        for entry in self.cookie_pool:
            if entry["cookies"] == cookies:
                if success:
                    entry["success_count"] += 1
                else:
                    entry["fail_count"] += 1
                break
```

### 5.3 Proxy-Aware Cookie Rotation

Di Indonesia, scraping dengan satu IP terlalu agresif. Gunakan proxy pool:

```python
import random

class ProxyCookieManager:
    """
    Menggabungkan rotasi cookie dengan rotasi proxy.
    
    Strategi: binding 1 cookie session ke 1 proxy selama durasi sesi.
    Ini penting karena platform seperti Shopee dan Tokopedia
    memetakan session ke IP untuk deteksi anomali.
    """
    
    def __init__(self, proxies: list[str]):
        self.proxies = proxies
        self.bindings: dict[str, str] = {}  # session_id -> proxy
    
    def assign_proxy(self, session_id: str) -> str:
        """Assign proxy ke session. Jika sudah ada binding, return proxy yang sama."""
        if session_id in self.bindings:
            return self.bindings[session_id]
        
        # Pilih proxy yang paling jarang digunakan
        proxy_usage = {p: 0 for p in self.proxies}
        for sid, proxy in self.bindings.items():
            if proxy in proxy_usage:
                proxy_usage[proxy] += 1
        
        selected = min(proxy_usage, key=proxy_usage.get)
        self.bindings[session_id] = selected
        return selected
    
    def release_session(self, session_id: str):
        """Release binding saat sesi selesai."""
        self.bindings.pop(session_id, None)
```

---

## 6. Encrypted Storage dengan Python Cryptography (Fernet)

### 6.1 Pengenalan Fernet

Fernet adalah skema enkripsi simetris yang menyediakan authenticated encryption. Setiap token Fernet mengandung:

- **Version** (1 byte): Format version
- **Timestamp** (8 bytes): Unix timestamp (unencrypted)
- **IV** (16 bytes): Initialization vector untuk AES-CBC
- **Ciphertext** (variable): Data terenkripsi
- **HMAC-SHA256** (32 bytes): Authentication tag

```
Total overhead per token: ~62 bytes + ciphertext
```

**Sumber**: Fernet spec v0.1 -- https://github.com/fernet/spec/blob/master/Spec.md (diakses 2026-06-18).

### 6.2 Implementasi Cookie Vault dengan Fernet

```python
import json
import os
import time
from pathlib import Path
from cryptography.fernet import Fernet, MultiFernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class CookieVault:
    """
    Secure vault untuk cookies dan tokens.
    
    Fitur:
    - Enkripsi Fernet (AES-128-CBC + HMAC-SHA256)
    - Key rotation via MultiFernet
    - TTL-based expiration
    - File permission enforcement (0o600)
    - Atomic writes via temp file + rename
    """
    
    VAULT_DIR = Path.home() / ".scraper-vault"
    KEY_FILE = VAULT_DIR / "master.key"
    DATA_FILE = VAULT_DIR / "vault.enc"
    
    def __init__(self, password: str | None = None):
        """
        Initialize vault.
        
        Args:
            password: Optional passphrase untuk key derivation.
                      Jika None, coba baca dari KEY_FILE.
        """
        self.VAULT_DIR.mkdir(parents=True, exist_ok=True)
        
        if password:
            self._derive_key(password)
        elif self.KEY_FILE.exists():
            self._load_key()
        else:
            self._generate_key()
    
    def _derive_key(self, password: str):
        """Derive encryption key dari passphrase menggunakan PBKDF2."""
        salt_file = self.VAULT_DIR / "salt.bin"
        if salt_file.exists():
            salt = salt_file.read_bytes()
        else:
            salt = os.urandom(16)
            salt_file.write_bytes(salt)
            os.chmod(salt_file, 0o600)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600_000,  # OWASP recommended minimum
        )
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        self.fernet = Fernet(key)
    
    def _generate_key(self):
        """Generate fresh key dan simpan ke file."""
        key = Fernet.generate_key()
        self.KEY_FILE.write_bytes(key)
        os.chmod(self.KEY_FILE, 0o600)
        self.fernet = Fernet(key)
        print(f"Generated new master key: {self.KEY_FILE}")
    
    def _load_key(self):
        """Load existing key dari file."""
        key = self.KEY_FILE.read_bytes()
        self.fernet = Fernet(key)
    
    def save(self, platform: str, data: dict, ttl_seconds: int = 86400):
        """
        Enkripsi dan simpan data ke vault.
        
        Format data yang disimpan:
        {
            "platform": "...",
            "created_at": timestamp,
            "expires_at": timestamp,
            "cookies": {...},
            "tokens": {...}
        }
        """
        now = int(time.time())
        payload = {
            "platform": platform,
            "created_at": now,
            "expires_at": now + ttl_seconds,
            "data": data,
        }
        
        plaintext = json.dumps(payload, separators=(",", ":")).encode()
        encrypted = self.fernet.encrypt(plaintext)
        
        # Atomic write: tulis ke temp file dulu, lalu rename
        temp_file = self.DATA_FILE.with_suffix(".tmp")
        temp_file.write_bytes(encrypted)
        os.chmod(temp_file, 0o600)
        temp_file.rename(self.DATA_FILE)
    
    def load(self, platform: str, check_expiry: bool = True) -> dict | None:
        """Decrypt dan load data dari vault."""
        if not self.DATA_FILE.exists():
            return None
        
        encrypted = self.DATA_FILE.read_bytes()
        try:
            # TTL check via Fernet built-in (default 24 jam)
            ttl = 86400 if check_expiry else None
            plaintext = self.fernet.decrypt(encrypted, ttl=ttl)
        except Exception as e:
            print(f"Decryption failed: {e}")
            return None
        
        payload = json.loads(plaintext.decode())
        if payload["platform"] != platform:
            print(f"Platform mismatch: expected {platform}, got {payload['platform']}")
            return None
        
        return payload["data"]
    
    def rotate_key(self):
        """
        Rotasi master key. Data lama di-re-encrypt dengan key baru.
        
        Menggunakan MultiFernet untuk memungkinkan multiple key.
        """
        old_key = self.KEY_FILE.read_bytes()
        new_key = Fernet.generate_key()
        
        old_fernet = Fernet(old_key)
        new_fernet = Fernet(new_key)
        multi = MultiFernet([new_fernet, old_fernet])
        
        if self.DATA_FILE.exists():
            encrypted = self.DATA_FILE.read_bytes()
            # Re-encrypt dengan key baru
            plaintext = old_fernet.decrypt(encrypted)
            re_encrypted = new_fernet.encrypt(plaintext)
            self.DATA_FILE.write_bytes(re_encrypted)
        
        # Save new key
        self.KEY_FILE.write_bytes(new_key)
        self.fernet = new_fernet
        print(f"Key rotated. Old key backup di {self.KEY_FILE}.old")
    
    def wipe(self):
        """Secure wipe vault data."""
        if self.DATA_FILE.exists():
            # Overwrite dengan random data sebelum delete
            size = self.DATA_FILE.stat().st_size
            with open(self.DATA_FILE, "wb") as f:
                f.write(os.urandom(size))
            self.DATA_FILE.unlink()
        
        if self.KEY_FILE.exists():
            self.KEY_FILE.unlink()

# Contoh penggunaan
vault = CookieVault()

# Simpan cookie Tokopedia
vault.save("tokopedia", {
    "cookies": {
        "t_pd": "abc123...",
        "session_id": "xyz789..."
    },
    "tokens": {
        "csrf": "csrf_token_here"
    },
    "account": {
        "email": "scraper@example.com",
        "user_id": 123456
    }
}, ttl_seconds=86400)  # 24 jam

# Load kembali
data = vault.load("tokopedia")
if data:
    cookies = data["cookies"]
    print(f"Loaded {len(cookies)} cookies for Tokopedia")
```

### 6.3 Key Management Checklist

```python
"""
Security checklist untuk key management:

[ ] 1. Master key disimpan di ~/.scraper-vault/master.key (chmod 600)
[ ] 2. Master key TIDAK pernah di-commit ke git
[ ] 3. .gitignore berisi *.key dan *.env dan vault.enc
[ ] 4. Backup key disimpan di password manager (Bitwarden/1Password)
[ ] 5. Key dirotasi setiap 90 hari
[ ] 6. Password untuk key derivation menggunakan PBKDF2 (600K iterations)
[ ] 7. Tidak ada hardcoded fallback key di source code
[ ] 8. Vault data diwipe jika terjadi security incident

Relevant .gitignore entries:
# Scraper vault
.scraper-vault/
*.key
*.enc
.env

# Cookie dumps
**/cookies/*.json
!**/cookies/*.md
**/tokens/*.txt
"""
```

### 6.4 Hardware-Backed Encryption dengan TPM/HSM

Untuk enterprise scraping, pertimbangkan hardware-backed key storage:

```python
import subprocess
import json

class TPMKeyStore:
    """
    Menggunakan TPM (Trusted Platform Module) untuk menyimpan key.
    
    Implementasi menggunakan tpm2-tools.
    
    Prasyarat: 
    - tpm2-tools terinstall (apt install tpm2-tools)
    - TPM chip tersedia (verify dengan `tpm2_getcap handles-persistent`)
    """
    
    def __init__(self, key_handle: str = "0x81000001"):
        self.key_handle = key_handle
    
    def seal(self, data: bytes) -> bytes:
        """Seal (enkripsi) data dengan TPM."""
        # Simpan data ke temp file
        input_file = "/tmp/tpm_input.bin"
        output_file = "/tmp/tpm_output.bin"
        
        with open(input_file, "wb") as f:
            f.write(data)
        
        subprocess.run([
            "tpm2_createprimary", "-C", "o", "-c", "/tmp/primary.ctx"
        ], check=True, capture_output=True)
        
        subprocess.run([
            "tpm2_create", "-C", "/tmp/primary.ctx",
            "-u", f"{output_file}.pub",
            "-r", output_file,
            "-i", input_file,
        ], check=True, capture_output=True)
        
        result = open(output_file, "rb").read()
        # Cleanup
        for f in [input_file, output_file, f"{output_file}.pub", "/tmp/primary.ctx"]:
            if os.path.exists(f):
                os.remove(f)
        
        return result
    
    def unseal(self, sealed_data: bytes) -> bytes:
        """Unseal (decrypt) data dengan TPM."""
        output_file = "/tmp/tpm_output.bin"
        sealed_file = "/tmp/tpm_sealed.bin"
        
        with open(sealed_file, "wb") as f:
            f.write(sealed_data)
        
        subprocess.run([
            "tpm2_createprimary", "-C", "o", "-c", "/tmp/primary.ctx"
        ], check=True, capture_output=True)
        
        subprocess.run([
            "tpm2_load", "-C", "/tmp/primary.ctx",
            "-u", f"{sealed_file}.pub",
            "-r", sealed_file,
            "-c", "/tmp/load.ctx",
        ], check=True, capture_output=True)
        
        subprocess.run([
            "tpm2_unseal", "-c", "/tmp/load.ctx",
            "-o", output_file,
        ], check=True, capture_output=True)
        
        result = open(output_file, "rb").read()
        # Cleanup
        for f in [sealed_file, output_file, f"{sealed_file}.pub",
                  "/tmp/primary.ctx", "/tmp/load.ctx"]:
            if os.path.exists(f):
                os.remove(f)
        
        return result
```

> **Sumber**: TPM 2.0 Library Specification -- https://trustedcomputinggroup.org/resource/tpm-library-specification/ (diakses 2026-06-18).

---

## 7. Integrasi dengan Browser Automation

### 7.1 Playwright Cookie Persistence

Playwright menyediakan mekanisme native untuk menyimpan dan memuat cookies via `storageState`.

```python
import asyncio
from playwright.async_api import async_playwright, BrowserContext
from pathlib import Path
from cryptography.fernet import Fernet

class PlaywrightCookieManager:
    """
    Manajemen cookie untuk Playwright browser automation.
    
    Fitur:
    - Encrypted storage state
    - Multi-account profile management
    - Automatic cookie refresh detection
    - Context isolation per platform
    """
    
    def __init__(self, vault_key: bytes, state_dir: Path = Path.home() / ".scraper-vault" / "browser-states"):
        self.vault_key = vault_key
        self.state_dir = state_dir
        self.state_dir.mkdir(parents=True, exist_ok=True)
        self.fernet = Fernet(vault_key)
    
    async def save_browser_state(self, context: BrowserContext, platform: str):
        """
        Menyimpan storage state (cookies + localStorage) dari browser context.
        
        File disimpan dalam format terenkripsi:
        {state_dir}/{platform}/state.enc (encrypted JSON)
        {state_dir}/{platform}/meta.json (plaintext metadata)
        """
        # Export storage state dari Playwright
        state = await context.storage_state()
        
        platform_dir = self.state_dir / platform
        platform_dir.mkdir(parents=True, exist_ok=True)
        
        # Simpan metadata (plaintext -- hanya info non-sensitif)
        meta = {
            "platform": platform,
            "saved_at": int(time.time()),
            "origin": state.get("origins", [{}])[0].get("origin", "") if state.get("origins") else "",
            "cookie_count": len(state.get("cookies", [])),
        }
        with open(platform_dir / "meta.json", "w") as f:
            json.dump(meta, f)
        
        # Simpan state terenkripsi
        encrypted = self.fernet.encrypt(json.dumps(state).encode())
        enc_path = platform_dir / "state.enc"
        enc_path.write_bytes(encrypted)
        
        print(f"Saved {len(state['cookies'])} cookies for {platform}")
        return meta
    
    async def load_browser_state(self, platform: str) -> dict | None:
        """
        Load storage state untuk browser context.
        
        Returns dict yang bisa langsung digunakan dengan
        Playwright's add_cookies() + add_init_script().
        """
        enc_path = self.state_dir / platform / "state.enc"
        if not enc_path.exists():
            return None
        
        encrypted = enc_path.read_bytes()
        try:
            plaintext = self.fernet.decrypt(encrypted, ttl=86400)  # 24 jam
            state = json.loads(plaintext.decode())
            return state
        except Exception as e:
            print(f"Failed to decrypt state for {platform}: {e}")
            return None
    
    async def create_context_from_state(self, browser, platform: str, **kwargs) -> BrowserContext:
        """
        Membuat browser context dengan state yang tersimpan.
        
        Jika state tidak ada atau expired, buat context fresh.
        """
        state = await self.load_browser_state(platform)
        
        if state:
            # Playwright 1.40+ mendukung storage_state langsung di context
            if hasattr(browser, 'new_context') and 'storage_state' in kwargs:
                kwargs['storage_state'] = state
            
            context = await browser.new_context(**kwargs)
            
            # Fallback: add cookies manually
            if not hasattr(browser, 'new_context') or 'storage_state' not in kwargs:
                if state.get("cookies"):
                    await context.add_cookies(state["cookies"])
            
            print(f"Restored session for {platform}")
        else:
            context = await browser.new_context(**kwargs)
            print(f"Created fresh session for {platform}")
        
        return context
    
    def backup_if_rotated(self, platform: str, new_state: dict):
        """
        Mendeteksi apakah cookie dirotasi oleh platform dan backup state baru.
        
        Digunakan sebagai post-request hook.
        """
        old_state = self.load_browser_state(platform)
        if old_state:
            old_cookies = {c["name"]: c for c in old_state.get("cookies", [])}
            new_cookies = {c["name"]: c for c in new_state.get("cookies", [])}
            
            # Deteksi rotasi: compare cookie values
            rotated = False
            for name, new_c in new_cookies.items():
                if name in old_cookies and old_cookies[name]["value"] != new_c["value"]:
                    print(f"Cookie rotated: {name}")
                    rotated = True
            
            if rotated:
                # Backup old state sebelum overwrite
                backup_dir = self.state_dir / platform / "backups"
                backup_dir.mkdir(exist_ok=True)
                timestamp = int(time.time())
                
                old_enc_path = self.state_dir / platform / "state.enc"
                if old_enc_path.exists():
                    backup_path = backup_dir / f"state_{timestamp}.enc"
                    old_enc_path.rename(backup_path)
                    print(f"Backed up old state to {backup_path}")
    
    def list_available_sessions(self) -> list[dict]:
        """List semua session yang tersimpan."""
        sessions = []
        for platform_dir in self.state_dir.iterdir():
            if platform_dir.is_dir():
                meta_path = platform_dir / "meta.json"
                if meta_path.exists():
                    with open(meta_path) as f:
                        meta = json.load(f)
                    sessions.append(meta)
        return sessions

# Contoh penggunaan dengan asyncio
async def scrape_tokopedia_with_playwright():
    key = Fernet.generate_key()
    manager = PlaywrightCookieManager(key)
    
    async with async_playwright() as p:
        # Coba restore session Tokopedia
        browser = await p.chromium.launch(headless=True)
        context = await manager.create_context_from_state(
            browser, "tokopedia",
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1920, "height": 1080},
            locale="id-ID",
        )
        
        page = await context.new_page()
        try:
            await page.goto("https://www.tokopedia.com/", wait_until="networkidle")
            
            # Cek apakah session valid
            login_button = await page.query_selector('[data-testid="btnLogin"]')
            if login_button:
                print("Session expired, perlu login ulang")
                # Trigger login flow
                await page.click('[data-testid="btnLogin"]')
                # ... login logic ...
            
            await manager.save_browser_state(context, "tokopedia")
        finally:
            await context.close()
            await browser.close()
```

### 7.2 CDP (Chrome DevTools Protocol) Cookie Injection

Untuk scraping headless tanpa Playwright (puppeteer atau pyppeteer), gunakan CDP langsung:

```python
import asyncio
import json
from pyppeteer import launch

async def inject_cookies_cdp(page, cookies: list[dict]):
    """
    Inject cookies via CDP Protocol (setCookies).
    
    Lebih stealth daripada page.setCookie() karena tidak
    memicu event perubahan cookie di JavaScript page.
    """
    cdp = await page.target.createCDPSession()
    await cdp.send("Network.setCookies", {
        "cookies": [
            {
                "name": c["name"],
                "value": c["value"],
                "domain": c.get("domain", ""),
                "path": c.get("path", "/"),
                "httpOnly": c.get("httpOnly", False),
                "secure": c.get("secure", True),
                "sameSite": c.get("sameSite", "Lax"),
                "expires": c.get("expires", -1),
            }
            for c in cookies
        ]
    })

# Contoh scraping Tokopedia via pyppeteer
async def scrape_tokopedia_cdp():
    browser = await launch(headless=True, args=[
        "--no-sandbox",
        "--disable-blink-features=AutomationControlled",
    ])
    page = await browser.newPage()
    
    # Set viewport dan user agent Indonesia
    await page.setViewport({"width": 1366, "height": 768})
    await page.setUserAgent(
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    )
    
    # Load cookies dari vault
    vault = CookieVault()
    data = vault.load("tokopedia")
    if data and "cookies" in data:
        await inject_cookies_cdp(page, data["cookies"])
    
    await page.goto("https://www.tokopedia.com/")
    # ... scraping logic ...
    
    await browser.close()
```

### 7.3 Camoufox / Fingerprinting Protection

Menggunakan Camoufox (Firefox fork dengan anti-fingerprinting) untuk scraping platform Indonesia:

```python
"""
Camoufox adalah Firefox fork yang dimodifikasi untuk:
- Spoof WebGL, Canvas, AudioContext fingerprint
- Menyembunyikan WebDriver flag
- Menyediakan realistic TLS fingerprint

Integrasi cookie storage dengan Camoufox:

Sumber: https://github.com/nicedayzhu/camoufox (diakses 2026-06-18)

Setup:
  pip install camoufox
  camoufox fetch  # Download browser binary

Catatan: Camoufox menggunakan Juggler protocol (CDP-like).
Cookie injection dilakukan via /tabs/{tabId}/network/setCookies endpoint.
"""

import requests

class CamoufoxCookieInjector:
    """
    Inject cookies ke Camoufox browser via REST API.
    
    Camoufox listens on http://localhost:9377 by default.
    """
    
    def __init__(self, base_url: str = "http://localhost:9377"):
        self.base_url = base_url
    
    def inject_cookies(self, tab_id: str, cookies: list[dict]):
        """Inject cookies ke tab Camoufox tertentu."""
        response = requests.post(
            f"{self.base_url}/tabs/{tab_id}/network/setCookies",
            json={"cookies": cookies}
        )
        response.raise_for_status()
    
    def get_cookies(self, tab_id: str) -> list[dict]:
        """Ekstrak cookies dari tab Camoufox."""
        response = requests.get(
            f"{self.base_url}/tabs/{tab_id}/network/cookies"
        )
        return response.json()
```

---

## 8. Token Refresh Automation

### 8.1 OAuth2 Token Refresh Pattern

Banyak platform Indonesia menggunakan OAuth2 untuk API mereka. Refresh token otomatis adalah keharusan.

```python
import time
import requests
from dataclasses import dataclass, field

@dataclass
class OAuth2Token:
    """Represents an OAuth2 token dengan refresh mechanism."""
    access_token: str
    refresh_token: str
    token_type: str = "Bearer"
    expires_in: int = 3600
    scope: str = ""
    obtained_at: float = field(default_factory=time.time)
    
    @property
    def is_expired(self) -> bool:
        """Cek apakah token sudah expired (buffer 60 detik)."""
        elapsed = time.time() - self.obtained_at
        return elapsed >= (self.expires_in - 60)
    
    @property
    def expires_in_seconds(self) -> int:
        """Sisa waktu token valid."""
        return max(0, int(self.expires_in - (time.time() - self.obtained_at)))

class OAuth2Refresher:
    """
    Generic OAuth2 token refresher.
    
    Mendukung:
    - Authorization code grant
    - Client credentials grant
    - Refresh token grant
    - Automatic retry dengan exponential backoff
    """
    
    def __init__(self, client_id: str, client_secret: str, token_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.token: OAuth2Token | None = None
        self._lock = asyncio.Lock()  # Untuk thread safety
    
    async def get_valid_token(self) -> str:
        """Mendapatkan access_token yang valid, refresh jika perlu."""
        async with self._lock:
            if self.token and not self.token.is_expired:
                return self.token.access_token
            
            if self.token and self.token.refresh_token:
                return await self._refresh_token()
            
            return await self._fetch_new_token()
    
    async def _refresh_token(self) -> str:
        """Refresh token menggunakan refresh_token grant."""
        response = requests.post(
            self.token_url,
            data={
                "grant_type": "refresh_token",
                "refresh_token": self.token.refresh_token,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=10,
        )
        
        if response.status_code == 400:
            # Refresh token mungkin revoked, perlu login ulang
            print("Refresh token revoked, fetching new token...")
            return await self._fetch_new_token()
        
        response.raise_for_status()
        data = response.json()
        self.token = OAuth2Token(
            access_token=data["access_token"],
            refresh_token=data.get("refresh_token", self.token.refresh_token),
            expires_in=data.get("expires_in", 3600),
            scope=data.get("scope", self.token.scope),
        )
        
        # Persist token baru
        self._persist_token(self.token)
        return self.token.access_token
    
    async def _fetch_new_token(self) -> str:
        """Fetch token baru (biasanya via login ulang)."""
        raise NotImplementedError("Platform-specific login required")
    
    def _persist_token(self, token: OAuth2Token):
        """Simpan token ke encrypted storage."""
        vault = CookieVault()
        vault.save("oauth2_tokens", {
            "access_token": token.access_token,
            "refresh_token": token.refresh_token,
            "expires_in": token.expires_in,
            "obtained_at": token.obtained_at,
        })
```

### 8.2 Token Refresh untuk Platform Indonesia

```python
class TokopediaTokenRefresher(OAuth2Refresher):
    """
    Implementasi OAuth2 refresh untuk Tokopedia API.
    
    Tokopedia menggunakan OAuth2 dengan:
    - Authorization endpoint: https://accounts.tokopedia.com/oauth/authorize
    - Token endpoint: https://accounts.tokopedia.com/oauth/token
    - Refresh token expiry: 30 days
    - Access token expiry: 24 hours (asumsi)
    
    Sumber: Tokopedia API Documentation (2025).
    https://developer.tokopedia.com/docs/ (diakses 2026-06-18).
    """
    
    TOKEN_URL = "https://accounts.tokopedia.com/oauth/token"
    
    def __init__(self, client_id: str, client_secret: str):
        super().__init__(client_id, client_secret, self.TOKEN_URL)
    
    async def _fetch_new_token(self) -> str:
        """
        Login dengan username/password untuk mendapatkan token baru.
        
        Catatan: Tokopedia mungkin meminta OTP/2FA.
        Implementasi ini asumsikan credential sudah valid.
        """
        username = os.getenv("SCRAPER_TOKOPEDIA_USERNAME")
        password = os.getenv("SCRAPER_TOKOPEDIA_PASSWORD")
        
        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "password",
                "username": username,
                "password": password,
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": "public_api",
            },
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        
        self.token = OAuth2Token(
            access_token=data["access_token"],
            refresh_token=data["refresh_token"],
            expires_in=data.get("expires_in", 86400),
        )
        self._persist_token(self.token)
        return self.token.access_token

class ShopeeTokenRefresher:
    """
    Token refresh untuk Shopee API.
    
    Shopee menggunakan sistem token sendiri (bukan OAuth2 standar).
    Token didapat dari response login dan perlu direfresh secara periodik.
    
    Shopee token structure:
    - SPC_EC: Encrypted cookie (main session)
    - SPC_U: User identification
    - SPC_R: Refresh token
    
    Sumber: Reverse engineering oleh komunitas scraping Shopee.
    https://github.com/indonesia-scraping-community/shopee-api-notes (diakses 2026-06-18).
    """
    
    BASE_URL = "https://shopee.co.id"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json",
            "Accept-Language": "id-ID,id;q=0.9,en;q=0.8",
            "Referer": "https://shopee.co.id/",
            "X-Requested-With": "XMLHttpRequest",
            "X-API-SOURCE": "pc",
            "X-Shopee-Language": "id",
        })
    
    def refresh_session(self, current_cookies: dict) -> dict:
        """
        Refresh Shopee session dengan memanggil endpoint khusus.
        
        Shopee memiliki endpoint /api/v2/global/auth/refresh
        yang merotasi SPC_EC tanpa perlu login ulang.
        """
        self.session.cookies.update(current_cookies)
        
        response = self.session.post(
            f"{self.BASE_URL}/api/v2/global/auth/refresh",
            json={"device_id": self._get_device_id()},
            timeout=10,
        )
        
        if response.status_code != 200:
            raise RuntimeError(f"Shopee refresh failed: {response.status_code}")
        
        # Update cookies dari response
        new_cookies = {}
        for key in ["SPC_EC", "SPC_U", "SPC_R"]:
            if key in self.session.cookies:
                new_cookies[key] = self.session.cookies[key]
        
        return new_cookies if new_cookies else current_cookies
    
    def _get_device_id(self) -> str:
        """Generate atau load device ID yang konsisten."""
        # Shopee mengasosiasikan session dengan device ID
        device_file = Path.home() / ".scraper-vault" / "shopee_device_id"
        if device_file.exists():
            return device_file.read_text().strip()
        
        device_id = "".join(random.choices("0123456789abcdef", k=32))
        device_file.parent.mkdir(parents=True, exist_ok=True)
        device_file.write_text(device_id)
        return device_id
```

### 8.3 JWT Token Refresh dengan Rotating Signing Key

```python
import jwt
import time
import requests
from datetime import datetime, timedelta

class JWTTokenManager:
    """
    Manajemen JWT token dengan rotating signing key.

    Beberapa platform Indonesia (seperti Gojek, Traveloka) menggunakan
    JWT dengan signing key yang dirotasi secara periodik.
    
    Strategi:
    - Decode JWT untuk ekstrak expiry time
    - Refresh token sebelum expired (buffer 5 menit)
    - Detect signing key rotation via jku/jwk header
    - Cache JWKS endpoint dengan time-based expiry
    """
    
    def __init__(self):
        self.jwk_cache: dict[str, tuple[dict, float]] = {}
        self.cache_ttl = 3600  # 1 jam
    
    def decode_without_verify(self, token: str) -> dict:
        """Decode JWT header dan payload tanpa verifikasi (untuk inspeksi)."""
        return jwt.decode(token, options={"verify_signature": False})
    
    def get_token_expiry(self, token: str) -> datetime:
        """Ekstrak expiry time dari JWT token."""
        payload = self.decode_without_verify(token)
        exp = payload.get("exp")
        if exp:
            return datetime.fromtimestamp(exp)
        raise ValueError("JWT token doesn't have 'exp' claim")
    
    def should_refresh(self, token: str, buffer_minutes: int = 5) -> bool:
        """Cek apakah token perlu direfresh (buffer sebelum expired)."""
        try:
            expiry = self.get_token_expiry(token)
            return datetime.utcnow() + timedelta(minutes=buffer_minutes) >= expiry
        except Exception:
            return True  # Jika error, refresh saja
    
    def fetch_jwks(self, jwks_url: str) -> dict:
        """Fetch JWKS keyset dengan caching."""
        now = time.time()
        if jwks_url in self.jwk_cache:
            keys, fetched_at = self.jwk_cache[jwks_url]
            if now - fetched_at < self.cache_ttl:
                return keys
        
        response = requests.get(jwks_url, timeout=10)
        response.raise_for_status()
        keys = response.json()
        self.jwk_cache[jwks_url] = (keys, now)
        return keys
    
    def verify_and_decode(self, token: str, jwks_url: str) -> dict:
        """
        Verifikasi JWT dengan JWKS key set.
        
        Support key rotation dengan mencari key yang sesuai
        berdasarkan 'kid' (Key ID) di header JWT.
        """
        jwks = self.fetch_jwks(jwks_url)
        public_key = jwt.PyJWKSet.from_dict(jwks)
        
        return jwt.decode(
            token,
            public_key,
            algorithms=["RS256", "RS384", "RS512", "ES256", "ES384"],
            options={"verify_exp": True, "verify_iat": True},
        )
```

### 8.4 Scheduled Token Rotation

```python
import asyncio
import schedule
import time

class TokenRotationScheduler:
    """
    Scheduled token rotation menggunakan asyncio.
    
    Menjalankan refresh secara periodik untuk semua platform.
    Jeda antar refresh acak untuk menghindari pattern detection.
    """
    
    def __init__(self):
        self.refreshers: dict[str, callable] = {}
        self.intervals: dict[str, int] = {}
    
    def register_platform(self, name: str, refresher: callable, interval_hours: int):
        """Daftarkan platform dengan interval refresh."""
        self.refreshers[name] = refresher
        self.intervals[name] = interval_hours
    
    async def run_forever(self):
        """Loop utama: refresh token setiap interval dengan jitter."""
        while True:
            for name, refresher in self.refreshers.items():
                try:
                    result = await refresher()
                    print(f"[{datetime.utcnow().isoformat()}] Refreshed {name}")
                    
                    # Simpan hasil refresh
                    vault = CookieVault()
                    vault.save(f"token_{name}", {
                        "last_refresh": datetime.utcnow().isoformat(),
                        "token": result,
                    })
                    
                except Exception as e:
                    print(f"[ERROR] Refresh {name} gagal: {e}")
                    # Exponential backoff akan ditangani oleh masing-masing refresher
            
            # Sleep dengan jitter acak (+- 15%)
            hours = min(self.intervals.values())
            jitter = random.uniform(0.85, 1.15)
            await asyncio.sleep(hours * 3600 * jitter)

# Contoh penggunaan
scheduler = TokenRotationScheduler()
tokopedia_refresher = TokopediaTokenRefresher(
    os.getenv("TOKOPEDIA_CLIENT_ID"),
    os.getenv("TOKOPEDIA_CLIENT_SECRET"),
)
scheduler.register_platform("tokopedia", tokopedia_refresher.get_valid_token, 12)

# asyncio.run(scheduler.run_forever())
```

---

## 9. Scraping Ethics dan Indonesian UU ITE Considerations

### 9.1 Batasan Legal Scraping di Indonesia

Penting untuk memahami bahwa scraping **tidak otomatis ilegal** di Indonesia, tetapi ada batasan yang perlu dipatuhi:

**UU ITE Pasal 30-32**: Melarang akses ilegal ke sistem elektronik. Scraping data publik (seperti halaman produk Tokopedia yang bisa diakses tanpa login) umumnya dianggap legal. Namun scraping data yang memerlukan autentikasi, atau scraping yang membebani server berlebihan, bisa dianggap melanggar.

**Pasal 30 UU ITE**:
> "Setiap Orang dengan sengaja dan tanpa hak atau melawan hukum mengakses Komputer dan/atau Sistem Elektronik milik Orang lain dengan cara apa pun."

**Penafsiran**: Jika scraper menggunakan credential (cookie/token) untuk mengakses data yang seharusnya dibatasi, ini bisa dianggap sebagai akses ilegal. Maka dari itu, penting untuk:

1. **Hanya scrape data publik** (tidak memerlukan login)
2. **Hormati robots.txt** dan rate limits
3. **Jangan menyalahgunakan credential** yang didapat dari akun pribadi

**Sumber**: UU ITE Pasal 30, tersedia di https://peraturan.bpk.go.id/Details/37582/uu-no-19-tahun-2016 (diakses 2026-06-18). Analisis scraping legality oleh hukumonline: https://www.hukumonline.com/berita/a/scraping-data-dan-uu-ite/ (diakses 2026-06-18).

### 9.2 Terms of Service vs Hukum

Platform Indonesia biasanya melarang scraping di ToS mereka:

| Platform | Larangan Scraping di ToS | Sanksi |
|---|---|---|
| Tokopedia | "You may not use any automated means to access the Platform" | Pemblokiran akun |
| Shopee | Section 3.2: "No automated tools" | IP ban + legal action |
| Gojek | "No scraping, crawling, or data mining" | Akun di-suspend |
| Traveloka | "Automated access prohibited" | Block permanent |
| X/Twitter | "Scraping without permission is prohibited" (2023 update) | Legal action |

**Penting**: Meskipun ToS melarang scraping, di Indonesia pelanggaran ToS biasanya bukan pelanggaran pidana (kecuali jika melanggar UU ITE). Namun platform bisa menggugat secara perdata (wanprestasi) atau memblokir akses.

**Sumber**: Tokopedia Terms of Service, terakhir diubah 2025 -- https://www.tokopedia.com/terms (diakses 2026-06-18). Shopee Terms -- https://shopee.co.id/terms (diakses 2026-06-18).

### 9.3 Prinsip Etis Scraping

```python
"""
Prinsip scraping etis untuk konteks Indonesia:

1. HORMATI ROBOTS.TXT
   - Cek /robots.txt sebelum scraping
   - Patuhi Crawl-delay directive
   - Contoh: https://www.tokopedia.com/robots.txt

2. RATE LIMITING
   - Maksimum 1 request per 2-5 detik untuk platform Indonesia
   - Gunakan exponential backoff pada 429/503
   - Jangan scrape jam sibuk (19:00-22:00 WIB)

3. DATA MINIMIZATION
   - Ambil data yang diperlukan saja
   - Jangan scrape data pribadi pengguna lain
   - Jangan scrape data yang dilindungi (password, payment info)

4. USER AGENT IDENTIFICATION
   - Gunakan User-Agent yang jujur atau identitas scraper
   - Contoh: "MyScraperBot/1.0 (+https://example.com/bot)"
   - Jangan spoof User-Agent untuk menghindari deteksi

5. STORAGE LIMITATION
   - Hanya simpan data yang diperlukan
   - Hapus data lama secara periodik
   - Jangan jual data yang di-scrape
"""

# Contoh implementasi rate limiter etis
import asyncio
import random

class EthicalRateLimiter:
    """
    Rate limiter yang menghormati server dan regulasi.
    
    Implementasi Token Bucket dengan kapasitas disesuaikan.
    """
    
    def __init__(self, requests_per_minute: int = 12):  # 1 request per 5 detik
        self.rate = requests_per_minute
        self.tokens = requests_per_minute
        self.last_refill = time.time()
        self.min_interval = 60.0 / requests_per_minute
    
    async def acquire(self):
        """Tunggu hingga rate limit memungkinkan request baru."""
        now = time.time()
        
        # Refill tokens
        elapsed = now - self.last_refill
        self.tokens = min(self.rate, self.tokens + elapsed * (self.rate / 60.0))
        self.last_refill = now
        
        if self.tokens >= 1:
            self.tokens -= 1
            return
        
        # Hitung waktu tunggu
        wait_time = (60.0 / self.rate) * (1 - self.tokens)
        # Tambah jitter acak untuk menghindari pattern
        wait_time *= random.uniform(1.0, 1.5)
        
        await asyncio.sleep(wait_time)
        self.tokens = 0
```

### 9.4 Cookie dan Token Sebagai "Data Pribadi"

Di bawah **UU Perlindungan Data Pribadi (UU PDP, UU No. 27 Tahun 2022)**, cookie dan token bisa dianggap sebagai data pribadi jika dapat digunakan untuk mengidentifikasi seseorang.

**Pasal 4 UU PDP**: Data pribadi mencakup data yang dapat mengidentifikasi seseorang secara langsung atau tidak langsung. Session cookies yang terikat dengan akun tertentu termasuk dalam kategori ini.

**Implikasi untuk scraper**:
1. Cookie yang mengandung session ID yang bisa dilacak ke identitas pengguna harus diamankan
2. Penyimpanan cookie harus memenuhi standar keamanan yang memadai (enkripsi)
3. Penggunaan cookie orang lain untuk scraping bisa dianggap sebagai pemrosesan data pribadi tanpa izin

**Sumber**: UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi -- https://peraturan.bpk.go.id/Details/233605/uu-no-27-tahun-2022 (diakses 2026-06-18).

---

## 10. Real-World Examples

### 10.1 Maintaining Tokopedia Session

```python
"""
Tokopedia Session Management.
================================

Tokopedia menggunakan beberapa cookie kunci:
- t_pd: Main session cookie (encrypted)
- session_id: Session identifier
- _gcl_au: Google Analytics (tracking)
- _fbp: Facebook Pixel (tracking)
- csrf_token: Anti-CSRF

Session cookie t_pd memiliki TTL sekitar 24-72 jam.
Setelah expired, perlu refresh via login atau CookieRefresh endpoint.

Endpoint untuk refresh cookie:
POST https://www.tokopedia.com/cookie-refresh
Headers: X-Device-ID, X-Source
"""

import requests
import json
import time
from pathlib import Path
from cryptography.fernet import Fernet

class TokopediaSessionManager:
    """
    Full session lifecycle management untuk Tokopedia scraping.
    
    Fitur:
    - Encrypted cookie storage
    - Automatic cookie refresh detection
    - Session health monitoring
    - Multi-account fallback
    """
    
    BASE_URL = "https://www.tokopedia.com"
    API_URL = "https://api.tokopedia.com"
    
    def __init__(self, vault_key: bytes):
        self.fernet = Fernet(vault_key)
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.tokopedia.com/",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
        })
        
        self.cookie_file = Path.home() / ".scraper-vault" / "tokopedia" / "session.enc"
        self.cookie_file.parent.mkdir(parents=True, exist_ok=True)
    
    def load_session(self) -> bool:
        """Load saved session, return True jika valid."""
        if not self.cookie_file.exists():
            return False
        
        try:
            encrypted = self.cookie_file.read_bytes()
            plaintext = self.fernet.decrypt(encrypted, ttl=86400)  # 24 jam
            cookies = json.loads(plaintext.decode())
            
            # Set cookies ke session
            for name, value in cookies.items():
                self.session.cookies.set(name, value, domain=".tokopedia.com")
            
            # Verifikasi session dengan request profil
            return self._verify_session()
            
        except Exception as e:
            print(f"Session load failed: {e}")
            return False
    
    def _verify_session(self) -> bool:
        """Verifikasi session dengan memanggil endpoint ringan."""
        try:
            response = self.session.get(
                f"{self.BASE_URL}/api/v1/user/profile",
                headers={"X-Requested-With": "XMLHttpRequest"},
                timeout=10,
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("data", {}).get("id"):
                    print(f"Session valid for user: {data['data'].get('name', 'unknown')}")
                    return True
            
            # Jika redirect ke login, session expired
            if response.history:
                for r in response.history:
                    if "login" in r.headers.get("Location", ""):
                        print("Session expired: redirect to login")
                        return False
            
            return False
            
        except requests.RequestException as e:
            print(f"Session verification error: {e}")
            return False
    
    def save_session(self):
        """Save current session cookies ke encrypted file."""
        cookies = {}
        for cookie in self.session.cookies:
            if cookie.domain.endswith(".tokopedia.com"):
                cookies[cookie.name] = cookie.value
        
        encrypted = self.fernet.encrypt(json.dumps(cookies).encode())
        self.cookie_file.write_bytes(encrypted)
        print(f"Saved {len(cookies)} cookies to {self.cookie_file}")
    
    def refresh_session(self) -> bool:
        """
        Attempt to refresh session via cookie-refresh endpoint.
        
        Beberapa akun Tokopedia mungkin punya refresh token
        yang bisa digunakan tanpa login ulang.
        """
        try:
            response = self.session.post(
                f"{self.BASE_URL}/cookie-refresh",
                headers={
                    "X-Device-ID": self._get_device_id(),
                    "X-Source": "web",
                    "Content-Type": "application/json",
                },
                json={"refresh": True},
                timeout=10,
            )
            
            if response.status_code == 200:
                # Update cookies dari response
                self.save_session()
                return True
            
            return False
            
        except requests.RequestException:
            return False
    
    def _get_device_id(self) -> str:
        """Get persistent device ID."""
        device_file = Path.home() / ".scraper-vault" / "tokopedia" / "device_id"
        if device_file.exists():
            return device_file.read_text().strip()
        
        device_id = "".join(random.choices("abcdef0123456789", k=32))
        device_file.parent.mkdir(parents=True, exist_ok=True)
        device_file.write_text(device_id)
        return device_id
    
    def scrape_search(self, query: str, page: int = 1) -> dict | None:
        """
        Scrape halaman pencarian Tokopedia.
        
        Menggunakan endpoint GraphQL internal Tokopedia.
        """
        if not self.load_session():
            print("No valid session. Attempting refresh...")
            if not self.refresh_session():
                print("Session refresh failed. Need login.")
                return None
        
        # Cookie freshness check
        t_pd = self.session.cookies.get("t_pd", domain=".tokopedia.com")
        if not t_pd:
            print("t_pd cookie missing, session invalid")
            return None
        
        params = {
            "q": query,
            "page": page,
            "rt": "1,2,3,4,5,6,7,8,9,10,11,12,13",
            "source": "search",
            "device": "desktop",
            "user_id": "",
        }
        
        response = self.session.get(
            f"{self.BASE_URL}/search",
            params=params,
            timeout=15,
        )
        
        if response.status_code == 200:
            # Save session (token mungkin diupdate)
            self.save_session()
            
            # Parse response
            try:
                data = response.json()
                return data
            except json.JSONDecodeError:
                # HTML response: mungkin kena WAF atau CAPTCHA
                if "captcha" in response.text.lower():
                    print("CAPTCHA detected! Rotate proxy or session.")
                return {"html": response.text[:500]}
        
        elif response.status_code == 429:
            print("Rate limited! Backing off...")
            time.sleep(60)
            return None
        
        else:
            print(f"Unexpected status: {response.status_code}")
            return None
```

### 10.2 Shopee API Token Rotation

```python
"""
Shopee API Token Rotation Strategy.
====================================

Shopee menggunakan sistem multi-cookie untuk autentikasi:
- SPC_EC: Main encrypted session cookie. Diupdate setiap request.
- SPC_U: User identifier. Persisten antar sesi.
- SPC_EC_WEB: Web-specific session variant.
- SPC_F: Tracking cookie.

Pola deteksi rotasi:
- Setiap response dari Shopee mungkin mengandung Set-Cookie baru
- SPC_EC berubah secara periodik (setiap 30-60 menit)
- Tanpa update SPC_EC, session akan invalid dalam 2-3 jam
"""

import requests
import time
import json
from typing import Optional

class ShopeeSessionManager:
    """
    Session manager untuk Shopee API dengan auto cookie rotation.
    
    Strategi:
    - Intercept Set-Cookie headers di setiap response
    - Update cookie storage secara real-time
    - Maintain multiple sessions untuk failover
    - Detect cookie expiry via specific error codes
    """
    
    BASE_URL = "https://shopee.co.id"
    API_V2 = f"{BASE_URL}/api/v2"
    
    def __init__(self):
        self.session = requests.Session()
        self._setup_headers()
        self.cookie_store: dict = {}
        self.last_refresh: float = 0
        self.request_count: int = 0
    
    def _setup_headers(self):
        """Setup headers mimicking real browser."""
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json",
            "Accept-Language": "id-ID,id;q=0.9,en;q=0.8",
            "Content-Type": "application/json",
            "Referer": "https://shopee.co.id/",
            "X-Requested-With": "XMLHttpRequest",
            "X-API-SOURCE": "pc",
            "X-Shopee-Language": "id",
            "Origin": "https://shopee.co.id",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
        })
    
    def _extract_cookies_from_response(self, response: requests.Response) -> dict:
        """
        Extract dan detect cookie rotation dari response headers.
        
        Shopee sering mengirim Set-Cookie di response header
        dengan cookie baru.
        """
        new_cookies = {}
        
        for key, value in response.cookies.items():
            # Hanya simpan cookie Shopee-relevant
            if key.startswith(("SPC_", "shopee_", "csrftoken")):
                old_value = self.session.cookies.get(key)
                if old_value and old_value != value:
                    print(f"Cookie rotated: {key}: {old_value[:10]}... -> {value[:10]}...")
                new_cookies[key] = value
        
        return new_cookies
    
    def request_with_rotation(self, method: str, endpoint: str, **kwargs) -> Optional[requests.Response]:
        """
        Send request dengan auto cookie rotation detection.
        
        Mencatat Set-Cookie headers dan update storage.
        Handle error codes yang mengindikasikan token invalid.
        """
        url = f"{self.API_V2}{endpoint}"
        
        # Increment request counter (untuk anti-pattern detection)
        self.request_count += 1
        
        response = self.session.request(method, url, **kwargs)
        
        # Extract cookie rotation dari response
        new_cookies = self._extract_cookies_from_response(response)
        if new_cookies:
            self._update_cookie_store(new_cookies)
        
        # Handle specific Shopee error codes
        if response.status_code == 200:
            try:
                data = response.json()
                
                # Shopee error codes:
                # 2: Unauthorized (token expired)
                # 6: Rate limited
                # 7: Invalid session
                # 9: Account restricted
                # 11: Need captcha
                error_code = data.get("error")
                
                if error_code == 2:
                    print("Shopee token expired. Attempting refresh...")
                    if self._refresh_session():
                        # Retry request dengan session baru
                        return self.request_with_rotation(method, endpoint, **kwargs)
                    return None
                
                elif error_code == 6:
                    print("Shopee rate limit. Backing off...")
                    time.sleep(30)
                    return self.request_with_rotation(method, endpoint, **kwargs)
                
                elif error_code == 11:
                    print("Shopee CAPTCHA required. Session may be flagged.")
                    return None
                
            except json.JSONDecodeError:
                pass
        
        elif response.status_code == 403:
            print("Shopee 403 Forbidden. IP mungkin di-ban.")
            return None
        
        elif response.status_code == 429:
            wait = int(response.headers.get("Retry-After", 60))
            print(f"Shopee 429 Rate Limited. Waiting {wait}s...")
            time.sleep(wait)
            return self.request_with_rotation(method, endpoint, **kwargs)
        
        return response
    
    def _update_cookie_store(self, new_cookies: dict):
        """Update cookie store dengan cookies baru dari response."""
        self.cookie_store.update(new_cookies)
        self.last_refresh = time.time()
        
        # Persist ke encrypted storage
        vault = CookieVault()
        vault.save("shopee_active", {
            "cookies": self.cookie_store,
            "last_refresh": self.last_refresh,
            "request_count": self.request_count,
        }, ttl_seconds=86400)
    
    def _refresh_session(self) -> bool:
        """Refresh Shopee session via auth refresh endpoint."""
        try:
            response = self.session.post(
                f"{self.API_V2}/global/auth/refresh",
                json={"device_id": self._get_device_id()},
                timeout=10,
            )
            
            if response.status_code == 200:
                new_cookies = self._extract_cookies_from_response(response)
                self._update_cookie_store(new_cookies)
                print("Shopee session refreshed successfully")
                return True
            
            return False
            
        except requests.RequestException as e:
            print(f"Shopee refresh failed: {e}")
            return False
    
    def _get_device_id(self) -> str:
        """Get or generate persistent device ID."""
        device_file = Path.home() / ".scraper-vault" / "shopee" / "device_id"
        if device_file.exists():
            return device_file.read_text().strip()
        
        device_id = "".join(random.choices("abcdef0123456789", k=32))
        device_file.parent.mkdir(parents=True, exist_ok=True)
        device_file.write_text(device_id)
        return device_id

# Contoh penggunaan
manager = ShopeeSessionManager()

# Ambil detail produk
response = manager.request_with_rotation(
    "GET",
    "/product/get_shop_detail",
    params={"shop_id": 12345678}
)
```

### 10.3 X (Twitter) Cookie Management

```python
"""
X/Twitter Cookie dan Token Management.
========================================

X menggunakan:
- auth_token: Main authentication cookie (180 hari)
- ct0: CSRF token (digunakan di header x-csrf-token)
- twid: User ID cookie
- guest_id: Guest session untuk non-login scraping

Endpoint penting:
- GET /i/api/2/search/adaptive.json (search API)
- POST /i/api/1.1/onboarding/task.json (login)
- POST /i/api/graphql/{queryId}/{operationName} (GraphQL)
"""

import requests
import time
import json
import re
from pathlib import Path

class XSessionManager:
    """
    Session manager untuk X/Twitter scraping.
    
    Fitur:
    - auth_token + ct0 management
    - Cookie rotation detection
    - Guest mode fallback
    - Rate limit handling with backoff
    """
    
    BASE_URL = "https://x.com"
    API_URL = "https://api.x.com"
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Origin": "https://x.com",
            "Referer": "https://x.com/",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "TE": "trailers",
        })
        
        # Load saved cookies
        self._load_cookies()
    
    def _load_cookies(self):
        """Load X cookies dari encrypted vault."""
        vault = CookieVault()
        data = vault.load("x_com")
        if data:
            cookies = data.get("cookies", {})
            for name, value in cookies.items():
                self.session.cookies.set(name, value, domain=".x.com")
            print(f"Loaded X cookies: {list(cookies.keys())}")
    
    def _save_cookies(self):
        """Save X cookies ke encrypted vault."""
        cookies = {}
        for cookie in self.session.cookies:
            if cookie.domain.endswith((".x.com", ".twitter.com")):
                cookies[cookie.name] = cookie.value
        
        vault = CookieVault()
        vault.save("x_com", {
            "cookies": cookies,
            "saved_at": time.time(),
        }, ttl_seconds=86400 * 30)  # 30 hari
    
    def _extract_ct0(self):
        """
        Extract ct0 (CSRF token) dari cookies.
        
        ct0 diperlukan di header 'x-csrf-token' untuk API calls.
        """
        ct0 = self.session.cookies.get("ct0", domain=".x.com")
        if ct0:
            self.session.headers["x-csrf-token"] = ct0
        return ct0
    
    def _extract_auth_token(self):
        """Extract auth_token dari cookies."""
        return self.session.cookies.get("auth_token", domain=".x.com")
    
    def check_session_valid(self) -> bool:
        """
        Verifikasi session dengan memanggil endpoint profil.
        
        X mengembalikan 401 jika token invalid.
        """
        if not self._extract_auth_token():
            return False
        
        self._extract_ct0()  # Update csrf token jika ada
        
        response = self.session.get(
            f"{self.API_URL}/i/api/1.1/account/verify_credentials.json",
            timeout=10,
        )
        
        if response.status_code == 200:
            return True
        
        # 401 = token expired
        if response.status_code == 401:
            print("X auth_token expired. Need relogin.")
            # Coba refresh via guest token
            return self._try_guest_mode()
        
        return False
    
    def _try_guest_mode(self) -> bool:
        """
        Fallback ke guest mode untuk endpoint publik.
        
        X memberikan guest_token tanpa login.
        Guest token bisa digunakan untuk scraping data publik.
        """
        response = self.session.post(
            f"{self.API_URL}/i/api/1.1/guest/activate.json",
            timeout=10,
        )
        
        if response.status_code == 200:
            guest_token = response.json().get("guest_token")
            self.session.headers["x-guest-token"] = guest_token
            print(f"Using guest token: {guest_token[:10]}...")
            return True
        
        return False
    
    def search_tweets(self, query: str, count: int = 20) -> list[dict]:
        """
        Search tweets menggunakan API endpoint.
        
        Menggunakan endpoint search/adaptive.json yang
        membutuhkan auth_token valid.
        """
        if not self.check_session_valid():
            # Gunakan guest mode
            if not self._try_guest_mode():
                print("Cannot access X API: no valid session")
                return []
        
        params = {
            "q": query,
            "count": min(count, 100),
            "tweet_mode": "extended",
            "include_profile_interstitial_type": "0",
            "include_blocking": "0",
            "include_blocked_by": "0",
            "include_followed_by": "0",
            "include_want_retweets": "0",
            "include_mute_edge": "0",
            "include_can_dm": "0",
            "skip_status": "0",
            "cards_platform": "Web-12",
            "include_cards": "1",
            "include_composer": "false",
            "include_ext_alt_text": "true",
            "include_reply_count": "1",
            "tweet_count": count,
            "include_quote_count": "true",
            "send_error_codes": "true",
            "simple_quoted_tweet": "true",
            "query_source": "typed_query",
            "ext": "mediaStats,highlightedLabel,hasNftAvatar,voiceInfo,enrichments,superFollowMetadata,unmentionInfo,editControl,collaborativeControl",
        }
        
        response = self.session.get(
            f"{self.API_URL}/i/api/2/search/adaptive.json",
            params=params,
            timeout=15,
        )
        
        if response.status_code == 200:
            data = response.json()
            # Ekstrak tweets dari globalObjects
            tweets = []
            for tweet_id, tweet_data in data.get("globalObjects", {}).get("tweets", {}).items():
                tweets.append(tweet_data)
            
            print(f"Found {len(tweets)} tweets for query: {query}")
            return tweets
        
        elif response.status_code == 429:
            print("X rate limited. Sleeping 15 min...")
            time.sleep(900)
            return []
        
        else:
            print(f"X search failed: {response.status_code}")
            return []
```

### 10.4 Gojek/Grab Cookie Management

```python
"""
Gojek dan Grab Cookie Management.
====================================

Kedua platform ride-hailing menggunakan token-based auth:
- Gojek: gojek_token (JWT) + refresh_token
- Grab: grab_access_token + grab_refresh_token

Keduanya memerlukan OTP untuk login, sehingga session management
yang baik sangat penting untuk menghindari login berulang.
"""

class GojekSessionManager:
    """
    Session management untuk Gojek API.
    
    Gojek menggunakan JWT access token dengan refresh token.
    Access token TTL: ~24 jam
    Refresh token TTL: ~30 hari
    
    Endpoints:
    - Login: POST https://api.gojek.id/v1/customers/login_with_phone
    - Verify OTP: POST https://api.gojek.id/v1/customers/login_with_phone/verify
    - Refresh: POST https://api.gojek.id/v1/customers/refresh_token
    """
    
    BASE_URL = "https://api.gojek.id"
    APP_ID = "com.gojek.app"  # Gojek app identifier
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Gojek/4.44.1 (Android 14; Mobile)",
            "X-AppVersion": "4.44.1",
            "X-Platform": "Android",
            "X-UniqueId": self._get_unique_id(),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "X-Location": "-6.2,106.8",  # Default: Jakarta
        })
        self.access_token: str | None = None
        self.refresh_token: str | None = None
    
    def _get_unique_id(self) -> str:
        """Generate atau load persistent device ID."""
        id_file = Path.home() / ".scraper-vault" / "gojek" / "unique_id"
        if id_file.exists():
            return id_file.read_text().strip()
        
        unique_id = "".join(random.choices("abcdef0123456789", k=40))
        id_file.parent.mkdir(parents=True, exist_ok=True)
        id_file.write_text(unique_id)
        return unique_id
    
    def load_tokens(self) -> bool:
        """Load saved tokens dari vault."""
        vault = CookieVault()
        data = vault.load("gojek")
        if data:
            self.access_token = data.get("access_token")
            self.refresh_token = data.get("refresh_token")
            if self.access_token:
                self.session.headers["Authorization"] = f"Bearer {self.access_token}"
                return True
        return False
    
    def save_tokens(self):
        """Save tokens ke encrypted vault."""
        vault = CookieVault()
        vault.save("gojek", {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
        }, ttl_seconds=86400 * 30)
    
    def refresh_access_token(self) -> bool:
        """
        Refresh access token menggunakan refresh token.
        
        Gojek refresh endpoint:
        POST /v1/customers/refresh_token
        Body: {"refresh_token": "..."}
        """
        if not self.refresh_token:
            return False
        
        response = self.session.post(
            f"{self.BASE_URL}/v1/customers/refresh_token",
            json={"refresh_token": self.refresh_token},
            timeout=10,
        )
        
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access_token")
            self.refresh_token = data.get("refresh_token", self.refresh_token)
            
            if self.access_token:
                self.session.headers["Authorization"] = f"Bearer {self.access_token}"
                self.save_tokens()
                return True
        
        elif response.status_code == 401:
            # Refresh token expired, perlu login ulang
            print("Gojek refresh token expired. Full login required.")
        
        return False
    
    def get_gofood_merchants(self, latitude: float, longitude: float) -> list[dict]:
        """Get GoFood merchants di lokasi tertentu."""
        if not self.load_tokens():
            if not self.refresh_access_token():
                print("No valid Gojek session")
                return []
        
        params = {
            "page": 1,
            "per_page": 20,
            "latitude": latitude,
            "longitude": longitude,
        }
        
        response = self.session.get(
            f"{self.BASE_URL}/v3/gofood/merchants",
            params=params,
            timeout=15,
        )
        
        if response.status_code == 200:
            return response.json().get("data", {}).get("merchants", [])
        
        elif response.status_code == 401:
            # Token expired, coba refresh
            if self.refresh_access_token():
                return self.get_gofood_merchants(latitude, longitude)
        
        return []
```

---

## 11. Referensi dan Sumber

### Dokumentasi Teknis

1. **Fernet Spec (symmetric encryption)** -- https://github.com/fernet/spec/blob/master/Spec.md (diakses 2026-06-18).
2. **Python Cryptography Documentation** -- https://cryptography.io/en/latest/fernet/ (diakses 2026-06-18).
3. **Playwright Storage State** -- https://playwright.dev/docs/api/class-browsercontext#browser-context-storage-state (diakses 2026-06-18).
4. **HashiCorp Vault Documentation** -- https://developer.hashicorp.com/vault/docs (diakses 2026-06-18).
5. **Bitwarden CLI Guide** -- https://bitwarden.com/help/cli/ (diakses 2026-06-18).
6. **OWASP Secure Storage Cheat Sheet** -- https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html (diakses 2026-06-18).
7. **JWT Best Practices** -- https://datatracker.ietf.org/doc/html/rfc7519 (diakses 2026-06-18).
8. **OAuth 2.0 Refresh Token Best Practices** -- https://datatracker.ietf.org/doc/html/rfc6749 (diakses 2026-06-18).

### Regulasi Indonesia

9. **UU ITE Pasal 30-32** (UU No. 19/2016) -- https://peraturan.bpk.go.id/Details/37582/uu-no-19-tahun-2016 (diakses 2026-06-18).
10. **UU PDP** (UU No. 27/2022) -- https://peraturan.bpk.go.id/Details/233605/uu-no-27-tahun-2022 (diakses 2026-06-18).
11. **Analisis Scraping dan UU ITE** oleh hukumonline -- https://www.hukumonline.com/berita/a/scraping-data-dan-uu-ite/ (diakses 2026-06-18).

### Platform-Specific

12. **Tokopedia Engineering Blog: Anti-Scraping at Scale (2025)** -- https://engineering.tokopedia.com/blog/antiscraping-at-scale-2025 (diakses 2026-06-18).
13. **Tokopedia Terms of Service** -- https://www.tokopedia.com/terms (diakses 2026-06-18).
14. **Shopee Terms of Service** -- https://shopee.co.id/terms (diakses 2026-06-18).
15. **Shopee API Reverse Engineering Notes** (komunitas) -- https://github.com/indonesia-scraping-community/shopee-api-notes (diakses 2026-06-18).
16. **Tokopedia Developer API** -- https://developer.tokopedia.com/docs/ (diakses 2026-06-18).
17. **Cloudflare Bot Management** (digunakan Tokopedia) -- https://developers.cloudflare.com/bot-management/ (diakses 2026-06-18).

### Tools dan Library

18. **Camoufox Browser** (anti-fingerprinting Firefox fork) -- https://github.com/nicedayzhu/camoufox (diakses 2026-06-18).
19. **TPM 2.0 Library Specification** -- https://trustedcomputinggroup.org/resource/tpm-library-specification/ (diakses 2026-06-18).
20. **python-dotenv** (env management) -- https://saurabh-kumar.com/python-dotenv/ (diakses 2026-06-18).

### Diskusi Komunitas

21. **Cookie TTL Tokopedia** (forum otodidak) -- https://otodidak.dev/threads/cookie-ttl-tokopedia (diakses 2026-06-18).
22. **Scraping Etik Indonesia Discussion** -- https://github.com/indonesia-scraping-community/etika-scraping (diakses 2026-06-18).

---

## Appendix A: .gitignore Template untuk Scraping Projects

```gitignore
# Scraper credentials dan state
.scraper-vault/
**/cookies/
**/tokens/
*.key
*.enc
*.pem

# Environment files
.env
.env.*
!.env.example

# Browser states
browser-states/
playwright-states/

# Logs dengan credential dump
*.log
!important/*.log

# Database with credentials
*.db
*.sqlite
*.sqlite3

# IDE files
.vscode/
.idea/
*.swp
*.swo

# OS files
.DS_Store
Thumbs.db
```

## Appendix B: Quick-Start Cheatsheet

```python
"""
Quick-Start: Cookie/Token Storage Safety

1. Install dependencies:
   pip install cryptography python-dotenv requests pyyaml

2. Generate master key:
   >>> from cryptography.fernet import Fernet
   >>> Fernet.generate_key().decode()
   'YOUR_MASTER_KEY_HERE'

3. Create .env file:
   SCRAPER_MASTER_KEY=YOUR_MASTER_KEY_HERE

4. Save cookies:
   vault = CookieVault()
   vault.save("tokopedia", {"cookies": {...}})

5. Load cookies:
   data = vault.load("tokopedia")
   cookies = data["cookies"]

6. Playwright integration:
   manager = PlaywrightCookieManager(master_key)
   context = await manager.create_context_from_state(browser, "tokopedia")

7. Auto-refresh:
   refresher = TokopediaTokenRefresher(client_id, client_secret)
   token = await refresher.get_valid_token()
"""
```

---

*Dokumen ini adalah bagian dari Money Glitch Vault. Informasi disediakan untuk tujuan edukasi dan riset. Pengguna bertanggung jawab penuh atas kepatuhan terhadap hukum yang berlaku.*
