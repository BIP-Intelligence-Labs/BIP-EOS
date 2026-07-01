"""
rename_business_domains.py

UEOS Atlas Migration
--------------------
Normalizes business-domain package names.

Run from repository root:

    python rename_business_domains.py
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path.cwd()

RENAMES = [
    ("src/bip_eos/home_builders/community", "src/bip_eos/home_builders/home_communities"),
    ("src/bip_eos/home_builders/inventory", "src/bip_eos/home_builders/inventory_homes"),
    ("src/bip_eos/home_builders/builder", "src/bip_eos/home_builders/home_builder"),
    ("src/bip_eos/home_builders/recommendation", "src/bip_eos/home_builders/recommendations"),
    ("src/bip_eos/home_builders/report", "src/bip_eos/home_builders/buyer_reports"),
]

TEXT_EXTENSIONS = {
    ".py",".md",".toml",".json",".yaml",".yml",".ini",".cfg",".txt",".rst"
}

REPLACEMENTS = [
    ("home_builders.home_communities", "home_builders.home_communities"),
    ("home_builders.inventory_homes", "home_builders.inventory_homes_homes"),
    ("home_builders.home_builder", "home_builders.home_builder"),
    ("home_builders.recommendations", "home_builders.recommendationss"),
    ("home_builders.buyer_reports", "home_builders.buyer_reports"),
    ("/home_communities/", "/home_communities/"),
    ("/inventory_homes/", "/inventory_homes/"),
    ("/home_builder/", "/home_builder/"),
    ("/recommendations/", "/recommendations/"),
    ("/buyer_reports/", "/buyer_reports/"),
    ("\\home_communities\\", "\\home_communities\\"),
    ("\\inventory_homes\\", "\\inventory_homes\\"),
    ("\\home_builder\\", "\\home_builder\\"),
    ("\\recommendations\\", "\\recommendations\\"),
    ("\\buyer_reports\\", "\\buyer_reports\\"),
]

print("="*60)
print("UEOS Business Domain Migration")
print("="*60)

renamed = 0
updated = 0

for src_rel, dst_rel in RENAMES:
    src = ROOT / src_rel
    dst = ROOT / dst_rel
    if not src.exists():
        print(f"SKIP : {src_rel}")
        continue
    if dst.exists():
        print(f"SKIP : {dst_rel} (already exists)")
        continue
    dst.parent.mkdir(parents=True, exist_ok=True)
    src.rename(dst)
    renamed += 1
    print(f"RENAMED: {src_rel} -> {dst_rel}")

for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
        continue
    try:
        original = path.read_text(encoding="utf-8")
    except Exception:
        continue
    text = original
    for old,new in REPLACEMENTS:
        text = text.replace(old,new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        updated += 1
        print(f"UPDATED: {path.relative_to(ROOT)}")

print("-"*60)
print(f"Directories renamed : {renamed}")
print(f"Files updated       : {updated}")
print("Migration complete.")
