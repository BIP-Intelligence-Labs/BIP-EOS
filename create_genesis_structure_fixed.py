"""
create_genesis_structure.py

Creates the initial Genesis / Bootstrap Kernel package structure.
"""

from pathlib import Path

ROOT = Path("genesis")

folders = [
    ROOT / "bootstrap" / "kernel",
    ROOT / "bootstrap" / "plugins",
    ROOT / "bootstrap" / "commands",
    ROOT / "bootstrap" / "templates",
    ROOT / "bootstrap" / "tests",
    ROOT / "bootstrap" / "docs",
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

files = {
    ROOT / "bootstrap" / "kernel" / "__init__.py": '"""Bootstrap Kernel Package"""\n',
    ROOT / "bootstrap" / "kernel" / "kernel.py": '"""Bootstrap Kernel"""\n',
    ROOT / "bootstrap" / "kernel" / "event_bus.py": '"""Event Bus"""\n',
    ROOT / "bootstrap" / "kernel" / "plugin_loader.py": '"""Plugin Loader"""\n',
    ROOT / "bootstrap" / "kernel" / "lifecycle.py": '"""Lifecycle Manager"""\n',
    ROOT / "bootstrap" / "kernel" / "registry.py": '"""Registry"""\n',
    ROOT / "bootstrap" / "kernel" / "configuration.py": '"""Configuration"""\n',
    ROOT / "bootstrap" / "kernel" / "workspace.py": '"""Workspace"""\n',
    ROOT / "bootstrap" / "kernel" / "cli.py": '"""Bootstrap CLI"""\n',
}

for path, content in files.items():
    if not path.exists():
        path.write_text(content, encoding="utf-8")

print()
print("Genesis structure created successfully!")
print(ROOT.resolve())
