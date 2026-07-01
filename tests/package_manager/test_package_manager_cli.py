"""
test_package_manager_cli.py

UEOS Atlas
CLI Integration Tests

Exercises the Package Manager CLI entry points.
"""

from __future__ import annotations

import json
import subprocess
import sys


def test_install_command(tmp_path):
    manifest = tmp_path / "package.json"
    manifest.write_text(
        json.dumps(
            {
                "name": "compiler",
                "version": "1.0.0",
                "description": "UEOS Compiler",
            }
        ),
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "bip_eos.cli.commands.install",
            str(manifest),
            "--registry",
            str(tmp_path / "registry"),
            "--cache",
            str(tmp_path / "cache"),
            "--packages",
            str(tmp_path / "packages"),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Installed compiler@1.0.0" in result.stdout


def test_list_command(tmp_path):
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "bip_eos.cli.commands.list",
            "--registry",
            str(tmp_path / "registry"),
            "--cache",
            str(tmp_path / "cache"),
            "--packages",
            str(tmp_path / "packages"),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.strip()


def test_search_command():
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "bip_eos.cli.commands.search",
            "compiler",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "compiler@1.0.0" in result.stdout
