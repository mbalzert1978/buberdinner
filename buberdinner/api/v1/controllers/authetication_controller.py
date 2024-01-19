import typing

import fastapi

from buberdinner.app import dependencies
from buberdinner.app.services.authentication.authentication import (
    IAuthentication,
)
from buberdinner.schemas.authentication.authentication_response import (
    AuthenticateResponse,
)
from buberdinner.schemas.authentication.login_request import LoginRequest
from buberdinner.schemas.authentication.register_request import RegisterRequest

auth = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@auth.post("/register", response_model=AuthenticateResponse)
def register(
    request: RegisterRequest,
    auth_service: typing.Annotated[
        IAuthentication, fastapi.Depends(dependencies.authentication_service)
    ],
):
    auth_result = auth_service.register(
        request.first_name, request.last_name, request.email, request.password
    )
    return AuthenticateResponse(
        id=auth_result.id,
        first_name=auth_result.first_name,
        last_name=auth_result.last_name,
        email=auth_result.email,
        token=auth_result.token,
    )


@auth.post("/login", response_model=AuthenticateResponse)
def login(
    request: LoginRequest,
    auth_service: typing.Annotated[
        IAuthentication, fastapi.Depends(dependencies.authentication_service)
    ],
):
    auth_result = auth_service.login(request.email, request.password)
    return AuthenticateResponse(
        id=auth_result.id,
        first_name=auth_result.first_name,
        last_name=auth_result.last_name,
        email=auth_result.email,
        token=auth_result.token,
    )
