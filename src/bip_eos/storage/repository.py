"""
BIP EOS Base Repository
"""

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
        )\n