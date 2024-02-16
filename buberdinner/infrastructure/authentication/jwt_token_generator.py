import jwt

from buberdinner.app.shared.error import Error, service
from buberdinner.app.shared.result import Err, Ok, Result
from buberdinner.domain.interfaces.services import IProvider
from buberdinner.domain.user import User
from buberdinner.infrastructure.authentication import JwtSettings
from buberdinner.infrastructure.authentication.error import JwtError

FAILED = "Failed to generate JWT token for user %s."


class JwtTokenGenerator:
    ALGORITHM = "HS256"

    def __init__(self, datetime_provider: IProvider, settings: JwtSettings) -> None:
        self._settings = settings
        self._datetime_provider = datetime_provider

    def generate_token(self, user: User) -> Result[str, Error]:
        match provider_result := self._datetime_provider.add_days(
            self._settings.expire_in_days
        ):
            case Ok(expire):
                try:
                    token = jwt.encode(
                        {
                            "issuer": self._settings.issuer,
                            "user_id": str(user.id),
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "exp": expire,
                        },
                        self._settings.secret_key.get_secret_value(),
                        algorithm=self.ALGORITHM,
                    )
                except jwt.PyJWTError as exc:
                    return Err(JwtError(*exc.args, detail=FAILED % user.id))
                else:
                    return Ok(token)
            case Err(_):
                return provider_result
            case _:
                return Err(service.UnreachableError())
