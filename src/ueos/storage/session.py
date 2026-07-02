from ueos.database.manager import DatabaseManager


class DatabaseSession:

    def __enter__(self):
        self.db = DatabaseManager()
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
