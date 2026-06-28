"""
bootstrap_new.py

Bootstrap Project Generator

Usage:
    python bootstrap_new.py plugin discovery
"""

from pathlib import Path
import sys

def create_plugin(name: str):
    root = Path("bootstrap") / "plugins" / name
    (root / "tests").mkdir(parents=True, exist_ok=True)

    templates = {
        "__init__.py": f'"""Bootstrap {name.title()} Plugin"""\n',
        "plugin.py": f'"""Main plugin for {name}."""\n',
        "crawler.py": "",
        "extractor.py": "",
        "validator.py": "",
        "repository.py": "",
        "scheduler.py": "",
        "configuration.py": "",
        "models.py": "",
        "README.md": f"# {name.title()} Plugin\n",
        "tests/__init__.py": "",
        "tests/test_plugin.py": '"""Plugin tests."""\n',
    }

    for rel, content in templates.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(content, encoding="utf-8")

    print(f"✓ Plugin '{name}' created at {root}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python bootstrap_new.py plugin <name>")
        raise SystemExit(1)

    resource, name = sys.argv[1], sys.argv[2]

    if resource == "plugin":
        create_plugin(name)
    else:
        raise SystemExit(f"Unknown resource: {resource}")

if __name__ == "__main__":
    main()
