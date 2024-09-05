

def print_sudoku_grid(grid):
    results_str_lst = []
    for row in range(len(grid)):
        tmp_row = [str(i) if i != 0 else ' ' for i in grid[row]]
        results_str_lst.append('|'.join(tmp_row))

    between_str = '\n' + '-' * 18 + '\n'
    result_str = between_str.join(results_str_lst)
    print(f'\nSolved sudoku: \n\n{result_str}')



def set_print(val, row, col):
    print(f'Value {val} set, row: {row}, col {col}')