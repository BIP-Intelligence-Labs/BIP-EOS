"""
compiler_service.py

UEOS
M-006.3 - Runtime Services

Place in:
    src/bip_eos/services/compiler/service.py
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from time import perf_counter


@dataclass(slots=True)
class CompilerResult:
    success: bool
    files_processed: int
    elapsed_seconds: float


class CompilerService:
    """
    Production service behind the `UEOS> compiler` command.
    """

    def __init__(self, repository_root: Path | None = None):
        self.repository_root = repository_root or Path.cwd()

    def compile(self) -> CompilerResult:
        start = perf_counter()

        # Initial implementation:
        # Count Python source files as compilation inputs.
        files_processed = sum(
            1 for _ in self.repository_root.rglob("*.py")
        )

        elapsed = perf_counter() - start

        result = CompilerResult(
            success=True,
            files_processed=files_processed,
            elapsed_seconds=elapsed,
        )

        self._display(result)
        return result

    @staticmethod
    def _display(result: CompilerResult) -> None:
        print("=" * 60)
        print("UEOS Compiler")
        print("=" * 60)
        print(f"Status          : {'SUCCESS' if result.success else 'FAILED'}")
        print(f"Python Files    : {result.files_processed}")
        print(f"Elapsed Seconds : {result.elapsed_seconds:.4f}")


def main() -> int:
    result = CompilerService().compile()
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
