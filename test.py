from datetime import datetime, timedelta

import simplecal

def main():
    cal = simplecal.Calendar()
    nine_am = datetime.now().replace(hour=9, minute=15, second=0, microsecond=0)
    an_hour = timedelta(seconds=60*60)
    event2 = simplecal.Event("My second event", nine_am + an_hour, an_hour)
    cal.add_event(event2)
    event = simplecal.Event("My first event", nine_am, an_hour)
    cal.add_event(event)
    return cal

if __name__ == '__main__':
    cal = main()
