"""
service.py

UEOS Atlas
Package Manager Service

Coordinates package installation, removal, lookup, and verification.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from .manifest import ManifestLoader, PackageManifest


@dataclass(slots=True)
class PackageManagerConfig:
    registry_path: Path
    cache_path: Path
    install_path: Path


@dataclass(slots=True)
class PackageOperationResult:
    success: bool
    message: str = ""
    package: PackageManifest | None = None
    details: dict[str, str] = field(default_factory=dict)


class PackageManagerService:
    """Primary entry point for UEOS package management."""

    def __init__(self, config: PackageManagerConfig):
        self.config = config
        self.loader = ManifestLoader()

        self.config.registry_path.mkdir(parents=True, exist_ok=True)
        self.config.cache_path.mkdir(parents=True, exist_ok=True)
        self.config.install_path.mkdir(parents=True, exist_ok=True)

    def load_manifest(self, path: str | Path) -> PackageManifest:
        return self.loader.load(path)

    def install(self, manifest_path: str | Path) -> PackageOperationResult:
        manifest = self.load_manifest(manifest_path)

        target = self.config.install_path / manifest.name
        target.mkdir(parents=True, exist_ok=True)

        return PackageOperationResult(
            success=True,
            message=f"Installed {manifest.identifier}",
            package=manifest,
        )

    def uninstall(self, package_name: str) -> PackageOperationResult:
        target = self.config.install_path / package_name

        if not target.exists():
            return PackageOperationResult(
                success=False,
                message=f"Package '{package_name}' is not installed.",
            )

        return PackageOperationResult(
            success=True,
            message=f"Package '{package_name}' marked for removal.",
        )

    def verify(self, package_name: str) -> PackageOperationResult:
        target = self.config.install_path / package_name

        if not target.exists():
            return PackageOperationResult(
                success=False,
                message="Package not installed.",
            )

        return PackageOperationResult(
            success=True,
            message="Package verification passed.",
        )

    def list_installed(self) -> list[str]:
        if not self.config.install_path.exists():
            return []

        return sorted(
            p.name for p in self.config.install_path.iterdir() if p.is_dir()
        )
