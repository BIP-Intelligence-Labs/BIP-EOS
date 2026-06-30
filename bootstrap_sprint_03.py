"""
bootstrap_sprint_03.py

Generates engineering/sprints/SPRINT_03.md
"""

from pathlib import Path

ROOT = Path.cwd()
TARGET = ROOT / "engineering" / "sprints" / "SPRINT_03.md"

DOCUMENT = """# Sprint 03 — Compiler Foundation

**Status:** Complete

## Objective

Establish the foundation of the BIP EOS compiler and continue building the Engineering Operating System through engineering-first development.

---

## Deliverables

### Compiler Front-End

- Implemented compiler package
- Implemented SourceFile
- Implemented Position
- Implemented Span
- Implemented Scanner
- Added scanner unit tests

### Compiler Architecture

- Established compiler front-end package structure
- Defined compiler engineering phases (C01–C10)
- Created compiler specification framework

### Engineering Documentation

Canonical ADRs:

- ADR-0001 Repository Architecture
- ADR-0002 EOS Platform
- ADR-0003 Compiler First
- ADR-0004 Bootstrap Engineering
- ADR-0005 Repository Freeze

- Expanded compiler engineering specifications
- Continued engineering standards documentation

### Bootstrap

- Reorganized Academy curriculum
- Began Bootstrap Documentation Engine
- Standardized compiler documentation generators

---

## Repository Status

- Engineering documentation organized
- Compiler package established
- Scanner operational
- Unit testing framework expanded
- Repository structure stabilized

---

## Outcome

Sprint 03 establishes the compiler foundation for BIP EOS.

The Engineering Operating System now contains the initial compiler front-end, standardized engineering documentation, and the infrastructure required for the remaining compiler phases.

---

## Sprint 04 Goals

- Complete Lexer
- Complete Token definitions
- Implement Parser
- Implement AST
- Expand compiler diagnostics
- Continue Bootstrap Engineering
"""

TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(DOCUMENT, encoding="utf-8")

print("=" * 60)
print("BIP EOS Bootstrap")
print("=" * 60)
print("Generated:")
print(TARGET)
