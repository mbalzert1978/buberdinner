from fastapi.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from buberdinner.app.error import ApiProblem

INSTANCE = "Buberdinner"


async def error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    err = ApiProblem(exc.status_code, exc.detail, INSTANCE)
    return JSONResponse(status_code=exc.status_code, content=err.to_dict())
