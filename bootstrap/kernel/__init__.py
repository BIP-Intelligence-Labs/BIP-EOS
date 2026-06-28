"""
Bootstrap Kernel Package

The public interface for the Bootstrap Engineering Factory Kernel.
"""

from .kernel import BootstrapKernel, BootstrapPlugin
from .event_bus import EventBus
from .registry import CommandRegistry
from .configuration import Configuration
from .workspace import Workspace
from .plugin_loader import PluginLoader
from .lifecycle import LifecycleManager, KernelState

__all__ = [
    "BootstrapKernel",
    "BootstrapPlugin",
    "EventBus",
    "CommandRegistry",
    "Configuration",
    "Workspace",
    "PluginLoader",
    "LifecycleManager",
    "KernelState",
]

__version__ = "0.1.0"
