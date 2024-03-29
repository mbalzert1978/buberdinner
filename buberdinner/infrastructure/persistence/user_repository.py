from buberdinner.app.shared.error import Error
from buberdinner.app.shared.result import Err, Ok, Result
from buberdinner.domain.user import User
from buberdinner.infrastructure.persistence.error import NotFoundError, WriteError

NOT_FOUND = "Email does not exist."
STATUS_CODE = 404


class UserRepository:
    _users: list[User] = []

    def add(self, user: User) -> Result[User, Error]:
        try:
            self._users.append(user)
        except Exception as exc:
            return Err(WriteError(*exc.args, detail=str(exc)))
        else:
            return Ok(user)

    def get_user_by_email(self, email: str) -> Result[User, Error]:
        for user in self._users:
            if email != user.email:
                continue
            return Ok(user)
        return Err(NotFoundError(status_code=STATUS_CODE, detail=NOT_FOUND))
