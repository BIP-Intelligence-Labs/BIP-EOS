"""
BIP EOS Database Bootstrap

Creates:

src/
└── bip_eos/
    └── database/
        ├── __init__.py
        ├── client.py
        ├── manager.py
        └── session.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATABASE = ROOT / "src" / "bip_eos" / "database"

FILES = {
    "__init__.py": '"""BIP EOS Database Package"""\n',

    "client.py": '''from supabase import Client, create_client
from bip_eos.config.settings import settings


class DatabaseClient:
    _client: Client | None = None

    @classmethod
    def get_client(cls) -> Client:
        if cls._client is None:
            cls._client = create_client(
                settings.SUPABASE_URL,
                settings.SUPABASE_KEY,
            )
        return cls._client
''',

    "manager.py": '''from supabase import Client
from bip_eos.database.client import DatabaseClient


class DatabaseManager:

    def __init__(self):
        self.client: Client = DatabaseClient.get_client()

    def table(self, table_name: str):
        return self.client.table(table_name)

    def health(self) -> bool:
        try:
            self.client.table("builders").select("*").limit(1).execute()
            return True
        except Exception:
            return False
''',

    "session.py": '''from bip_eos.database.manager import DatabaseManager


class DatabaseSession:

    def __enter__(self):
        self.db = DatabaseManager()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
''',
}


def write_file(path: Path, content: str):
    if path.exists():
        print(f"[SKIP] {path}")
        return
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"[FILE] {path}")


def main():
    print("=" * 70)
    print("BIP EOS Database Bootstrap")
    print("=" * 70)

    DATABASE.mkdir(parents=True, exist_ok=True)

    for filename, content in FILES.items():
        write_file(DATABASE / filename, content)

    print("-" * 70)
    print("Database package ready.")


if __name__ == "__main__":
    main()
