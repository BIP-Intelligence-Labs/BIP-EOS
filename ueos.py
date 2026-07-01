#!/usr/bin/env python3
"""
bootstrap.py

UEOS Bootstrap CLI
Architecture Version: 1.0 (Genesis)

Single entry point for all UEOS bootstrap operations.
"""

from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path

COMMANDS = {
    "architecture": "bootstrap/architecture",
    "runtime": "bootstrap/runtime",
    "engineering": "bootstrap/engineering",
    "registry": "bootstrap/registry",
    "graph": "bootstrap/graph",
    "compiler": "bootstrap/compiler",
    "publishing": "bootstrap/publishing",
    "academy": "bootstrap/academy",
    "knowledge": "bootstrap/knowledge",
    "doctor": None,
    "validate": None,
    "clean": None,
    "migrate": "bootstrap/migrations",
    "build": None,
    "install": None,
    "update": None,
}


def repo_root() -> Path:
    return Path(__file__).resolve().parent


def find_first_python(directory: Path) -> Path | None:
    if not directory.exists():
        return None
    files = sorted(p for p in directory.glob("*.py") if p.name != "__init__.py")
    return files[0] if files else None


def doctor(root: Path) -> int:
    print("UEOS Repository Doctor")
    print("=" * 72)
    checks = [
        "src",
        "engineering",
        "bootstrap",
        "tests",
        "docs",
        "tools",
        "pyproject.toml",
        "README.md",
    ]
    ok = True
    for item in checks:
        exists = (root / item).exists()
        print(f"[{'OK' if exists else 'MISSING':7}] {item}")
        ok &= exists
    return 0 if ok else 1


def validate(root: Path) -> int:
    print("UEOS Validation")
    print("=" * 72)
    print("Repository layout validation complete.")
    return doctor(root)


def main() -> int:
    parser = argparse.ArgumentParser(description="UEOS Bootstrap CLI")
    parser.add_argument("command", nargs="?", help="Command")
    parser.add_argument("target", nargs="?", help="Optional build target")
    args = parser.parse_args()

    if not args.command:
        print("UEOS Bootstrap CLI\n")
        print("Commands:")
        for cmd in COMMANDS:
            print(f"  {cmd}")
        return 0

    root = repo_root()
    cmd = args.command.lower()

    if cmd not in COMMANDS:
        print(f"Unknown command: {cmd}")
        return 1

    if cmd == "doctor":
        return doctor(root)

    if cmd == "validate":
        return validate(root)

    if cmd == "build":
        if not args.target:
            print("Usage: py bootstrap.py build <target>")
            return 1
        target = args.target.lower()
        if target not in COMMANDS or COMMANDS[target] is None:
            print(f"Unsupported build target: {target}")
            return 1
        directory = root / COMMANDS[target]
        script = find_first_python(directory)
        if not script:
            print(f"No bootstrap script found in {directory}")
            return 1
        sys.argv = [str(script)]
        runpy.run_path(str(script), run_name="__main__")
        return 0

    location = COMMANDS[cmd]
    if location is None:
        print(f"'{cmd}' command is reserved for future implementation.")
        return 0

    directory = root / location
    script = find_first_python(directory)
    if not script:
        print(f"No bootstrap script found in {directory}")
        return 1

    print(f"Running {script.relative_to(root)}")
    sys.argv = [str(script)]
    runpy.run_path(str(script), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
