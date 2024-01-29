import fastapi

from buberdinner.app import dependencies
from buberdinner.app.error.authentication import AuthenticationError
from buberdinner.schemas.authentication.login import LoginRequest
from buberdinner.schemas.authentication.register import RegisterRequest
from buberdinner.schemas.authentication.response import AuthenticationResponse

auth = fastapi.APIRouter(prefix="/auth", tags=["auth"])
INCORRECT = "Incorrect email or password"
EMAIL_TAKEN = "Email already taken."


@auth.post("/register", response_model=AuthenticationResponse)
def register(
    request: RegisterRequest, auth_service: dependencies.Authentication
) -> AuthenticationResponse:
    email_taken_error = fastapi.HTTPException(
        status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail=EMAIL_TAKEN
    )
    try:
        auth_result = auth_service.register(
            request.first_name, request.last_name, request.email, request.password
        )
    except AuthenticationError as exc:
        raise email_taken_error from exc
    else:
        return AuthenticationResponse(
            id=auth_result.user.id,
            first_name=auth_result.user.first_name,
            last_name=auth_result.user.last_name,
            email=auth_result.user.email,
            token=auth_result.token,
        )


@auth.post("/login", response_model=AuthenticationResponse)
def login(
    request: LoginRequest, auth_service: dependencies.Authentication
) -> AuthenticationResponse:
    wrong_login_error = fastapi.HTTPException(
        status_code=fastapi.status.HTTP_400_BAD_REQUEST, detail=INCORRECT
    )
    try:
        auth_result = auth_service.login(request.email, request.password)
    except AuthenticationError as exc:
        raise wrong_login_error from exc
    else:
        return AuthenticationResponse(
            id=auth_result.user.id,
            first_name=auth_result.user.first_name,
            last_name=auth_result.user.last_name,
            email=auth_result.user.email,
            token=auth_result.token,
        )
