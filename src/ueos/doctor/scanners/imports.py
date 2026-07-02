from __future__ import annotations

from pathlib import Path
from ast import parse, walk, Import, ImportFrom
import importlib.util


class ImportScanner:
    name = "Import Validation Scanner"

    def __init__(self, root: str | Path = "."):
        self.root = Path(root)

    def scan(self) -> list[str]:
        findings: list[str] = []

        for path in self.root.rglob("*.py"):
            if "__pycache__" in path.parts:
                continue

            try:
                source = path.read_text(encoding="utf-8", errors="ignore")
                tree = parse(source)
            except Exception as ex:
                findings.append(f"{path}: parse error: {ex}")
                continue

            for node in walk(tree):
                if isinstance(node, Import):
                    for alias in node.names:
                        self._validate(alias.name, path, findings)
                elif isinstance(node, ImportFrom):
                    if node.module:
                        self._validate(node.module, path, findings)

        return findings

    def _validate(self, module: str, path: Path, findings: list[str]) -> None:
        root = module.split(".")[0]

        try:
            if importlib.util.find_spec(root) is None:
                findings.append(
                    f"{path}: unresolved import '{module}'"
                )
        except Exception:
            findings.append(
                f"{path}: invalid import '{module}'"
            )
