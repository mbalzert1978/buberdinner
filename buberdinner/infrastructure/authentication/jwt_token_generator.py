import uuid

import jwt

from buberdinner.api.core.config import get_app_settings
from buberdinner.app.common.interfaces.services import IProvider


class JwtTokenGenerator:
    ALGORITHM = "HS256"

    def __init__(self, datetime_provider: IProvider) -> None:
        self._secret_key = get_app_settings().secret_key
        self._datetime_provider = datetime_provider

    def generate_token(self, user_id: uuid.UUID, first_name: str, last_name) -> str:
        return jwt.encode(
            {
                "issuer": "Buberdinner",
                "user_id": str(user_id),
                "first_name": first_name,
                "last_name": last_name,
                "exp": self._datetime_provider.add_days(1),
            },
            self._secret_key.get_secret_value(),
            algorithm=self.ALGORITHM,
        )
