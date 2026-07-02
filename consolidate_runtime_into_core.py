"""
consolidate_runtime_into_core.py

Consolidates foundational infrastructure from src/ueos/runtime into
src/ueos/core, updates architecture documentation, and removes duplicate
runtime packages when they are empty.

Run:
    python consolidate_runtime_into_core.py
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

MAPPINGS = {
    "configuration": "configuration",
    "dependency_injection": "dependency_injection",
    "event_bus": "event_bus",
    "lifecycle": "lifecycle",
}

CORE = ROOT / "src" / "ueos" / "core"
RUNTIME = ROOT / "src" / "ueos" / "runtime"
ARCH = ROOT / "engineering" / "architecture" / "UEOS-001"
DOC = ARCH / "CORE_RUNTIME_BOUNDARY.md"

DOC_TEXT = """# CORE / RUNTIME BOUNDARY

## ueos.core (Platform Infrastructure)

- kernel
- configuration
- dependency_injection
- event_bus
- lifecycle
- platform
- service_registry

## ueos.runtime (Runtime Services)

- diagnostics
- health
- logging
- plugins
- registry
- scheduler
- security
- service_host
- telemetry
- version

## Dependency Rule

Allowed:
runtime --> core

Forbidden:
core --> runtime
"""

def move_contents(src: Path, dst: Path):
    if not src.exists():
        return
    dst.mkdir(parents=True, exist_ok=True)
    for item in list(src.iterdir()):
        target = dst / item.name
        if item.name == "__pycache__":
            continue
        if item.is_dir():
            if target.exists():
                move_contents(item, target)
                if not any(item.iterdir()):
                    item.rmdir()
            else:
                shutil.move(str(item), str(target))
                print(f"[MOVE DIR] {item} -> {target}")
        else:
            if target.exists():
                print(f"[KEEP] {target}")
            else:
                shutil.move(str(item), str(target))
                print(f"[MOVE FILE] {item} -> {target}")

def cleanup(path: Path):
    if not path.exists():
        return
    remaining = [p for p in path.iterdir() if p.name != "__pycache__"]
    if not remaining:
        shutil.rmtree(path)
        print(f"[REMOVE] {path}")
    elif all(p.name == "__init__.py" and p.stat().st_size == 0 for p in remaining if p.is_file()) and not any(p.is_dir() for p in remaining):
        shutil.rmtree(path)
        print(f"[REMOVE EMPTY] {path}")
    else:
        print(f"[REVIEW] {path} still contains content")

def main():
    print("=== UEOS Core Consolidation ===")
    for rt_name, core_name in MAPPINGS.items():
        src = RUNTIME / rt_name
        dst = CORE / core_name
        move_contents(src, dst)
        cleanup(src)

    ARCH.mkdir(parents=True, exist_ok=True)
    DOC.write_text(DOC_TEXT, encoding="utf-8")
    print(f"[DOC] Updated {DOC}")

    print("\nComplete. Run tests and import validation before committing.")

if __name__ == "__main__":
    main()
