import dataclasses
import uuid


@dataclasses.dataclass
class User:
    id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    password: str
