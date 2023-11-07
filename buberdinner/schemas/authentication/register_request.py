import pydantic

class RegisterRequest(pydantic.BaseModel):
    fistname: str
    lastname: str
    email: str
    password: str
