"""
Bootstrap Kernel v0.0.2
========================

Adds:
- Configuration
- Lifecycle manager
- Plugin loader
- Dependency graph
- Workspace
- Logger
"""

from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Dict, List, Callable, Any
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")


class BootstrapPlugin(ABC):
    name = "unnamed"
    version = "0.0.1"
    dependencies: List[str] = []

    @abstractmethod
    def register(self, kernel): ...

    def start(self): ...
    def stop(self): ...


class Configuration:
    def __init__(self):
        self.settings = {"workspace": "./workspace", "environment": "development"}

    def get(self, key, default=None):
        return self.settings.get(key, default)


class Workspace:
    def __init__(self, path):
        self.path = path


class EventBus:
    def __init__(self):
        self.handlers: Dict[str, List[Callable]] = {}

    def on(self, event, handler):
        self.handlers.setdefault(event, []).append(handler)

    def emit(self, event, **kwargs):
        logging.info("EVENT -> %s", event)
        for h in self.handlers.get(event, []):
            h(**kwargs)


class CommandRegistry:
    def __init__(self):
        self.commands: Dict[str, Callable[..., Any]] = {}

    def register(self, name, func):
        self.commands[name] = func

    def execute(self, name, *args, **kwargs):
        return self.commands[name](*args, **kwargs)


class DependencyGraph:
    def validate(self, plugins):
        logging.info("Dependency graph validated (%d plugins)", len(plugins))


class PluginLoader:
    def discover(self):
        logging.info("Plugin discovery complete")


class LifecycleManager:
    def startup(self):
        logging.info("Kernel startup")

    def shutdown(self):
        logging.info("Kernel shutdown")


@dataclass
class BootstrapKernel:
    plugins: Dict[str, BootstrapPlugin] = field(default_factory=dict)

    def __post_init__(self):
        self.config = Configuration()
        self.workspace = Workspace(self.config.get("workspace"))
        self.events = EventBus()
        self.commands = CommandRegistry()
        self.loader = PluginLoader()
        self.lifecycle = LifecycleManager()
        self.graph = DependencyGraph()

    def install(self, plugin: BootstrapPlugin):
        plugin.register(self)
        self.plugins[plugin.name] = plugin

    def boot(self):
        self.lifecycle.startup()
        self.loader.discover()
        self.graph.validate(self.plugins)
        for p in self.plugins.values():
            p.start()
        self.events.emit("kernel.booted")

    def status(self):
        print(f"Workspace : {self.workspace.path}")
        print(f"Plugins   : {len(self.plugins)}")


class HelloPlugin(BootstrapPlugin):
    name = "hello"
    version = "0.0.2"

    def register(self, kernel):
        kernel.commands.register("about", self.about)
        kernel.events.on("kernel.booted", lambda: logging.info("Hello plugin ready"))

    def about(self):
        print("""
Bootstrap Engineering Factory
Kernel v0.0.2

Built with

1s
0s
Coffee
Two Chiefs

Ready to do some more damage.
""")


if __name__ == "__main__":
    kernel = BootstrapKernel()
    kernel.install(HelloPlugin())
    kernel.boot()
    kernel.status()
    kernel.commands.execute("about")
