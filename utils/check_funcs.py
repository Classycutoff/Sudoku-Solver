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


def _get_single_val_list(single_val_dict):
    single_possible_val_list = []
    for key, grid_index in single_val_dict.items():
        if not grid_index:
            continue
        single_possible_val_list.append((key, grid_index))

    return single_possible_val_list

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

    return _get_single_val_list(val_count)


def check_if_box_has_possible_single_vals() -> list[int, tuple[int, int]]:
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

def _check_row_helper(is_row: bool, index: int):
    row_single_vals = {}
    for i in range(len(_global.possible_vals_grid)):
        if is_row:
            index_dict = {'row': index, 'col': i}
        else:
            index_dict = {'row': i, 'col': index}

        possible_cell_vals = _global.possible_vals_grid[index_dict['row']][index_dict['col']]

        if not possible_cell_vals:
            continue
        for val in possible_cell_vals:
            if val in row_single_vals:
                row_single_vals[val] = False
                continue

            if is_row:
                row_single_vals[val] = (index_dict['row'], index_dict['col'])


    return _get_single_val_list(row_single_vals)


def check_if_row_or_columns_has_possible_vals():
    single_cells_to_be_filled = []
    for i in range(len(_global.possible_vals_grid)):
        row_single_val_list = _check_row_helper(is_row=True, index=i)
        single_cells_to_be_filled.extend(row_single_val_list)

        col_single_val_list = _check_row_helper(is_row=False, index=i)
        single_cells_to_be_filled.extend(col_single_val_list)

    # print(single_cells_to_be_filled)
    return single_cells_to_be_filled

                

