#!/usr/bin/env python3
"""
bootstrap.py

BIP EOS Bootstrap

Primary bootstrap entry point for the entire platform.
"""

from __future__ import annotations

from bip_eos.application import Application


def main() -> int:
    app = Application()

    print("=" * 70)
    print("BIP EOS Bootstrap")
    print("=" * 70)

    try:
        status = app.start()
        print("[ OK ] Runtime started")
        print(status)
        return 0
    except Exception as exc:
        print(f"[FAIL] {exc}")
        return 1
    finally:
        try:
            app.stop()
        except Exception:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
