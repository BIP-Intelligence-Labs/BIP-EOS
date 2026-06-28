"""
bootstrap/plugins/discovery/extractor.py

Universal Discovery Engine HTML Extractor
"""

from __future__ import annotations

from dataclasses import dataclass
from bs4 import BeautifulSoup


@dataclass
class ExtractedDocument:
    title: str
    description: str
    links: list[str]


class DiscoveryExtractor:
    """Extracts structured information from HTML."""

    def extract(self, html: str) -> ExtractedDocument:
        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.string.strip() if soup.title and soup.title.string else ""

        description = ""
        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            description = meta.get("content", "").strip()

        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href not in links:
                links.append(href)

        return ExtractedDocument(
            title=title,
            description=description,
            links=links,
        )


if __name__ == "__main__":
    print("=" * 40)
    print(" Bootstrap Discovery Extractor")
    print("=" * 40)
    print("Ready to extract HTML.")
