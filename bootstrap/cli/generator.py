"""
bootstrap/cli/generator.py

Bootstrap Scaffold Generator
"""

from __future__ import annotations

from pathlib import Path


class Generator:
    """Utility for generating files and folders from templates."""

    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root

    def create_directory(self, relative_path: str) -> Path:
        path = self.project_root / relative_path
        path.mkdir(parents=True, exist_ok=True)
        return path

    def create_file(self, relative_path: str, content: str = "") -> Path:
        path = self.project_root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(content, encoding="utf-8")
        return path

    def scaffold(self, files: dict[str, str]) -> None:
        for relative_path, content in files.items():
            self.create_file(relative_path, content)

    def exists(self, relative_path: str) -> bool:
        return (self.project_root / relative_path).exists()


if __name__ == "__main__":
    print("Bootstrap Generator")
    print("===================")
    print("Reusable scaffolding engine ready.")
