"""
bootstrap_compiler_phase1.py

BIP Engineering Labs
Engineering Compiler - Phase 1 Bootstrap

Creates the initial compiler specification set.

Safe to run multiple times.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENGINEERING = ROOT / "engineering"
COMPILER = ENGINEERING / "compiler"
SPEC = COMPILER / "specifications"

DOCS = {
    "EC-001-engineering-compiler-architecture.md": "# EC-001 — Engineering Compiler Architecture\n",
    "ER-001-engineering-registry-specification.md": "# ER-001 — Engineering Registry Specification\n",
    "MF-001-engineering-manifest-specification.md": "# MF-001 — Engineering Manifest Specification\n",
    "DG-001-dependency-graph-specification.md": "# DG-001 — Dependency Graph Specification\n",
    "EV-001-engineering-validation-engine.md": "# EV-001 — Engineering Validation Engine\n",
    "EC-002-compiler-pipeline.md": "# EC-002 — Compiler Pipeline\n",
}

README = """# Engineering Compiler

The Engineering Compiler transforms governed engineering specifications
into deterministic engineering artifacts.

Pipeline

Engineering Manifest
        ↓
Engineering Registry
        ↓
Engineering Parser
        ↓
Engineering Model
        ↓
Dependency Graph
        ↓
Validation Engine
        ↓
Engineering Compiler
        ↓
Emitters
        ↓
Generated Repository
"""

MANIFEST = """version: 1.0.0

compiler:
  name: Engineering Compiler

phase: EC-01

specifications:
  - EC-001
  - EC-002
  - ER-001
  - MF-001
  - DG-001
  - EV-001

runtime:
  next:
    - loader
    - registry
"""

def ensure_dir(p):
    if p.exists():
        print(f"[SKIP] {p}")
    else:
        p.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {p}")

def ensure_file(path, content):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.write_text(content, encoding="utf-8")
        print(f"[FILE] {path}")

print("="*70)
print("Engineering Compiler Phase 1")
print("="*70)

ensure_dir(COMPILER)
ensure_dir(SPEC)

ensure_file(COMPILER/"README.md", README)
ensure_file(COMPILER/"compiler.manifest.yaml", MANIFEST)

for name, content in DOCS.items():
    ensure_file(SPEC/name, content)

print("-"*70)
print("Phase EC-01 complete")
print()
print("Next implementation sprint:")
print("  bootstrap/compiler/")
print("    loader.py")
print("    registry.py")
