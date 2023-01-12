from datetime import datetime


def get_times(day, month, year, hour, minute):
    print(f"{year} {month} {day} {hour} {minute}")
    print(hex(int(
        (datetime(year, month, day, hour, minute).timestamp() - datetime(2019, 1, 1, 0, 0).timestamp()) * 60)))


def gen_dates(day, month, year):
    print(f"{year} {month} {day}")
    print(hex(int(
        (datetime(year, month, day, 0, 0).timestamp() - datetime(2019, 1, 1, 0, 0).timestamp()) / 60 / 60 / 24) + 1))
    print(hex(int(
        (datetime(year, month, day, 0, 0).timestamp() - datetime(2016, 1, 1, 0, 0).timestamp()) / 60 / 60 / 24) + 1))
    print(hex(int(
        (datetime(year, month, day, 0, 0).timestamp() - datetime(1992, 1, 1, 0, 0).timestamp()) / 60 / 60 / 24) + 1))
    print(hex(int(
        (datetime(year, month, day, 0, 0).timestamp() - datetime(2016, 1, 1, 0, 0).timestamp()) / 60 / 24)))
    print(hex(int(
        (datetime(year, month, day, 0, 0).timestamp() - datetime(1992, 1, 1, 0, 0).timestamp()) / 60 / 24)))


def parse_date(data):
    print(f"{data}")
    print(datetime.fromtimestamp(datetime(2019, 1, 1, 0, 0).timestamp() + (data - 1) * 24 * 60 * 60))
    print(datetime.fromtimestamp(datetime(2016, 1, 1, 0, 0).timestamp() + (data - 1) * 24 * 60 * 60))
    print(datetime.fromtimestamp(datetime(1992, 1, 1, 0, 0).timestamp() + (data - 1) * 24 * 60 * 60))


# gen_dates(9, 1, 2023)

parse_date(0xA5F0)

get_times(11, 1, 2023, 13, 44)
