import functools
import typing

import fastapi

from buberdinner.api.core.config import get_app_settings
from buberdinner.app.services import authentication
from buberdinner.domain.interfaces.authentication import ITokenGenerator
from buberdinner.domain.interfaces.persistence import IUserRepository
from buberdinner.domain.interfaces.services import IProvider
from buberdinner.infrastructure.authentication import JwtSettings, JwtTokenGenerator
from buberdinner.infrastructure.persistence import UserRepository
from buberdinner.infrastructure.services import DateTimeProvider


def get_dt_provider() -> IProvider:
    return DateTimeProvider()


@functools.lru_cache
def get_jwt_settings() -> JwtSettings:
    settings = get_app_settings()
    return JwtSettings(
        issuer=settings.issuer,
        expire_in_days=settings.jwt_token_expires_in_days,
        secret_key=settings.secret_key,
    )


def get_jwt(
    provider: typing.Annotated[IProvider, fastapi.Depends(get_dt_provider)],
    token_settings: typing.Annotated[JwtSettings, fastapi.Depends(get_jwt_settings)],
) -> ITokenGenerator:
    return JwtTokenGenerator(provider, token_settings)


def get_user_repo() -> IUserRepository:
    return UserRepository()


def authentication_service(
    jwt_generator: typing.Annotated[ITokenGenerator, fastapi.Depends(get_jwt)],
    user_repository: typing.Annotated[IUserRepository, fastapi.Depends(get_user_repo)],
) -> authentication.IAuthentication:
    return authentication.AuthenticationService(
        jwt_generator=jwt_generator, user_repository=user_repository
    )


Authentication = typing.Annotated[
    authentication.IAuthentication, fastapi.Depends(authentication_service)
]
