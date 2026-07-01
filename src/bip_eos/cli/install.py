"""
========================================================================
UEOS

INS-001
Installation CLI

UEOS M-003
========================================================================
"""

from __future__ import annotations

from bip_eos.installer.audit import AuditInstaller
from bip_eos.installer.dispatcher import InstallationDispatcher
from bip_eos.installer.registry import InstallerRegistry


def build_registry() -> InstallerRegistry:
    """
    Build the constitutional installer registry.
    """

    registry = InstallerRegistry()

    registry.register(
        "audit",
        AuditInstaller,
        "eaus",
        "eaus-001",
    )

    #
    # Future constitutional systems
    #

    # registry.register("registry", RegistryInstaller, "ers", "ers-001")
    # registry.register("graph", GraphInstaller, "ueg", "ueg-001")
    # registry.register("compiler", CompilerInstaller, "ecs", "ecs-001")
    # registry.register("publish", PublishInstaller, "epf", "epf-001")
    # registry.register("academy", AcademyInstaller, "eas", "eas-001")

    return registry


def handle(command: str | None, args: list[str]) -> None:
    """
    Handle

        ueos install <subsystem>
    """

    if command is None:
        print("Usage:")
        print()
        print("    ueos install <subsystem>")
        return

    registry = build_registry()

    dispatcher = InstallationDispatcher(registry)

    result = dispatcher.install(command)

    print()
    print("=" * 72)
    print("Installation Result")
    print("=" * 72)
    print(f"Subsystem : {result.subsystem}")
    print(f"Success   : {result.success}")
    print(f"Message   : {result.message}")
    print("=" * 72)
