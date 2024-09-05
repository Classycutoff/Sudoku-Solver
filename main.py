import time
import os
import json
import re

from dotenv import load_dotenv

import utils._global as _global
from utils.sudoku_funcs import *
from utils.print_funcs import print_sudoku_grid

test_grid = [
    [2, 5, 0, 0, 3, 0, 9, 0, 1],
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]

solved_grid = [
    [2,5,8,7,3,6,9,4,1],
    [6,1,9,8,2,4,3,5,7],
    [4,3,7,9,1,5,2,6,8],
    [3,9,5,2,7,1,4,8,6],
    [7,6,2,4,9,8,1,3,5],
    [8,4,1,6,5,3,7,2,9],
    [1,8,4,3,6,9,5,7,2],
    [5,7,6,1,4,2,8,9,3],
    [9,2,3,5,8,7,6,1,4]
]

def main(grid=test_grid):
    load_dotenv()
    # set_possible_vals_grid(test_grid)
    # print(possible_vals_grid)
    is_finished, result_grid = loop_through_possible_vals(grid)
    # print(_global.possible_vals_grid)
    # print(_global.check_if_cell_has_one_possible)

    print_sudoku_grid(result_grid)

    if result_grid == solved_grid:
        print('Matches the solved grid.')



if __name__ == '__main__':
    start = time.time()
    main()
    print(f'{round(time.time() - start, 4)} seconds.')