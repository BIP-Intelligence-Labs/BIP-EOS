"""
test_registry.py

UEOS Atlas
Package Registry Tests
"""

from __future__ import annotations

from ueos.package_manager.manifest import PackageManifest
from ueos.package_manager.registry import PackageRegistry


def test_register_package():
    registry = PackageRegistry()

    manifest = PackageManifest(
        name="compiler",
        version="1.0.0",
        description="UEOS Compiler",
    )

    registry.register(manifest)

    assert registry.exists("compiler")
    assert len(registry) == 1


def test_get_package():
    registry = PackageRegistry()

    manifest = PackageManifest(
        name="runtime",
        version="1.0.0",
        description="UEOS Runtime",
    )

    registry.register(manifest)

    loaded = registry.get("runtime")

    assert loaded is not None
    assert loaded.identifier == "runtime@1.0.0"


def test_search_packages():
    registry = PackageRegistry()

    registry.load([
        PackageManifest(
            name="compiler",
            version="1.0.0",
            description="Compiler",
        ),
        PackageManifest(
            name="runtime",
            version="1.0.0",
            description="Runtime",
        ),
    ])

    matches = registry.search("comp")

    assert len(matches) == 1
    assert matches[0].name == "compiler"


def test_unregister_package():
    registry = PackageRegistry()

    registry.register(
        PackageManifest(
            name="graph",
            version="1.0.0",
        )
    )

    assert registry.unregister("graph") is True
    assert registry.exists("graph") is False
    assert len(registry) == 0
