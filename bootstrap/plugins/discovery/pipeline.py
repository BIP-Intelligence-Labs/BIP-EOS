"""
bootstrap/plugins/discovery/pipeline.py

Engineering Improvement:
- Fetches the page only once.
- Returns both the repository record and the downloaded HTML.
"""

from __future__ import annotations

from dataclasses import dataclass

from .crawler import DiscoveryCrawler
from .extractor import DiscoveryExtractor
from .validator import DiscoveryValidator
from .repository import DiscoveryRepository
from .scheduler import DiscoveryScheduler
from .kernel_events import DiscoveryKernelEvents


@dataclass
class DiscoveryResult:
    record: object
    html: str


class DiscoveryPipeline:

    def __init__(self) -> None:
        self.scheduler = DiscoveryScheduler()
        self.crawler = DiscoveryCrawler()
        self.extractor = DiscoveryExtractor()
        self.validator = DiscoveryValidator()
        self.repository = DiscoveryRepository()

    def run(self, url: str) -> DiscoveryResult:

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.STARTED,
            url,
        )

        self.scheduler.enqueue(url)
        job = self.scheduler.dequeue()

        if job is None:
            raise RuntimeError("No queued discovery job.")

        crawl = self.crawler.fetch(job.url)

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.PAGE_FETCHED,
            url,
        )

        document = self.extractor.extract(crawl.content)

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.EXTRACTED,
            url,
        )

        validation = self.validator.validate(document)

        if not validation.valid:
            raise ValueError("; ".join(validation.errors))

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.VALIDATED,
            url,
        )

        record = self.repository.save(url, document)

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.STORED,
            url,
        )

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.COMPLETED,
            url,
        )

        return DiscoveryResult(
            record=record,
            html=crawl.content,
        )
