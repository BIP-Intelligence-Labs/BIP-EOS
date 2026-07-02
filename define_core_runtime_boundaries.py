"""
define_core_runtime_boundaries.py

Creates a markdown document defining the architectural boundary between
ueos.core and ueos.runtime.

Usage:
    python define_core_runtime_boundaries.py
"""

from pathlib import Path

DOC = """# UEOS Core vs Runtime Boundary

## Rule

`ueos.core` contains platform infrastructure.

`ueos.runtime` contains runtime services built on top of `ueos.core`.

---

## ueos.core

Stable foundational components:

- kernel
- lifecycle
- dependency_injection
- event_bus
- service_registry
- configuration
- platform

These packages should have minimal external dependencies and may be used
by every other UEOS subsystem.

---

## ueos.runtime

Runtime services:

- scheduler
- telemetry
- diagnostics
- health
- logging
- plugins
- registry
- security
- service_host

Runtime services consume `ueos.core` but `ueos.core` must never depend on
`ueos.runtime`.

---

## Dependency Rule

Allowed:

    runtime  ---> core

Not allowed:

    core ----> runtime

This prevents circular dependencies and keeps the platform foundation
stable.
"""

def main():
    root = Path.cwd()
    target = root / "engineering" / "architecture" / "UEOS-001"
    target.mkdir(parents=True, exist_ok=True)
    outfile = target / "CORE_RUNTIME_BOUNDARY.md"
    outfile.write_text(DOC, encoding="utf-8")
    print(f"Created: {outfile}")

if __name__ == "__main__":
    main()
