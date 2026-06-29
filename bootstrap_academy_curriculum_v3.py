
"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Academy Curriculum Bootstrap v3

Creates the Academy curriculum structure.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()
BASE = ROOT / "bootstrap" / "academy" / "curriculum"

DIRECTORIES = [
    BASE / "engineering_foundation",
    BASE / "eos_compiler",
    BASE / "bip_platform",
    BASE / "academy_instructor",
    BASE / "certifications",
    BASE / "labs",
    BASE / "capstone",
]

FILES = {
    "engineering_foundation/README.md": "# Engineering Foundation Curriculum\n",
    "engineering_foundation/M01-Engineering-Principles.md": "# M01 — Engineering Principles\n",
    "engineering_foundation/M02-Repository-Architecture.md": "# M02 — Repository Architecture\n",
    "engineering_foundation/M03-Governance.md": "# M03 — Engineering Governance\n",
    "engineering_foundation/M04-Compiler-Architecture.md": "# M04 — Compiler Architecture\n",
    "engineering_foundation/M05-Bootstrap-Engineering.md": "# M05 — Bootstrap Engineering\n",
    "engineering_foundation/M06-Engineering-Documentation.md": "# M06 — Engineering Documentation\n",
    "engineering_foundation/M07-Engineering-QA.md": "# M07 — Engineering QA\n",
    "engineering_foundation/M08-Engineering-Standards.md": "# M08 — Engineering Standards\n",

    "eos_compiler/README.md": "# EOS Compiler Curriculum\n",
    "eos_compiler/C01-Position-and-Source-Files.md": "# C01 — Position & Source Files\n",
    "eos_compiler/C02-Scanner.md": "# C02 — Scanner\n",
    "eos_compiler/C03-Tokens-and-Token-Types.md": "# C03 — Tokens & Token Types\n",
    "eos_compiler/C04-Lexer.md": "# C04 — Lexer\n",
    "eos_compiler/C05-Parser.md": "# C05 — Parser\n",
    "eos_compiler/C06-AST.md": "# C06 — Abstract Syntax Tree\n",
    "eos_compiler/C07-Engineering-Model.md": "# C07 — Engineering Model\n",
    "eos_compiler/C08-Validator.md": "# C08 — Validator\n",
    "eos_compiler/C09-Emitters.md": "# C09 — Emitters\n",
    "eos_compiler/C10-Runtime.md": "# C10 — Runtime\n",

    "bip_platform/README.md": "# BIP Platform Curriculum\n",
    "academy_instructor/README.md": "# Academy Instructor Resources\n",
    "certifications/README.md": "# Certifications\n",
    "labs/README.md": "# Hands-on Engineering Labs\n",
    "capstone/README.md": "# Capstone Projects\n",
}

def ensure_dir(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")

def ensure_file(path: Path, content: str):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"[FILE] {path}")

print("=" * 70)
print("EOS Academy Curriculum Bootstrap v3")
print("=" * 70)

for d in DIRECTORIES:
    ensure_dir(d)

for rel_path, content in FILES.items():
    ensure_file(BASE / rel_path, content)

print("-" * 70)
print("Academy curriculum ready.")
print("=" * 70)
