import typing

from buberdinner.domain.entities import User


class ITokenGenerator(typing.Protocol):
    def generate_token(self, user: User) -> str:
        ...
