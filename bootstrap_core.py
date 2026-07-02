"""
bootstrap_core.py

Creates the UEOS Core Platform directory structure.

Usage:
    python bootstrap_core.py
    python bootstrap_core.py C:\Project\BIP-Intelligence-Labs\genesis
"""

from pathlib import Path
import sys

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

CORE = ROOT / "src" / "ueos" / "core"

DIRECTORIES = [
    "kernel",
    "lifecycle",
    "configuration",
    "dependency_injection",
    "event_bus",
    "service_registry",
    "platform",
]

README = """# UEOS Core

The UEOS Core Platform provides the foundational services used by
all runtime subsystems.

Subpackages:
- kernel
- lifecycle
- configuration
- dependency_injection
- event_bus
- service_registry
- platform
"""

INIT = '"""UEOS Core Package."""\n'

def ensure(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    init = path / "__init__.py"
    if not init.exists():
        init.write_text(INIT, encoding="utf-8")

def main():
    ensure(CORE)
    readme = CORE / "README.md"
    if not readme.exists():
        readme.write_text(README, encoding="utf-8")

    for name in DIRECTORIES:
        pkg = CORE / name
        ensure(pkg)
        placeholder = pkg / "README.md"
        if not placeholder.exists():
            placeholder.write_text(f"# {name.replace('_',' ').title()}\n", encoding="utf-8")

    print("\\nUEOS Core Platform created successfully.")
    print(f"Location: {CORE}")

if __name__ == "__main__":
    main()
