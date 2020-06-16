from dataclasses import dataclass
import datetime
import itertools
from typing import List, Union


@dataclass
class Event:
    description: str
    start: datetime.datetime
    duration: datetime.timedelta

    @property
    def end(self) -> datetime.datetime:
        return self.start + self.duration

    def contains_time(self, time: datetime.datetime) -> bool:
        if time >= self.start and time <= self.end:
            return True
        return False


NINE_AM = datetime.datetime.combine(datetime.datetime.today(), datetime.time(9, 0))
NINE_PM = datetime.datetime.combine(datetime.datetime.today(), datetime.time(21, 0))


class Calendar:
    events: List[Event] = []

    def add_event(self, event: Event) -> None:
        self.events += [event]

    def delete_event(self, event: Event) -> None:
        self.events = [e for e in self.events if e != event]

    def get_event_at(self, time: datetime.time) -> List[Event]:
        events_at_that_time = []
        dt = datetime.datetime.combine(datetime.datetime.today(), time)
        for event in self.get_events():
            if event.contains_time(time):
                events_at_that_time += [event]
        return events_at_that_time

    def get_events(self) -> List:
        return sorted(self.events, key=lambda e: e.start)

    def get_free_time_blocks(self) -> List:
        free_time_blocks = []
        events = self.get_events()
        a, b = itertools.tee(events)
        next(b, None)
        for i, j in zip(a, b):
            duration = j.start - i.end
            start = i.end
            free_time_blocks += [Event("free time", start, duration)]
        return free_time_blocks

    def calculate_minutes_of_free_time(self) -> int:
        free_time_blocks = self.get_free_time_blocks()
        durations = [x.duration.total_seconds() for x in free_time_blocks]
        return sum(durations) // 60
