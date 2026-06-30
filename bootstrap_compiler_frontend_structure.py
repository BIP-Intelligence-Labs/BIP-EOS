"""
bootstrap_compiler_frontend_structure.py

Creates the canonical BIP EOS compiler package structure.

Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "src/bip_eos/compiler",
    "src/bip_eos/compiler/frontend",
    "src/bip_eos/compiler/diagnostics",
    "src/bip_eos/compiler/ast",
    "src/bip_eos/compiler/semantic",
    "src/bip_eos/compiler/emitters",
    "src/bip_eos/compiler/runtime",
    "src/bip_eos/compiler/shared",
    "src/bip_eos/compiler/tests",
]

INIT_FILES = [
    "src/bip_eos/compiler/__init__.py",
    "src/bip_eos/compiler/frontend/__init__.py",
    "src/bip_eos/compiler/diagnostics/__init__.py",
    "src/bip_eos/compiler/ast/__init__.py",
    "src/bip_eos/compiler/semantic/__init__.py",
    "src/bip_eos/compiler/emitters/__init__.py",
    "src/bip_eos/compiler/runtime/__init__.py",
    "src/bip_eos/compiler/shared/__init__.py",
]

HEADER = '"""BIP EOS Compiler Package."""\n'

print("=" * 60)
print("BIP EOS")
print("Compiler Structure Bootstrap")
print("=" * 60)

created_dirs = 0
created_files = 0

for directory in DIRECTORIES:
    path = ROOT / directory
    if path.exists():
        print(f"[SKIP]   {directory}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        created_dirs += 1
        print(f"[CREATE] {directory}")

for filename in INIT_FILES:
    path = ROOT / filename
    if path.exists():
        print(f"[SKIP]   {filename}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(HEADER, encoding="utf-8")
        created_files += 1
        print(f"[CREATE] {filename}")

print("-" * 60)
print(f"Directories : {created_dirs}")
print(f"Packages    : {created_files}")
print("Compiler structure ready.")
