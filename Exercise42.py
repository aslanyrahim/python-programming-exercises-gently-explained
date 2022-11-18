def bubbleSort(numbers: list) -> list:
    """
    Return a sorted list.

    :param numbers: numbers in list
    :type numbers: list
    :raise TypeError: If numbers is not a list
    :return: list
    :rtype: list
    """

    if len(numbers) == 0:
        return []

    for i in range(len(numbers)):
        for j in range(i + 1, (len(numbers))):
            if numbers[j] < numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers
    ...


assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]

assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
