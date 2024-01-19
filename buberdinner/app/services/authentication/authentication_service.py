import uuid

from buberdinner.app.common.interfaces.authentication import ITokenGenerator
from buberdinner.app.services.authentication.authentication_result import (
    AuthenticationResult,
)


class AuthenticationService:
    def __init__(self, jwt_generator: ITokenGenerator) -> None:
        self._jwt_generator = jwt_generator

    def login(self, email: str, password: str) -> AuthenticationResult:
        return AuthenticationResult(
            first_name="first_name", last_name="last_name", email=email, token="token"
        )

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> AuthenticationResult:
        # TODO: Check if user already exists
        # TODO: Create new user (generate unique ID)
        token = self._jwt_generator.generate_token(uuid.uuid4(), first_name, last_name)
        return AuthenticationResult(
            first_name=first_name, last_name=last_name, email=email, token=token
        )
