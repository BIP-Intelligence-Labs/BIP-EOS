"""
cache.py

UEOS Atlas
Package Cache

Manages the local package cache.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class CacheEntry:
    package: str
    version: str
    location: Path
    checksum: str


class PackageCache:
    """Manages cached package artifacts."""

    def __init__(self, cache_root: str | Path):
        self.cache_root = Path(cache_root)
        self.cache_root.mkdir(parents=True, exist_ok=True)

    def package_path(self, package: str, version: str) -> Path:
        return self.cache_root / package / version

    def exists(self, package: str, version: str) -> bool:
        return self.package_path(package, version).exists()

    def store(self, package: str, version: str, artifact: bytes) -> CacheEntry:
        target = self.package_path(package, version)
        target.mkdir(parents=True, exist_ok=True)

        archive = target / "package.bin"
        archive.write_bytes(artifact)

        checksum = hashlib.sha256(artifact).hexdigest()

        (target / "SHA256").write_text(checksum, encoding="utf-8")

        return CacheEntry(
            package=package,
            version=version,
            location=archive,
            checksum=checksum,
        )

    def remove(self, package: str, version: str) -> bool:
        target = self.package_path(package, version)

        if not target.exists():
            return False

        for child in target.iterdir():
            child.unlink()

        target.rmdir()

        parent = target.parent
        if parent.exists() and not any(parent.iterdir()):
            parent.rmdir()

        return True

    def clear(self) -> None:
        if not self.cache_root.exists():
            return

        for path in sorted(self.cache_root.rglob("*"), reverse=True):
            if path.is_file():
                path.unlink()
            elif path.is_dir():
                path.rmdir()
