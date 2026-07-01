#!/usr/bin/env python3
"""
========================================================================
UEOS
UEG-001 Bootstrap Installer

Universal Engineering Graph
========================================================================
"""

from pathlib import Path

ROOT = Path("src") / "bip_eos" / "graph"

FILES = {
    "__init__.py": '"""UEG-001 Universal Engineering Graph."""\n',
    "engine.py": '"""GraphEngine orchestrator."""\n',
    "models.py": '"""Graph models."""\n',
    "index.py": '"""Graph index."""\n',
    "storage.py": '"""Graph storage."""\n',
}

SERVICES = [
    "node.py",
    "edge.py",
    "builder.py",
    "query.py",
    "traversal.py",
    "serializer.py",
    "validator.py",
    "reporter.py",
]

def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"[EXISTS ] {path}")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"[CREATE ] {path}")

def main():
    print("="*72)
    print("UEG-001 Bootstrap Installer")
    print("="*72)

    for name, content in FILES.items():
        write(ROOT / name, content)

    write(ROOT / "services" / "__init__.py",
          '"""Graph services."""\n')

    for svc in SERVICES:
        title = svc.replace(".py","").title()
        write(ROOT / "services" / svc,
              f'"""\nUEG-001\n{title}\n"""\n')

    print("="*72)
    print("Architecture")
    print("="*72)
    print(r"""
src/
└── bip_eos/
    └── graph/
        ├── __init__.py
        ├── engine.py
        ├── models.py
        ├── index.py
        ├── storage.py
        └── services/
            ├── __init__.py
            ├── node.py
            ├── edge.py
            ├── builder.py
            ├── query.py
            ├── traversal.py
            ├── serializer.py
            ├── validator.py
            └── reporter.py
""")
    print("="*72)

if __name__ == "__main__":
    main()
