# seconds generator:
def gen_secs():
    return (n for n in range(0, 60))


# minutes generator:
def gen_minutes():
    return (n for n in range(0, 60))


# hours generator:
def gen_hours():
    return (n for n in range(0, 24))


# time generator, returns every hh/mm/ss that exist and make sense:
def gen_time():
    for hours in gen_hours():
        for minutes in gen_minutes():
            for seconds in gen_secs():
                yield "%02d:%02d:%02d" % (hours, minutes, seconds)


# year generator, works from the given year (default = 2023):
def gen_years(start=2023):
    while True:
        yield start
        start += 1


# month generator:
def gen_months():
    return (n for n in range(1, 13))


# returns the number of days in month:
def gen_days(month, leap_year=True):
    days = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month == 2:
        if leap_year:
            days = 29
        else:
            days = 28
    else:
        days = 30

    return (day for day in range(1, days+1))


# Checks if a year is a leap year.
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# returns dd/mm/yy  hh/mm/ss
def gen_date():
    for years in gen_years():
        for months in gen_months():
            for days in gen_days(months, is_leap_year(years)):
                for gt in gen_time():
                    yield "%02d/%02d/%d %s" % (days, months, years, gt)


def main():
    # printing every after the 1000000 ge
    counter = 1000000
    for gd in gen_date():
        if counter % 1000000 == 0:
            print(gd)
        counter += 1


if __name__ == '__main__':
    main()
