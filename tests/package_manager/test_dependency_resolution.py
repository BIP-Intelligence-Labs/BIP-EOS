"""
test_dependency_resolution.py

UEOS Atlas
Integration Tests

Validates dependency resolution through the package manager.
"""

from __future__ import annotations

from ueos.package_manager.manifest import PackageManifest
from ueos.package_manager.resolver import DependencyResolver


def test_dependency_resolution_success():
    resolver = DependencyResolver()

    manifest = PackageManifest(
        name="compiler",
        version="1.0.0",
        dependencies={
            "runtime": ">=1.0.0",
            "registry": ">=1.0.0",
        },
    )

    available = {
        "runtime": "1.2.0",
        "registry": "1.1.0",
    }

    result = resolver.resolve(manifest, available)

    assert result.success
    assert len(result.issues) == 0
    assert set(result.resolved) == {
        "runtime@1.2.0",
        "registry@1.1.0",
    }


def test_dependency_resolution_failure():
    resolver = DependencyResolver()

    manifest = PackageManifest(
        name="compiler",
        version="1.0.0",
        dependencies={
            "runtime": ">=1.0.0",
            "graph": ">=1.0.0",
        },
    )

    available = {
        "runtime": "1.2.0",
    }

    result = resolver.resolve(manifest, available)

    assert not result.success
    assert len(result.issues) == 1
    assert result.issues[0].package == "graph"


def test_dependency_resolution_no_dependencies():
    resolver = DependencyResolver()

    manifest = PackageManifest(
        name="runtime",
        version="1.0.0",
    )

    result = resolver.resolve(manifest, {})

    assert result.success
    assert result.resolved == []
    assert result.issues == []
