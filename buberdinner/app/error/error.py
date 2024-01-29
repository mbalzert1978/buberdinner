import typing

from fastapi import status
from fastapi.exceptions import RequestValidationError
from httpproblem import Problem
from pydantic import ValidationError

INTERNAL_SERVER_ERROR = "Internal Server Error"
VALIDATION_ERROR = "Validation Error"

types: dict[int, str] = {
    status.HTTP_400_BAD_REQUEST: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.1",
    status.HTTP_401_UNAUTHORIZED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.2",
    status.HTTP_402_PAYMENT_REQUIRED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.3",
    status.HTTP_403_FORBIDDEN: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.4",
    status.HTTP_404_NOT_FOUND: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.5",
    status.HTTP_405_METHOD_NOT_ALLOWED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.6",
    status.HTTP_406_NOT_ACCEPTABLE: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.7",
    status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.8",
    status.HTTP_408_REQUEST_TIMEOUT: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.9",
    status.HTTP_409_CONFLICT: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.10",
    status.HTTP_410_GONE: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.11",
    status.HTTP_411_LENGTH_REQUIRED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.12",
    status.HTTP_412_PRECONDITION_FAILED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.13",
    status.HTTP_413_REQUEST_ENTITY_TOO_LARGE: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.14",
    status.HTTP_414_REQUEST_URI_TOO_LONG: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.15",
    status.HTTP_415_UNSUPPORTED_MEDIA_TYPE: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.16",
    status.HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.17",
    status.HTTP_417_EXPECTATION_FAILED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.18",
    status.HTTP_422_UNPROCESSABLE_ENTITY: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.20",
    status.HTTP_423_LOCKED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.21",
    status.HTTP_424_FAILED_DEPENDENCY: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.22",
    status.HTTP_426_UPGRADE_REQUIRED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.23",
    status.HTTP_428_PRECONDITION_REQUIRED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.24",
    status.HTTP_429_TOO_MANY_REQUESTS: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.25",
    status.HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.26",
    status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS: "https://www.rfc-editor.org/rfc/rfc2616#section-10.4.28",
    status.HTTP_500_INTERNAL_SERVER_ERROR: "https://www.rfc-editor.org/rfc/rfc2616#section-10.5.1",
    status.HTTP_501_NOT_IMPLEMENTED: "https://www.rfc-editor.org/rfc/rfc2616#section-10.5.2",
    status.HTTP_502_BAD_GATEWAY: "https://www.rfc-editor.org/rfc/rfc2616#section-10.5.3",
    status.HTTP_503_SERVICE_UNAVAILABLE: "https://www.rfc-editor.org/rfc/rfc2616#section-10.5.4",
    status.HTTP_504_GATEWAY_TIMEOUT: "https://www.rfc-editor.org/rfc/rfc2616#section-10.5.5",
}


def get_type(status_code: int, default: str = "about : blank") -> str:
    return types.get(status_code, default)


class Error(Exception):
    def __init__(
        self,
        *args,
        status_code: int = 500,
        detail: str = INTERNAL_SERVER_ERROR,
        errors: typing.Sequence[typing.Any] | None = None,
    ) -> None:
        self.status_code = status_code
        self.detail = detail
        self.type = get_type(status_code)
        self.errors = errors or [str(self)]
        super().__init__(*args)

    def map_error(self) -> dict:
        return Problem(
            status=self.status_code,
            type=self.type,
            detail=self.detail,
            errors=self.errors,
        ).to_dict()

    @classmethod
    def from_validation_error(
        self, exc: RequestValidationError | ValidationError
    ) -> "Error":
        return Error(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=VALIDATION_ERROR,
            errors=exc.errors(),
        )

    def __str__(self) -> str:
        return f"{self.status_code}: {self.detail}"
