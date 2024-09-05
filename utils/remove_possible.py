
import utils._global as _global


def remove_row_and_col_possible_vals(cell_val: int, row: int, col: int):
    for _row in range(len(_global.possible_vals_grid)):
        if cell_val in _global.possible_vals_grid[_row][col]:
            _global.possible_vals_grid[_row][col].remove(cell_val)
    for _col in range(len(_global.possible_vals_grid[row])):
        if cell_val in _global.possible_vals_grid[row][_col]:
            _global.possible_vals_grid[row][_col].remove(cell_val)


def remove_box_possible_vals(cell_val: int, row: int, col: int):
    # Check if box empty of sudoku values.
    box_row_start_index = row // 3
    box_col_start_index = col // 3
    for i in range(3):
        for j in range(3):
            box_row_index = box_row_start_index * 3 + i
            box_col_index = box_col_start_index * 3 + j
            if cell_val in _global.possible_vals_grid[box_row_index][box_col_index]:
                _global.possible_vals_grid[box_row_index][box_col_index].remove(cell_val)
