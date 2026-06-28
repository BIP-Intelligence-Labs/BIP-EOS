"""
bootstrap/cli/discover.py

Bootstrap Discover Command
"""

from __future__ import annotations

from bootstrap.plugins.discovery.pipeline import DiscoveryPipeline


class DiscoverCommand:
    """Runs the Universal Discovery Engine."""

    def __init__(self) -> None:
        self.pipeline = DiscoveryPipeline()

    def run(self, url: str) -> None:
        print("=" * 50)
        print(" Bootstrap Universal Discovery Engine")
        print("=" * 50)
        print(f"Target: {url}\n")

        record = self.pipeline.run(url)

        print("\nDiscovery Complete")
        print("------------------")
        print(f"Title : {record.document.title}")
        print(f"Links : {len(record.document.links)}")
        print("✓ Repository updated")
        print("✓ Events published")


if __name__ == "__main__":
    DiscoverCommand().run("https://example.com")
