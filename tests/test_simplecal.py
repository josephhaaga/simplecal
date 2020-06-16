from datetime import datetime, timedelta, time
import pytest

from context import simplecal


class TestEvent:
    @pytest.mark.parametrize("start_time,duration,time_to_test,expected", [
        (datetime.now(), timedelta(seconds=50), datetime.now(), True),
        (datetime.now() - timedelta(days=1), timedelta(seconds=50), datetime.now(), False),
    ])
    def test_contains_time(self, start_time: datetime.time, duration: timedelta, time_to_test: time, expected: bool):
        e = simplecal.Event("Sample event", start_time, duration)
        assert e.contains_time(time_to_test) == expected
