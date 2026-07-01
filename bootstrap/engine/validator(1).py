"""
bootstrap/engine/validator.py

UEOS BFS-002
Template Validator
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


class TemplateValidator:
    """
    Performs basic validation on rendered templates.
    """

    def validate_text(self, text: str) -> list[str]:
        issues: list[str] = []

        if not text.strip():
            issues.append("Rendered output is empty.")

        if "${" in text:
            issues.append("Unresolved template variables detected.")

        return issues

    def validate_required(
        self,
        context: dict,
        required: Iterable[str],
    ) -> list[str]:
        issues: list[str] = []

        for key in required:
            if key not in context or context[key] in (None, ""):
                issues.append(f"Missing required variable: {key}")

        return issues

    def validate_output_path(self, output: str | Path) -> list[str]:
        issues: list[str] = []

        path = Path(output)

        if not path.parent.exists():
            issues.append(
                f"Parent directory does not exist: {path.parent}"
            )

        return issues


if __name__ == "__main__":
    validator = TemplateValidator()

    sample = "# ${title}"

    print("=" * 72)
    print("UEOS Template Validator")
    print("=" * 72)

    print("Text Issues:")
    print(validator.validate_text(sample))

    print("\nContext Issues:")
    print(
        validator.validate_required(
            {"title": "UEOS"},
            ["title", "author"],
        )
    )
