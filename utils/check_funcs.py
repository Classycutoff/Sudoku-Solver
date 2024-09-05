import math

import utils._global as _global
# from utils.set_values import set_possible_vals_grid, set_single_value


def check_if_solved(grid) -> bool:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            cell_val = grid[row][col]
            if cell_val == 0:
                return False
    return True


def check_if_cell_has_one_possible_answer(row, col):
    # for row in range(len(_global.possible_vals_grid)):
    #     for col in range(len(_global.possible_vals_grid[row])):
    # if len(_global.possible_vals_grid[row][col]) == 0:
    #     return False
    if len(_global.possible_vals_grid[row][col]) == 1:
        return True
    return False


def _check_box(box):
    val_count = {}
    for row in range(len(box)):
        for col in range(len(box[row])):
            if not box[row][col]:
                continue
            for inner_index in range(len(box[row][col])):
                cell_val = box[row][col][inner_index]
                if cell_val in val_count:
                    val_count[cell_val] = False
                    continue
                elif cell_val not in val_count:
                    # val_count[cell_val] = {}
                    # val_count[cell_val]['count'] = 1
                    # val_count[cell_val]['index'] = ()
                    val_count[cell_val] = (row, col)
                    continue

    single_possible_val = []
    for key, grid_index in val_count.items():
        if not grid_index:
            continue
        single_possible_val.append((key, grid_index))

    return single_possible_val


def check_if_box_has_possible_single_values() -> list[int, tuple[int, int]]:
    result_single_val = []
    box_amount = int(math.sqrt(len(_global.possible_vals_grid)))
    for box_row in range(box_amount):
        for box_col in range(box_amount):
            temp_box = []
            for i in range(box_amount):
                temp_box.append(_global.possible_vals_grid[box_row * box_amount + i][box_col * box_amount: box_col * box_amount + box_amount])

            box_single_val_count = _check_box(temp_box)
            if not box_single_val_count:
                continue
            
            for val, (row, col) in box_single_val_count:
                result_single_val.append((val, (box_row * box_amount + row, box_col * box_amount + col)))
                # print(f'Row: {row}, col: {col}, val: {val}')
        
    return result_single_val