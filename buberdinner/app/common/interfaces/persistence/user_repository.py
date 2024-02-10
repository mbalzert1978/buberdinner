import typing

from result import Result

from buberdinner.app.error import Error
from buberdinner.domain.user.user import User


class IUserRepository(typing.Protocol):
    def add(self, user: User) -> Result[User, Error]:
        ...

    def get_user_by_email(self, email: str) -> Result[User, Error]:
        ...
