import pydantic


class LoginRequest(pydantic.BaseModel):
    email: pydantic.EmailStr
    password: pydantic.SecretStr
