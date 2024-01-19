import datetime
import uuid

import jwt

from buberdinner.api.core.config import get_app_settings


class JwtTokenGenerator:
    ALGORITHM = "HS256"

    def __init__(self) -> None:
        self._secret_key = get_app_settings().secret_key

    def generate_token(self, user_id: uuid.UUID, first_name: str, last_name) -> str:
        return jwt.encode(
            {
                "issuer": "Buberdinner",
                "user_id": str(user_id),
                "first_name": first_name,
                "last_name": last_name,
                "exp": _get_expirie_date(days=1),
            },
            self._secret_key.get_secret_value(),
            algorithm=self.ALGORITHM,
        )


def _get_expirie_date(days: int) -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=days)
