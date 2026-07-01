from __future__ import annotations

from pathlib import Path

PLACEHOLDER_PATTERNS = (
    "TODO:",
    "FIXME",
    "XXX",
    "AUTO-GENERATED",
    "Replace scaffold",
    "Placeholder",
    "Stub",
    "NotImplementedError",
    "raise NotImplementedError",
)


class PlaceholderScanner:
    name = "Placeholder Scanner"

    def __init__(self, root: str | Path = "."):
        self.root = Path(root)

    def scan(self) -> list[str]:
        findings: list[str] = []

        for path in self.root.rglob("*.py"):
            if "__pycache__" in path.parts:
                continue

            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            for lineno, line in enumerate(text.splitlines(), start=1):
                for pattern in PLACEHOLDER_PATTERNS:
                    if pattern in line:
                        findings.append(
                            f"{path}:{lineno}: {pattern}"
                        )

        return findings
