#!/usr/bin/env python3
"""
========================================================================
UEOS
ERS-001 Bootstrap Installer

Engineering Registry System
========================================================================
"""

from pathlib import Path

ROOT = Path("src") / "bip_eos" / "registry"

FILES = {
    "__init__.py": '"""\nERS-001\nEngineering Registry System\n"""\n',
    "engine.py": '"""\nERS-001\n\nRegistry Engine\n\nOrchestrates the Engineering Registry lifecycle.\n"""\n',
    "models.py": '"""\nERS-001\n\nRegistry Models\n\nRegistryEntry\n"""\n',
    "ids.py": '"""\nERS-001\n\nEngineering ID Generator\n"""\n',
    "resolver.py": '"""\nERS-001\n\nIdentity Resolver\n"""\n',
    "store.py": '"""\nERS-001\n\nRegistry Store\n"""\n',
    "validator.py": '"""\nERS-001\n\nRegistry Validator\n"""\n',
    "serializer.py": '"""\nERS-001\n\nRegistry Serializer\n"""\n',
    "index.py": '"""\nERS-001\n\nRegistry Index\n"""\n',
}

REGISTRY_JSON = """{
    "version": "1.0",
    "entries": []
}
"""

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"[EXISTS ] {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"[CREATE ] {path}")

def main():
    print("=" * 72)
    print("ERS-001 Bootstrap Installer")
    print("=" * 72)
    for name, content in FILES.items():
        write(ROOT / name, content)
    reg = ROOT / "registry.json"
    if reg.exists():
        print(f"[EXISTS ] {reg}")
    else:
        reg.write_text(REGISTRY_JSON, encoding="utf-8")
        print(f"[CREATE ] {reg}")
    print("=" * 72)
    print("ERS-001 structure installed.")
    print("=" * 72)

if __name__ == "__main__":
    main()
