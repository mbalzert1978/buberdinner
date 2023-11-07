import uuid

import pydantic


class AuthenticateResponse(pydantic.BaseModel):
    id: uuid.UUID = pydantic.Field(default_factory=uuid.uuid4)
    first_name: str
    last_name: str
    email: str
    token: str
