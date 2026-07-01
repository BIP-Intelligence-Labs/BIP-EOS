"""
verify_c03.py

Verifies the C03 Token System layout.
"""

from pathlib import Path
import sys

ROOT = Path.cwd()

REQUIRED = [
    "src/bip_eos/compiler/token.py",
    "src/bip_eos/compiler/token_type.py",
    "src/bip_eos/compiler/keywords.py",
    "tests/unit/test_token.py",
    "tests/unit/test_token_type.py",
]

print("=" * 60)
print("BIP EOS")
print("Frontend Token Verification")
print("=" * 60)

missing = []

for rel in REQUIRED:
    path = ROOT / rel
    if path.exists():
        print(f"[PASS] {rel}")
    else:
        print(f"[FAIL] {rel}")
        missing.append(rel)

print("-" * 60)

if missing:
    print(f"Missing: {len(missing)} file(s)")
    sys.exit(1)

print("C03 Token System verification PASSED.")
sys.exit(0)
