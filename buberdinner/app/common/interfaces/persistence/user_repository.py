import typing

from buberdinner.domain.entities.user import User


class IUserRepository(typing.Protocol):
    def add(self, user: User) -> User:
        ...

    def get_user_by_email(self, email: str) -> User | None:
        ...
