import typing

from buberdinner.app.services.authentication.authentication_result import (
    AuthenticationResult,
)
from buberdinner.app.shared.error import Error
from buberdinner.app.shared.result import Result


class IAuthentication(typing.Protocol):
    def login(self, email: str, password: str) -> Result[AuthenticationResult, Error]:
        """Log in to the system."""

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> Result[AuthenticationResult, Error]:
        """Register with the system."""
