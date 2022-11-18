def commaFormat(number: int) -> str:
    """
    Return a string of the number with comma formatting

    :param number: Number in string
    :type number: int
    :raise TypeError: If number is not a int
    :return: str
    :rtype: str
    """
    numberStr = str(number)

    if "." in numberStr:
        fractionalPart = numberStr[numberStr.index(".") :]
        numberStr = numberStr[: numberStr.index(".")]
    else:
        fractionalPart = ""

    triplet = ""
    commaNumber = ""

    for i in range(len(numberStr) - 1, -1, -1):
        triplet = numberStr[i] + triplet
        if len(triplet) == 3:
            commaNumber = triplet + "," + commaNumber
            triplet = ""

    if triplet != "":
        commaNumber = triplet + "," + commaNumber

    return commaNumber[:-1] + fractionalPart


assert commaFormat(1) == "1"

assert commaFormat(10) == "10"

assert commaFormat(100) == "100"

assert commaFormat(1000) == "1,000"

assert commaFormat(10000) == "10,000"

assert commaFormat(100000) == "100,000"

assert commaFormat(1000000) == "1,000,000"

assert commaFormat(1234567890) == "1,234,567,890"

assert commaFormat(1000.123456) == "1,000.123456"
