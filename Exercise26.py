def printHandshakes(people: list):
    if len(people) < 2:
        return None

    index = 1
    count = 0
    for name in people:
        for nextName in people[index:]:
            print(f"{name} shakes hands with {nextName}")
            count += 1
        index += 1
    return count
    ...


assert printHandshakes(["Alice", "Bob"]) == 1

assert printHandshakes(["Alice", "Bob", "Carol"]) == 3

assert printHandshakes(["Alice", "Bob", "Carol", "David"]) == 6
