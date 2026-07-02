from supabase import Client, create_client
from ueos.config.settings import settings


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
