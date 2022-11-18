def collatz(startingNumber: int) -> list:
    """
    List the numeric sequence.
    Begin with a positive, nonzero integer called n.
    If n is 1, the sequence terminates.
    If n is even, the next value of n is n / 2.
    If n is odd, the next value of n is 3n + 1.

    :param startingNumber: startingNumber in int
    :type startingNumber: int
    :raise TypeError: If startingNumber is not a int
    :return: list
    :rtype: list
    """

    if startingNumber < 1:
        return []

    sequence = [startingNumber]
    num = startingNumber

    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        sequence.append(num)

    return sequence

    ...


assert collatz(0) == []

assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]

assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

assert len(collatz(256)) == 9

assert len(collatz(257)) == 123

import random

random.seed(42)

for i in range(1000):

    startingNum = random.randint(1, 10000)

    seq = collatz(startingNum)

    assert seq[0] == startingNum  # Make sure it includes the starting number.

    assert seq[-1] == 1  # Make sure the last integer is 1.
