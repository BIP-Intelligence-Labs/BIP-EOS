#!/usr/bin/env python3
"""
bootstrap_domain_architecture.py
"""

from pathlib import Path

ROOT = Path.cwd()

DOMAINS = {
    "lead": ["__init__.py","model.py","repository.py","service.py","validator.py","api.py"],
    "builder": ["__init__.py","model.py","repository.py","service.py","matcher.py"],
    "community": ["__init__.py","model.py","repository.py","service.py","matcher.py"],
    "inventory": ["__init__.py","model.py","repository.py","service.py","matcher.py"],
    "questionnaire": ["__init__.py","model.py","repository.py","service.py","engine.py"],
    "recommendation": ["__init__.py","engine.py","repository.py","service.py","scoring.py"],
    "report": ["__init__.py","generator.py","templates.py","service.py"],
    "appointment": ["__init__.py","model.py","repository.py","service.py"],
}

HEADER = '"""BIP EOS Domain Module."""\n\nfrom __future__ import annotations\n'

print("=" * 70)
print("BIP EOS Domain Architecture Bootstrap")
print("=" * 70)

created = 0
skipped = 0

base = ROOT / "src" / "bip_eos" / "builders"

for domain, files in DOMAINS.items():
    domain_dir = base / domain
    domain_dir.mkdir(parents=True, exist_ok=True)
    print(f"[DIR ] {domain_dir}")

    for filename in files:
        path = domain_dir / filename
        if path.exists():
            print(f"[SKIP] {path}")
            skipped += 1
            continue

        if filename == "__init__.py":
            content = f'"""{domain.title()} domain."""\n'
        else:
            content = HEADER

        path.write_text(content, encoding="utf-8")
        print(f"[FILE] {path}")
        created += 1

print("-" * 70)
print(f"Created : {created}")
print(f"Skipped : {skipped}")
print("Domain architecture ready.")
