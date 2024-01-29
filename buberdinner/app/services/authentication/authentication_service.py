import uuid

from result import Err, Ok, Result

from buberdinner.app.common.interfaces.authentication import ITokenGenerator
from buberdinner.app.common.interfaces.persistence import IUserRepository
from buberdinner.app.error import Error
from buberdinner.app.error.authentication import PasswordError, UserError
from buberdinner.app.services.authentication import AuthenticationResult
from buberdinner.domain.entities import User


class AuthenticationService:
    def __init__(
        self, jwt_generator: ITokenGenerator, user_repository: IUserRepository
    ) -> None:
        self._jwt_generator = jwt_generator
        self._user_repository = user_repository

    def login(self, email: str, password: str) -> Result[AuthenticationResult, Error]:
        user_by_email = self._user_repository.get_user_by_email(email)
        match user_by_email:
            case Ok(user):
                if user.password != password:
                    detail = "Invalid password"
                    return Err(PasswordError(status_code=401, detail=detail))
            case Err(_):
                return user_by_email

        token_result = self._jwt_generator.generate_token(user=user)
        match token_result:
            case Ok(token):
                return Ok(AuthenticationResult(user=user, token=token))
            case Err(_):
                return token_result

    def register(
        self, first_name: str, last_name: str, email: str, password: str
    ) -> Result[AuthenticationResult, Error]:
        if self._user_repository.get_user_by_email(email).is_ok():
            return Err(UserError(status_code=409, detail="Email allready registered."))
        user_to_db = User(
            id=uuid.uuid4(),
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )
        user_result = self._user_repository.add(user_to_db)
        match user_result:
            case Ok(user):
                token_result = self._jwt_generator.generate_token(user=user)
                match token_result:
                    case Ok(token):
                        return Ok(AuthenticationResult(user=user, token=token))
                    case Err(_):
                        return token_result
            case Err(_):
                detail = f"Error inserting user{user_to_db}."
                return Err(UserError(detail=detail))
