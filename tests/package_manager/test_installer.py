"""
test_installer.py

UEOS Atlas
Package Installer Tests
"""

from __future__ import annotations

from bip_eos.package_manager.installer import PackageInstaller
from bip_eos.package_manager.manifest import PackageManifest
from bip_eos.package_manager.registry import PackageRegistry
from bip_eos.package_manager.resolver import DependencyResolver


def test_install_success():
    registry = PackageRegistry()
    resolver = DependencyResolver()
    installer = PackageInstaller(registry, resolver)

    manifest = PackageManifest(
        name="compiler",
        version="1.0.0",
        dependencies={"runtime": ">=1.0.0"},
    )

    result = installer.install(
        manifest,
        {"runtime": "1.0.0"},
    )

    assert result.success
    assert registry.exists("compiler")


def test_install_missing_dependency():
    registry = PackageRegistry()
    resolver = DependencyResolver()
    installer = PackageInstaller(registry, resolver)

    manifest = PackageManifest(
        name="compiler",
        version="1.0.0",
        dependencies={"runtime": ">=1.0.0"},
    )

    result = installer.install(
        manifest,
        {},
    )

    assert not result.success
    assert result.dependency_result is not None
    assert len(result.dependency_result.issues) == 1


def test_remove_package():
    registry = PackageRegistry()
    resolver = DependencyResolver()
    installer = PackageInstaller(registry, resolver)

    registry.register(
        PackageManifest(
            name="runtime",
            version="1.0.0",
        )
    )

    result = installer.remove("runtime")

    assert result.success
    assert not registry.exists("runtime")


def test_remove_missing_package():
    registry = PackageRegistry()
    resolver = DependencyResolver()
    installer = PackageInstaller(registry, resolver)

    result = installer.remove("missing")

    assert not result.success
