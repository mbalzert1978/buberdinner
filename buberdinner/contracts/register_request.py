import dataclasses


@dataclasses.dataclass(frozen=True)
class RegisterRequest:
    fistname: str
    lastname: str
    email: str
    password: str
