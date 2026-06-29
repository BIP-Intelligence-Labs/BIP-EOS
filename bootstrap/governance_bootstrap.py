#!/usr/bin/env python3
from pathlib import Path

ROOT = Path.cwd()

RULES = '''# BIP EOS Development Rules

## Repository Rules

1. All NEW development goes into `src/bip_eos/`.
2. `src/genesis/` is READ-ONLY.
3. Changes to `src/genesis/` are allowed only for migration fixes, critical bug fixes, and compatibility shims.

## Production
- src/
- docs/
- tests/

## Developer Tooling
- bootstrap/
- engineering/
- tools/

## Runtime Assets
- logs/
- registry/
- reports/
- plugins/

## CLI Vision

bip bootstrap
bip doctor
bip audit
bip docs
bip migrate
bip registry
bip plugins
'''

FILES = {
    "src/bip_eos/config/__init__.py": '"""Configuration package."""\n',
    "src/bip_eos/config/settings.py": '"""Application settings."""\n',
    "src/bip_eos/config/environment.py": '"""Environment helpers."""\n',
    "src/bip_eos/config/constants.py": 'PRODUCT = "BIP EOS"\nCODENAME = "Genesis"\nVERSION = "0.1.0"\n',
    "engineering/governance/BIP_EOS_DEVELOPMENT_RULES.md": RULES,
}

def ensure(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.write_text(content, encoding="utf-8")
        print(f"[FILE] {path}")

print("="*70)
print("BIP EOS Governance Bootstrap")
print("="*70)

for rel, content in FILES.items():
    ensure(ROOT / rel, content)

print("-"*70)
print("Governance rules installed.")
print("Configuration package created.")
