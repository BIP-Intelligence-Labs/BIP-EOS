"""
consolidate_configuration.py
"""
from pathlib import Path
import shutil

ROOT = Path.cwd()
CORE = ROOT / "src" / "ueos" / "core" / "configuration"
RUNTIME = ROOT / "src" / "ueos" / "runtime" / "configuration"

def move_file(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        print(f"[KEEP] {dst.relative_to(ROOT)}")
        return
    shutil.move(str(src), str(dst))
    print(f"[MOVE] {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}")

def main():
    print("="*68)
    print("UEOS Configuration Consolidation")
    print("="*68)
    if not RUNTIME.exists():
        print("Runtime configuration package not found.")
        return
    CORE.mkdir(parents=True, exist_ok=True)
    for file in sorted(RUNTIME.glob("*.py")):
        if file.name == "__init__.py":
            continue
        move_file(file, CORE / file.name)
    shim = RUNTIME / "__init__.py"
    shim.write_text("""\"""
Compatibility layer.

Deprecated: import from ueos.core.configuration
\"""

from ueos.core.configuration import *
""", encoding="utf-8")
    print("Configuration consolidation complete.")
    print("Run: pytest")

if __name__ == "__main__":
    main()