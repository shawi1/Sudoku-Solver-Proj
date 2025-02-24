# Python algorithm to solve a Sudoku Board

# First check if it is valid to place num at board[row][col]
def is_valid(board, row, col, num):
    # check if num is in row
    for x in range(9):
        if board[row][x] == num:
            return False

    # check if num is in col   
    for x in range(9):
        if board[x][col] == num:
            return False
        
    # check if num is in the 3x3 sub-matrix
    start_row = row - (row % 3)
    start_col = col - (col % 3)

    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
            

    return True


def sudoku_algorithm(board, row, col):
    # base case:
    if row == 8 and col == 9:
        return True
    
    # check if last column of the row, go to next row
    if col == 9:
        row += 1
        col = 0

        