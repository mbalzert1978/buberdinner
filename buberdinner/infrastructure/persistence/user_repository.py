import typing

from buberdinner.domain.entities import User


class UserRepository:
    _users: list[User] = []

    def add(self, user: User) -> User:
        self._users.append(user)
        return user

    def get_user_by_email(self, email: str) -> User | None:
        for user in self._users:
            if user.email != email:
                continue
            return user
        return None
