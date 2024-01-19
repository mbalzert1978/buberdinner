import typing

import fastapi

from buberdinner.app.common.interfaces.authentication import ITokenGenerator
from buberdinner.app.services.authentication import (
    AuthenticationService,
    IAuthentication,
)
from buberdinner.infrastructure.authentication import JwtTokenGenerator


def get_jwt() -> ITokenGenerator:
    return JwtTokenGenerator()


TokenGenerator = typing.Annotated[ITokenGenerator, fastapi.Depends(get_jwt)]


def authentication_service(jwt_gen: TokenGenerator) -> IAuthentication:
    return AuthenticationService(jwt_generator=jwt_gen)


Authentication = typing.Annotated[
    IAuthentication, fastapi.Depends(authentication_service)
]
