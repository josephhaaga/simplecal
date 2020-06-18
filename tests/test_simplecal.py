from datetime import datetime, timedelta, time
import pytest

from context import simplecal


def test_get_arithmetic_time():
    nine_am = time(9, 0, 0)
    ten_am = time(10, 0, 0)
    # Make sure Exception is not raised from doing arithmetic
    assert (
        simplecal.get_arithmetic_time(ten_am) - simplecal.get_arithmetic_time(nine_am)
    ) == timedelta(seconds=3600)


class TestEvent:
    @pytest.mark.parametrize(
        "start_time,duration,time_to_test,expected",
        [
            (datetime.now().time(), timedelta(seconds=50), datetime.now().time(), True),
            (
                (datetime.now() - timedelta(hours=1)).time(),
                timedelta(seconds=50),
                datetime.now().time(),
                False,
            ),
        ],
    )
    def test_contains_time(
        self, start_time: time, duration: timedelta, time_to_test: time, expected: bool
    ):
        e = simplecal.Event("Sample event", start_time, duration)
        assert e.contains_time(time_to_test) == expected


@pytest.fixture(scope="module")
def midnight():
    return time(0, 0, 0)


@pytest.fixture(scope="module")
def event(midnight):
    one_minute = timedelta(seconds=60)
    return simplecal.Event("Sample Event", midnight, one_minute)


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

    def test_get_events_at(self, nonempty_calendar, midnight, event):
        midnight_oh_two = simplecal.get_arithmetic_time(midnight) + timedelta(seconds=2)
        events_at_midnight = nonempty_calendar.get_events_at(midnight_oh_two.time())
        assert event in events_at_midnight

    @pytest.mark.parametrize(
        "cal,expected", [(nonempty_calendar, 2), (empty_calendar, 1)]
    )
    def test_get_free_time_blocks(self, cal, expected):
        free_time = cal.get_free_time_blocks()
        assert len(free_time) == expected

    def test_calculate_minutes_of_free_time(self):
        assert True == False
