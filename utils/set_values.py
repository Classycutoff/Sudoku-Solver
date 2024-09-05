import utils._global as _global

from utils.remove_possible import remove_box_possible_vals, remove_row_and_col_possible_vals


def set_possible_vals_grid(sudoku_grid):
    for row in range(len(sudoku_grid)):
        for col in range(len(sudoku_grid[row])):
            cell_val = sudoku_grid[row][col]

            if cell_val == 0:
                continue
            
            _global.possible_vals_grid[row][col] = []

            remove_row_and_col_possible_vals(cell_val, row, col)
            remove_box_possible_vals(cell_val, row, col)


def set_single_value(grid, val, row, col):
    grid[row][col] = val
    _global.possible_vals_grid[row][col] = []
    remove_row_and_col_possible_vals(val, row, col)
    remove_box_possible_vals(val, row, col)
    return grid
