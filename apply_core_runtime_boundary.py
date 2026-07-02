"""
apply_core_runtime_boundary.py

Synchronizes the UEOS architecture by documenting the official
responsibilities of src/ueos/core and src/ueos/runtime.

Usage:
    python apply_core_runtime_boundary.py
"""

from pathlib import Path

ROOT = Path.cwd()

CORE_PKGS = [
    "kernel",
    "configuration",
    "dependency_injection",
    "event_bus",
    "lifecycle",
    "platform",
    "service_registry",
]

RUNTIME_PKGS = [
    "diagnostics",
    "health",
    "logging",
    "plugins",
    "scheduler",
    "security",
    "service_host",
    "telemetry",
    "version",
]

DOC = f"""# UEOS Core / Runtime Boundary

## src/ueos/core

The **Core Platform** contains foundational infrastructure shared by every
UEOS subsystem.

Packages:
{chr(10).join(f"- {x}" for x in CORE_PKGS)}

---

## src/ueos/runtime

The **Runtime** contains executable runtime services built on top of
`ueos.core`.

Packages:
{chr(10).join(f"- {x}" for x in RUNTIME_PKGS)}

---

## Dependency Rule

Allowed:

runtime ---> core

Forbidden:

core -/-> runtime

Core must never import Runtime.
"""

def ensure_readme(path: Path, title: str):
    path.mkdir(parents=True, exist_ok=True)
    readme = path / "README.md"
    if not readme.exists():
        readme.write_text(f"# {title}\n", encoding="utf-8")

def main():
    core = ROOT / "src" / "ueos" / "core"
    runtime = ROOT / "src" / "ueos" / "runtime"

    for pkg in CORE_PKGS:
        ensure_readme(core / pkg, pkg.replace("_"," ").title())

    for pkg in RUNTIME_PKGS:
        ensure_readme(runtime / pkg, pkg.replace("_"," ").title())

    arch = ROOT / "engineering" / "architecture" / "UEOS-001"
    arch.mkdir(parents=True, exist_ok=True)
    (arch / "CORE_RUNTIME_BOUNDARY.md").write_text(DOC, encoding="utf-8")

    print("UEOS architectural boundary updated.")
    print(f"Documentation: {arch/'CORE_RUNTIME_BOUNDARY.md'}")

if __name__ == "__main__":
    main()
