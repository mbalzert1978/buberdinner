import typing

import fastapi

from buberdinner.app.common.interfaces.authentication.token_generator import (
    ITokenGenerator,
)
from buberdinner.app.services.authentication.authentication import (
    IAuthentication,
)
from buberdinner.app.services.authentication.authentication_service import (
    AuthenticationService,
)
from buberdinner.infrastructure.authentication.jwt_token_generator import (
    JwtTokenGenerator,
)


def get_jwt() -> ITokenGenerator:
    return JwtTokenGenerator()


def authentication_service(
    jwt_gen: typing.Annotated[ITokenGenerator, fastapi.Depends(get_jwt)]
) -> IAuthentication:
    return AuthenticationService(jwt_generator=jwt_gen)
