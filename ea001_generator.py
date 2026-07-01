#!/usr/bin/env python3
"""
EA-001 Generator
UEOS Architecture Constitution

Generates:
    engineering/architecture/EA-001-UEOS-Architecture-Constitution.md
"""

from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent

OUTPUT = ROOT / "engineering" / "architecture"
OUTPUT.mkdir(parents=True, exist_ok=True)

DOC = OUTPUT / "EA-001-UEOS-Architecture-Constitution.md"

CONTENT = dedent("""\
# EA-001 — UEOS Architecture Constitution

## Status
Draft 1

## System

**BIP Universal Engineering Operating System (UEOS)**

---

# Mission

UEOS provides a Universal Engineering Operating System that transforms
engineering knowledge into governed engineering artifacts through a
Registry-driven architecture.

---

# Constitutional Principles

1. Registry is the Single Source of Engineering Truth.
2. All engineering artifacts SHALL be generated.
3. Generated artifacts SHALL NOT be edited manually.
4. Runtime code SHALL NOT be the source of engineering truth.
5. Engineering knowledge precedes engineering implementation.
6. Every subsystem shall have a single owner and responsibility.

---

# Core Pipeline

Knowledge
→ Registry
→ Engineering Compiler
→ Engineering Model
→ Generator Engine
→ Engineering Artifacts

---

# Core Systems

- Engineering Knowledge System (EKS)
- Engineering Registry System (ERS)
- Engineering Compiler System (ECS)
- Engineering Publishing System (EGS)
- Engineering Runtime System (ERTS)
- Engineering Academy System (EAS)
- Engineering AI System (EAIS)
- Engineering Plugin System (EPS)
- Engineering CLI System (ECLS)

---

# Repository Categories

## Source

Editable engineering definitions.

## Runtime

Executable UEOS implementation.

## Generated

Compiler-produced engineering artifacts.

## Knowledge

Reference material, research, lessons, architecture.

## Tooling

Bootstrap, installers, migrations, maintenance.

---

# Governance Rules

- One source of truth.
- One responsibility per subsystem.
- No circular dependencies.
- All generated content must be reproducible.
- Architecture changes require an Engineering Architecture (EA) decision.

---

# Next Documents

EA-002 Repository Structure Standard

EA-003 Directory Ownership Matrix

EA-004 Dependency Rules

EA-005 Artifact Lifecycle
""")

DOC.write_text(CONTENT, encoding="utf-8")

print("=" * 70)
print("EA-001 generated")
print(DOC)
