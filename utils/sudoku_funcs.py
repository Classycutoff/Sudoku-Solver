import math

import utils._global as _global
from utils.set_values import set_possible_vals_grid, set_single_value, set_vals_box, set_vals_row_and_cols
from utils.check_funcs import check_if_cell_has_one_possible_answer, check_if_solved
from utils.print_funcs import set_print


def loop_through_possible_vals(grid) -> tuple[bool, list]:
    set_possible_vals_grid(grid)
    # check_if_cell_has_one_possible_answer()

    for i in range(_global.max_limit):
        print(f'Iteration {i}')
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cell_val = grid[row][col]
                if cell_val != 0:
                    continue
                if check_if_cell_has_one_possible_answer(row, col):
                    # set_print(_global.possible_vals_grid[row][col][0], row, col)
                    set_single_value(grid, _global.possible_vals_grid[row][col][0], row, col)

        grid = set_vals_box(grid)
        grid = set_vals_row_and_cols(grid)

        set_possible_vals_grid(grid)
        if check_if_solved(grid):
            return True, grid
    print('Didn\'t find a solution in the iteration time...')
    return False, grid


# def get_possible_vals_grid():
#     possible_vals_grid = [[[k for k  in range(1, 10)] for j in range(9)] for i in range(9)]
#     return possible_vals_grid
