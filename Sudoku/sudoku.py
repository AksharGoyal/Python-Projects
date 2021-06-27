def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c 
    return None, None

def is_Valid(puzzle, guess, row, col):
    
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False 
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def sudoku_solver(puzzle):
    # print(f'Puzzle {puzzle}')
    row, col = find_next_empty(puzzle)
    # print(f'row: {row}, col: {col}')
    if row is None:
        return True
    
    for guess in range(1, 10):
        if is_Valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            
            if sudoku_solver(puzzle):
                return True
        puzzle[row][col] = -1
    return False 

if __name__ == '__main__':
    example_board1 = [[-1 for _ in range(9)] for _ in range(9)]
    example_board2 = [
        [-1, 2, 3,      -1, 5, -1,      -1, 8, 9],
        [9, -1, 4,      -1, 6, 2,       1, 3, -1], 
        [-1, 6, 8,      7, 4, 3,        5, -1, -1],
        [7, 9, -1,      4, 2, 5,        -1, 6, 1],
        [5, 3, 1,       -1, 8, 2,       -1, 4, 7],
        [4, 7, 2,       8, 9, 1,        3, 5, 6],
        [6, -1, 9,      3, -1, 7,       4, 2, 8],
        [-1, 4, 5,      9, 7, -1,       2, -1, 3],
        [-1, -1, -1,    -1, 3, -1,      -1, -1, -1]
    ]
    
    print(sudoku_solver(example_board1))
    print(example_board1)