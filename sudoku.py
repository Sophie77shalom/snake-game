def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None

def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
        if guess in col_vals:
            return False

    row_start =  (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start +3):
            if puzzle [r][c] == guess:
                return False
    return True



def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    if row is None:
        return True
 