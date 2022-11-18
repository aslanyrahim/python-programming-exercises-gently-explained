def drawPyramid(height: int):
    """
    Draw a pyramid

    :param height: Height of pyramid
    :type height: int
    :raise TypeError: If height is not an int
    :return: None
    :rtype: None
    """

    for h in range(height):
        print(f" " * (height - (h + 1)), end="")
        print(f"#" * (2 * h + 1))
    ...


drawPyramid(6)
