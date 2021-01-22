
def queensAttack(n, k, r_q, c_q, obstacles):
    steps = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
    counter = 0

    for step in steps:
        pos = [r_q, c_q]
        while 1:
            pos = [pos[0] + step[0], pos[1] + step[1]]
            if (1 <= pos[0] <= n) and (1 <= pos[1] <= n):
                if pos not in obstacles:
                    counter += 1
                else:
                    break
            else:
                break
    return counter


def help_diagonal(pos, obs, step):
    while (1 <= pos[0] <= n) and (1 <= pos[1] <= n):
        pass


def queensAttack_fast(n, k, r_q, c_q, obstacles):
    steps = []

    for obstacle in obstacles:
        if obstacle[1] == r_q:
            pass



