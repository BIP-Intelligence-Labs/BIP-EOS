"""
repair_discovery_plugin.py

Removes the accidentally generated nested plugin folder.

Run from the Genesis repository root.
"""

from pathlib import Path
import shutil

ROOT = Path("bootstrap") / "plugins" / "discovery"
NESTED = ROOT / "bootstrap"

print("Bootstrap Discovery Repair")
print("==========================")

if NESTED.exists():
    print(f"Removing nested folder:\n{NESTED}")
    shutil.rmtree(NESTED)
    print("✓ Nested plugin removed.")
else:
    print("✓ No nested plugin found.")

expected = [
    "__init__.py",
    "plugin.py",
    "crawler.py",
    "extractor.py",
    "validator.py",
    "repository.py",
    "scheduler.py",
    "configuration.py",
    "models.py",
    "README.md",
    "tests",
]

print("\nDiscovery Plugin Structure")
for item in expected:
    status = "✓" if (ROOT / item).exists() else "✗"
    print(f"{status} {item}")

print("\nRepair complete.")
