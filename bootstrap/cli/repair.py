"""
bootstrap/cli/repair.py

Bootstrap Repair Manager
"""

from __future__ import annotations

from pathlib import Path
import shutil


class RepairManager:
    """Repairs common Bootstrap repository issues."""

    def __init__(self, root: Path | None = None):
        self.root = Path(root or Path.cwd()).resolve()

    def remove_nested_bootstrap(self) -> bool:
        nested = (
            self.root /
            "bootstrap" /
            "plugins" /
            "discovery" /
            "bootstrap"
        )

        if nested.exists():
            shutil.rmtree(nested)
            print(f"✓ Removed nested folder: {nested}")
            return True

        print("✓ No nested Bootstrap folder found.")
        return False

    def run(self) -> None:
        print("=" * 40)
        print(" Bootstrap Repair Manager")
        print("=" * 40)
        self.remove_nested_bootstrap()
        print("\nRepair complete.")


if __name__ == "__main__":
    RepairManager().run()
