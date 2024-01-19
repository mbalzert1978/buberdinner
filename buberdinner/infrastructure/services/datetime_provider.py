import datetime


class DateTimeProvider:
    def __init__(self):
        self._now = datetime.datetime.now(tz=datetime.timezone.utc)

    @property
    def now(self) -> datetime.datetime:
        return self._now

    def add_days(self, days: int) -> datetime.datetime:
        return self._now + datetime.timedelta(days=days)

    def add_hours(self, hours: int) -> datetime.datetime:
        return self._now + datetime.timedelta(hours=hours)

    def add_minutes(self, minutes: int) -> datetime.datetime:
        return self._now + datetime.timedelta(minutes=minutes)

    def add_seconds(self, seconds: float) -> datetime.datetime:
        return self._now + datetime.timedelta(seconds=seconds)
