# Version 1
# def getChessSquareColor(column, row):
#     if column not in range(1,9):
#         return ""
#     if row not in range(1,9):
#         return ""
#     if column % 2 == 1:
#         if row % 2 == 1:
#             return "white"
#         else:
#             return "black"
#     else:
#         if row % 2 == 1:
#             return "black"
#         else:
#             return "white"

# Version 2
def getChessSquareColor(column, row):
    if column not in range(1, 9):
        return ""
    if row not in range(1, 9):
        return ""
    if column % 2 == row % 2:
        return "white"
    else:
        return "black"


assert getChessSquareColor(1, 1) == "white"

assert getChessSquareColor(2, 1) == "black"

assert getChessSquareColor(1, 2) == "black"

assert getChessSquareColor(8, 8) == "white"

assert getChessSquareColor(0, 8) == ""

assert getChessSquareColor(2, 9) == ""
