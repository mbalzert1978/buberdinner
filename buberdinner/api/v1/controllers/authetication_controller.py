import fastapi
from result import Err, Ok

from buberdinner.app import dependencies
from buberdinner.schemas.authentication.login import LoginRequest
from buberdinner.schemas.authentication.register import RegisterRequest
from buberdinner.schemas.authentication.response import AuthenticationResponse

auth = fastapi.APIRouter(prefix="/auth", tags=["auth"])


@auth.post("/register", response_model=AuthenticationResponse)
def register(
    request: RegisterRequest, auth_service: dependencies.Authentication
) -> AuthenticationResponse:
    auth_result = auth_service.register(
        request.first_name,
        request.last_name,
        request.email,
        request.password,
    )
    match auth_result:
        case Ok(credentials):
            return AuthenticationResponse(
                id=credentials.user.id.value,
                first_name=credentials.user.first_name,
                last_name=credentials.user.last_name,
                email=credentials.user.email,
                token=credentials.token,
            )
        case Err(exc):
            raise exc


@auth.post("/login", response_model=AuthenticationResponse)
def login(
    request: LoginRequest, auth_service: dependencies.Authentication
) -> AuthenticationResponse:
    auth_result = auth_service.login(
        request.email,
        request.password,
    )
    match auth_result:
        case Ok(credentials):
            return AuthenticationResponse(
                id=credentials.user.id.value,
                first_name=credentials.user.first_name,
                last_name=credentials.user.last_name,
                email=credentials.user.email,
                token=credentials.token,
            )
        case Err(exc):
            raise exc
