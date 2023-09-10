import numpy as np

def is_internal(board, row, col):
    size = len(board)
    return (
        row != 0 and 
        col != 0 and
        row + 1 < size and 
        col + 1 < size
    )

def neighbours(board, row, col):
    if is_internal(board, row, col):
        return (
            board[row, col - 1] + 
            board[row - 1, col - 1] + 
            board[row - 1, col] + 
            board[row - 1, col + 1] + 
            board[row, col + 1] + 
            board[row + 1, col + 1] + 
            board[row + 1, col] +
            board[row + 1, col - 1]
            )
    else: return 0

def next_iteration(board):
    for row, _ in enumerate(board):
        for column, smt in enumerate(_):
            val = neighbours(board, row, column)
            if val <= 1 and not is_internal(board, row, column):
                pass
            elif val <= 1 or val >= 4:
                board[row, column] = 0
            elif val == 3:
                board[row, column] = 1
    return board