from supabase import Client
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
