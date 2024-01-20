import functools
import typing

import fastapi

from buberdinner.api.core.config import get_app_settings
from buberdinner.app.common.interfaces.authentication import ITokenGenerator
from buberdinner.app.common.interfaces.persistence.user_repository import (
    IUserRepository,
)
from buberdinner.app.common.interfaces.services import IProvider
from buberdinner.app.services.authentication import (
    AuthenticationService,
    IAuthentication,
)
from buberdinner.infrastructure.authentication import JwtTokenGenerator
from buberdinner.infrastructure.authentication.jwt_settings import JwtSettings
from buberdinner.infrastructure.persistence import UserRepository
from buberdinner.infrastructure.services import DateTimeProvider


def get_dt_provider() -> IProvider:
    return DateTimeProvider()


Provider = typing.Annotated[IProvider, fastapi.Depends(get_dt_provider)]


@functools.lru_cache
def get_jwt_settings() -> JwtSettings:
    settings = get_app_settings()
    return JwtSettings(
        issuer=settings.issuer,
        expire_in_days=settings.jwt_token_expires_in_days,
        secret_key=settings.secret_key,
    )


TokenSettings = typing.Annotated[JwtSettings, fastapi.Depends(get_jwt_settings)]


def get_jwt(provider: Provider, token_settings: TokenSettings) -> ITokenGenerator:
    return JwtTokenGenerator(provider, token_settings)


TokenGenerator = typing.Annotated[ITokenGenerator, fastapi.Depends(get_jwt)]


def get_user_repo() -> IUserRepository:
    return UserRepository()


UserRepo = typing.Annotated[IUserRepository, fastapi.Depends(get_user_repo)]


def authentication_service(
    jwt_generator: TokenGenerator, user_repository: UserRepo
) -> IAuthentication:
    return AuthenticationService(
        jwt_generator=jwt_generator, user_repository=user_repository
    )


Authentication = typing.Annotated[
    IAuthentication, fastapi.Depends(authentication_service)
]
