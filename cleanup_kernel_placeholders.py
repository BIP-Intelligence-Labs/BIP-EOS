"""
cleanup_kernel_placeholders.py

Removes the scaffold placeholder files and renames the real "(1)" files.

Run from the Genesis repository root.

Safe to run multiple times.
"""

from pathlib import Path

KERNEL = Path("bootstrap") / "kernel"

FILES = [
    "__init__",
    "kernel",
    "event_bus",
    "registry",
    "configuration",
    "workspace",
    "plugin_loader",
    "lifecycle",
    "cli",
]

print(f"Kernel directory: {KERNEL.resolve()}")

for name in FILES:
    placeholder = KERNEL / f"{name}.py"
    real = KERNEL / f"{name} (1).py"

    if real.exists():
        if placeholder.exists():
            placeholder.unlink()
            print(f"🗑  Deleted placeholder: {placeholder.name}")

        real.rename(placeholder)
        print(f"✅ Renamed: {real.name} -> {placeholder.name}")

    else:
        print(f"⏭  No replacement found for: {name}.py")

print("\nBootstrap Kernel cleanup complete.")
