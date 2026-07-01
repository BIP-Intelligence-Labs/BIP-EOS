"""
========================================================================
ERS-001

Engineering Registry System

Registry Validator
========================================================================
"""

from __future__ import annotations

from collections import Counter

from .models import RegistryEntry


class RegistryValidator:
    """
    Constitutional Registry Validator.

    Responsible for validating the engineering registry before it is
    persisted or consumed by other constitutional systems.
    """

    # ==================================================================

    def validate(
        self,
        entries: list[RegistryEntry],
    ) -> None:
        """
        Validate the registry.

        Raises
        ------
        ValueError
            If the registry violates constitutional rules.
        """

        self._validate_duplicate_ids(entries)
        self._validate_duplicate_paths(entries)
        self._validate_required_fields(entries)

    # ==================================================================

    def _validate_duplicate_ids(
        self,
        entries: list[RegistryEntry],
    ) -> None:

        ids = [entry.id for entry in entries]

        duplicates = [
            value
            for value, count in Counter(ids).items()
            if count > 1
        ]

        if duplicates:

            raise ValueError(

                "Duplicate Registry IDs detected:\n"

                + "\n".join(duplicates)

            )

    # ==================================================================

    def _validate_duplicate_paths(
        self,
        entries: list[RegistryEntry],
    ) -> None:

        paths = [str(entry.path) for entry in entries]

        duplicates = [

            value

            for value, count in Counter(paths).items()

            if count > 1

        ]

        if duplicates:

            raise ValueError(

                "Duplicate Registry Paths detected:\n"

                + "\n".join(duplicates)

            )

    # ==================================================================

    def _validate_required_fields(
        self,
        entries: list[RegistryEntry],
    ) -> None:

        for entry in entries:

            if not entry.id:

                raise ValueError(

                    f"RegistryEntry missing ID: {entry}"

                )

            if not entry.artifact_type:

                raise ValueError(

                    f"{entry.id} missing artifact_type"

                )

            if not entry.name:

                raise ValueError(

                    f"{entry.id} missing name"

                )

            if not entry.path:

                raise ValueError(

                    f"{entry.id} missing path"

                )

            if not entry.checksum:

                raise ValueError(

                    f"{entry.id} missing checksum"

                )

    # ==================================================================

    def summary(
        self,
        entries: list[RegistryEntry],
    ) -> None:

        print("=" * 72)
        print("ERS-001 Registry Validation")
        print("=" * 72)
        print(f"Entries : {len(entries)}")
        print("Status  : PASS")
        print("=" * 72)
