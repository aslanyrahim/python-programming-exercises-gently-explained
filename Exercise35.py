def getTitleCase(text: str) -> str:
    """
    Return a titlecase of the text

    :param text: text in string
    :type text: str
    :raise TypeError: If text is not a str
    :return: str
    :rtype: str
    """
    titleCase = ""

    if len(text) == 0:
        return titleCase

    for i in range(len(text)):
        if i == 0:
            titleCase += text[i].upper()
        elif text[i].isalpha() and not text[i - 1].isalpha():
            titleCase += text[i].upper()
        else:
            titleCase += text[i].lower()

    return titleCase
    ...


assert getTitleCase("Hello, world!") == "Hello, World!"

assert getTitleCase("HELLO") == "Hello"

assert getTitleCase("hello") == "Hello"

assert getTitleCase("hElLo") == "Hello"

assert getTitleCase("") == ""

assert getTitleCase("abc123xyz") == "Abc123Xyz"

assert getTitleCase("cat dog RAT") == "Cat Dog Rat"

assert getTitleCase("cat,dog,RAT") == "Cat,Dog,Rat"

import random

random.seed(42)

chars = list("abcdefghijklmnopqrstuvwxyz1234567890 ,.")

for i in range(1000):

    random.shuffle(chars)

    assert getTitleCase("".join(chars)) == "".join(chars).title()
