#!/usr/bin/env python3
"""
========================================================================
UEOS
ERS-001 Architecture Documentation Installer
========================================================================
"""

from pathlib import Path

ROOT = Path("engineering") / "architecture" / "ERS-001"

FILES = {
    "ADR-001-Registry-Architecture.md": """# ADR-001 — ERS-001 Registry Architecture

## Status
Accepted

## Decision

ERS-001 SHALL be implemented as an orchestration engine with dedicated
constitutional services.

RegistryEngine
    ├── IdentityResolver
    ├── RegistryStore
    ├── RegistryValidator
    ├── RegistrySerializer
    └── RegistryIndex

## Rationale

- Single Responsibility Principle
- Stable constitutional identities
- Storage independence
- Extensible architecture
- Reusable engineering services
""",
    "Component-Diagram.md": """# ERS-001 Component Diagram

```text
RegistryEngine
        │
        ├──► IdentityResolver
        ├──► RegistryStore
        ├──► RegistryValidator
        ├──► RegistrySerializer
        └──► RegistryIndex
```
""",
    "Sequence-Diagram.md": """# ERS-001 Build Sequence

```text
ueos registry build
        │
        ▼
AuditEngine
        │
        ▼
EngineeringEvidence
        │
        ▼
IdentityResolver
        │
        ▼
RegistryValidator
        │
        ▼
RegistrySerializer
        │
        ▼
RegistryStore
        │
        ▼
registry.json
```
""",
    "Registry-Lifecycle.md": """# Registry Lifecycle

```text
Repository
    │
    ▼
Discovery
    │
    ▼
EngineeringEvidence
    │
    ▼
RegistryEntry
    │
    ▼
Registry Validation
    │
    ▼
Registry Serialization
    │
    ▼
Persistent Registry
    │
    ▼
Engineering Graph
```
"""
}

def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"[EXISTS ] {path}")
    else:
        path.write_text(content.strip() + "\n", encoding="utf-8")
        print(f"[CREATE ] {path}")

def main():
    print("=" * 72)
    print("ERS-001 Architecture Installer")
    print("=" * 72)
    for name, content in FILES.items():
        write(ROOT / name, content)
    print("=" * 72)
    print("ERS-001 architecture documentation installed.")
    print("=" * 72)

if __name__ == "__main__":
    main()
