"""
base_plugin.py

Common plugin contract for all BIP EOS plugins.
"""

from abc import ABC, abstractmethod


class BasePlugin(ABC):
    """Base contract implemented by every BIP EOS plugin."""

    name: str = "plugin"
    version: str = "0.1.0"

    @abstractmethod
    def load(self) -> None:
        """Initialize the plugin."""
        raise NotImplementedError

    @abstractmethod
    def capabilities(self):
        """Return plugin capabilities."""
        raise NotImplementedError


class AcademyPlugin(BasePlugin):
    name = "academy"

    def load(self):
        print(f"Loading {self.name} plugin")

    def capabilities(self):
        return {"courses": True, "certifications": True}


class AIPlugin(BasePlugin):
    name = "ai"

    def load(self):
        print(f"Loading {self.name} plugin")

    def capabilities(self):
        return {"providers": True, "agents": True, "reasoning": True}


class BuildersPlugin(BasePlugin):
    name = "builders"

    def load(self):
        print(f"Loading {self.name} plugin")

    def capabilities(self):
        return {"recommendations": True, "questionnaires": True, "crm": True}


class ReportsPlugin(BasePlugin):
    name = "reports"

    def load(self):
        print(f"Loading {self.name} plugin")

    def capabilities(self):
        return {
            "exports": {
                "pdf": True,
                "docx": True,
                "html": True,
            }
        }


class SalesPlugin(BasePlugin):
    name = "sales"

    def load(self):
        print(f"Loading {self.name} plugin")

    def capabilities(self):
        return {"pipeline": True, "follow_up": True, "analytics": True}


PLUGINS = [
    AcademyPlugin,
    AIPlugin,
    BuildersPlugin,
    ReportsPlugin,
    SalesPlugin,
]
