import dataclasses


@dataclasses.dataclass(frozen=True)
class LoginRequest:
    email: str
    password: str
