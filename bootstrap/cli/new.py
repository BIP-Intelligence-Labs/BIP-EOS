"""
bootstrap/cli/new.py

Bootstrap "new" command.
"""

from __future__ import annotations

from .generator import Generator
from .project_locator import ProjectLocator


class NewCommand:
    """Creates Bootstrap resources."""

    def __init__(self) -> None:
        self.root = ProjectLocator.find_root()
        self.generator = Generator(self.root)

    def plugin(self, name: str) -> None:
        base = f"bootstrap/plugins/{name}"

        files = {
            f"{base}/__init__.py": f'"""Bootstrap {name.title()} Plugin."""\n',
            f"{base}/plugin.py": f'"""Main plugin."""\n',
            f"{base}/crawler.py": "",
            f"{base}/extractor.py": "",
            f"{base}/validator.py": "",
            f"{base}/repository.py": "",
            f"{base}/scheduler.py": "",
            f"{base}/configuration.py": "",
            f"{base}/models.py": "",
            f"{base}/README.md": f"# {name.title()} Plugin\n",
            f"{base}/tests/__init__.py": "",
            f"{base}/tests/test_plugin.py": '"""Plugin tests."""\n',
        }

        self.generator.scaffold(files)
        print(f"✓ Plugin '{name}' created.")


if __name__ == "__main__":
    NewCommand().plugin("example")
