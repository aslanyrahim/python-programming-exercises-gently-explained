def rot13(text: str) -> str:
    """
    Return a ROT13 cipher text.

    :param text: text in str
    :type text: str
    :raise TypeError: If text is not a str
    :return: str
    :rtype: str
    """
    rot13 = ""

    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 77 or 97 <= ord(text[i]) <= 109:
            # A-Ma-m -> N-Zn-z
            rot13 += chr(ord(text[i]) + 13)
        elif 78 <= ord(text[i]) <= 90 or 110 <= ord(text[i]) <= 122:
            # N-Zn-z -> A-Ma-m
            rot13 += chr(ord(text[i]) - 13)
        else:
            # non alpha
            rot13 += text[i]

    return rot13
    ...


assert rot13("Hello, world!") == "Uryyb, jbeyq!"

assert rot13("Uryyb, jbeyq!") == "Hello, world!"

assert rot13(rot13("Hello, world!")) == "Hello, world!"

assert rot13("abcdefghijklmnopqrstuvwxyz") == "nopqrstuvwxyzabcdefghijklm"

assert rot13("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "NOPQRSTUVWXYZABCDEFGHIJKLM"
