
"""
bootstrap_m005_doctor_cli.py

Generates the UEOS Doctor CLI integration.
"""

from pathlib import Path

ROOT = Path("src/bip_eos/doctor")
ROOT.mkdir(parents=True, exist_ok=True)

CLI = ROOT / "cli.py"

CLI.write_text("""from __future__ import annotations

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
""", encoding="utf-8")

print("=" * 64)
print("UEOS Doctor CLI Generated")
print(CLI)
print("=" * 64)
print("NEXT")
print("  Wire into ueos CLI:")
print("    ueos doctor")
print("    ueos doctor repository")
print("    ueos doctor imports")
print("    ueos doctor duplicates")
print("    ueos doctor placeholders")
print("=" * 64)
