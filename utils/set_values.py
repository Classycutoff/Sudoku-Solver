import utils._global as _global

from utils.remove_possible import remove_box_possible_vals, remove_row_and_col_possible_vals
from utils.check_funcs import check_if_box_has_possible_single_vals, check_if_row_or_columns_has_possible_vals

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


def set_mult_vals(grid, set_vals: tuple[int, tuple[int, int]]):
    for val, (row, col) in set_vals:
        grid = set_single_value(grid, val, row, col)
    return grid


def set_vals_box(grid):
    result_single_val = check_if_box_has_possible_single_vals()
    grid = set_mult_vals(grid, result_single_val)
    
    return grid


def set_vals_row_and_cols(grid):
    col_and_row_set_vals = check_if_row_or_columns_has_possible_vals()
    grid = set_mult_vals(grid, col_and_row_set_vals)
    return grid