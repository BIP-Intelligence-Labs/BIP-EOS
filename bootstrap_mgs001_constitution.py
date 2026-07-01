#!/usr/bin/env python3
"""
========================================================================
MGS-001

Migration & Governance System

Constitutional Architecture
========================================================================
"""

ARCHITECTURE = r"""
MGS-001
Migration & Governance System
        │
        ├────────────────────────────────────────────┐
        │                                            │
        ▼                                            ▼
Migration Engine                             Governance Engine
        │                                            │
        │                                            │
        ├── Repository Migration                     ├── Architecture Rules
        ├── Registry Migration                       ├── Engineering Standards
        ├── Graph Migration                          ├── Policy Enforcement
        ├── Runtime Migration                        ├── Compliance Validation
        ├── Compiler Migration                       ├── Repository Governance
        ├── Knowledge Migration                      ├── Dependency Governance
        └── Upgrade Planning                         └── Constitutional Validation
"""

DIRECTORIES = [
    "src/bip_eos/migration",
    "src/bip_eos/migration/engine",
    "src/bip_eos/migration/governance",
]

ENGINE_MODULES = [
    "planner.py",
    "executor.py",
    "validator.py",
    "rollback.py",
    "reporter.py",
    "repository.py",
    "registry.py",
    "graph.py",
    "runtime.py",
    "compiler.py",
    "knowledge.py",
]

GOVERNANCE_MODULES = [
    "architecture.py",
    "standards.py",
    "policies.py",
    "compliance.py",
    "repository.py",
    "dependencies.py",
    "constitution.py",
]

def ensure(path):
    path.mkdir(parents=True, exist_ok=True)

def touch_module(path, title):
    if not path.exists():
        path.write_text(
f'"""\nMGS-001\n{title}\n"""\n',
            encoding="utf-8"
        )

def main():
    from pathlib import Path

    print("=" * 72)
    print("MGS-001 Constitutional Installer")
    print("=" * 72)

    for d in DIRECTORIES:
        ensure(Path(d))
        print("[ OK ]", d)

    touch_module(Path("src/bip_eos/migration/engine.py"),
                 "Migration Engine")
    touch_module(Path("src/bip_eos/migration/models.py"),
                 "Migration Models")
    touch_module(Path("src/bip_eos/migration/index.py"),
                 "Migration Index")
    touch_module(Path("src/bip_eos/migration/serializer.py"),
                 "Migration Serializer")
    touch_module(Path("src/bip_eos/migration/rules.py"),
                 "Governance Rules")

    eng = Path("src/bip_eos/migration/engine")
    gov = Path("src/bip_eos/migration/governance")

    for m in ENGINE_MODULES:
        touch_module(eng / m, m.replace(".py","").replace("_"," ").title())

    for m in GOVERNANCE_MODULES:
        touch_module(gov / m, m.replace(".py","").replace("_"," ").title())

    print()
    print(ARCHITECTURE)
    print("=" * 72)

if __name__ == "__main__":
    main()
