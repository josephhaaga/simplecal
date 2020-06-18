# simplecal

A simple library to create Calendars containing Events.

## Usage

### Basic Usage
```python
import simplecal
from datetime import datetime, time, timedelta

c = simplecal.Calendar(day_start=nine_am, day_end=five_pm) # TODO: Add day start/end params, and default to midnight

nine_am = time(9)
today = datetime.now()
today_at_nine = datetime.datetime.combine(today, nine_am)
fifteen_minutes = timedelta(seconds=15*60)

standup = simplecal.Event("Daily Standup", today_at_nine, fifteen_minutes)
c.add_event(standup)

c.get_free_time_blocks()

c.calculate_minutes_of_free_time() # TODO: return a timedelta
```

### Example: Productivity app
```python
import simplecal

work = simplecal.Calendar(day_start=nine_am, day_end=five_pm)
play = simplecal.Calendar(day_start=five_pm, day_end=ten_pm)

# TODO: add events to the relevant calendars, and demonstrate why free time calculations are useful for automated planning/scheduling

```


## TODO
- What other functions do we need before publishing this?
    - `get_events_between(self, start_time, end_time)` so people can render a calendar in a UI
- If a user adds an event that extends beyond `day_end`, should we raise an Error?
- Is a Calendar supposed to be for a single day?
    - Maybe it should be for a single day, and every parameter is a `time` (rather than a datetime)
