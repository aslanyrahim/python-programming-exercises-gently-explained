def drawBox(size: int):
    """
    Draw a 3D Box

    :param size: Contains an integer for the width, length and height of the box
    :type size: int
    :raise TypeError: If size is not an int
    :return: None
    :rtype: None
    """

    if size < 1:
        return

    # Print Top Layer
    print(f" " * (size + 1), end="")
    print(f"+" + "-" * (size * 2) + "+")

    # Print Next Layer
    for n in range(size):
        print(f" " * (size - n), end="")
        print(f"/" + " " * (size * 2) + "/", end="")
        print(f" " * n + "|")

    # Print Next Next Layer
    print(f"+" + "-" * (size * 2) + "+", end="")
    print(f" " * size + "+")

    # Print Next Next Next Layer
    for m in range(size):
        # print(f" " * (size - n), end="")
        print(f"|" + " " * (size * 2) + "|", end="")
        print(f" " * (size - (m + 1)) + "/")

    # Print Last Layer
    print(f"+" + "-" * (size * 2) + "+")
    ...


drawBox(1)
drawBox(2)
drawBox(3)
drawBox(4)
drawBox(5)
