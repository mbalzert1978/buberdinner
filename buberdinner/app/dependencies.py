import typing

import fastapi

from buberdinner.app.common.interfaces.authentication import ITokenGenerator
from buberdinner.app.common.interfaces.services import IProvider
from buberdinner.app.services.authentication import (
    AuthenticationService,
    IAuthentication,
)
from buberdinner.infrastructure.authentication import JwtTokenGenerator
from buberdinner.infrastructure.services import DateTimeProvider


def get_dt_provider() -> IProvider:
    return DateTimeProvider()


Provider = typing.Annotated[IProvider, fastapi.Depends(get_dt_provider)]


def get_jwt(provider: Provider) -> ITokenGenerator:
    return JwtTokenGenerator(provider)


TokenGenerator = typing.Annotated[ITokenGenerator, fastapi.Depends(get_jwt)]


def authentication_service(jwt_gen: TokenGenerator) -> IAuthentication:
    return AuthenticationService(jwt_generator=jwt_gen)


Authentication = typing.Annotated[
    IAuthentication, fastapi.Depends(authentication_service)
]
