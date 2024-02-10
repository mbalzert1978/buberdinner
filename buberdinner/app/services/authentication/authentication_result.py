import pydantic

from buberdinner.domain.user import User


class AuthenticationResult(pydantic.BaseModel):
    user: User
    token: str
