def mode(numbers):
    if len(numbers) == 0:
        return None

    numberCount = {}

    mostFreqNumber = None
    mostFreqNumberCount = 0

    for n in numbers:
        if n not in numberCount:
            numberCount[n] = 0
        numberCount[n] += 1
        if numberCount[n] > mostFreqNumberCount:
            mostFreqNumber = n
            mostFreqNumberCount = numberCount[n]
    return mostFreqNumber


assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1
