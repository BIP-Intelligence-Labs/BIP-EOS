"""
ast_generator.py

UEOS Atlas
Compiler Generator

Responsible for generating Abstract Syntax Tree (AST) source artifacts.
"""

from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass


@dataclass(slots=True)
class ASTGenerationResult:
    """Result returned by the AST generator."""

    files_created: int = 0
    files_updated: int = 0
    success: bool = True


class ASTGenerator:
    """
    Generates Abstract Syntax Tree (AST) source files.

    This generator is responsible for creating the AST layer used by
    the UEOS compiler frontend.
    """

    def __init__(self, output_directory: Path):
        self.output_directory = Path(output_directory)

    def generate(self) -> ASTGenerationResult:
        """
        Generate the AST package.

        Returns
        -------
        ASTGenerationResult
            Generation statistics.
        """

        result = ASTGenerationResult()

        self.output_directory.mkdir(parents=True, exist_ok=True)

        self._create_package(result)
        self._create_node(result)
        self._create_visitor(result)

        return result

    def _write_file(self, filename: str, content: str,
                    result: ASTGenerationResult) -> None:

        path = self.output_directory / filename

        if path.exists():
            result.files_updated += 1
        else:
            result.files_created += 1

        path.write_text(content, encoding="utf-8")

    def _create_package(self, result: ASTGenerationResult) -> None:

        self._write_file(
            "__init__.py",
            '"""UEOS Compiler AST."""\n',
            result,
        )

    def _create_node(self, result: ASTGenerationResult) -> None:

        self._write_file(
            "node.py",
            '''"""
AST Node
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ASTNode:
    """Base AST node."""
''',
            result,
        )

    def _create_visitor(self, result: ASTGenerationResult) -> None:

        self._write_file(
            "visitor.py",
            '''"""
AST Visitor
"""

class ASTVisitor:
    """Base AST visitor."""

    def visit(self, node):
        raise NotImplementedError
''',
            result,
        )


def main() -> int:

    generator = ASTGenerator(
        Path("src/bip_eos/compiler/ast")
    )

    result = generator.generate()

    print("=" * 60)
    print("UEOS AST Generator")
    print("=" * 60)
    print(f"Created : {result.files_created}")
    print(f"Updated : {result.files_updated}")

    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
