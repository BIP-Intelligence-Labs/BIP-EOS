"""
BIP EOS Manifesto Generator
Creates engineering/manifesto.md
"""

from pathlib import Path

ROOT = Path("engineering")
FILE = ROOT / "manifesto.md"

CONTENT = """# BIP EOS Manifesto

## We do not build software.

We build systems that build software.

## We do not preserve code.

We preserve engineering knowledge.

Every lesson learned becomes permanent knowledge.
Every architecture decision becomes institutional memory.
Every successful pattern becomes reusable.
Every mistake becomes education.

## Principles

- Architecture before implementation
- Automation before repetition
- Documentation is part of the product
- Engineering knowledge must never be lost
- Build once. Teach forever.

## Pillars

- The Academy teaches.
- Engineering governs.
- AI reasons.
- Plugins extend.
- The CLI unifies.

Together they form the BIP Engineering Operating System.
"""

def main():
    ROOT.mkdir(exist_ok=True)

    if FILE.exists():
        print(f"• Exists   {FILE}")
    else:
        FILE.write_text(CONTENT, encoding="utf-8")
        print(f"✓ Created {FILE}")

    print("Manifesto ready.")

if __name__ == "__main__":
    main()
