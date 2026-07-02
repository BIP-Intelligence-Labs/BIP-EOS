"""
installer.py

UEOS Atlas
Package Installer

Coordinates installation of UEOS packages.
"""

from __future__ import annotations

from dataclasses import dataclass

from .manifest import PackageManifest
from .registry import PackageRegistry
from .resolver import DependencyResolver, DependencyResolution


@dataclass(slots=True)
class InstallResult:
    success: bool
    message: str
    dependency_result: DependencyResolution | None = None


class PackageInstaller:
    """Installs packages after dependency validation."""

    def __init__(
        self,
        registry: PackageRegistry,
        resolver: DependencyResolver,
    ) -> None:
        self.registry = registry
        self.resolver = resolver

    def install(
        self,
        manifest: PackageManifest,
        available_packages: dict[str, str],
    ) -> InstallResult:

        resolution = self.resolver.resolve(
            manifest,
            available_packages,
        )

        if not resolution.success:
            return InstallResult(
                success=False,
                message="Dependency resolution failed.",
                dependency_result=resolution,
            )

        self.registry.register(manifest)

        return InstallResult(
            success=True,
            message=f"Installed {manifest.identifier}",
            dependency_result=resolution,
        )

    def upgrade(
        self,
        manifest: PackageManifest,
        available_packages: dict[str, str],
    ) -> InstallResult:
        return self.install(manifest, available_packages)

    def remove(self, package_name: str) -> InstallResult:
        if not self.registry.unregister(package_name):
            return InstallResult(
                success=False,
                message=f"Package '{package_name}' is not installed.",
            )

        return InstallResult(
            success=True,
            message=f"Removed '{package_name}'.",
        )
