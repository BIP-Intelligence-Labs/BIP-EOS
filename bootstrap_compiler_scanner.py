"""
bootstrap_compiler_scanner.py

Sprint 2 begins here.
Creates the EOS Compiler Front-End scanner package.
"""
from pathlib import Path
from textwrap import dedent

ROOT = Path.cwd()

FILES = {
    "src/bip_eos/compiler/__init__.py": '"""EOS Compiler."""\n',
    "src/bip_eos/compiler/frontend/__init__.py": '"""Compiler Front-End."""\n',
    "src/bip_eos/compiler/frontend/source_file.py": """
from dataclasses import dataclass
from pathlib import Path

@dataclass(slots=True)
class SourceFile:
    path: Path
    text: str
""",
    "src/bip_eos/compiler/frontend/position.py": """
from dataclasses import dataclass

@dataclass(slots=True)
class Position:
    line: int
    column: int
    offset: int
""",
    "src/bip_eos/compiler/frontend/span.py": """
from dataclasses import dataclass
from .position import Position

@dataclass(slots=True)
class Span:
    start: Position
    end: Position
""",
    "src/bip_eos/compiler/frontend/scanner.py": """
from pathlib import Path
from .source_file import SourceFile

class Scanner:
    DEFAULT_EXTENSIONS = {'.md','.yaml','.yml','.json','.bip','.adr'}

    def scan(self, root: Path):
        root = Path(root)
        for path in root.rglob('*'):
            if path.is_file() and path.suffix.lower() in self.DEFAULT_EXTENSIONS:
                yield SourceFile(
                    path=path,
                    text=path.read_text(encoding='utf-8', errors='replace')
                )
""",
    "tests/unit/test_scanner.py": """
from pathlib import Path
from bip_eos.compiler.frontend.scanner import Scanner

def test_scanner_discovers_files():
    scanner = Scanner()
    files = list(scanner.scan(Path('engineering')))
    assert isinstance(files, list)
"""
}

def write(rel, content):
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        print(f"[SKIP]   {p}")
    else:
        p.write_text(dedent(content).lstrip(), encoding="utf-8")
        print(f"[CREATE] {p}")

def main():
    print("="*70)
    print("BIP EOS - Compiler Front-End Bootstrap")
    print("="*70)
    for rel, content in FILES.items():
        write(rel, content)
    print("\\nSprint 2 initialized.")
    print("Next: Token Types -> Lexer -> Parser -> AST")

if __name__ == "__main__":
    main()
