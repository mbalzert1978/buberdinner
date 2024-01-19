import datetime
import typing


class IProvider(typing.Protocol):
    @property
    def now(self) -> datetime.datetime:
        ...

    def add_days(self, days: int) -> datetime.datetime:
        ...

    def add_hours(self, hours: int) -> datetime.datetime:
        ...

    def add_minutes(self, minutes: int) -> datetime.datetime:
        ...

    def add_seconds(self, seconds: int) -> datetime.datetime:
        ...
