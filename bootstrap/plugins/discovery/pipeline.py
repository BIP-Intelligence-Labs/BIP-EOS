"""
bootstrap/plugins/discovery/pipeline.py

Universal Discovery Engine Pipeline
"""

from __future__ import annotations

from .crawler import DiscoveryCrawler
from .extractor import DiscoveryExtractor
from .validator import DiscoveryValidator
from .repository import DiscoveryRepository
from .scheduler import DiscoveryScheduler
from .kernel_events import DiscoveryKernelEvents


class DiscoveryPipeline:
    """Coordinates the end-to-end discovery workflow."""

    def __init__(self) -> None:
        self.scheduler = DiscoveryScheduler()
        self.crawler = DiscoveryCrawler()
        self.extractor = DiscoveryExtractor()
        self.validator = DiscoveryValidator()
        self.repository = DiscoveryRepository()

    def run(self, url: str):
        DiscoveryKernelEvents.emit(DiscoveryKernelEvents.STARTED, url)

        self.scheduler.enqueue(url)
        job = self.scheduler.dequeue()
        if job is None:
            raise RuntimeError("No discovery job available.")

        result = self.crawler.fetch(job.url)
        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.PAGE_FETCHED, job.url
        )

        document = self.extractor.extract(result.content)
        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.EXTRACTED, job.url
        )

        validation = self.validator.validate(document)
        if not validation.valid:
            raise ValueError("; ".join(validation.errors))

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.VALIDATED, job.url
        )

        record = self.repository.save(job.url, document)
        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.STORED, job.url
        )

        DiscoveryKernelEvents.emit(
            DiscoveryKernelEvents.COMPLETED, job.url
        )

        return record
