import typing

from buberdinner.app.shared.error import Error
from buberdinner.app.shared.result import Result
from buberdinner.domain.user.user import User


class IUserRepository(typing.Protocol):
    def add(self, user: User) -> Result[User, Error]:
        ...

    def get_user_by_email(self, email: str) -> Result[User, Error]:
        ...
