import re, sys, pathlib

PATTERNS = [r"AKIA[0-9A-Z]{16}", r"(?i)(api_key|secret|password)\s*=\s*['\"][^'\"]+['\"]"]
IGNORE = {".env.example", "secret_scan.py"}

failed = False
for p in pathlib.Path(".").rglob("*"):
    if p.is_file() and ".git" not in p.parts and p.name not in IGNORE:
        text = p.read_text(errors="ignore")
        for pat in PATTERNS:
            if re.search(pat, text):
                print(f"[BLOCKED] Potential secret in {p}")
                failed = True
sys.exit(1 if failed else 0)
