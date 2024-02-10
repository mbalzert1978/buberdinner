import typing

from result import Result

from buberdinner.app.error import Error
from buberdinner.domain.user import User


class ITokenGenerator(typing.Protocol):
    def generate_token(self, user: User) -> Result[str, Error]:
        ...
