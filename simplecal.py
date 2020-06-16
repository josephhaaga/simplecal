from dataclasses import dataclass
import datetime

EIGHT_HOURS_IN_SECONDS = 60 * 60 * 8

@dataclass
class TimeBlock:
    start: datetime.datetime
    duration: datetime.timedelta

    def end(self):
        return self.start + self.duration

class Calendar:
    timeblocks = [TimeBlock(start=datetime.datetime.now(), duration=datetime.timedelta(seconds=EIGHT_HOURS_IN_SECONDS))]

    def get_timeblock_during(self, time: datetime.datetime):
        for block in self.timeblocks:
            if time >= block.start and time < block.end:
                return block

    def add_event(self, description, start_time: datetime.datetime, duration: datetime.timedelta):
        existing_timeblock = self.timeblocks.index(self.get_timeblock_during(start_time))
        # TODO divide the existing TimeBlock into three TimeBlocks
            # What if the event intersects multiple TimeBlocks?
        before = None
        event_block = None
        after = None

