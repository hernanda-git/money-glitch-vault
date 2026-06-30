try:
    import telethon
    print(f"telethon: {telethon.__version__}")
except ImportError:
    print("telethon: NOT INSTALLED")

try:
    import httpx
    print(f"httpx: {httpx.__version__}")
except ImportError:
    print("httpx: NOT INSTALLED")

try:
    import dotenv
    print(f"dotenv: OK")
except ImportError:
    print("dotenv: NOT INSTALLED")
