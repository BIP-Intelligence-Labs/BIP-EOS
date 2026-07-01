"""
BIP EOS Production Runtime Test

Verifies that the core platform imports and initializes correctly.

Usage:
    python bootstrap/test_runtime.py
"""

from importlib import import_module

MODULES = [
    # Platform
    "bip_eos",
    "bip_eos.config",
    "bip_eos.shared",
    "bip_eos.database",
    "bip_eos.integrations",

    # Core
    "bip_eos.core",
    "bip_eos.core.repository",
    "bip_eos.core.registry",
    "bip_eos.core.plugins",
    "bip_eos.core.version",
    "bip_eos.core.logging",

    # CLI
    "bip_eos.cli",

    # Builder Domains
    "bip_eos.home_builders.lead",
    "bip_eos.home_builders.home_builder",
    "bip_eos.home_builders.home_communities",
    "bip_eos.home_builders.inventory_homes",
    "bip_eos.home_builders.questionnaire",
    "bip_eos.home_builders.recommendations",
    "bip_eos.home_builders.buyer_reports",
    "bip_eos.home_builders.appointment",
]

print("=" * 70)
print("BIP EOS Runtime Verification")
print("=" * 70)

passed = 0
failed = 0

for module in MODULES:
    try:
        import_module(module)
        print(f"[ OK ] {module}")
        passed += 1
    except Exception as ex:
        print(f"[FAIL] {module}")
        print(f"       {type(ex).__name__}: {ex}")
        failed += 1

print("-" * 70)
print(f"Passed : {passed}")
print(f"Failed : {failed}")

if failed == 0:
    print("\n✓ Runtime verification PASSED")
else:
    print("\n✗ Runtime verification FAILED")
