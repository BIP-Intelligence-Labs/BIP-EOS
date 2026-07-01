from pathlib import Path
import sys

ROOT = Path.cwd()

REQUIRED = [
    "src/bip_eos/compiler/frontend/lexer.py",
    "src/bip_eos/compiler/frontend/scanner.py",
    "src/bip_eos/compiler/frontend/source_file.py",
    "src/bip_eos/compiler/frontend/position.py",
    "src/bip_eos/compiler/frontend/span.py",

    "src/bip_eos/compiler/token.py",
    "src/bip_eos/compiler/token_type.py",
    "src/bip_eos/compiler/keywords.py",

    "tests/unit/test_lexer.py",
]

print("VERIFY VERSION 2")

missing = []

for rel in REQUIRED:
    if (ROOT / rel).exists():
        print("[PASS]", rel)
    else:
        print("[FAIL]", rel)
        missing.append(rel)

sys.exit(1 if missing else 0)