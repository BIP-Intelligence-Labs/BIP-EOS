#!/usr/bin/env python3
"""
console.py

BIP EOS Console Utilities
"""

from __future__ import annotations

import json
from typing import Any


class Console:
    WIDTH = 70

    @staticmethod
    def banner(title: str) -> None:
        print("=" * Console.WIDTH)
        print(title)
        print("=" * Console.WIDTH)

    @staticmethod
    def section(title: str) -> None:
        print("\n" + "-" * Console.WIDTH)
        print(title)
        print("-" * Console.WIDTH)

    @staticmethod
    def success(message: str) -> None:
        print(f"[ OK ] {message}")

    @staticmethod
    def warning(message: str) -> None:
        print(f"[WARN] {message}")

    @staticmethod
    def error(message: str) -> None:
        print(f"[FAIL] {message}")

    @staticmethod
    def json(data: Any) -> None:
        print(json.dumps(data, indent=2, default=str))


def main():
    Console.banner("BIP EOS Console")
    Console.success("Console initialized")
    Console.section("Sample JSON")
    Console.json({"status": "ready"})


if __name__ == "__main__":
    main()
