import typing

import fastapi

from buberdinner.app.common.interfaces.authentication.jwt_gen_interface import (
    IJwtTokenGenerator,
)
from buberdinner.app.services.authentication.auth_interface import (
    AuthenticationInterface,
)
from buberdinner.app.services.authentication.authentication_service import (
    AuthenticationService,
)
from buberdinner.infrastructure.authentication.jwt_token_generator import (
    JwtTokenGenerator,
)


def get_jwt() -> IJwtTokenGenerator:
    return JwtTokenGenerator()


def authentication_service(
    jwt_gen: typing.Annotated[IJwtTokenGenerator, fastapi.Depends(get_jwt)]
) -> AuthenticationInterface:
    return AuthenticationService(jwt_gen=jwt_gen)
