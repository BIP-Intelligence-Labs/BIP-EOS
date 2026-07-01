#!/usr/bin/env python3
"""
========================================================================
UEOS
MGS-001 Architecture Refactor

Migration & Governance System
========================================================================

Refactors MGS-001 to the constitutional layout:

migration/
    engine.py
    services/
    governance/

Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path("src") / "bip_eos" / "migration"

SERVICES = [
    "__init__.py",
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

GOVERNANCE = [
    "__init__.py",
    "architecture.py",
    "standards.py",
    "policies.py",
    "compliance.py",
    "repository.py",
    "dependencies.py",
    "constitution.py",
]

def ensure_module(path: Path, title: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"[EXISTS ] {path}")
        return
    path.write_text(f'"""\nMGS-001\n{title}\n"""\n', encoding="utf-8")
    print(f"[CREATE ] {path}")

def main():
    print("=" * 72)
    print("MGS-001 Constitutional Refactor")
    print("=" * 72)

    ensure_module(ROOT / "__init__.py", "Migration & Governance System")
    ensure_module(ROOT / "engine.py", "Constitutional Orchestrator")

    services = ROOT / "services"
    governance = ROOT / "governance"

    services.mkdir(parents=True, exist_ok=True)
    governance.mkdir(parents=True, exist_ok=True)

    print(f"[ OK ] {services}")
    print(f"[ OK ] {governance}")

    for name in SERVICES:
        title = name.replace(".py", "").replace("_", " ").title()
        ensure_module(services / name, title)

    for name in GOVERNANCE:
        title = name.replace(".py", "").replace("_", " ").title()
        ensure_module(governance / name, title)

    print("=" * 72)
    print("Recommended Structure")
    print("=" * 72)
    print(r"""
migration/
├── engine.py
├── services/
│   ├── planner.py
│   ├── executor.py
│   ├── validator.py
│   ├── rollback.py
│   ├── reporter.py
│   ├── repository.py
│   ├── registry.py
│   ├── graph.py
│   ├── runtime.py
│   ├── compiler.py
│   └── knowledge.py
└── governance/
    ├── architecture.py
    ├── standards.py
    ├── policies.py
    ├── compliance.py
    ├── repository.py
    ├── dependencies.py
    └── constitution.py
""")
    print("=" * 72)
    print("NOTE: Existing 'engine/' package can be removed after")
    print("any implementation files have been migrated into 'services/'.")
    print("=" * 72)

if __name__ == "__main__":
    main()
