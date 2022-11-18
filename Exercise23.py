for n in range(99, 1, -1):
    print(f"{n} bottles of beer on the wall,")
    print(f"{n} bottles of beer,")
    print(f"Take one down,")
    print(f"Pass it around,")

    if (n - 1) == 1:
        print(f"{n - 1} bottle of beer on the wall,")
        print()
    else:
        print(f"{n - 1} bottles of beer on the wall,")
        print()

print(f"1 bottle of beer on the wall,")
print(f"1 bottle of beer,")
print(f"Take one down,")
print(f"Pass it around,")
print(f"No more bottles of beer on the wall!")
