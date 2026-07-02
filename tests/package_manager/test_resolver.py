"""
test_resolver.py

UEOS Atlas
Dependency Resolver Tests
"""

from __future__ import annotations

from ueos.package_manager.manifest import PackageManifest
from ueos.package_manager.resolver import DependencyResolver


def test_resolve_success():
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
        "runtime": "1.0.0",
        "registry": "1.0.0",
    }

    result = resolver.resolve(manifest, available)

    assert result.success
    assert len(result.issues) == 0
    assert len(result.resolved) == 2
    assert "runtime@1.0.0" in result.resolved
    assert "registry@1.0.0" in result.resolved


def test_resolve_missing_dependency():
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
        "runtime": "1.0.0",
    }

    result = resolver.resolve(manifest, available)

    assert not result.success
    assert len(result.issues) == 1
    assert result.issues[0].package == "graph"
    assert result.issues[0].message == "Package not found."


def test_resolve_without_dependencies():
    resolver = DependencyResolver()

    manifest = PackageManifest(
        name="runtime",
        version="1.0.0",
    )

    result = resolver.resolve(manifest, {})

    assert result.success
    assert result.resolved == []
    assert result.issues == []
