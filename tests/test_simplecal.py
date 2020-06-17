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

@pytest.fixture(scope="module")
def epoch():
    return datetime(1970, 1, 1, 0, 0, 0)

@pytest.fixture(scope="module")
def event(epoch):
    one_minute = timedelta(seconds=60)
    return simplecal.Event("Sample Event", epoch, one_minute)

@pytest.fixture(scope="module")
def empty_calendar():
    return simplecal.Calendar()

@pytest.fixture(scope="function")
def nonempty_calendar(event):
    cal = simplecal.Calendar()
    cal.events = [event]
    return cal

class TestCalendar:
    def test_add_event(self, empty_calendar, event):
        empty_calendar.add_event(event)
        assert event in empty_calendar.events

    def test_delete_event(self, nonempty_calendar, event):
        nonempty_calendar.delete_event(event)
        assert nonempty_calendar.events == []

    def test_get_events_at(self, nonempty_calendar, epoch, event):
        events_at_epoch = nonempty_calendar.get_events_at(epoch + timedelta(seconds=2))
        assert event in events_at_epoch

    def test_free_time_blocks(self):
        assert True == False

    def test_calculate_minutes_of_free_time(self):
        assert True == False
