"""
test_package_installation.py

UEOS Atlas
Integration Tests

Validates package installation workflow.
"""

from __future__ import annotations

from pathlib import Path

from ueos.package_manager.service import (
    PackageManagerConfig,
    PackageManagerService,
)


def test_package_installation(tmp_path):
    manifest = tmp_path / "package.json"

    manifest.write_text(
        """
{
    "name": "compiler",
    "version": "1.0.0",
    "description": "UEOS Compiler"
}
""".strip(),
        encoding="utf-8",
    )

    service = PackageManagerService(
        PackageManagerConfig(
            registry_path=tmp_path / "registry",
            cache_path=tmp_path / "cache",
            install_path=tmp_path / "packages",
        )
    )

    result = service.install(manifest)

    assert result.success
    assert result.package is not None
    assert result.package.name == "compiler"

    installed = service.list_installed()

    assert "compiler" in installed


def test_install_missing_manifest(tmp_path):
    service = PackageManagerService(
        PackageManagerConfig(
            registry_path=tmp_path / "registry",
            cache_path=tmp_path / "cache",
            install_path=tmp_path / "packages",
        )
    )

    try:
        service.install(tmp_path / "missing.json")
    except Exception:
        return

    raise AssertionError("Expected installation to fail for a missing manifest.")
