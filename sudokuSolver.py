sudokuBoard = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]


def solveBoard(board):
    printBoard(board)
    print("---------------------------")
    current_space = findEmptySpace(board)
    if not findEmptySpace:
        return True
    else:
        row, column = current_space
    for i in range(1, 10):
        if isValidEntry(board, i, (row, column)):
            board[row][column] = i

            if solveBoard(board):
                return True

            board[row][column] = 0
    return False


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def findEmptySpace(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return 0


def checkSolved(board):
    if findEmptySpace(board) == 0:
        return 1
    return 0


def isValidEntry(board, value, position):
    # Check Rows
    for i in range(len(board[0])):
        if board[position[0]][i] == value and position[1] != i:
            return False
    # Check Columns
    for i in range(len(board)):
        if board[i][position[1]] == value and position[0] != i:
            return False
    # Check Square
    square_x = position[1] // 3
    square_y = position[0] // 3

    for i in range(square_y*3, square_y*3 + 3):
        for j in range(square_x * 3, square_x*3 + 3):
            if board[i][j] == value and (i,j) != position:
                return False
    return True

solveBoard(sudokuBoard)
