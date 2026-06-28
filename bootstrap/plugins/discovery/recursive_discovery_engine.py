"""
bootstrap/plugins/discovery/rde.py

Recursive Discovery Engine (RDE)

Builds on the Universal Discovery Engine by recursively discovering
additional pages within the same domain.
"""

from __future__ import annotations

from collections import deque
from urllib.parse import urljoin, urlparse

from .pipeline import DiscoveryPipeline


class RecursiveDiscoveryEngine:
    """Recursively discovers pages within a website."""

    def __init__(self, max_pages: int = 25) -> None:
        self.pipeline = DiscoveryPipeline()
        self.max_pages = max_pages
        self.visited: set[str] = set()

    def discover(self, start_url: str) -> set[str]:
        queue = deque([start_url])
        domain = urlparse(start_url).netloc

        while queue and len(self.visited) < self.max_pages:
            url = queue.popleft()

            if url in self.visited:
                continue

            print(f"→ Discovering: {url}")

            result = self.pipeline.run(url)
            self.visited.add(url)

            for href in result.record.document.links:
                absolute = urljoin(url, href)

                parsed = urlparse(absolute)

                if parsed.netloc != domain:
                    continue

                if absolute not in self.visited:
                    queue.append(absolute)

        print("\nRecursive Discovery Complete")
        print(f"Pages Discovered: {len(self.visited)}")

        return self.visited


if __name__ == "__main__":
    print("=" * 50)
    print(" Recursive Discovery Engine (RDE)")
    print("=" * 50)
    print("Ready.")
