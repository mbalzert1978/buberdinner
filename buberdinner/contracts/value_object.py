from typing import Any
from uuid import uuid4


class ValueObject:
    pass


class UUID(ValueObject):
    __slots__ = ("value", )
    __match_args__ = ("value", )

    def __init__(self) -> None:
        self.value = uuid4().hex

    def __setattr__(self, __name: str, __value: Any) -> None:
        if hasattr(self, __name):
            raise AttributeError(f"'{__name}' is read-only")
        return super().__setattr__(__name, __value)

    def repr(self) -> str:
        return f"{type(self).__name__}({self.value!r})"

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.value})"
