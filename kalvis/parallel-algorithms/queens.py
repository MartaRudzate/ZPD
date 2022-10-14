import copy

# Adapted from https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/


class QueenPosition:
    board = []
    n = 1
    latestSolution = []
    breadcrumbs = []

    def __init__(self, N, latestSolution=None):
        self.n = N
        self.board = [[0] * self.n for k in range(0, self.n)]
        self.breadcrumbs = [-1] * self.n
        if latestSolution is None:
            self.latestSolution = [-1] * self.n
        else:
            self.latestSolution = copy.deepcopy(latestSolution)

    def printLatestSolution(self):
        for i in range(self.n):
            for j in range(self.n):
                print(int(self.latestSolution[i] == j), end=" ")
            print()

    def isSafe(self, row, col):
        # Check this row on left side
        for i in range(col):
            if self.board[row][i] == 1:
                return False
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def findFirst(self, col):
        if col >= self.n:
            self.latestSolution = self.compactifySolution()
            return True
        for i in range(self.n):
            if self.isSafe(i, col):
                self.board[i][col] = 1
                if self.findFirst(col + 1):
                    return True
                self.board[i][col] = 0
        return False

    def compactifySolution(self):
        result = [-1] * self.n
        for col in range(0, self.n):
            for i in range(0, self.n):
                if self.board[i][col] == 1:
                    result[col] = i
        return result

    def getLatestSolution(self):
        return self.latestSolution

    def findNextPosition(self, col):
        if col >= self.n:
            self.latestSolution = self.compactifySolution()
            self.breadcrumbs = copy.deepcopy(self.latestSolution)
            self.board = [[0] * self.n for k in range(0, self.n)]
            return True

        for i in range(self.n):
            if i < self.breadcrumbs[col]:
                continue
            if i == self.breadcrumbs[col] and col == self.n - 1:
                continue
            if self.isSafe(i, col):
                # Place this queen in board[i][col]
                self.board[i][col] = 1
                # recursive call - an attempt to place remaining queens
                if self.findNextPosition(col + 1):
                    return True
                # If there is no solution on row "i", remove queen from board[i][col]
                self.board[i][col] = 0

        # The queen can not be placed in any row in this column
        self.breadcrumbs = [-1] * self.n
        return False


def print_solution(board):
    n = len(board)  # size of the chessboard - number of rows
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


# A utility function to check if a queen can be placed on board[row][col].
# (Assume that "col" queens are already placed in columns from 0 to col-1.)
def is_safe(board, row, col):
    n = len(board)
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col):
    n = len(board)
    # If all queens are placed, then return true
    if col >= n:
        return True
    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 1  # Try to place a queen
            if solve_nqueens(board, col + 1):  # recurrent call to go deeper
                return True
            board[i][col] = 0  # If does not work, remove queen from board[i][col]
    return False  # Dead end: Cannot place anywhere in the column

