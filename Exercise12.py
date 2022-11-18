# Version 1 - while loop
# def getSmallest(number):
#     if len(number) == 0:
#         return None

#     i = 0
#     smallest = number[0]
#     while i < len(number):
#         if number[i] < smallest:
#             smallest = number[i]
#         i += 1
#     return smallest

# def getBiggest(number):
#     if len(number) == 0:
#         return None

#     i = 0
#     biggest = number[0]
#     while i < len(number):
#         if number[i] > biggest:
#             biggest = number[i]
#         i += 1
#     return biggest

# Version 2 - for loop
def getSmallest(number):
    if len(number) == 0:
        return None

    smallest = number[0]
    for n in number:
        if n < smallest:
            smallest = n
    return smallest


def getBiggest(number):
    if len(number) == 0:
        return None

    biggest = number[0]
    for n in number:
        if n > biggest:
            biggest = n
    return biggest


assert getSmallest([1, 2, 3]) == 1

assert getSmallest([3, 2, 1]) == 1

assert getSmallest([28, 25, 42, 2, 28]) == 2

assert getSmallest([1]) == 1

assert getSmallest([]) == None
