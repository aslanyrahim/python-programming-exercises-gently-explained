print(f"  |  1  2  3  4  5  6  7  8  9 10")
print(f"--+------------------------------")

for n in range(1, 11):
    print(f"{n}".rjust(2) + "|", end=" ")
    for m in range(1, 11):
        print(f"{m * n}".rjust(2), sep=" ", end=" ")
    print()
