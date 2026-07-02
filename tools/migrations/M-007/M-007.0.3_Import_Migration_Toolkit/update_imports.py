"""Enterprise Import Migrator (starter)."""
import argparse
from pathlib import Path
SKIP={".git",".venv","venv","__pycache__","archive","backup"}
def files():
    for p in Path.cwd().rglob("*.py"):
        if any(x in p.parts for x in SKIP): continue
        yield p
def run(dry=False):
    changed=0
    for f in files():
        t=f.read_text(encoding="utf-8",errors="ignore")
        n=t.replace("from bip_eos","from ueos").replace("import bip_eos","import ueos")
        if n!=t:
            changed+=1
            if not dry: f.write_text(n,encoding="utf-8")
    print(f"Modified: {changed}")
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--dry-run",action="store_true")
    run(ap.parse_args().dry_run)
