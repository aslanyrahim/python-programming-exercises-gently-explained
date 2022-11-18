def drawBorder(width: int, height: int):
    """
    Draw a border

    :param width: Width of border
    :param height: Height of border
    :type width: int
    :type height: int
    :raise TypeError: If width or height is not an int
    :return: None
    :rtype: None
    """
    if width < 1 or height < 1:
        return

    print(f"+" + "-" * (width - 2) + "+")
    for _ in range(height - 2):
        print(f"|" + " " * (width - 2) + "|")
    print(f"+" + "-" * (width - 2) + "+")
    ...


drawBorder(6, 8)
