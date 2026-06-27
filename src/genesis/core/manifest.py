
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import tomllib

@dataclass
class Manifest:
    path: Path

class ManifestError(Exception):
    pass

class ManifestReader:
    def read(self, path: Path) -> dict:
        with path.open("rb") as f:
            return tomllib.load(f)

class ManifestWriter:
    def write(self, path: Path, content: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

class ManifestValidator:
    def validate(self, path: Path) -> bool:
        try:
            ManifestReader().read(path)
            return True
        except Exception as exc:
            raise ManifestError(str(exc))

class ManifestEngine:
    def create(self, path: Path, content: str) -> bool:
        ManifestWriter().write(path, content)
        return ManifestValidator().validate(path)
