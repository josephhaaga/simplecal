import simplecal


def main():
    cal = simplecal.Calendar()
    event = simplecal.Event("My first event")
    cal.schedule(event)
    breakpoint()
    print(cal)

if __name__ == '__main__':
    main()
