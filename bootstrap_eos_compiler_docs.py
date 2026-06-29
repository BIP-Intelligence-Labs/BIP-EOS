"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates the Engineering Compiler documentation structure.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "engineering/compiler",
    "engineering/compiler/specifications",
    "engineering/compiler/api",
    "engineering/compiler/diagrams",
    "engineering/compiler/decisions",
    "engineering/compiler/examples",
    "engineering/compiler/changelog",
]

FILES = {
    "engineering/compiler/README.md": "# EOS Compiler Documentation\n\nCompiles Engineering Knowledge into Executable Engineering Systems.\n",

    "engineering/compiler/specifications/EOS-001-kernel-architecture.md": "# EOS-001 Kernel Architecture\n",
    "engineering/compiler/specifications/EC-001-compiler-architecture.md": "# EC-001 Compiler Architecture\n",
    "engineering/compiler/specifications/LC-001-lexer-specification.md": "# LC-001 Lexer Specification\n",
    "engineering/compiler/specifications/PR-001-parser-specification.md": "# PR-001 Parser Specification\n",
    "engineering/compiler/specifications/AST-001-ast-specification.md": "# AST-001 AST Specification\n",
    "engineering/compiler/specifications/IR-001-engineering-model.md": "# IR-001 Engineering Model\n",
    "engineering/compiler/specifications/DV-001-validator-specification.md": "# DV-001 Validator Specification\n",
    "engineering/compiler/specifications/EMT-001-emitter-specification.md": "# EMT-001 Emitter Specification\n",

    "engineering/compiler/api/README.md": "# Compiler API\n",
    "engineering/compiler/api/compiler-api.md": "# EOS Compiler API\n",

    "engineering/compiler/diagrams/README.md": "# Compiler Diagrams\n",
    "engineering/compiler/diagrams/compiler-overview.md": "# Compiler Overview\n",
    "engineering/compiler/diagrams/frontend.md": "# Front-End\n",
    "engineering/compiler/diagrams/pipeline.md": "# Compiler Pipeline\n",
    "engineering/compiler/diagrams/dependency-graph.md": "# Dependency Graph\n",

    "engineering/compiler/decisions/README.md": "# Architecture Decision Records\n",
    "engineering/compiler/decisions/ADR-001-front-end-design.md": "# ADR-001 Front-End Design\n",
    "engineering/compiler/decisions/ADR-002-engineering-model.md": "# ADR-002 Engineering Model\n",
    "engineering/compiler/decisions/ADR-003-emitter-strategy.md": "# ADR-003 Emitter Strategy\n",

    "engineering/compiler/examples/README.md": "# Examples\n",
    "engineering/compiler/examples/hello-engineering.md": "# Hello Engineering\n",
    "engineering/compiler/examples/lexer-output.md": "# Lexer Output\n",
    "engineering/compiler/examples/parser-output.md": "# Parser Output\n",
    "engineering/compiler/examples/engineering-model.md": "# Engineering Model Example\n",

    "engineering/compiler/changelog/README.md": "# Changelog\n",
    "engineering/compiler/changelog/CHANGELOG.md": "# CHANGELOG\n",
}

def create_dir(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")

def create_file(path: Path, text: str):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        print(f"[FILE] {path}")

def main():
    print("="*70)
    print("EOS Compiler Documentation Bootstrap")
    print("="*70)
    for d in DIRECTORIES:
        create_dir(ROOT / d)
    for f,t in FILES.items():
        create_file(ROOT / f, t)
    print("-"*70)
    print(f"Directories : {len(DIRECTORIES)}")
    print(f"Files       : {len(FILES)}")
    print("="*70)

if __name__ == "__main__":
    main()
