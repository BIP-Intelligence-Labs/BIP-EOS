#!/usr/bin/env python3
from __future__ import annotations
import argparse, shutil
from pathlib import Path

TEXT_EXTENSIONS={".py",".md",".txt",".toml",".yaml",".yml",".json",".ini",".cfg"}
REPLACEMENTS=[
("from genesis","from bip_eos"),
("import genesis","import bip_eos"),
("genesis.","bip_eos."),
("BIP EOS Engineering Operating System","BIP EOS Engineering Operating System"),
]
SKIP={".git","__pycache__",".venv","venv","node_modules",".pytest_cache",".mypy_cache"}

def should_skip(path):
    return any(p in SKIP for p in path.parts)

def process(path, execute):
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return False
    try:
        text=path.read_text(encoding="utf-8")
    except Exception:
        return False
    new=text
    for a,b in REPLACEMENTS:
        new=new.replace(a,b)
    if new==text:
        return False
    print("[UPDATE]",path)
    if execute:
        path.write_text(new,encoding="utf-8")
    return True

def rename_pkg(root, execute):
    src=root/"src"/"genesis"
    dst=root/"src"/"bip_eos"
    if src.exists():
        print("[RENAME]",src,"->",dst)
        if execute and not dst.exists():
            shutil.move(str(src),str(dst))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--execute",action="store_true")
    args=ap.parse_args()
    root=Path.cwd()
    print("BIP EOS Rename Utility")
    print("Mode:", "EXECUTE" if args.execute else "DRY RUN")
    count=0
    for p in root.rglob("*"):
        if p.is_file() and not should_skip(p):
            if process(p,args.execute):
                count+=1
    rename_pkg(root,args.execute)
    print("Files requiring updates:",count)
    print("Codename remains: Genesis")

if __name__=="__main__":
    main()
