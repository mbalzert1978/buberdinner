from buberdinner.app.services.authentication.authentication_result import (
    AuthenticationResult,
)


class AuthenticationService:
    def login(self, email: str, password: str) -> AuthenticationResult:
        return AuthenticationResult(
            first_name="first_name", last_name="last_name", email=email, token="token"
        )

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> AuthenticationResult:
        return AuthenticationResult(
            first_name=first_name, last_name=last_name, email=email, token="token"
        )
