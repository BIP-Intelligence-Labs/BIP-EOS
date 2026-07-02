"""
namespace_migrator_v2.py

Enterprise namespace migration tool.

Features:
- Dry-run by default
- Include path filtering
- Exclude path filtering
- Migration report
- Skips archive/history by default

Usage:
  python namespace_migrator_v2.py --dry-run
  python namespace_migrator_v2.py --apply
"""

from pathlib import Path
import argparse

DEFAULT_INCLUDE = ["src", "tests", ".github", "engineering"]
DEFAULT_EXCLUDE = {
    ".git",".venv","venv","build","dist","__pycache__",
    "archive","tools/archive","tools/migrations","reports"
}

TEXT_EXTS={".py",".md",".toml",".yaml",".yml",".json",".ini",".cfg",".txt"}

REPLACEMENTS=[
    ("from bip_eos","from ueos"),
    ("import bip_eos","import ueos"),
    ("bip_eos.","ueos."),
    ('"bip_eos"','"ueos"'),
    ("'bip_eos'","'ueos'")
]

def skip(path:Path):
    s=path.as_posix()
    return any(e in s for e in DEFAULT_EXCLUDE)

def included(path:Path):
    s=path.as_posix()
    return any(s.startswith(p+"/") or s==p for p in DEFAULT_INCLUDE)

def process(path:Path, apply:bool):
    try:
        txt=path.read_text(encoding="utf-8")
    except Exception:
        return False
    new=txt
    changed=False
    for a,b in REPLACEMENTS:
        if a in new:
            new=new.replace(a,b)
            changed=True
    if changed and apply:
        path.write_text(new,encoding="utf-8")
    return changed

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--apply",action="store_true")
    ap.add_argument("--dry-run",action="store_true")
    args=ap.parse_args()

    root=Path.cwd()
    report=[]
    for f in root.rglob("*"):
        if not f.is_file(): continue
        rel=f.relative_to(root)
        if f.suffix.lower() not in TEXT_EXTS: continue
        if skip(rel): continue
        if not included(rel): continue
        if process(f,args.apply):
            report.append(rel.as_posix())
            print(("[UPDATE]" if args.apply else "[WOULD UPDATE]"),rel)

    rep=root/"reports"
    rep.mkdir(exist_ok=True)
    out=rep/"namespace_migration_v2.md"
    lines=["# Namespace Migration v2","","Mode: "+("APPLY" if args.apply else "DRY RUN"),"",f"Files: {len(report)}",""]
    lines.extend(f"- {x}" for x in report)
    out.write_text("\n".join(lines),encoding="utf-8")
    print(f"\nReport: {out}")
    print(f"Files {'updated' if args.apply else 'identified'}: {len(report)}")

if __name__=="__main__":
    main()
