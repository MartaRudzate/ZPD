# Adapted from https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

# A utility function to check if a queen can
# be placed on board[row][col].
# (Assume that "col" queens are already placed in columns from 0 to col -1.
def isSafe(board, row, col):

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
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQone(board, col):
    global resuming
    global rowStart

    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1  # Try to place a queen
            if solveNQone(board, col + 1) == True:  # recurrent call to go deeper
                return True
            board[i][col] = 0  # If does not work, remove queen from board[i][col]
    return False  # Dead end: Cannot place anywhere in the column




resuming = False  # are we freshly resuming from the previous solution?
rowStarts = [-1]*N  # The position where to resume search (after adding 1)
allBoards = []

def setRowStarts(board):
    result = [-1]*N
    for col in range(0,N):
        for i in range(0,N):
            if board[i][col] == 1:
                result[col] = i
    return result

# A variant of solveNQone(...) that enables to find subsequent NQueens solutions.
# Return False, if everything is done; Return True, if something else can be found.
def solveNQall(board, col):
    global resuming
    global rowStarts
    global allBoards

    # base case: If all queens are placed
    # then return true
    if col >= N:
        rowStarts = setRowStarts(board)
        #allBoards.append(board)
        allBoards.append(rowStarts)
        resuming = True
        return True

    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
        if resuming and i < rowStarts[col]:
            #print('Jumping out ({},{}), rowstats = {}'.format(i,col,rowStarts[col]))
            #printSolution(board)
            continue
        if resuming and (i==rowStarts[col]) and (col==N-1):
            #print('Jumping out last ({},{})'.format(i,col))
            resuming = False
            continue

        if isSafe(board, i, col):

            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solveNQall(board, col + 1) == True:
                return True

            # If doesn't lead to a solution, remove queen from board[i][col]
            board[i][col] = 0

    # The queen can not be placed in any row in this column
    return False


# Prints one of the feasible solutions.
def printOne(NN):
    global N
    N = NN
    board = [[0]*N for k in range(0,N)]

    if solveNQone(board, 0) == False:
        print ("Solution does not exist")
        return False

    printSolution(board)


# Prints all feasible solutions
def printAll(NN):
    global N
    global allBoards
    N = NN
    allBoards = []

    board = [[0]*N for k in range(0,N)]

    while solveNQall(board, 0):
        board = [[0]*N for k in range(0,N)]

    num = 1
    for bb in allBoards:
        print('**** Solution #{}: {}'.format(num, bb))
        num += 1

    print('num = {}'.format(len(allBoards)))
