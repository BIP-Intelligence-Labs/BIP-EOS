"""
bootstrap/plugins/discovery/builder_extractor.py

Builder Intelligence Extractor
"""

from __future__ import annotations

from dataclasses import dataclass, field
from bs4 import BeautifulSoup


@dataclass
class BuilderProfile:
    name: str = ""
    title: str = ""
    description: str = ""
    communities: list[str] = field(default_factory=list)
    plan_links: list[str] = field(default_factory=list)
    image_urls: list[str] = field(default_factory=list)


class BuilderExtractor:
    """Extract builder intelligence from a builder website."""

    COMMUNITY_HINTS = ("community", "communities")
    PLAN_HINTS = ("plan", "floorplan", "floor-plan", "homes")

    def extract(self, html: str) -> BuilderProfile:
        soup = BeautifulSoup(html, "html.parser")

        profile = BuilderProfile()

        if soup.title and soup.title.string:
            profile.title = soup.title.string.strip()
            profile.name = profile.title.split("|")[0].strip()

        meta = soup.find("meta", attrs={"name": "description"})
        if meta:
            profile.description = meta.get("content", "").strip()

        for a in soup.find_all("a", href=True):
            href = a["href"]
            text = a.get_text(" ", strip=True)

            lower = f"{href} {text}".lower()

            if any(k in lower for k in self.COMMUNITY_HINTS):
                if text and text not in profile.communities:
                    profile.communities.append(text)

            if any(k in lower for k in self.PLAN_HINTS):
                if href not in profile.plan_links:
                    profile.plan_links.append(href)

        for img in soup.find_all("img", src=True):
            src = img["src"]
            if src not in profile.image_urls:
                profile.image_urls.append(src)

        return profile


if __name__ == "__main__":
    print("=" * 50)
    print(" Builder Intelligence Extractor")
    print("=" * 50)
    print("Ready.")
