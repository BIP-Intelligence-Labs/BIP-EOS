"""
========================================================================
INS-001
UEOS Installation Framework

Installation Dispatcher
========================================================================
"""

from __future__ import annotations

from .registry import InstallerRegistry


class InstallationDispatcher:
    """
    Dispatches installation requests to registered installers.
    """

    def __init__(self, registry: InstallerRegistry) -> None:
        self._registry = registry

    def install(self, subsystem: str):
        """
        Install a constitutional subsystem.
        """
        installer_cls = self._registry.get(subsystem)
        installer = installer_cls()

        # Banner is printed by the installer itself.
        return installer.install()

    def verify(self, subsystem: str):
        installer_cls = self._registry.get(subsystem)
        installer = installer_cls()
        return installer.verify()

    def update(self, subsystem: str):
        installer_cls = self._registry.get(subsystem)
        installer = installer_cls()
        return installer.update()

    def repair(self, subsystem: str):
        installer_cls = self._registry.get(subsystem)
        installer = installer_cls()
        return installer.repair()

    def uninstall(self, subsystem: str):
        installer_cls = self._registry.get(subsystem)
        installer = installer_cls()
        return installer.uninstall()
