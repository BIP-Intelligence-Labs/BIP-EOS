"""
bootstrap_engineering_rule_ec004.py

Generates:
engineering/governance/rules/EC-004-Architecture-Freeze.md
"""

from pathlib import Path

ROOT = Path.cwd()

OUTPUT = ROOT / "engineering" / "governance" / "rules" / "EC-004-Architecture-Freeze.md"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

DOCUMENT = """# EC-004 — Architecture Freeze

**Engineering Rule:** EC-004
**Status:** Active
**Owner:** BIP EOS Engineering

---

## Purpose

Protect the architectural integrity of BIP EOS by preventing unnecessary
repository reorganization after the platform architecture has been established.

---

## Rule

The repository architecture is considered frozen.

Directory organization, subsystem boundaries, package hierarchy, and
engineering structure SHALL NOT be modified unless an Architecture
Decision Record (ADR) explicitly approves the change.

Normal engineering work shall occur within the established architecture.

---

## Allowed

- Implement new features
- Add compiler phases
- Add plugins
- Add engineering specifications
- Add tests
- Add documentation
- Improve implementations
- Improve performance
- Fix defects

---

## Requires ADR Approval

- Moving major directories
- Renaming engineering subsystems
- Changing package hierarchy
- Repository restructuring
- Bootstrap architecture changes
- Compiler architecture changes
- Runtime architecture changes

---

## Exceptions

Emergency production fixes may temporarily violate this rule but SHALL be
documented by a follow-up ADR.

---

## Engineering Principle

**Stability before expansion.**

Stable architecture enables rapid engineering.

---

## Compliance

Every pull request should answer:

- Does this preserve the architecture?

If the answer is **No**, an ADR is required before implementation.

---

## Applies To

- BIP EOS
- Bootstrap
- Compiler
- Engineering
- Academy
- Repository
- Plugins
- AI
- Reports

---

Approved by:

**BIP EOS Engineering**
"""

OUTPUT.write_text(DOCUMENT, encoding="utf-8")

print("=" * 60)
print("BIP EOS")
print("=" * 60)
print("Engineering Rule Generated")
print(OUTPUT)
