"""
vault.py — encrypted at-rest cookie/token store for the scraper module.

Safe-room standard for money-glitch-vault/01-crawler-scrapper/cookies-tokens.
See storage-safety.md for the full threat model and rationale.

Design guarantees:
  * No live credential is ever written to disk in plaintext.
  * The key-encryption-key (KEK) comes from the OS keyring, or is derived
    from MG_VAULT_PASSPHRASE via PBKDF2-HMAC-SHA256 (600k iterations).
  * Encrypted blobs go in local/ (git-ignored). Nothing here is committed.
  * MultiFernet supports zero-downtime KEK rotation.

This file contains NO secrets. It is safe to commit.
"""
from __future__ import annotations

import base64
import json
import os
import secrets
from pathlib import Path

from cryptography.fernet import Fernet, MultiFernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

VAULT_DIR = Path(__file__).parent / "local"
VAULT_PATH = VAULT_DIR / "cookies.enc"
SALT_PATH = VAULT_DIR / "kek.salt"
SERVICE, SLOT = "money-glitch-vault", "scraper-kek"
PBKDF2_ITERATIONS = 600_000


def _keyring_kek() -> bytes | None:
    import keyring
    v = keyring.get_password(SERVICE, SLOT)
    if not v:
        return None
    if "plaintext" in type(keyring.get_keyring()).__name__.lower():
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
                      salt=SALT_PATH.read_bytes(), iterations=PBKDF2_ITERATIONS)
    return dk.derive(phrase.encode())


def _load_ring() -> MultiFernet:
    import keyring
    raw = keyring.get_password(SERVICE, SLOT + ":ring")
    if raw:
        keys = [Fernet(k.encode()) for k in json.loads(raw)]
    else:
        kek = _keyring_kek() or _pbkdf2_kek()
        fk = Fernet(base64.urlsafe_b64encode(kek))
        keys = [fk]
        keyring.set_password(SERVICE, SLOT + ":ring",
                             json.dumps([fk._signing_key.decode()]))
    return MultiFernet(keys)


class CookieVault:
    """Encrypt/decrypt a credentials dict. Callers import this from elsewhere."""

    def __init__(self) -> None:
        self._mf = _load_ring()
        VAULT_DIR.mkdir(parents=True, exist_ok=True)

    def save(self, cookies: dict) -> None:
        tmp = VAULT_PATH.with_suffix(".enc.tmp")
        tmp.write_bytes(self._mf.encrypt(json.dumps(cookies).encode()))
        os.replace(tmp, VAULT_PATH)  # atomic

    def load(self) -> dict:
        if not VAULT_PATH.exists():
            return {}
        try:
            return json.loads(self._mf.decrypt(VAULT_PATH.read_bytes()))
        except InvalidToken:
            raise RuntimeError("Vault integrity failure: KEK mismatch or tamper")

    def rotate_kek(self) -> None:
        import keyring
        new_raw = base64.urlsafe_b64encode(secrets.token_bytes(32))
        new = Fernet(new_raw)
        old_ring = json.loads(keyring.get_password(SERVICE, SLOT + ":ring") or "[]")
        old_ring.insert(0, new_raw.decode())
        keyring.set_password(SERVICE, SLOT + ":ring", json.dumps(old_ring))
        self._mf = MultiFernet([new] + [Fernet(k.encode()) for k in old_ring[1:]])
        self.save(self.load())


if __name__ == "__main__":
    # smoke test: round-trips an empty->sample->empty vault
    v = CookieVault()
    v.save({"smoke": "test"})
    assert v.load()["smoke"] == "test"
    print("vault.py OK")
