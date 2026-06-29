#!/usr/bin/env python3
"""
formatter.py

BIP EOS CLI Output Formatter
"""

from __future__ import annotations

import json
from typing import Any


class Formatter:
    """Shared formatting helpers for CLI output."""

    @staticmethod
    def json(data: Any) -> str:
        return json.dumps(data, indent=2, default=str)

    @staticmethod
    def kv(data: dict[str, Any]) -> str:
        width = max((len(str(k)) for k in data), default=0)
        return "\n".join(f"{k:<{width}} : {v}" for k, v in data.items())

    @staticmethod
    def table(headers: list[str], rows: list[list[Any]]) -> str:
        cols = len(headers)
        widths = [len(str(h)) for h in headers]
        for row in rows:
            for i in range(min(cols, len(row))):
                widths[i] = max(widths[i], len(str(row[i])))

        def fmt(row):
            return " | ".join(str(row[i]).ljust(widths[i]) for i in range(cols))

        sep = "-+-".join("-" * w for w in widths)

        output = [fmt(headers), sep]
        for row in rows:
            output.append(fmt(row))
        return "\n".join(output)

    @staticmethod
    def title(text: str) -> str:
        line = "=" * 70
        return f"{line}\n{text}\n{line}"


def main():
    print(Formatter.title("BIP EOS Formatter"))
    print(Formatter.kv({
        "Status": "Ready",
        "Version": "0.1.0",
        "Codename": "Genesis"
    }))
    print()
    print(Formatter.table(
        ["Command", "State"],
        [
            ["doctor", "OK"],
            ["status", "OK"],
            ["plugins", "OK"],
        ]
    ))


if __name__ == "__main__":
    main()
