#!/usr/bin/env python3
"""
documentation_engine.py

BIP EOS Documentation Engine
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Document:
    title: str
    filename: str
    content: str


class DocumentationEngine:
    def __init__(self, root: Path | None = None):
        self.root = root or Path.cwd()
        self.docs = self.root / "docs"
        self.docs.mkdir(parents=True, exist_ok=True)

    def generate(self):
        generated = datetime.utcnow().isoformat()

        documents = [
            Document(
                "Architecture",
                "architecture.md",
                f"# BIP EOS Architecture\n\nGenerated: {generated}\n",
            ),
            Document(
                "ADR Index",
                "adr-index.md",
                f"# Architecture Decision Records\n\nGenerated: {generated}\n",
            ),
            Document(
                "Engineering Log",
                "engineering-log.md",
                f"# Engineering Log\n\nGenerated: {generated}\n",
            ),
            Document(
                "System Overview",
                "system-overview.md",
                f"# BIP EOS System Overview\n\nGenerated: {generated}\n",
            ),
        ]

        created = []

        for doc in documents:
            path = self.docs / doc.filename
            if not path.exists():
                path.write_text(doc.content, encoding="utf-8")
                created.append(path.name)

        return {
            "generated": generated,
            "created": created,
            "docs_directory": str(self.docs),
        }

    def status(self):
        return {
            "docs_directory": str(self.docs),
            "documents": len(list(self.docs.glob("*.md"))),
        }


def main():
    engine = DocumentationEngine()
    result = engine.generate()

    print("=" * 70)
    print("BIP EOS Documentation Engine")
    print("=" * 70)
    print(f"Documents created : {len(result['created'])}")
    for name in result["created"]:
        print(f"  - {name}")
    print(f"Documentation Dir : {result['docs_directory']}")
    print("=" * 70)


if __name__ == "__main__":
    main()
