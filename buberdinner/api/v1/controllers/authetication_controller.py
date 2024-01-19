import fastapi

from buberdinner.app import dependencies
from buberdinner.schemas.authentication.login import LoginRequest
from buberdinner.schemas.authentication.register import RegisterRequest
from buberdinner.schemas.authentication.response import (
    AuthenticateResponse,
)

auth = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@auth.post("/register", response_model=AuthenticateResponse)
def register(
    request: RegisterRequest, auth_service: dependencies.Authentication
) -> AuthenticateResponse:
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
    request: LoginRequest, auth_service: dependencies.Authentication
) -> AuthenticateResponse:
    auth_result = auth_service.login(request.email, request.password)
    return AuthenticateResponse(
        id=auth_result.id,
        first_name=auth_result.first_name,
        last_name=auth_result.last_name,
        email=auth_result.email,
        token=auth_result.token,
    )
