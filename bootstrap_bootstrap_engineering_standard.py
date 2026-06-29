"""
Bootstrap Engineering Standard Update

Updates EOS governance documentation with the Bootstrap Engineering
standard based on explicit file maps.
"""

from pathlib import Path

ROOT = Path.cwd()

CONSTITUTION = ROOT / "engineering" / "governance" / "EOS-Engineering-Constitution.md"
CODING = ROOT / "engineering" / "standards" / "Coding-Standards.md"
ADR = ROOT / "engineering" / "decisions" / "ADR-0004-Bootstrap-Engineering.md"

ARTICLE = r"""
## Article XII — Bootstrap Engineering

### Principle

Bootstrap scripts shall generate repository artifacts from explicit file
maps rather than embedded executable source blocks.

### Requirements

Bootstrap scripts shall:

- Use explicit `FILES` maps.
- Use explicit `DIRECTORIES` maps.
- Be deterministic.
- Be idempotent.
- Never overwrite existing engineering artifacts unless explicitly requested.
- Produce consistent execution logs.

Bootstrap scripts shall not:

- Generate executable Python through nested executable source blocks.
- Depend on fragile string concatenation.

### Engineering Philosophy

Engineering infrastructure is production software.
"""

CODING_TEXT = r"""
# Bootstrap Development Standards

## Repository Generation

Use explicit file maps.

```python
FILES = {
    "README.md": "...",
    "version.py": "...",
}
```

Use explicit directory maps.

```python
DIRECTORIES = [
    "compiler/frontend",
]
```

Bootstrap scripts shall be deterministic, idempotent, and safe to run
multiple times.
"""

ADR_TEXT = r"""# ADR-0004 Bootstrap Engineering

## Status

Accepted

## Decision

EOS bootstrap scripts shall generate repository artifacts using explicit
file maps instead of embedded executable source blocks.

## Consequences

- Deterministic output
- Easier maintenance
- Easier review
- Fewer quoting/escaping errors
- Consistent engineering pattern
"""


def append_if_missing(path: Path, marker: str, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        current = path.read_text(encoding="utf-8")
    else:
        current = ""
    if marker in current:
        print(f"[SKIP] {path}")
        return
    if current and not current.endswith("\n"):
        current += "\n"
    current += "\n" + text.strip() + "\n"
    path.write_text(current, encoding="utf-8")
    print(f"[UPDATE] {path}")


print("="*70)
print("EOS Bootstrap Engineering Standard Update")
print("="*70)

append_if_missing(CONSTITUTION, "Article XII — Bootstrap Engineering", ARTICLE)
append_if_missing(CODING, "Bootstrap Development Standards", CODING_TEXT)

if ADR.exists():
    print(f"[SKIP] {ADR}")
else:
    ADR.parent.mkdir(parents=True, exist_ok=True)
    ADR.write_text(ADR_TEXT, encoding="utf-8")
    print(f"[FILE] {ADR}")

print("-"*70)
print("Bootstrap engineering standards installed.")
