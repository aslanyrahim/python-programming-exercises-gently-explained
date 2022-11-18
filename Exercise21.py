import Exercise20 as leapyear


def isValidDate(year, month, day):
    if 1 <= month <= 12:
        if month in [9, 4, 6, 11]:
            return maxDay(day, 30)
        elif month == 2:
            if leapyear.isLeapYear(year) == True:
                return maxDay(day, 29)
            else:
                return maxDay(day, 28)
        else:
            return maxDay(day, 31)
    else:
        return False
    ...


def maxDay(day, maxDay):
    if 1 <= day <= maxDay:
        return True
    else:
        return False


assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay
