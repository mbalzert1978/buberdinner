from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from buberdinner.app.error import Error


async def http422_error_handler(
    _: Request,
    exc: RequestValidationError | ValidationError,
) -> JSONResponse:
    err = Error.from_validation_error(exc)
    return JSONResponse(status_code=err.status_code, content=err.map_error())
