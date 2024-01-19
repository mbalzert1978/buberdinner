import uuid

import pydantic


class AuthenticationResponse(pydantic.BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    token: str
