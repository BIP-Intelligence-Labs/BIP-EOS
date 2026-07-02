"""
registry.py

UEOS Atlas
Package Registry

In-memory package registry used by the Package Manager.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .manifest import PackageManifest


@dataclass(slots=True)
class RegistryEntry:
    """A registered package."""

    manifest: PackageManifest


class PackageRegistry:
    """Stores and queries available packages."""

    def __init__(self) -> None:
        self._packages: dict[str, RegistryEntry] = {}

    def register(self, manifest: PackageManifest) -> None:
        self._packages[manifest.name] = RegistryEntry(manifest)

    def unregister(self, package_name: str) -> bool:
        return self._packages.pop(package_name, None) is not None

    def exists(self, package_name: str) -> bool:
        return package_name in self._packages

    def get(self, package_name: str) -> PackageManifest | None:
        entry = self._packages.get(package_name)
        return entry.manifest if entry else None

    def list(self) -> list[PackageManifest]:
        return sorted(
            (entry.manifest for entry in self._packages.values()),
            key=lambda m: m.name.lower(),
        )

    def search(self, text: str) -> list[PackageManifest]:
        query = text.lower()
        return [
            m for m in self.list()
            if query in m.name.lower() or query in m.description.lower()
        ]

    def load(self, manifests: Iterable[PackageManifest]) -> None:
        for manifest in manifests:
            self.register(manifest)

    def __len__(self) -> int:
        return len(self._packages)
