import uuid

from buberdinner.app.common.interfaces.authentication import ITokenGenerator
from buberdinner.app.common.interfaces.persistence import IUserRepository
from buberdinner.app.services.authentication.authentication_result import (
    AuthenticationResult,
)
from buberdinner.domain.entities import User


class UserExistsError(Exception):
    """Exception raised when a user already exists"""


class AuthenticationService:
    def __init__(
        self, jwt_generator: ITokenGenerator, user_repository: IUserRepository
    ) -> None:
        self._jwt_generator = jwt_generator
        self._user_repository = user_repository

    def login(self, email: str, password: str) -> AuthenticationResult:
        if (user := self._user_repository.get_user_by_email(email)) is None:
            raise UserExistsError(f"User {email} does not exist.")
        if user.password != password:
            raise ValueError("Invalid password")
        return AuthenticationResult(
            user=user,
            token=self._jwt_generator.generate_token(user=user),
        )

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> AuthenticationResult:
        if self._user_repository.get_user_by_email(email) is not None:
            msg = f"User {email} allready exists."
            raise UserExistsError(msg)
        user = self._user_repository.add(
            User(
                id=uuid.uuid4(),
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
        )
        return AuthenticationResult(
            user=user,
            token=self._jwt_generator.generate_token(user=user),
        )
