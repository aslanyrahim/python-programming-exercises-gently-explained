def reverseString(text: str) -> str:
    """
    Return a reverse string of the text

    :param text: text in string
    :type text: str
    :raise TypeError: If text is not a str
    :return: str
    :rtype: str
    """
    reverseString = ""

    if len(text) == 0:
        return reverseString

    for i in range(len(text)):
        reverseString = text[i] + reverseString

    return reverseString

    ...


assert reverseString("Hello") == "olleH"

assert reverseString("") == ""

assert reverseString("aaazzz") == "zzzaaa"

assert reverseString("xxxx") == "xxxx"
