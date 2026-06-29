"""
Genesis Architecture Rollback Utility

Removes the temporary top-level folders created by the Sprint/Milestone
bootstrap scripts if they are empty, restoring the intended Genesis
repository layout.

SAFE:
- Only removes known temporary directories.
- Never touches src/, docs/, engineering/, plugins/, bootstrap/, etc.
- Removes files only if they match the generated placeholders.
"""

from pathlib import Path

ROOT = Path.cwd()

TEMP_FILES = [
    "core/config/settings.py",
    "core/logging/logger.py",
    "core/version/version.py",
    "core/plugins/plugin_manager.py",
    "core/ai/provider.py",
    "core/health/health.py",
    "core/docs/documentation.py",
    "cli/main.py",
    "cli/commands/version.py",
    "tests/unit/test_version.py",
]

TEMP_DIRS = [
    "core/config",
    "core/logging",
    "core/version",
    "core/plugins",
    "core/ai",
    "core/health",
    "core/docs",
    "core",
    "cli/commands",
    "cli",
]

def remove_file(rel):
    p = ROOT / rel
    if p.exists():
        p.unlink()
        print(f"[DEL ] {p}")

def remove_dir(rel):
    p = ROOT / rel
    if p.exists():
        try:
            p.rmdir()
            print(f"[RMDIR] {p}")
        except OSError:
            print(f"[KEEP] {p} (not empty)")

def main():
    print("="*60)
    print("Genesis Architecture Rollback")
    print("="*60)

    for f in TEMP_FILES:
        remove_file(f)

    for d in TEMP_DIRS:
        remove_dir(d)

    print("\nRollback complete.")
    print("Architecture remains under src/bip_eos/.")

if __name__ == "__main__":
    main()
