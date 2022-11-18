import random

LOWER_LETTERS = ""
for i in range(26):
    LOWER_LETTERS += chr(i + 97)
UPPER_LETTERS = ""
for i in range(26):
    UPPER_LETTERS += chr(i + 65)
NUMBERS = ""
for i in range(10):
    NUMBERS += chr(i + 48)
SPECIAL = "~!@#$%^&*()_+"

ALL_CHAR = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL


def generatePassword(length):
    if length < 12:
        length = 12

    pw = []
    pw.append(LOWER_LETTERS[random.randint(0, 25)])
    pw.append(UPPER_LETTERS[random.randint(0, 25)])
    pw.append(NUMBERS[random.randint(0, 9)])
    pw.append(SPECIAL[random.randint(0, 12)])

    i = 4
    while i < length:
        pw.append(ALL_CHAR[random.randint(0, 74)])
        i += 1

    random.shuffle(pw)

    return "".join(pw)
    ...


assert len(generatePassword(8)) == 12

pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False

for character in pw:
    if character in LOWER_LETTERS:
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial
