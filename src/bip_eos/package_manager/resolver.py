"""
resolver.py

UEOS Atlas
Dependency Resolver

Resolves and validates package dependencies.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .manifest import PackageManifest


@dataclass(slots=True)
class DependencyIssue:
    package: str
    requirement: str
    message: str


@dataclass(slots=True)
class DependencyResolution:
    success: bool
    resolved: list[str] = field(default_factory=list)
    issues: list[DependencyIssue] = field(default_factory=list)


class DependencyResolver:
    """Resolves package dependency graphs."""

    def resolve(
        self,
        manifest: PackageManifest,
        available_packages: dict[str, str],
    ) -> DependencyResolution:

        result = DependencyResolution(success=True)

        for package, requirement in manifest.dependencies.items():
            version = available_packages.get(package)

            if version is None:
                result.success = False
                result.issues.append(
                    DependencyIssue(
                        package=package,
                        requirement=requirement,
                        message="Package not found.",
                    )
                )
                continue

            result.resolved.append(f"{package}@{version}")

        return result
