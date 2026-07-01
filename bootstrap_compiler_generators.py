"""
bootstrap_compiler_generators.py

Creates a clean compiler generator layout.

Run:
    python bootstrap_compiler_generators.py
"""

from pathlib import Path

ROOT = Path.cwd()
BASE = ROOT / "bootstrap" / "compiler" / "generators"

FILES = {
    "ast_generator.py": AST Generator,

    }
