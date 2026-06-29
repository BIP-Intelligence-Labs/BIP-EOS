"""
========================================================================

BIP Engineering Labs
Engineering Operating System (EOS)

Bootstrap Script

Creates the EOS Compiler repository structure.

========================================================================
"""

from pathlib import Path

ROOT = Path.cwd()

DIRECTORIES = [
    "bootstrap/compiler",
    "bootstrap/compiler/frontend",
    "bootstrap/compiler/frontend/lexer",
    "bootstrap/compiler/frontend/lexer/tests",
    "bootstrap/compiler/frontend/parser",
    "bootstrap/compiler/frontend/ast",
    "bootstrap/compiler/frontend/diagnostics",
    "bootstrap/compiler/registry",
    "bootstrap/compiler/engineering_model",
    "bootstrap/compiler/dependency",
    "bootstrap/compiler/validation",
    "bootstrap/compiler/emitters",
    "bootstrap/compiler/runtime",
    "bootstrap/compiler/shared",
    "bootstrap/compiler/tests",
]

FILES = {
    "bootstrap/compiler/README.md": "# EOS Compiler\n\nCompiles Engineering Knowledge into Executable Engineering Systems.\n",
    "bootstrap/compiler/__init__.py": "",
    "bootstrap/compiler/compiler.py": '"""EOS Compiler"""\n',
    "bootstrap/compiler/compiler_pipeline.py": '"""EOS Compiler Pipeline"""\n',
    "bootstrap/compiler/frontend/README.md": "# EOS Compiler Front-End\n",
    "bootstrap/compiler/frontend/__init__.py": "",
    "bootstrap/compiler/frontend/frontend.py": '"""EOS Front-End"""\n',
    "bootstrap/compiler/frontend/lexer/README.md": "# EOS Lexer\n",
    "bootstrap/compiler/frontend/lexer/__init__.py": "",
    "bootstrap/compiler/frontend/lexer/position.py": "",
    "bootstrap/compiler/frontend/lexer/token_types.py": "",
    "bootstrap/compiler/frontend/lexer/token.py": "",
    "bootstrap/compiler/frontend/lexer/scanner.py": "",
    "bootstrap/compiler/frontend/lexer/lexer.py": "",
    "bootstrap/compiler/frontend/lexer/exceptions.py": "",
    "bootstrap/compiler/frontend/lexer/tests/__init__.py": "",
    "bootstrap/compiler/frontend/lexer/tests/test_position.py": "",
    "bootstrap/compiler/frontend/lexer/tests/test_token_types.py": "",
    "bootstrap/compiler/frontend/lexer/tests/test_token.py": "",
    "bootstrap/compiler/frontend/lexer/tests/test_scanner.py": "",
    "bootstrap/compiler/frontend/lexer/tests/test_lexer.py": "",
}

def create_directory(path: Path):
    if path.exists():
        print(f"[SKIP] {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        print(f"[DIR ] {path}")

def create_file(path: Path, content: str):
    if path.exists():
        print(f"[SKIP] {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"[FILE] {path}")

def main():
    print("=" * 70)
    print("EOS Compiler Repository Bootstrap")
    print("=" * 70)
    for directory in DIRECTORIES:
        create_directory(ROOT / directory)
    for filename, text in FILES.items():
        create_file(ROOT / filename, text)
    print("-" * 70)
    print(f"Directories : {len(DIRECTORIES)}")
    print(f"Files       : {len(FILES)}")
    print("=" * 70)

if __name__ == "__main__":
    main()
