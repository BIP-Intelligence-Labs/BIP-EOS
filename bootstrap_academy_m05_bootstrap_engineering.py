
"""
EOS Academy Curriculum Bootstrap

Creates:
bootstrap/academy/curriculum/core/engineering/
    M05-Bootstrap-Engineering.md
"""

from pathlib import Path

ROOT = Path.cwd()

BASE = ROOT / "bootstrap" / "academy" / "curriculum" / "core" / "engineering"
BASE.mkdir(parents=True, exist_ok=True)

CONTENT = """# M05 — Bootstrap Engineering

## Module Overview

Bootstrap Engineering teaches how EOS creates and governs repository
artifacts in a deterministic, repeatable, and maintainable way.

---

## Learning Objectives

After completing this module, students will be able to:

- Explain the purpose of bootstrap engineering.
- Design idempotent bootstrap scripts.
- Use explicit FILES maps.
- Use explicit DIRECTORIES maps.
- Generate repository artifacts safely.
- Apply EOS engineering standards.

---

## Lesson 1 — Why Bootstrap Engineering?

Bootstrap scripts are engineering infrastructure.

Engineering infrastructure is production software.

---

## Lesson 2 — Repository Generation

Preferred pattern:

```python
FILES = {
    "README.md": "...",
    "version.py": "...",
}

DIRECTORIES = [
    "compiler/frontend",
    "compiler/parser",
]
```

---

## Lesson 3 — Engineering Standards

Bootstrap scripts shall:

- Be deterministic.
- Be idempotent.
- Preserve existing artifacts.
- Produce consistent logs.
- Avoid fragile source generation.

---

## Lesson 4 — Engineering Truth

Engineering artifacts belong in:

engineering/

Published documentation belongs in:

docs/

---

## Practical Exercise

Create a bootstrap that generates:

- one directory
- three files
- execution logging
- safe re-execution

---

## Knowledge Check

1. Why are explicit FILES maps preferred?
2. What is idempotency?
3. Why is engineering/ the source of truth?
4. Why should bootstrap scripts avoid nested executable source generation?

---

## Completion Criteria

The student can implement EOS-compliant bootstrap scripts that safely
generate repository artifacts.
"""

TARGET = BASE / "M05-Bootstrap-Engineering.md"

print("=" * 70)
print("EOS Academy Curriculum Bootstrap")
print("=" * 70)

if TARGET.exists():
    print(f"[SKIP] {TARGET}")
else:
    TARGET.write_text(CONTENT, encoding="utf-8")
    print(f"[FILE] {TARGET}")

print("-" * 70)
print("Bootstrap Engineering curriculum ready.")
