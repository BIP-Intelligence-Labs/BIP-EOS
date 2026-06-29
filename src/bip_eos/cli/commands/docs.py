#!/usr/bin/env python3
"""
docs.py

BIP EOS Documentation Command
"""

from __future__ import annotations

from bip_eos.application import Application


def run(argv=None):
    app = Application()
    return app.runtime.documentation.generate()


def main():
    print("=" * 70)
    print("BIP EOS Documentation")
    print("=" * 70)

    result = run()

    print(f"Generated : {result.get('generated')}")
    print(f"Directory : {result.get('docs_directory')}")

    created = result.get("created", [])
    if created:
        print("\nCreated Documents")
        for doc in created:
            print(f"  - {doc}")
    else:
        print("\nNo new documentation created.")

    print("=" * 70)


if __name__ == "__main__":
    main()
