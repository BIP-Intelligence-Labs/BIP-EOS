
"""
EOS Academy Curriculum Bootstrap v2

Creates the Engineering Foundation and EOS Compiler curriculum.
"""

from pathlib import Path

ROOT = Path.cwd()
BASE = ROOT / "bootstrap" / "academy" / "curriculum" / "core"

DIRECTORIES = [
    BASE / "engineering_foundation",
    BASE / "eos_compiler",
]

FILES = {
    "engineering_foundation/M01-Engineering-Principles.md": "# M01 — Engineering Principles\n\nLearn the philosophy behind EOS.\n",
    "engineering_foundation/M02-Repository-Architecture.md": "# M02 — Repository Architecture\n\nDesign scalable repositories.\n",
    "engineering_foundation/M03-Governance.md": "# M03 — Engineering Governance\n\nConstitutions, ADRs and standards.\n",
    "engineering_foundation/M04-Compiler-Architecture.md": "# M04 — Compiler Architecture\n\nOverview of the EOS Compiler.\n",
    "engineering_foundation/M05-Bootstrap-Engineering.md": "# M05 — Bootstrap Engineering\n\nDeterministic repository generation.\n",
    "engineering_foundation/M06-Engineering-Documentation.md": "# M06 — Engineering Documentation\n\nEngineering Truth vs Published Documentation.\n",
    "engineering_foundation/M07-Engineering-QA.md": "# M07 — Engineering QA\n\nValidation and review practices.\n",
    "engineering_foundation/M08-Engineering-Standards.md": "# M08 — Engineering Standards\n\nCoding and engineering conventions.\n",

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
print("EOS Academy Curriculum Bootstrap v2")
print("=" * 70)

for d in DIRECTORIES:
    ensure_dir(d)

for rel_path, content in FILES.items():
    ensure_file(BASE / rel_path, content)

print("-" * 70)
print("Engineering Foundation curriculum ready.")
print("EOS Compiler curriculum ready.")
print("=" * 70)
