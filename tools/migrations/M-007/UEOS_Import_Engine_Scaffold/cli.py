"""CLI entry point (scaffold)."""
import argparse
from .engine import ImportMigrationEngine
def main():
    p=argparse.ArgumentParser("ueos-import-engine")
    p.add_argument("--dry-run",action="store_true")
    p.add_argument("--backup",action="store_true")
    args=p.parse_args()
    ImportMigrationEngine().run(dry_run=args.dry_run, backup=args.backup)
if __name__=="__main__":
    main()
