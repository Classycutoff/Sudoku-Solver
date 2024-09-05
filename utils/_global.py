# _global.py is where I store global variables that are needed all over the place in my funcs. This way I can make sure that they are easily changeable and easily retrievable.

max_limit = 40

possible_vals_grid = [[[k for k  in range(1, 10)] for j in range(9)] for i in range(9)]


check_if_cell_has_one_possible = [[False for k in range(9)] for i in range(9)]
