"""
bootstrap_rename_compiler_specifications.py

Renames bootstrap generator scripts that were accidentally placed in
engineering/compiler/specifications/.

These are generators, not specifications.

The script moves them to:

    bootstrap/compiler/generators/

and leaves engineering/compiler/specifications/ for *.md documents only.
"""

from pathlib import Path
import shutil

ROOT = Path.cwd()

SPEC_DIR = ROOT / "engineering" / "compiler" / "specifications"
GEN_DIR = ROOT / "bootstrap" / "compiler" / "generators"

GEN_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("BIP EOS")
print("Compiler Generator Migration")
print("=" * 60)

moved = 0
skipped = 0

for py_file in sorted(SPEC_DIR.glob("*.py")):
    destination = GEN_DIR / py_file.name

    if destination.exists():
        print(f"[SKIP] {py_file.name}")
        skipped += 1
        continue

    shutil.move(str(py_file), str(destination))
    print(f"[MOVE] {py_file.name} -> {destination.relative_to(ROOT)}")
    moved += 1

print("-" * 60)
print(f"Moved   : {moved}")
print(f"Skipped : {skipped}")

remaining = list(SPEC_DIR.glob("*.py"))
if not remaining:
    print("[OK] engineering/compiler/specifications now contains only documentation.")
else:
    print(f"[WARN] {len(remaining)} Python file(s) remain.")

print()
print("Next step:")
print("Generate canonical specification documents:")
print("  C01-Source-Files.md")
print("  C02-Scanner.md")
print("  C03-Token-System.md")
print("  C04-Lexer.md")
print("  C05-Parser.md")
print("  C06-AST.md")
print("  C07-Engineering-Model.md")
print("  C08-Validator.md")
print("  C09-Emitters.md")
print("  C10-Runtime.md")
