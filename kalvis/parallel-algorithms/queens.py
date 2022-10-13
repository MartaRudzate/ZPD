# Adapted from https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

def printSolution(board):
    n = len(board)  # size of the chessboard - number of rows
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

# A utility function to check if a queen can
# be placed on board[row][col].
# (Assume that "col" queens are already placed in columns from 0 to col -1.
def isSafe(board, row, col):
    n = len(board)

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQone(board, col):
    n = len(board)

    # base case: If all queens are placed
    # then return true
    if col >= n:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1  # Try to place a queen
            if solveNQone(board, col + 1) == True:  # recurrent call to go deeper
                return True
            board[i][col] = 0  # If does not work, remove queen from board[i][col]
    return False  # Dead end: Cannot place anywhere in the column


def setRowStarts(board):
    n = len(board)
    result = [-1]*n
    for col in range(0,n):
        for i in range(0,n):
            if board[i][col] == 1:
                result[col] = i
    return result

# A variant of solveNQone(...) finding all NQueens solutions.
def solveNQall(board, col, allBoards):
    n = len(board)
    rowStarts = [-1] * n

    # base case: If all queens are placed
    # then return true
    if col >= n:
        rowStarts = setRowStarts(board)
        allBoards.append(rowStarts)
        return rowStarts

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(n):
        if i < rowStarts[col] or ((i == rowStarts[col]) and (col == n-1)):
            continue
        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
            # recur to place rest of the queens
            if solveNQall(board, col + 1, allBoards) == True:
                return True
            # If doesn't lead to a solution, remove queen from board[i][col]
            board[i][col] = 0

    # Dead end: The queen can not be placed in any row in this column
    return False


# Prints one of the feasible solutions.
def printOne(n):
    board = [[0]*n for k in range(0,n)]
    if solveNQone(board, 0) == False:
        print('Solution does not exist')
        return False
    printSolution(board)


# Prints all feasible solutions
def printAll(n):
    allBoards = []  # all solutions stored in compact form
    board = [[0]*n for k in range(0,n)]
    solveNQall(board, 0, allBoards)
    for bb in allBoards:
        print(bb)

    print('Total solutions: {}'.format(len(allBoards)))
