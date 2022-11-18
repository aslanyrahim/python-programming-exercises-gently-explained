def calculateSum(numbers):
    if len(numbers) == 0:
        return 0

    totalSum = 0
    for n in numbers:
        totalSum += n
    return totalSum
    ...


def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1

    totalProduct = 1
    for n in numbers:
        totalProduct *= n
    return totalProduct
    ...


assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840
