"""
bootstrap_m005_repository_scanner.py

Generates the UEOS Doctor Repository Scanner.
"""

from pathlib import Path


ROOT = Path("src/bip_eos/doctor/scanners")
ROOT.mkdir(parents=True, exist_ok=True)

TARGET = ROOT / "repository.py"

TARGET.write_text("""from __future__ import annotations

from pathlib import Path


DEFAULT_IGNORE = {
    ".git",
    "__pycache__",
    ".venv",
    "node_modules",
    "dist",
    "build",
    ".pytest_cache",
    ".mypy_cache",
}


class RepositoryScanner:
    name = "Repository Scanner"

    def __init__(self, root: str | Path = ".", ignore=None):
        self.root = Path(root)
        self.ignore = set(ignore or DEFAULT_IGNORE)

    def scan(self) -> list[str]:
        findings: list[str] = []

        if not self.root.exists():
            findings.append(f"Repository not found: {self.root}")
            return findings

        py_files = 0
        directories = 0
        empty_dirs = 0

        for item in self.root.rglob("*"):
            if any(part in self.ignore for part in item.parts):
                continue

            if item.is_dir():
                directories += 1
                try:
                    next(item.iterdir())
                except StopIteration:
                    empty_dirs += 1
                    findings.append(f"Empty directory: {item}")
            elif item.suffix == ".py":
                py_files += 1
                if item.stat().st_size == 0:
                    findings.append(f"Empty Python file: {item}")

        findings.append(f"Repository Summary")
        findings.append(f"Directories : {directories}")
        findings.append(f"Python Files: {py_files}")
        findings.append(f"Empty Dirs  : {empty_dirs}")

        return findings
""", encoding="utf-8")

print("=" * 60)
print("UEOS Repository Scanner Generated")
print(TARGET)
print("=" * 60)
