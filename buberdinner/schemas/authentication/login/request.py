import pydantic


class LoginRequest(pydantic.BaseModel):
    email: str
    password: str
