from result import Err, Ok, Result

from buberdinner.app.error import Error
from buberdinner.domain.entities import User
from buberdinner.infrastructure.error import NotFoundError


class UserRepository:
    _users: list[User] = []

    def add(self, user: User) -> Result[User, Error]:
        self._users.append(user)
        return Ok(user)

    def get_user_by_email(self, email: str) -> Result[User, Error]:
        for user in self._users:
            if user.email != email:
                continue
            return Ok(user)
        detail = "Email does not exist."
        return Err(NotFoundError(status_code=404, detail=detail))
