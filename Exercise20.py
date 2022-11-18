# A leap year occurs on all years divisible by four (e.g., 2016, 2020, 2024, and so on).
# However, the exception to this rule is that years divisible by one hundred (e.g., 2100, 2200, 2300, and so on)
# aren’t leap years. And the exception to this exception is that years divisible by four hundred (e.g., 2000, 2400, and so on) are leap years


def isLeapYear(year):
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
    ...


assert isLeapYear(1999) == False

assert isLeapYear(2000) == True

assert isLeapYear(2001) == False

assert isLeapYear(2004) == True

assert isLeapYear(2100) == False

assert isLeapYear(2400) == True
