def drawRectangle(width: int, height: int) -> None:
    """
    Draw a rectangle

    :param width: Width of rectangle
    :param height: Height of rectangle
    :type width: int
    :type height: int
    :raise TypeError: If width or height is not an int
    :return: None
    :rtype: None
    """
    if width < 1 or height < 1:
        return

    for _ in range(height):
        print(f"#" * width)


drawRectangle(3, 4)
