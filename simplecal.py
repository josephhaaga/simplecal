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


midnight = datetime.datetime.combine(datetime.datetime.now(), datetime.time(0, 0, 0))
twenty_three_fifty_nine = datetime.datetime.combine(
    datetime.datetime.now(), datetime.time(23, 59, 59)
)


class Calendar:
    events: List[Event] = []

    def __init__(
        self,
        events: List[Event] = [],
        day_start: datetime.datetime = midnight,
        day_end: datetime.datetime = twenty_three_fifty_nine,
    ):
        self.events = events
        self.day_start = day_start
        self.day_end = day_end
        self.day_length = self.day_end - self.day_start

    def add_event(self, event: Event) -> None:
        self.events += [event]
        self.events = sorted(self.events, key=lambda e: e.start)

    def delete_event(self, event: Event) -> None:
        self.events = [e for e in self.events if e != event]

    def get_events_at(self, time: datetime.datetime) -> List[Event]:
        events_at_that_time = []
        for event in self.events:
            if event.contains_time(time):
                events_at_that_time += [event]
        return events_at_that_time

    def get_events_between(self, start_time, end_time) -> List[Event]:
        raise NotImplementedError

    def get_free_time_blocks(self) -> List[Event]:
        if len(self.events) == 0:
            return [Event("free time", self.day_start, self.day_length)]
        elif len(self.events) == 1:
            only_event_for_today = self.events[0]
            amount_of_free_time_before_only_event = (
                only_event_for_today.start - self.day_start
            )
            amount_of_free_time_after_only_event = (
                self.day_end - only_event_for_today.end
            )
            return [
                Event(
                    "free time", self.day_start, amount_of_free_time_before_only_event
                ),
                Event(
                    "free time",
                    only_event_for_today.end,
                    amount_of_free_time_after_only_event,
                ),
            ]
            pass
        free_time_blocks = []
        a, b = itertools.tee(self.events)
        next(b, None)
        for i, j in zip(a, b):
            duration = j.start - i.end
            start = i.end
            free_time_blocks += [Event("free time", start, duration)]
        return free_time_blocks

    def calculate_minutes_of_free_time(self) -> float:
        free_time_blocks = self.get_free_time_blocks()
        durations = [x.duration.total_seconds() for x in free_time_blocks]
        total = sum(durations) // 60
        return total
