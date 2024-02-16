from typing import Any, Sequence

from buberdinner.app.shared.error import Error


class ServiceError(Error):
    """Exception raised when an service error occurs."""


class UnreachableError(ServiceError):
    """Exception raised when an unreachable code error occurs."""

    def __init__(
        self,
        *args,
        status_code: int = 500,
        detail: str = "Unreachable code error.",
        errors: Sequence[Any] | None = None,
    ) -> None:
        super().__init__(*args, status_code=status_code, detail=detail, errors=errors)
