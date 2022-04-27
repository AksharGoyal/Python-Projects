import pprint
import time

def find_next_empty(puzzle):
    '''
    The function helps find an empty cell to fill a number
    '''
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1: # we found an empty cell
                return r,c 
    return None, None # no empty cell

def is_Valid(puzzle, guess, row, col):
    '''
    The function tells us if our guess is valid or not. If a cell in a row or column
    already contains our guess then we don't use it and return False else we return True
    '''
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    if guess in col_vals:
        return False 
    
    row_start = (row // 3) * 3 # get the box's starting row number
    col_start = (col // 3) * 3 # get the box's starting column number
    
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess: # check if the neighbours have the same guess
                return False
    return True

def sudoku_solver(puzzle):
    '''
    The functions is the game solver! Using the above 2 functions, it solves the game with various guesses!
    If the game is not solvable, it will return False else True.
    '''

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

    print(sudoku_solver(example_board2))
    time.sleep(0.8)
    pprint.pprint(example_board1)
    
