def average(numbers):
    if len(number) == 0:
        return None

    total = 0
    for n in numbers:
        total += n

    return total / len(numbers)
    ...


assert average([1, 2, 3]) == 2

assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2

assert average([12, 20, 37]) == 23

assert average([0, 0, 0, 0, 0]) == 0

import random

random.seed(42)

testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2
