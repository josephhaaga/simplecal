import datetime

# I want to be able to do arithmetic on time objects without adding a date

# Assuming all the times are related to Today (the date) is an acceptable concession


class Time(datetime.time):
    def __add__(self, t: datetime.timedelta) -> "Time":
        result: datetime.datetime = datetime.datetime.combine(
            datetime.datetime.now(), self
        ) + t
        result_time = result.time()
        breakpoint()
        return Time(
            hour=result_time.hour,
            minute=result_time.minute,
            second=result_time.second,
            microsecond=result_time.microsecond,
        )

    def __sub__(self, t: "Time") -> datetime.timedelta:
        a = datetime.datetime.combine(datetime.datetime.now(), self)
        b = datetime.datetime.combine(datetime.datetime.now(), t)
        result = a - b
        return result


nine = Time(9)
ten = Time(10)
print(ten - nine)

print(nine + datetime.timedelta(seconds=30))
