from queens import *

# See also: https://docs.pytest.org/en/7.1.x/getting-started.html

def test_isSafe01():
    board = [[0,1,0,0], [0,0,0,0], [1,0,0,0], [0,0,0,0]]
    assert not isSafe(board, 0, 3)
    assert isSafe(board, 1, 3)
    assert not isSafe(board, 2, 3)
    assert isSafe(board, 3, 3)
