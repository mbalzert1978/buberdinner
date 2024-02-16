import typing

from result import Err, Ok

from buberdinner.app.error.common.error import Error

T = typing.TypeVar("T")
E = typing.TypeVar("E", bound=Error)

Result: typing.TypeAlias = Ok[T] | Err[E]