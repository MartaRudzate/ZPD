import copy

# Adapted from https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/

class QueenPosition:
    # An n*n two-dimensional array; board[i][j]==1 iff there is a queen in the i-th row and j-th column.
    board = []
    # The size of the chessboard.
    n = 1
    # Remember the latest valid solution.
    latestSolution = []
    # "breadcrumbs" remember the queen positions in the most recent solution - but unlike "latestSolution" may be overwritten.
    # "breadcrumbs" allow findNextPosition(...) to avoid re-discovering something multiple times
    breadcrumbs = []

    # Class constructor. "latestSolution" parameter is a list of length n (the latest valid solution).
    # Normally we resume our search starting from "latestSolution".
    # If "latestSolution" is unspecified, fill it with [-1,-1,...,-1] - to start from the very beginning.
    def __init__(self, N, latestSolution=None):
        self.n = N
        self.board = [[0] * self.n for k in range(0, self.n)]
        self.breadcrumbs = [-1] * self.n
        if latestSolution is None:
            self.latestSolution = [-1] * self.n
        else:
            # self.latestSolution = copy.deepcopy(latestSolution)
            self.latestSolution = latestSolution

    # Output a solution as a n*n matrix of 0's and 1's (the content of "board").
    # Here we use "latestSolution" array instead of "board" (as "board" may now contain something else)
    def printLatestSolution(self):
        for i in range(self.n):
            for j in range(self.n):
                print(int(self.latestSolution[i] == j), end=" ")
            print()

    # Check if the next queen can be safely placed on board[row][col].
    # Assume that the columns 0,1,...,(col-1) are already occupied by some queens.
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

    # Convert n*n array with 0's and 1's into a list showing where is the queen in every column
    # For example, self.board = [[0,1,0,0], [0,0,0,1], [1,0,0,0], [0,0,1,0]] converts to result = [1, 3, 0, 2]
    def compactifySolution(self):
        result = [-1] * self.n
        for col in range(0, self.n):
            for i in range(0, self.n):
                if self.board[i][col] == 1:
                    result[col] = i
        return result

    # Return True iff the next position can be found (assigned to "latestSolution").
    # Otherwise return False: if no new queen can be placed in the column "col".
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

        # The queen can not be placed in any row in this column.
        # Backtrack the search and erase breadcrumbs ("board" now remembers the most recent position).
        self.breadcrumbs = [-1] * self.n
        return False

