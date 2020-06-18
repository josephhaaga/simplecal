from datetime import datetime, timedelta, time
import pytest

from context import simplecal


class TestEvent:
    @pytest.mark.parametrize(
        "start_time,duration,time_to_test,expected",
        [
            (datetime.now(), timedelta(seconds=50), datetime.now(), True),
            (
                datetime.now() - timedelta(days=1),
                timedelta(seconds=50),
                datetime.now(),
                False,
            ),
        ],
    )
    def test_contains_time(
        self,
        start_time: datetime,
        duration: timedelta,
        time_to_test: datetime,
        expected: bool,
    ):
        e = simplecal.Event("Sample event", start_time, duration)
        assert e.contains_time(time_to_test) == expected


@pytest.fixture(scope="module")
def epoch():
    return datetime.combine(datetime.now(), time(0))


@pytest.fixture(scope="module")
def event(epoch):
    one_minute = timedelta(seconds=60)
    return simplecal.Event("Sample Event", epoch, one_minute)


@pytest.fixture()
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

    def test_get_free_time_blocks_on_empty_calendar(self):
        ccal = simplecal.Calendar()
        # cant use empty_calendar fixture due to "deep copy" changes? https://github.com/pytest-dev/pytest-django/issues/601

        # TODO: WHY IS THIS FAILING!!!
        assert len(ccal.events) == 0

        free_time_blocks = ccal.get_free_time_blocks()
        assert len(free_time_blocks) == 1
        assert ccal.get_free_time_blocks() == [
            simplecal.Event("free time", ccal.day_start, ccal.day_length)
        ]

    # TODO: @pytest.mark.parametrize("calendar,mins_free_time", [(nonempty_calendar,
    def test_calculate_minutes_of_free_time(self, nonempty_calendar):
        cal = nonempty_calendar
        minutes_of_free_time = cal.calculate_minutes_of_free_time()
        seconds_spent_in_meetings = sum(
            [event.duration.total_seconds() for event in cal.events]
        )
        total_seconds_in_day = (cal.day_end - cal.day_start).total_seconds()
        assert (cal.calculate_minutes_of_free_time()) == (
            (total_seconds_in_day - seconds_spent_in_meetings) // 60
        )
