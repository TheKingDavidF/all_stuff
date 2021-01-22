

def connectedCell(matrix):
    clasters = dict()
    n = len(matrix)
    m = len(matrix[0])
    kk = 2
    steps = [(0,1), (0,-1), (1,0), (-1,0), (-1, -1), (1,1), (-1,1), (1,-1)]
    same = list()
    for ii in range(n):
        for jj in range(m):
            if matrix[ii][jj] == 1:
                for step in steps:
                    if 0 <= ii+step[0] <= n-1 and 0 <= jj+step[1] <= m-1:
                        if matrix[ii+step[0]][jj+step[1]] > 1:
                            matrix[ii][jj] = matrix[ii+step[0]][jj+step[1]]
                            clasters[matrix[ii][jj]] += 1
                            break
                else:
                    matrix[ii][jj] = kk
                    clasters[kk] = 1
                    kk += 1
            elif matrix[ii][jj] > 1:
                for step in steps:
                    if 0 <= ii+step[0] <= n-1 and 0 <= jj+step[1] <= m-1:
                        if matrix[ii+step[0]][jj+step[1]] == 1:
                            matrix[ii + step[0]][jj + step[1]] = matrix[ii][jj]
                            clasters[matrix[ii][jj]] += 1
                        elif matrix[ii+step[0]][jj+step[1]] > 1:
                            for ii in range(len(same)):
                                if matrix[ii+step[0]][jj+step[1]] in same[ii]:
                                    same[ii].add(matrix[ii][jj])
                                    break
                                elif matrix[ii][jj] in same[ii]:
                                    same[ii].add(matrix[ii+step[0]][jj+step[1]])
                                    break
                            else:
                                same.append({matrix[ii][jj], matrix[ii+step[0]][jj+step[1]]})

    #TODO: суммировать все соприкасающиеся регионы

    print(same)
    for set_ in same:
        clasters[frozenset(set_)] = 0
        for claster_name in set_:
            clasters[frozenset(set_)] += clasters[claster_name]

    for row in matrix:
        print(row)
    return clasters  # max(clasters.values())



def approach1(matrix):
    # рекурсия
    res = -1
    n = len(matrix)
    m = len(matrix[0])
    def check(i, j):
        if i < 0 or j < 0 or i >= n or j >= m or matrix[i][j] == -1 or matrix[i][j] == 0:
            return 0
        else:
            matrix[i][j] = -1
            return 1 + (check(i, j + 1) + check(i, j - 1) + check(i + 1, j) + check(i - 1, j + 1) + check(i - 1, j - 1)
                        + check(i, j + 1) + check(i + 1, j - 1) + check(i + 1, j + 1))
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                res = max(res, check(i, j))
    return res


def approach2(matrix):
    mx = 0
    filled = [(i, j) for i, row in enumerate(matrix) for j, n in enumerate(row) if n]
    while filled:
        region = [filled.pop()]
        count = 0
        while region:
            n = region.pop()
            count += 1
            for f in list(filled):
                if abs(n[0] - f[0]) <= 1 and abs(n[1] - f[1]) <= 1:
                    region.append(f)
                    filled.remove(f)
        else:
            mx = max(mx, count)
    return mx



def approach3(matrix):
    # тоже рекурсия
    m = len(matrix)
    n = len(matrix[0])
    max_size = 0

    def dfs(matrix, i, j, m, n, size):
        matrix[i][j] = 0
        dis = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        for di in dis:
            n_i = i + di[0]
            n_j = j + di[1]
            if 0 <= n_i < m and 0 <= n_j < n and matrix[n_i][n_j] == 1:
                size = dfs(matrix, n_i, n_j, m, n, size + 1)
        return size

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                size = dfs(matrix, i, j, m, n, 1)
                max_size = max(size, max_size)
    return max_size


data1 = '''1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0'''.split('\n')

data2 = '''1 1 0 0 0
0 1 1 0 0
0 0 1 0 1
1 0 0 0 1
0 1 0 1 1'''.split('\n')

data3 = '''1 1 1 0 1
0 0 1 0 0
1 1 0 1 0
0 1 1 0 0
0 0 0 0 0
0 1 0 0 0
0 0 1 1 0'''.split('\n')


data4 = '''0 1 0 0 0 0 1 1 0
1 1 0 0 1 0 0 0 1
0 0 0 0 1 0 1 0 0
0 1 1 1 0 1 0 1 1
0 1 1 1 0 0 1 1 0
0 1 0 1 1 0 1 1 0
0 1 0 0 1 1 0 1 1
1 0 1 1 1 1 0 0 0'''.split('\n')

matrix = []
for row in data4:
    matrix.append(list(map(int, row.rstrip().split())))

result = approach2(matrix)
print(result)
