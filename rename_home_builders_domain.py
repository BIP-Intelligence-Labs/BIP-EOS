"""
rename_home_builders_domain.py

Renames every UEOS "builders" domain directory to "home_builders".

Run from the repository root:

    python rename_home_builders_domain.py

Directories renamed:

    src/bip_eos/home_builders      -> src/bip_eos/home_builders
    plugins/home_builders          -> plugins/home_builders
    bip/home_builders              -> bip/home_builders
    bootstrap/home_builders        -> bootstrap/home_builders

Also updates references in source files.
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    ("src/bip_eos/home_builders", "src/bip_eos/home_builders"),
    ("plugins/home_builders", "plugins/home_builders"),
    ("bip/home_builders", "bip/home_builders"),
    ("bootstrap/home_builders", "bootstrap/home_builders"),
]

TEXT_EXTENSIONS = {
    ".py", ".md", ".txt", ".json", ".toml",
    ".yaml", ".yml", ".ini", ".cfg", ".rst"
}

REPLACEMENTS = [
    ("src/bip_eos/home_builders", "src/bip_eos/home_builders"),
    ("plugins/home_builders", "plugins/home_builders"),
    ("bip/home_builders", "bip/home_builders"),
    ("bootstrap/home_builders", "bootstrap/home_builders"),
    ("bip.home_builders", "bip.home_builders"),
    ("bip_eos.home_builders", "bip_eos.home_builders"),
    ("bootstrap.home_builders", "bootstrap.home_builders"),
    ("plugins.home_builders", "plugins.home_builders"),
]

print("=" * 60)
print("UEOS Domain Rename")
print("=" * 60)

for src_rel, dst_rel in DIRECTORIES:
    src = ROOT / src_rel
    dst = ROOT / dst_rel

    if not src.exists():
        print(f"SKIP : {src_rel} (not found)")
        continue

    if dst.exists():
        print(f"SKIP : {dst_rel} (already exists)")
        continue

    dst.parent.mkdir(parents=True, exist_ok=True)
    src.rename(dst)
    print(f"RENAMED: {src_rel} -> {dst_rel}")

updated = 0

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        continue

    try:
        original = path.read_text(encoding="utf-8")
    except Exception:
        continue

    text = original
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)

    if text != original:
        path.write_text(text, encoding="utf-8")
        updated += 1
        print(f"UPDATED: {path.relative_to(ROOT)}")

print("-" * 60)
print(f"Files updated: {updated}")
print("Migration complete.")
