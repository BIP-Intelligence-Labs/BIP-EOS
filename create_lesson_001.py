"""
============================================================
 BIP EOS Academy
 Lesson 001 Generator
============================================================
"""
from pathlib import Path

ROOT = Path("bootstrap") / "academy" / "curriculum" / "core" / "engineering"
FILE = ROOT / "001-engineering-philosophy.md"

CONTENT = """# BIP EOS Academy

# Lesson 001 — Engineering Philosophy

## Engineering is More Than Writing Code

Software changes.
Technologies change.
Programming languages change.

Engineering principles endure.

---

# Mission

Build systems that build software.

Build once.
Teach forever.

---

# The First Law

Engineering knowledge must never be lost.

---

# Architecture Before Code

Before writing code ask:

- What responsibility does this component have?
- Does it belong here?
- Can another subsystem reuse it?
- Will this design still make sense in two years?

---

# Core Principles

- Architecture before code
- Engineering before features
- Automation before repetition
- Documentation before memory
- Build once. Teach forever.

---

# Reflection

Will this improve only today's project, or the platform for every future engineer?
"""

def main():
    print("="*60)
    print(" BIP EOS Lesson Generator")
    print("="*60)
    ROOT.mkdir(parents=True, exist_ok=True)
    if FILE.exists():
        print(f"• Exists   {FILE}")
    else:
        FILE.write_text(CONTENT, encoding="utf-8")
        print(f"✓ Created {FILE}")
    print("-"*60)
    print("Lesson 001 Ready")
    print("="*60)

if __name__ == "__main__":
    main()
