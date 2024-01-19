import typing

from buberdinner.app.services.authentication.authentication_result import (
    AuthenticationResult,
)


class IAuthentication(typing.Protocol):
    def login(self, email: str, password: str) -> AuthenticationResult:
        """Log in to the system."""

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> AuthenticationResult:
        """Register with the system."""
