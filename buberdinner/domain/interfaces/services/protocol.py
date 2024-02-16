import datetime
import typing

from buberdinner.app.shared.error.error import Error
from buberdinner.app.shared.result import Result


class IProvider(typing.Protocol):
    @property
    def now(self) -> datetime.datetime:
        ...

    def add_days(self, days: int) -> Result[datetime.datetime, Error]:
        ...

    def add_hours(self, hours: int) -> Result[datetime.datetime, Error]:
        ...

    def add_minutes(self, minutes: int) -> Result[datetime.datetime, Error]:
        ...

    def add_seconds(self, seconds: int) -> Result[datetime.datetime, Error]:
        ...
