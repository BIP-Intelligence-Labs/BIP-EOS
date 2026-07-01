"""
bootstrap_m005_duplicate_scanner.py

Generates the UEOS Doctor Duplicate File Scanner.
"""

from pathlib import Path
import hashlib
from collections import defaultdict


ROOT = Path("src/bip_eos/doctor/scanners")
ROOT.mkdir(parents=True, exist_ok=True)

TARGET = ROOT / "duplicates.py"

TARGET.write_text("""from __future__ import annotations

from pathlib import Path
from collections import defaultdict
import hashlib


class DuplicateScanner:
    name = "Duplicate File Scanner"

    def __init__(self, root: str | Path = "."):
        self.root = Path(root)

    def _sha256(self, path: Path) -> str:
        h = hashlib.sha256()
        with path.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()

    def scan(self) -> list[str]:
        findings: list[str] = []

        by_name: dict[str, list[Path]] = defaultdict(list)
        by_hash: dict[str, list[Path]] = defaultdict(list)

        for path in self.root.rglob("*"):
            if (
                not path.is_file()
                or "__pycache__" in path.parts
                or ".git" in path.parts
            ):
                continue

            by_name[path.name].append(path)

            try:
                digest = self._sha256(path)
                by_hash[digest].append(path)
            except OSError:
                continue

        for name, files in by_name.items():
            if len(files) > 1:
                findings.append(
                    f"Duplicate filename: {name} ({len(files)} copies)"
                )
                findings.extend(f"  - {p}" for p in files)

        for digest, files in by_hash.items():
            if len(files) > 1:
                findings.append(
                    f"Duplicate content: SHA256={digest[:12]}... ({len(files)} copies)"
                )
                findings.extend(f"  - {p}" for p in files)

        return findings
""", encoding="utf-8")

print("=" * 60)
print("UEOS Duplicate Scanner Generated")
print(TARGET)
print("=" * 60)
