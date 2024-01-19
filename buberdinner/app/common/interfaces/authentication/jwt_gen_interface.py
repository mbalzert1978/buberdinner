import typing
import uuid


class IJwtTokenGenerator(typing.Protocol):
    def generate_token(
        self, user_id: uuid.UUID, first_name: str, last_name: str
    ) -> str:
        ...
