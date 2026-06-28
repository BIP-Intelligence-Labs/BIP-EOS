"""
bootstrap/plugins/discovery/crawler.py

Bootstrap Discovery Crawler
"""

from __future__ import annotations

from dataclasses import dataclass
import requests


@dataclass
class CrawlResult:
    url: str
    status_code: int
    content: str


class DiscoveryCrawler:
    """Simple HTTP crawler used by the Discovery plugin."""

    USER_AGENT = "BootstrapEngineeringLab/0.1"

    def fetch(self, url: str, timeout: int = 20) -> CrawlResult:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": self.USER_AGENT},
        )
        response.raise_for_status()

        return CrawlResult(
            url=url,
            status_code=response.status_code,
            content=response.text,
        )


if __name__ == "__main__":
    print("=" * 40)
    print(" Bootstrap Discovery Crawler")
    print("=" * 40)
    print("Ready to crawl.")
