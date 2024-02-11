import pydantic


class RegisterRequest(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr = pydantic.Field(min_length=8)
