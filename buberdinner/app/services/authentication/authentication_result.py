import pydantic

from buberdinner.domain.entities import User


class AuthenticationResult(pydantic.BaseModel):
    user: User
    token: str
