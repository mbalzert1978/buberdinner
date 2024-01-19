import pydantic
import pydantic_settings


class JwtSettings(pydantic_settings.BaseSettings):
    issuer: str = "Buberdinner"
    expire_in_days: int = 1
    secret_key: pydantic.SecretStr
