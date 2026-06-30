"""
bootstrap_compiler_architecture_sync.py

Synchronizes the Bootstrap compiler architecture with the runtime compiler
architecture by creating the canonical package layout.

Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path.cwd()

BOOTSTRAP_DIRS = [
    "bootstrap/compiler/frontend",
    "bootstrap/compiler/diagnostics",
    "bootstrap/compiler/ast",
    "bootstrap/compiler/semantic",
    "bootstrap/compiler/emitters",
    "bootstrap/compiler/runtime",
    "bootstrap/compiler/shared",
    "bootstrap/compiler/tests",
]

RUNTIME_DIRS = [
    "src/bip_eos/compiler/frontend",
    "src/bip_eos/compiler/diagnostics",
    "src/bip_eos/compiler/ast",
    "src/bip_eos/compiler/semantic",
    "src/bip_eos/compiler/emitters",
    "src/bip_eos/compiler/runtime",
    "src/bip_eos/compiler/shared",
    "src/bip_eos/compiler/tests",
]

HEADER = '"""BIP EOS Compiler Package."""\n'

def ensure_package(relpath: str):
    path = ROOT / relpath
    existed = path.exists()
    path.mkdir(parents=True, exist_ok=True)
    init = path / "__init__.py"
    if not init.exists():
        init.write_text(HEADER, encoding="utf-8")
        init_created = True
    else:
        init_created = False
    return existed, init_created

print("=" * 60)
print("BIP EOS")
print("Compiler Architecture Synchronization")
print("=" * 60)

dirs_created = 0
pkgs_created = 0

print("\nBootstrap")
print("-" * 60)
for d in BOOTSTRAP_DIRS:
    existed, init_created = ensure_package(d)
    print(f"[{'SKIP' if existed else 'CREATE'}] {d}")
    dirs_created += 0 if existed else 1
    if init_created:
        pkgs_created += 1

print("\nRuntime")
print("-" * 60)
for d in RUNTIME_DIRS:
    existed, init_created = ensure_package(d)
    print(f"[{'SKIP' if existed else 'CREATE'}] {d}")
    dirs_created += 0 if existed else 1
    if init_created:
        pkgs_created += 1

print("-" * 60)
print(f"Directories created : {dirs_created}")
print(f"Packages initialized: {pkgs_created}")
print("Status              : SUCCESS")
