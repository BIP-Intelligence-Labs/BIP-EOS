from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


class Scanner(Protocol):
    name: str

    def scan(self) -> list[str]:
        ...


@dataclass
class DoctorResult:
    scanner: str
    findings: list[str] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return len(self.findings) == 0


class DoctorEngine:
    """UEOS Doctor orchestration engine."""

    def __init__(self) -> None:
        self._scanners: list[Scanner] = []

    def register(self, scanner: Scanner) -> None:
        self._scanners.append(scanner)

    def run(self) -> list[DoctorResult]:
        results: list[DoctorResult] = []
        for scanner in self._scanners:
            results.append(
                DoctorResult(scanner=scanner.name, findings=scanner.scan())
            )
        return results

    def health_score(self) -> float:
        if not self._scanners:
            return 100.0
        results = self.run()
        passed = sum(r.passed for r in results)
        return round((passed / len(results)) * 100.0, 2)
