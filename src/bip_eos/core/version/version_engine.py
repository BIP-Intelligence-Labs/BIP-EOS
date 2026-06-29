#!/usr/bin/env python3
"""
version_engine.py

BIP EOS Version Engine
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
import json


@dataclass
class VersionInfo:
    version: str = "0.1.0"
    codename: str = "Genesis"
    product: str = "BIP EOS"
    build: int = 1
    released: str | None = None


class VersionEngine:
    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()
        self.file = self.root / "VERSION.json"

    def load(self) -> VersionInfo:
        if self.file.exists():
            data = json.loads(self.file.read_text(encoding="utf-8"))
            return VersionInfo(**data)
        return VersionInfo()

    def save(self, info: VersionInfo) -> None:
        self.file.write_text(
            json.dumps(asdict(info), indent=2),
            encoding="utf-8"
        )

    def bump(self, level: str = "patch") -> VersionInfo:
        info = self.load()
        major, minor, patch = map(int, info.version.split("."))

        if level == "major":
            major += 1
            minor = patch = 0
        elif level == "minor":
            minor += 1
            patch = 0
        else:
            patch += 1

        info.version = f"{major}.{minor}.{patch}"
        info.build += 1
        info.released = datetime.utcnow().isoformat()

        self.save(info)
        return info

    def status(self) -> dict:
        info = self.load()
        return asdict(info)


def main():
    engine = VersionEngine()
    info = engine.load()

    print("=" * 70)
    print("BIP EOS Version Engine")
    print("=" * 70)
    print(f"Product  : {info.product}")
    print(f"Version  : {info.version}")
    print(f"Codename : {info.codename}")
    print(f"Build    : {info.build}")
    print("=" * 70)


if __name__ == "__main__":
    main()
