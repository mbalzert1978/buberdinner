import pydantic


class RegisterRequest(pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
