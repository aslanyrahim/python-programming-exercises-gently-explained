def getUppercase(text: str) -> str:
    """
    Return a uppercase of the text

    :param text: text in string
    :type text: str
    :raise TypeError: If text is not a str
    :return: str
    :rtype: str
    """
    upperCase = ""

    if len(text) == 0:
        return upperCase

    for i in range(len(text)):
        if 97 <= ord(text[i]) <= 122:
            upperCase += chr(ord(text[i]) - 32)
        else:
            upperCase += text[i]

    return upperCase
    ...


assert getUppercase("Hello") == "HELLO"

assert getUppercase("hello") == "HELLO"

assert getUppercase("HELLO") == "HELLO"

assert getUppercase("Hello, world!") == "HELLO, WORLD!"

assert getUppercase("goodbye 123!") == "GOODBYE 123!"

assert getUppercase("12345") == "12345"

assert getUppercase("") == ""
