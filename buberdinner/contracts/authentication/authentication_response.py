import dataclasses
from . import value_object


@dataclasses.dataclass(frozen=True)
class AuthenticateResponse:
    id: value_object.ValueObject
    fistname: str
    lastname: str
    email: str
    token: str
