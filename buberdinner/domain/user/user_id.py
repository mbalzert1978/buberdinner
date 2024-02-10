import dataclasses
import typing
import uuid


@dataclasses.dataclass
class UserId:
    value: uuid.UUID

    @classmethod
    def create(cls) -> typing.Self:
        return cls(uuid.uuid4())

    def __eq__(self, __value: object) -> bool:
        cls = type(self)
        if not isinstance(__value, cls):
            raise NotImplementedError()
        return self.value == __value.value

    def __str__(self) -> str:
        return str(self.value)
