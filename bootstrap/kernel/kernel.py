"""bootstrap/kernel/kernel.py"""

from dataclasses import dataclass, field
from typing import Dict

from .event_bus import EventBus
from .registry import CommandRegistry
from .configuration import Configuration
from .workspace import Workspace
from .plugin_loader import PluginLoader
from .lifecycle import LifecycleManager


class BootstrapPlugin:
    name = "unnamed"

    def register(self, kernel):
        raise NotImplementedError

    def start(self):
        pass

    def stop(self):
        pass


@dataclass
class BootstrapKernel:
    plugins: Dict[str, BootstrapPlugin] = field(default_factory=dict)

    def __post_init__(self):
        self.config = Configuration()
        self.workspace = Workspace(self.config.get("workspace", "./workspace"))
        self.events = EventBus()
        self.commands = CommandRegistry()
        self.loader = PluginLoader()
        self.lifecycle = LifecycleManager()

    def install(self, plugin):
        plugin.register(self)
        self.plugins[plugin.name] = plugin

    def boot(self):
        self.lifecycle.startup()
        self.loader.discover()
        for plugin in self.plugins.values():
            plugin.start()
        self.events.emit("kernel.booted")

    def shutdown(self):
        for plugin in self.plugins.values():
            plugin.stop()
        self.lifecycle.shutdown()

    def status(self):
        return {
            "plugins": len(self.plugins),
            "workspace": self.workspace.path,
            "environment": self.config.get("environment", "development"),
        }
