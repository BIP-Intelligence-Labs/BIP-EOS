"""
bootstrap_compiler_packages.py

Creates the canonical Bootstrap compiler package hierarchy.
"""

from pathlib import Path

ROOT = Path.cwd()

PACKAGES = [
    "bootstrap/compiler/frontend",
    "bootstrap/compiler/frontend/scanner",
    "bootstrap/compiler/frontend/lexer",
    "bootstrap/compiler/frontend/parser",
    "bootstrap/compiler/ast",
    "bootstrap/compiler/semantic",
    "bootstrap/compiler/diagnostics",
    "bootstrap/compiler/emitters",
    "bootstrap/compiler/runtime",
    "bootstrap/compiler/shared",
    "bootstrap/compiler/templates",
    "bootstrap/compiler/generators",
]

HEADER = '"""BIP EOS Compiler Package."""\n'

print("=" * 60)
print("BIP EOS")
print("Bootstrap Compiler Packages")
print("=" * 60)

created_dirs = 0
created_packages = 0

for package in PACKAGES:
    directory = ROOT / package

    if directory.exists():
        print(f"[SKIP]   {package}")
    else:
        directory.mkdir(parents=True, exist_ok=True)
        created_dirs += 1
        print(f"[CREATE] {package}")

    init = directory / "__init__.py"

    if not init.exists():
        init.write_text(HEADER, encoding="utf-8")
        created_packages += 1

print("-" * 60)
print(f"Directories created : {created_dirs}")
print(f"Packages initialized: {created_packages}")
print("Status              : SUCCESS")
print()

print("Canonical Bootstrap compiler structure:")
print("""
bootstrap/compiler/

    frontend/
        scanner/
        lexer/
        parser/

    ast/
    semantic/
    diagnostics/
    emitters/
    runtime/
    shared/
    templates/
    generators/
""")
