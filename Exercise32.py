def convertStrToInt(stringNum: str) -> int:
    """
    Convert String Number to Integer

    :param stringNum: Number in string
    :type stringNum: str
    :raise TypeError: If stringNum is not a str
    :return: int
    :rtype: int
    """

    if stringNum == "0":
        return 0

    DIGITS_STR_TO_INT = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    integerNum = 0

    if stringNum[0] == "-":
        isNegative = True
        stringNum = stringNum[1:]
    else:
        isNegative = False

    # do something here
    for i in range(len(stringNum)):
        integerNum = (integerNum * 10) + DIGITS_STR_TO_INT[stringNum[i]]

    if isNegative:
        return -integerNum
    else:
        return integerNum

    ...


for i in range(-10000, 10000):

    assert convertStrToInt(str(i)) == i
