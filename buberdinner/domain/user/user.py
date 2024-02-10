import dataclasses

from buberdinner.domain.user.user_id import UserId


@dataclasses.dataclass
class User:
    id: UserId
    first_name: str
    last_name: str
    email: str
    password: str
