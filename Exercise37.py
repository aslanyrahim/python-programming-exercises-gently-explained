def makeChange(amount: int) -> dict:
    """
    Return the amount of quartes dimes nickels and pennies in dict

    :param amount: amount in int
    :type amount: int
    :raise TypeError: If amount is not a int
    :return: dict
    :rtype: dict
    """

    change = {}

    if amount == 0:
        return change

    if amount // 25 != 0:
        change["quarters"] = amount // 25
        amount = amount % 25
    if amount // 10 != 0:
        change["dimes"] = amount // 10
        amount = amount % 10
    if amount // 5 != 0:
        change["nickels"] = amount // 5
        amount = amount % 5
    if amount // 1 != 0:
        change["pennies"] = amount

    return change

    ...


assert makeChange(30) == {"quarters": 1, "nickels": 1}

assert makeChange(10) == {"dimes": 1}

assert makeChange(57) == {"quarters": 2, "nickels": 1, "pennies": 2}

assert makeChange(100) == {"quarters": 4}

assert makeChange(125) == {"quarters": 5}
