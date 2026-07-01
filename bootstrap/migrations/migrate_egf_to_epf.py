#!/usr/bin/env python3
from pathlib import Path
import argparse

TEXT_EXTENSIONS={".md",".txt",".py",".json",".yaml",".yml",".toml",".rst",".cfg",".ini"}
REPLACEMENTS=[
("Engineering Publishing Framework","Engineering Publishing Framework"),
("Engineering Publishing System","Engineering Publishing System"),
("Engineering Publishing Engine","Engineering Publishing Engine"),
("EPF","EPF"),
]
SKIP_DIRS={".git","__pycache__",".venv","venv","node_modules",".mypy_cache",".pytest_cache"}

def find_repo_root(start: Path)->Path:
    cur=start.resolve()
    while cur!=cur.parent:
        if (cur/"bootstrap").exists() and (cur/"src").exists():
            return cur
        cur=cur.parent
    raise RuntimeError("Unable to locate UEOS repository root.")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--apply",action="store_true")
    args=ap.parse_args()
    root=find_repo_root(Path(__file__).parent)
    scanned=modified=0
    print("="*72)
    print("UEOS Migration: EPF -> EPF")
    print("Mode:", "APPLY" if args.apply else "DRY RUN")
    print("="*72)
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(p in SKIP_DIRS for p in path.parts):
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        scanned+=1
        try:
            original=path.read_text(encoding="utf-8")
        except Exception:
            continue
        updated=original
        for old,new in REPLACEMENTS:
            updated=updated.replace(old,new)
        if updated!=original:
            modified+=1
            print("[CHANGE]", path.relative_to(root))
            if args.apply:
                path.write_text(updated,encoding="utf-8")
    print("-"*72)
    print("Files scanned :",scanned)
    print("Files changed :",modified)
    print("Repository modified." if args.apply else "Dry run complete. No files changed.")
if __name__=="__main__":
    main()
