"""
BIP EOS Repository Bootstrap

Creates:
    src/bip_eos/database/repository.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATABASE = ROOT / "src" / "bip_eos" / "database"
REPOSITORY = DATABASE / "repository.py"

CONTENT = """\"\"\"
BIP EOS Base Repository
\"\"\"

from bip_eos.database.manager import DatabaseManager


class BaseRepository:
    TABLE = ""

    def __init__(self):
        if not self.TABLE:
            raise ValueError(f"{self.__class__.__name__} must define TABLE.")
        self.db = DatabaseManager()

    def table(self):
        return self.db.table(self.TABLE)

    def get(self, record_id):
        return (
            self.table()
            .select("*")
            .eq("id", record_id)
            .single()
            .execute()
        )

    def list(self):
        return self.table().select("*").execute()

    def create(self, data: dict):
        return self.table().insert(data).execute()

    def update(self, record_id, data: dict):
        return (
            self.table()
            .update(data)
            .eq("id", record_id)
            .execute()
        )

    def delete(self, record_id):
        return (
            self.table()
            .delete()
            .eq("id", record_id)
            .execute()
        )
"""


def main():
    print("=" * 70)
    print("BIP EOS Repository Bootstrap")
    print("=" * 70)

    DATABASE.mkdir(parents=True, exist_ok=True)

    if REPOSITORY.exists():
        print(f"[SKIP] {REPOSITORY}")
    else:
        REPOSITORY.write_text(CONTENT.strip() + "\\n", encoding="utf-8")
        print(f"[FILE] {REPOSITORY}")

    print("-" * 70)
    print("BaseRepository ready.")


if __name__ == "__main__":
    main()
