"""
bootstrap_m005_console_reporter.py

Generates the UEOS Doctor Console Report Generator.
"""

from pathlib import Path

ROOT = Path("src/bip_eos/doctor/reporters")
ROOT.mkdir(parents=True, exist_ok=True)

TARGET = ROOT / "console.py"

TARGET.write_text("""from __future__ import annotations

from typing import Iterable


class ConsoleReporter:
    \"\"\"Renders UEOS Doctor results to the terminal.\"\"\"

    def render(self, results: Iterable) -> None:
        print("=" * 64)
        print("UEOS Doctor")
        print("Unified Engineering Operating System")
        print("=" * 64)

        passed = 0
        total = 0

        for result in results:
            total += 1

            status = "PASS" if result.passed else "FAIL"
            if result.passed:
                passed += 1

            print(f"[{status}] {result.scanner}")

            if not result.passed:
                for finding in result.findings:
                    print(f"    - {finding}")

        score = 100.0 if total == 0 else round((passed / total) * 100.0, 2)

        print("-" * 64)
        print(f"Health Score : {score}%")
        print(f"Checks       : {passed}/{total}")

        if score == 100.0:
            print("Status       : Genesis Certified")
        else:
            print("Status       : Attention Required")

        print("=" * 64)
""", encoding="utf-8")

print("=" * 64)
print("UEOS Console Reporter Generated")
print(TARGET)
print("=" * 64)
