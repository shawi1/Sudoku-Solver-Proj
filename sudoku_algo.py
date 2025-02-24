# Python algorithm to solve a Sudoku Board

# First check if it is valid to place num at board[row][col]
def isValid(board, row, col, num):
    # check if num is in row
    for x in range(9):
        if board[row][x] == num:
            return False

    # check if num is in col   
    for x in range(9):
        if board[x][col] == num:
            return False
        
    # check if num is in the 3x3 sub-matrix
    startRow = row - (row % 3)
    startCol = col - (col % 3)