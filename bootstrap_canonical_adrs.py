
"""
========================================================================
BIP Engineering Labs
Engineering Operating System (EOS)

ADR Bootstrap

Creates the canonical Architecture Decision Records.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()
BASE = ROOT / "engineering" / "decisions"

BASE.mkdir(parents=True, exist_ok=True)

FILES = {
    "ADR-0001-Repository-Architecture.md": """# ADR-0001 — Repository Architecture

## Status
Accepted

## Decision

Establish the canonical EOS repository architecture.

## Consequences

- Consistent project organization
- Scalable engineering structure
- Clear separation of concerns
""",

    "ADR-0002-EOS-Platform.md": """# ADR-0002 — EOS Platform

## Status
Accepted

## Decision

EOS shall serve as the Engineering Operating System platform.

## Consequences

- Unified engineering platform
- Shared services and governance
""",

    "ADR-0003-Compiler-First.md": """# ADR-0003 — Compiler First

## Status
Accepted

## Decision

Develop the EOS Compiler before higher-level platform capabilities.

## Consequences

- Stable engineering foundation
- Reusable compiler infrastructure
""",

    "ADR-0004-Bootstrap-Engineering.md": """# ADR-0004 — Bootstrap Engineering

## Status
Accepted

## Decision

Bootstrap scripts shall generate repository artifacts using explicit
file maps rather than embedded executable source blocks.

## Consequences

- Deterministic generation
- Easier maintenance
- Consistent engineering standards
""",

    "ADR-0005-Repository-Freeze.md": """# ADR-0005 — Repository Freeze

## Status
Accepted

## Decision

Freeze the EOS Foundation repository architecture after BIP EOS v0.1.0.
Future structural changes require an ADR.

## Consequences

- Stable repository structure
- Controlled architectural evolution
""",
}

print("=" * 70)
print("EOS ADR Bootstrap")
print("=" * 70)

for name, content in FILES.items():
    target = BASE / name
    if target.exists():
        print(f"[SKIP] {target}")
    else:
        target.write_text(content, encoding="utf-8")
        print(f"[FILE] {target}")

print("-" * 70)
print("Canonical ADR set ready.")
print("=" * 70)
