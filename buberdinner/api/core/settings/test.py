import logging

from pydantic import PostgresDsn, SecretStr

from buberdinner.api.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI Buber Dinner API Test"

    secret_key: SecretStr = SecretStr("test_secret")

    database_url: PostgresDsn
    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG
