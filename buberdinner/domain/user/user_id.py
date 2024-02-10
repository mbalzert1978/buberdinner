import dataclasses
import typing
import uuid

DETAIL = "Comparisation between %s and %s is not implemented."
UUID_FN = uuid.uuid4


@dataclasses.dataclass(frozen=True)
class UserId:
    value: uuid.UUID

    @classmethod
    def create(cls) -> typing.Self:
        return cls(UUID_FN())

    def __eq__(self, __value: object) -> bool:
        cls = type(self)
        if not isinstance(__value, cls):
            raise NotImplementedError(DETAIL % (cls, type(__value)))
        return self.value == __value.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return str(self.value)
