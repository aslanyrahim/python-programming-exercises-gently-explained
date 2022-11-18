def mergeTwoLists(list1: list, list2: list) -> list:
    """
    Merge two list.

    :param list1: list1 in list
    :param list2: list2 in list
    :type list1: list
    :type list2: list
    :raise TypeError: If list1 or list2 is not a list
    :return: list
    :rtype: list
    """

    mergeList = []

    i1 = 0
    i2 = 0

    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            mergeList.append(list1[i1])
            i1 += 1
        else:
            mergeList.append(list2[i2])
            i2 += 1

    if i1 < len(list1):
        for j in range(i1, len(list1)):
            mergeList.append(list1[j])

    if i2 < len(list2):
        for j in range(i2, len(list2)):
            mergeList.append(list2[j])

    return mergeList
    ...


assert mergeTwoLists([1, 3, 6], [5, 7, 8, 9]) == [1, 3, 5, 6, 7, 8, 9]

assert mergeTwoLists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]

assert mergeTwoLists([2, 2, 2], [2, 2, 2]) == [2, 2, 2, 2, 2, 2]

assert mergeTwoLists([1, 2, 3], []) == [1, 2, 3]

assert mergeTwoLists([], [1, 2, 3]) == [1, 2, 3]
