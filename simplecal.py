from dataclasses import dataclass
import datetime
import itertools
from typing import List, Union


def get_arithmetic_time(t: datetime.time) -> datetime.datetime:
    """Returns a datetime object for performing time arithmetic."""
    return datetime.datetime.combine(datetime.datetime.now(), t)


@dataclass
class Event:
    description: str
    start: datetime.time
    duration: datetime.timedelta

    @property
    def end(self) -> datetime.time:
        return (get_arithmetic_time(self.start) + self.duration).time()

    def contains_time(self, time: datetime.time) -> bool:
        t = get_arithmetic_time(time)
        event_start = get_arithmetic_time(self.start)
        event_end = get_arithmetic_time(self.end)
        if t >= event_start and t <= event_end:
            return True
        return False


class Calendar:
    events: List[Event] = []

    def add_event(self, event: Event) -> None:
        self.events += [event]
        self.events = sorted(self.events, key=lambda e: e.start)

    def delete_event(self, event: Event) -> None:
        self.events = [e for e in self.events if e != event]

    def get_events_at(self, time: datetime.datetime) -> List[Event]:
        events_at_that_time = []
        for event in self.events:
            if event.contains_time(time.time()):
                events_at_that_time += [event]
        return events_at_that_time

    def get_events_between(self, start_time, end_time) -> List[Event]:
        raise NotImplementedError

    def get_free_time_blocks(self) -> List:
        free_time_blocks = []
        a, b = itertools.tee(self.events)
        next(b, None)
        for i, j in zip(a, b):
            duration = get_arithmetic_time(j.start) - get_arithmetic_time(i.end)
            start = i.end
            free_time_blocks += [Event("free time", start, duration)]
        return free_time_blocks

    def calculate_minutes_of_free_time(self) -> int:
        free_time_blocks = self.get_free_time_blocks()
        durations = [x.duration.total_seconds() for x in free_time_blocks]
        return sum(durations) // 60
