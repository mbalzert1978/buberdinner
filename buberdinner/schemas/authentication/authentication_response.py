import uuid

import pydantic


class AuthenticateResponse(pydantic.BaseModel):
    id: uuid.UUID
    fistname: str
    lastname: str
    email: str
    token: str
