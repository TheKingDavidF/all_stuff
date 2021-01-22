# https://www.hackerrank.com/dashboard
# tunnel
# calculate exit condition

def find_A(maze):
    for ii in range(len(maze)):
        row = maze[ii]
        for jj in range(len(row)):
            if row[jj] == 'A':
                return ii, jj


def step_gen(cursor, arr):
    steps = list()
    aux_arr = [[0,1], [0,-1], [1,0], [-1,0]]
    size = [len(arr), len(arr[0])]
    for step in aux_arr:
        if (0 <= cursor[0]+step[0] < size[0]) and (0 <= cursor[1]+step[1] < size[1]):
            steps.append([cursor[0]+step[0], cursor[1]+step[1]])

    return steps


def near_prob_fill(cursor, maze, prob_arr, tunnels):
    total = 0
    steps = step_gen(cursor, maze)

    for step in steps:
        if maze[step[0]][step[1]] != '#':
            total += 1
    for step in steps:
        if (maze[step[0]][step[1]] != '#') and (maze[step[0]][step[1]] != '*'):
            prob_arr[step[0]][step[1]] = + prob_arr[cursor[0]][cursor[1]]/total
            for tunnel in tunnels:
                if tunnel[0] == step:
                    prob_arr[tunnel[1][0]][tunnel[1][1]] += prob_arr[cursor[0]][cursor[1]]/total
                elif tunnel[1] == step:
                    prob_arr[tunnel[0][0]][tunnel[0][1]] += prob_arr[cursor[0]][cursor[1]] / total
    return prob_arr


def choose_next_cell(history_arr, tunnels):
    condition = True
    next_cell = None

    for ii in range(len(history_arr)):
        for jj in range(len(history_arr[ii])):
            if history_arr[ii][jj] == 0:
                steps = step_gen([ii, jj], history_arr)
                print(steps)
                for step in steps:
                    if history_arr[step[0]][step[1]] == 1:
                        condition = False
                        next_cell = [ii, jj]
                        return next_cell, condition
                for tunnel in tunnels:
                    if tunnel[0] == [ii, jj]:
                        ii_new, jj_new = tunnel[1]
                    elif tunnel[1] == [ii, jj]:
                        ii_new, jj_new = tunnel[0]
                    else:
                        return next_cell, condition
                    steps = step_gen([ii_new, jj_new], history_arr)
                    for step in steps:
                        if history_arr[step[0]][step[1]] == 1:
                            condition = False
                            next_cell = [ii, jj]
                            return next_cell, condition
    return next_cell, condition




if __name__ == '__main__':
    # input part
    n = 3
    m = 6
    k = 1

    i1 = 2
    j1 = 3
    i2 = 2
    j2 = 1

    maze = [['#', '#', '#', '*', 'O', 'O'],
            ['O', '#', 'O', 'A', '%', 'O'],
            ['#', '#', '#', '*', 'O', 'O']]


    i_A, j_A = find_A(maze)

    tunnels = list()
    tunnels.append(((i1, j1), (i2, j2)))

    prob_arr = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
    prob_arr[i_A][j_A] = 1

    history_arr = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
    for ii in range(len(maze)):
        for jj in range(len(maze[ii])):
            if (maze[ii][jj] != 'O') and (maze[ii][jj] != 'A'):
                history_arr[ii][jj] = -1


    cursor = [i_A, j_A]
    condition = True
    while condition:
        prob_arr = near_prob_fill(cursor, maze, prob_arr, tunnels)
        history_arr[cursor[0]][cursor[1]] = 1
        cursor, condition = choose_next_cell(history_arr, tunnels)

    exit_prob = 0
    for ii in range(len(maze)):
        for jj in range(len(maze[ii])):
            if maze[ii][jj] == '%':
                exit_prob += prob_arr[ii][jj]

    print(exit_prob)






