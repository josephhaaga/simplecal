from dataclasses import dataclass
import datetime
import itertools


@dataclass
class Event:
    description: str
    start: datetime.datetime
    duration: datetime.timedelta

    @property
    def end(self):
        return self.start + self.duration

    def contains_time(self, time: datetime.time):
        t = datetime.datetime.combine(self.start, time)
        if t >= self.start and t <= self.end:
            return True


NINE_AM = datetime.datetime.combine(datetime.datetime.today(), datetime.time(9, 0))
NINE_PM = datetime.datetime.combine(datetime.datetime.today(), datetime.time(21, 0))

class Calendar:
    events = []

    def __init__(self):
        day_start = Event("day start", NINE_AM, datetime.timedelta(microseconds=0))
        day_end = Event("day end", NINE_PM, datetime.timedelta(microseconds=0))
        self.add_event(day_start)
        self.add_event(day_end)

    def add_event(self, event: Event):
        self.events += [event]

    def delete_event(self, event: Event):
        self.events = [e for e in self.events if e != event]

    def get_event_at(self, time: datetime.time):
        dt = datetime.datetime.combine(datetime.datetime.today(), time)
        for event in self.get_events():
            if event.contains_time(time):
                return event

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

    def calculate_minutes_of_free_time(self):
        free_time_blocks = self.get_free_time_blocks()
        durations = [x.duration.total_seconds() for x in free_time_blocks]
        return sum(durations) // 60

