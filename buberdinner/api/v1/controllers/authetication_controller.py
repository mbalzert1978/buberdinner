import fastapi

from buberdinner.app import dependencies
from buberdinner.app.services.authentication.auth_interface import (
    AuthenticationInterface,
)
from buberdinner.schemas.authentication.authentication_response import (
    AuthenticateResponse,
)
from buberdinner.schemas.authentication.loginrequest import LoginRequest
from buberdinner.schemas.authentication.register_request import RegisterRequest

auth = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@auth.post("/register", response_model=AuthenticateResponse)
def register(
    request: RegisterRequest,
    _auth_service: AuthenticationInterface = fastapi.Depends(
        dependencies.authentication_service
    ),
):
    auth_result = _auth_service.register(
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
    _auth_service: AuthenticationInterface = fastapi.Depends(
        dependencies.authentication_service
    ),
):
    auth_result = _auth_service.login(request.email, request.password)
    return AuthenticateResponse(
        id=auth_result.id,
        first_name=auth_result.first_name,
        last_name=auth_result.last_name,
        email=auth_result.email,
        token=auth_result.token,
    )
