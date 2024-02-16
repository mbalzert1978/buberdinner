import datetime

from buberdinner.app.shared.error.error import Error
from buberdinner.app.shared.result import Err, Ok, Result
from buberdinner.infrastructure.services.error import DateTimeError


class DateTimeProvider:
    def __init__(self):
        self._now = datetime.datetime.now(tz=datetime.timezone.utc)

    @property
    def now(self) -> datetime.datetime:
        return self._now

    def add_days(self, days: int) -> Result[datetime.datetime, Error]:
        try:
            return Ok(self._now + datetime.timedelta(days=days))
        except Exception as exc:
            return Err(DateTimeError(*exc.args, detail=str(exc)))

    def add_hours(self, hours: int) -> Result[datetime.datetime, Error]:
        try:
            return Ok(self._now + datetime.timedelta(hours=hours))
        except Exception as exc:
            return Err(DateTimeError(*exc.args, detail=str(exc)))

    def add_minutes(self, minutes: int) -> Result[datetime.datetime, Error]:
        try:
            return Ok(self._now + datetime.timedelta(minutes=minutes))
        except Exception as exc:
            return Err(DateTimeError(*exc.args, detail=str(exc)))

    def add_seconds(self, seconds: int) -> Result[datetime.datetime, Error]:
        try:
            return Ok(self._now + datetime.timedelta(seconds=seconds))
        except Exception as exc:
            return Err(DateTimeError(*exc.args, detail=str(exc)))
