from buberdinner.app.services.authentication.authentication_result import (
    AuthenticationResult,
)
from buberdinner.app.shared.error import Error, authentication, service
from buberdinner.app.shared.result import Err, Ok, Result
from buberdinner.domain.interfaces.authentication import ITokenGenerator
from buberdinner.domain.interfaces.persistence import IUserRepository
from buberdinner.domain.user import User, UserId

INVALID_PASSWORD = "Invalid password."
INVALID_EMAIL = "Email allready registered."


class AuthenticationService:
    def __init__(
        self, jwt_generator: ITokenGenerator, user_repository: IUserRepository
    ) -> None:
        self._jwt_generator = jwt_generator
        self._user_repository = user_repository

    def login(self, email: str, password: str) -> Result[AuthenticationResult, Error]:
        match user_result := self._user_repository.get_user_by_email(email):
            case Ok(user) if user.password == password:
                return self._prepare_token(user)
            case Ok(user) if user.password != password:
                return Err(
                    authentication.PasswordError(
                        status_code=401,
                        detail=INVALID_PASSWORD,
                    )
                )
            case Err(_):
                return user_result
            case _:
                return Err(service.UnreachableError())

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> Result[AuthenticationResult, Error]:
        if self._user_repository.get_user_by_email(email).is_ok():
            return Err(authentication.UserError(status_code=409, detail=INVALID_EMAIL))

        match id_result := UserId.create():
            case Ok(_id):
                user_to_db = User(
                    id=_id,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password,
                )
            case Err(_):
                return id_result
            case _:
                return Err(service.UnreachableError())

        match write_result := self._user_repository.add(user_to_db):
            case Ok(user):
                return self._prepare_token(user)
            case Err(_):
                return write_result
            case _:
                return Err(service.UnreachableError())

    def _prepare_token(self, user: User) -> Result[AuthenticationResult, Error]:
        match token_result := self._jwt_generator.generate_token(user=user):
            case Ok(token):
                return Ok(AuthenticationResult(user=user, token=token))
            case Err(_):
                return token_result
            case _:
                return Err(service.UnreachableError())
