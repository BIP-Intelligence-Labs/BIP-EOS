from __future__ import annotations

from ueos.doctor.engine import DoctorEngine
from ueos.doctor.reporters.console import ConsoleReporter

from ueos.doctor.scanners.repository import RepositoryScanner
from ueos.doctor.scanners.placeholders import PlaceholderScanner
from ueos.doctor.scanners.duplicates import DuplicateScanner
from ueos.doctor.scanners.imports import ImportScanner


def run() -> int:
    engine = DoctorEngine()

    engine.register(RepositoryScanner())
    engine.register(PlaceholderScanner())
    engine.register(DuplicateScanner())
    engine.register(ImportScanner())

    results = engine.run()

    ConsoleReporter().render(results)

    return 0 if engine.health_score() == 100.0 else 1


if __name__ == "__main__":
    raise SystemExit(run())
