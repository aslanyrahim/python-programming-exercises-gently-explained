def writeToFile(filename, content):
    with open(filename, "w") as fileObj:
        fileObj.write(content)


def appendToFile(filename, content):
    with open(filename, "a") as fileObj:
        fileObj.write(content)


def readFromFile(filename):
    with open(filename) as fileObj:
        return fileObj.read()


writeToFile("greet.txt", "Hello!\n")
appendToFile("greet.txt", "Goodbye!\n")
assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"
