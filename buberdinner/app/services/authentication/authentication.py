import typing

from result import Result

from buberdinner.app.error import Error
from buberdinner.app.services.authentication.authentication_result import (
    AuthenticationResult,
)


class IAuthentication(typing.Protocol):
    def login(self, email: str, password: str) -> Result[AuthenticationResult, Error]:
        """Log in to the system."""

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> Result[AuthenticationResult, Error]:
        """Register with the system."""
