import typing
import uuid


class ITokenGenerator(typing.Protocol):
    def generate_token(
        self, user_id: uuid.UUID, first_name: str, last_name: str
    ) -> str:
        ...
