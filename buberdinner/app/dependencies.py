from buberdinner.app.services.authentication.authentication_service import (
    AuthenticationService,
)
from buberdinner.app.services.authentication.auth_interface import (
    AuthenticationInterface,
)


def authentication_service() -> AuthenticationInterface:
    return AuthenticationService()
