import jwt

from buberdinner.app.common.interfaces.services import IProvider
from buberdinner.domain.entities import User
from buberdinner.infrastructure.authentication import JwtSettings


class JwtTokenGenerator:
    ALGORITHM = "HS256"

    def __init__(self, datetime_provider: IProvider, settings: JwtSettings) -> None:
        self._settings = settings
        self._datetime_provider = datetime_provider

    def generate_token(self, user: User) -> str:
        return jwt.encode(
            {
                "issuer": self._settings.issuer,
                "user_id": str(user.id),
                "first_name": user.first_name,
                "last_name": user.last_name,
                "exp": self._datetime_provider.add_days(self._settings.expire_in_days),
            },
            self._settings.secret_key.get_secret_value(),
            algorithm=self.ALGORITHM,
        )
