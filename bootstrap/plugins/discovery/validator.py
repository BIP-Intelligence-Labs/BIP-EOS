"""
bootstrap/plugins/discovery/validator.py

Universal Discovery Engine Validator
"""

from __future__ import annotations

from dataclasses import dataclass

from .extractor import ExtractedDocument


@dataclass
class ValidationResult:
    valid: bool
    errors: list[str]


class DiscoveryValidator:
    """Validates extracted discovery documents."""

    def validate(self, document: ExtractedDocument) -> ValidationResult:
        errors: list[str] = []

        if not document.title:
            errors.append("Missing page title.")

        if len(document.links) == 0:
            errors.append("No hyperlinks discovered.")

        if len(document.description) > 1000:
            errors.append("Meta description exceeds 1000 characters.")

        return ValidationResult(
            valid=len(errors) == 0,
            errors=errors,
        )


if __name__ == "__main__":
    print("=" * 40)
    print(" Bootstrap Discovery Validator")
    print("=" * 40)
    print("Ready to validate extracted documents.")
