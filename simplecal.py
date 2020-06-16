from dataclasses import dataclass
from datetime import datetime, timedelta
import itertools


@dataclass
class Event:
    description: str
    start: datetime
    duration: timedelta

    @property
    def end(self):
        return self.start + self.duration


NINE_AM = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
NINE_PM = NINE_AM + timedelta(seconds=60*60*12)

class Calendar:
    events = []

    def __init__(self):
        self.add_event(Event("day start", NINE_AM, timedelta(microseconds=1)))
        self.add_event(Event("day end", NINE_PM, timedelta(microseconds=1)))

    def add_event(self, event: Event):
        self.events += [event]

    def delete_event(self, event: Event):
        self.events = [e for e in self.events if e != event]

    def get_events(self):
        return sorted(self.events, key = lambda e: e.start)

    def get_free_time_blocks(self):
        free_time_blocks = []
        a, b = itertools.tee(self.get_events())
        next(b, None)
        for i, j in zip(a, b):
            duration = j.start - i.end
            start = i.end
            free_time_blocks += [Event("free time", start, duration)]
        return free_time_blocks



