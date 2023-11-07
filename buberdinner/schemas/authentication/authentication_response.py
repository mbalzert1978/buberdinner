import uuid

import pydantic


class AuthenticateResponse(pydantic.BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    token: str
