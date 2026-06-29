"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates the EOS Engineering Constitution.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

TARGET = ROOT / "engineering/governance/EOS-Engineering-Constitution.md"

CONTENT = """# EOS Engineering Constitution

## Preamble

The Engineering Operating System (EOS) exists to transform Engineering
Knowledge into Executable Engineering Systems through disciplined,
traceable, and reproducible engineering practices.

---

# Article I
Engineering Knowledge is the authoritative source of truth.

# Article II
Every engineering artifact shall be traceable to governed Engineering
Knowledge.

# Article III
The EOS Compiler shall compile Engineering Knowledge into Executable
Engineering Systems.

# Article IV
The Engineering Model (IR) is the canonical representation used by the
compiler. Validation and emitters operate on the Engineering Model, not
on source documents.

# Article V
Engineering shall be deterministic and reproducible.

# Article VI
Every change shall include:
- Specification updates
- Implementation
- Tests
- Documentation

# Article VII
Engineering integrity takes precedence over implementation speed.

# Article VIII
Architecture Decisions (ADRs) shall record significant engineering
decisions.

# Article IX
All compiler components shall satisfy the Definition of Done before
integration.

# Article X
EOS continuously governs, validates, documents, and improves itself.
"""

def main():
    TARGET.parent.mkdir(parents=True, exist_ok=True)

    if TARGET.exists():
        print(f"[SKIP] {TARGET}")
    else:
        TARGET.write_text(CONTENT, encoding="utf-8")
        print(f"[FILE] {TARGET}")

    print("-" * 70)
    print("EOS Engineering Constitution ready.")
    print("-" * 70)

if __name__ == "__main__":
    main()
