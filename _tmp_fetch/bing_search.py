import re, html, urllib.parse, subprocess, sys

VPY = r"C:\Users\it26\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe"

def fetch(url, ua="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"):
    r = subprocess.run(["curl", "-sS", "-m", "25", "-A", ua, url],
                       capture_output=True, text=True)
    return r.stdout

def bing(q):
    txt = fetch("https://www.bing.com/search?q=" + urllib.parse.quote(q))
    # organic result blocks
    titles = re.findall(r'<li class="b_algo"[^>]*>.*?<h2[^>]*><a[^>]*href="([^"]+)"[^>]*>(.*?)</a>',
                        txt, re.S)
    out = []
    for u, title in titles[:12]:
        title = re.sub(r'<[^>]+>', '', title)
        title = html.unescape(title).strip()
        if u.startswith('http'):
            out.append((title, u))
    return out

if __name__ == "__main__":
    queries = sys.argv[1:]
    for q in queries:
        print("### QUERY:", q)
        for t, u in bing(q):
            print(" -", t)
            print("   ", u)
