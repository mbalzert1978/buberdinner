import typing

from buberdinner.app.shared.error import Error
from buberdinner.app.shared.result import Result
from buberdinner.domain.user import User


class ITokenGenerator(typing.Protocol):
    def generate_token(self, user: User) -> Result[str, Error]:
        ...
