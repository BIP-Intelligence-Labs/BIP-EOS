"""
bootstrap/plugins/discovery/builder_pipeline.py

Builder Intelligence Pipeline
"""

from __future__ import annotations

from .pipeline import DiscoveryPipeline
from .builder_extractor import BuilderExtractor


class BuilderDiscoveryPipeline(DiscoveryPipeline):
    """Discovery pipeline specialized for home builder websites."""

    def __init__(self) -> None:
        super().__init__()
        self.builder_extractor = BuilderExtractor()

    def discover_builder(self, url: str):
        record = self.run(url)

        profile = self.builder_extractor.extract(
            record.document.title if False else self.crawler.fetch(url).content
        )

        print("\nBuilder Intelligence")
        print("--------------------")
        print(f"Builder      : {profile.name}")
        print(f"Communities  : {len(profile.communities)}")
        print(f"Plan Links   : {len(profile.plan_links)}")
        print(f"Images       : {len(profile.image_urls)}")

        return profile


if __name__ == "__main__":
    print("=" * 50)
    print(" Builder Discovery Pipeline")
    print("=" * 50)
    print("Ready.")
