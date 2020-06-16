from dataclasses import dataclass


class Calendar:
    def schedule(self, event: 'Event'):
        pass

@dataclass
class Event:
    description: str

