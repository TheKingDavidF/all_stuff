

def bomberMan_l(n, grid):
    result_grid = []
    row_num = len(grid)
    col_num = len(grid[0])
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for time in range(n-1):
        for ii in range(row_num):
            for jj in range(col_num):
                if grid[ii][jj] == '.' and (time+1) % 2 == 0:
                    grid[ii][jj] = 'O'
                elif grid[ii][jj] == 'O':
                    grid[ii][jj] = '1'
                elif grid[ii][jj] == '1':
                    grid[ii][jj] = '2'
                elif grid[ii][jj] == '2':
                    for neighbor in neighbors:
                        if 0 <= ii+neighbor[0] < row_num and 0 <= jj+neighbor[1] < col_num:
                            if grid[ii+neighbor[0]][jj+neighbor[1]] != '2':
                                grid[ii + neighbor[0]][jj + neighbor[1]] = '.'
                    grid[ii][jj] = '.'

    for ii in range(row_num):
        for jj in range(col_num):
            if grid[ii][jj] == '.' and n % 2 == 0:
                grid[ii][jj] = 'O'
            elif grid[ii][jj] == '2':
                for neighbor in neighbors:
                    if 0 <= ii + neighbor[0] < row_num and 0 <= jj + neighbor[1] < col_num:
                        if grid[ii + neighbor[0]][jj + neighbor[1]] != '2':
                            grid[ii + neighbor[0]][jj + neighbor[1]] = '.'
                grid[ii][jj] = '.'
            if grid[ii][jj] != '.':
                grid[ii][jj] = 'O'
    for ii in range(row_num):
        result_grid.append(''.join(grid[ii]))
    return result_grid


def bomberMan(n, grid):
    if n in [0, 1]:
        return grid
    elif n % 2 == 0:
        return ['O' * len(x) for x in grid]
    else:
        # replace symbols
        grid = [x.replace('O', '2') for x in grid]
        grid = [x.replace('.', '0') for x in grid]
        # split rows into list
        grid = [list(map(int, list(x))) for x in grid]

        R = len(grid)
        C = len(grid[0])
        t = 1
        while t < 4 + n % 4:
            t += 1
            # each second check whole grid
            destroyed = []  # for location of cells that will explode
            for r in range(R):
                for c in range(C):
                    # decrease bomb timer (simultaneously with either planting or explosion)
                    if grid[r][c] > 0: grid[r][c] -= 1

                    # plant
                    if t % 2 == 0 and grid[r][c] == 0:
                        grid[r][c] = 3

                    # explode
                    elif grid[r][c] == 0:
                        destroyed.append([r, c])
                        if r < R - 1: destroyed.append([r + 1, c])
                        if r > 0: destroyed.append([r - 1, c])
                        if c < C - 1: destroyed.append([r, c + 1])
                        if c > 0: destroyed.append([r, c - 1])
            if destroyed:
                grid = [[2] * len(x) for x in grid]
                for r, c in destroyed:
                    grid[r][c] = 0

        # convert lists to strings
        grid = [''.join(list(map(str, x))) for x in grid]
        # replace symbols
        grid = [x.replace('2', 'O') for x in grid]
        grid = [x.replace('0', '.') for x in grid]

        return grid

n = 3
grid_raw = '''.......
...O...
....O..
.......
OO.....
OO.....'''.split('\n')

input_grid = []

for row in grid_raw:
    input_grid.append(list(row))

res_grid = bomberMan(n, input_grid)
print('True result grid:')
print('''OOO.OOO
OO...OO
OOO...O
..OO.OO
...OOOO
...OOO\n\n''')
print('My result grid:')

print('\n'.join(res_grid))


