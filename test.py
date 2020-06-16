from datetime import datetime, timedelta

import simplecal

def main():
    cal = simplecal.Calendar()
    nine_am = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)
    an_hour = timedelta(seconds=60*60)
    event = simplecal.Event("My first event", nine_am, an_hour)
    cal.add_event(event)
    breakpoint()
    print(cal)

if __name__ == '__main__':
    main()
