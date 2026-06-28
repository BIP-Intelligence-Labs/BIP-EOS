"""
restructure_genesis.py

Fixes the accidental genesis/genesis nesting created during bootstrap.

Run from:
C:\Project\BIP-Intelligence-Labs\genesis

It will move bootstrap/ out of the nested genesis folder,
create common top-level folders, and remove the empty nested folder.
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

nested = ROOT / "genesis"
bootstrap_src = nested / "bootstrap"
bootstrap_dst = ROOT / "bootstrap"

if bootstrap_src.exists():
    if bootstrap_dst.exists():
        print("bootstrap already exists at destination. Nothing moved.")
    else:
        print("Moving bootstrap...")
        shutil.move(str(bootstrap_src), str(bootstrap_dst))

for name in ["archive", "docs", "scripts", "shared", "discovery", "ai", "media", "bip"]:
    (ROOT / name).mkdir(exist_ok=True)

# remove nested folder if empty
if nested.exists():
    try:
        nested.rmdir()
        print("Removed empty nested genesis folder.")
    except OSError:
        print("Nested genesis folder not empty; review remaining files.")

print("\nRepository structure:")
for p in sorted(ROOT.iterdir()):
    if p.is_dir():
        print(f"  📁 {p.name}")
