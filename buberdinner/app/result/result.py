import typing

from buberdinner.app.error.common.error import Error
from buberdinner.app.result import Err, Ok

T = typing.TypeVar("T")
E = typing.TypeVar("E", bound=Error)

Result: typing.TypeAlias = Ok[T] | Err[E]