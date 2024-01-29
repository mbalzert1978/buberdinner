from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from buberdinner.app.error import ApiProblem


async def http422_error_handler(
    _: Request,
    exc: RequestValidationError | ValidationError,
) -> JSONResponse:
    err = parse_error(exc)
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content=tuple(ap_err.to_dict() for ap_err in err),
    )


def parse_error(
    exc: RequestValidationError | ValidationError,
) -> tuple[ApiProblem, ...]:
    return tuple(
        ApiProblem(HTTP_422_UNPROCESSABLE_ENTITY, **err) for err in exc.errors()
    )
