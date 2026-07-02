from __future__ import annotations

from pathlib import Path
from datetime import datetime


class GenesisCertificationEngine:
    """Produces a Genesis certification report from Doctor results."""

    def __init__(self, report_dir: str | Path = "reports/doctor"):
        self.report_dir = Path(report_dir)
        self.report_dir.mkdir(parents=True, exist_ok=True)

    def _grade(self, score: float) -> str:
        if score >= 100.0:
            return "A+"
        if score >= 95:
            return "A"
        if score >= 90:
            return "B"
        if score >= 80:
            return "C"
        return "FAIL"

    def certify(self, results, score: float) -> Path:
        report = self.report_dir / "genesis_certification.md"

        passed = sum(1 for r in results if r.passed)
        total = len(results)
        grade = self._grade(score)

        lines = [
            "# UEOS Genesis Certification",
            "",
            f"Generated: {datetime.utcnow().isoformat()}Z",
            "",
            f"Health Score: {score:.2f}%",
            f"Grade: {grade}",
            f"Checks Passed: {passed}/{total}",
            "",
            "## Results",
            "",
        ]

        for r in results:
            status = "PASS" if r.passed else "FAIL"
            lines.append(f"- [{status}] {r.scanner}")
            if not r.passed:
                for f in r.findings:
                    lines.append(f"  - {f}")

        lines.extend([
            "",
            "## Certification",
            "",
        ])

        if score == 100.0:
            lines.append("🏆 Genesis Certified")
            lines.append("")
            lines.append("Repository complies with constitutional engineering requirements.")
        else:
            lines.append("⚠ Certification Pending")
            lines.append("")
            lines.append("Resolve outstanding findings and rerun `ueos doctor`.")

        report.write_text("\n".join(lines), encoding="utf-8")
        return report
