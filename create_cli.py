"""
create_cli.py

Creates the Bootstrap CLI structure.

Run:
    python create_cli.py
"""

from pathlib import Path

root = Path("bootstrap") / "cli"

files = {
    "__init__.py": '"""Bootstrap CLI Package."""\n',
    "bootstrap.py": '"""CLI entry point."""\n',
    "project_locator.py": '"""Project locator."""\n',
    "command_dispatcher.py": '"""Command dispatcher."""\n',
    "generator.py": '"""Scaffold generator."""\n',
    "doctor.py": '"""Repository diagnostics."""\n',
    "repair.py": '"""Repository repair commands."""\n',
    "release.py": '"""Release management."""\n',
    "README.md": "# Bootstrap CLI\n\nCommand-line tools for the Bootstrap Engineering Factory.\n",
}

templates = root / "templates"
templates.mkdir(parents=True, exist_ok=True)

for name, content in files.items():
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")
        print(f"✓ Created {path}")
    else:
        print(f"• Exists   {path}")

print("\n✓ Bootstrap CLI scaffold ready.")
