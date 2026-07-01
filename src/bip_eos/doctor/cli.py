from __future__ import annotations

from bip_eos.doctor.engine import DoctorEngine
from bip_eos.doctor.reporters.console import ConsoleReporter

from bip_eos.doctor.scanners.repository import RepositoryScanner
from bip_eos.doctor.scanners.placeholders import PlaceholderScanner
from bip_eos.doctor.scanners.duplicates import DuplicateScanner
from bip_eos.doctor.scanners.imports import ImportScanner


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
