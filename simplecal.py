from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Event:
    description: str
    start: datetime
    duration: timedelta

    @property
    def end(self):
        return self.start + self.duration

class Calendar:
    events = []

    def add_event(self, event: Event):
        self.events += [event]

    def delete_event(self, event: Event):
        self.events = [e for e in self.events if e != event]

