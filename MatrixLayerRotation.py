import math


def aux(ii, jj, r, circle, n, m):
    if ii == circle and jj != circle:
        diff = min(r, jj - circle)
        jj -= diff
        r -= diff
    elif jj == circle and ii != m - 1 - circle:
        diff = min(r, m - 1 - circle - ii)
        ii += diff
        r -= diff
    elif ii == m - 1 - circle and jj != n - 1 - circle:
        diff = min(r, n - 1 - circle - jj)
        jj += diff
        r -= diff
    elif jj == n - 1 - circle and ii != circle:
        diff = min(r, ii - circle)
        ii -= diff
        r -= diff
    else:
        k = 1/0
        return None
    return ii, jj, r

def matrixRotation(matrix, r):
    m = len(matrix)
    n = len(matrix[0])
    new_matrix = [[1 for i in range(n)] for j in range(m)]
    for ii in range(m):
        for jj in range(n):
            if ii < m/2:
                circle_i = ii
            else:
                circle_i = m - 1 - ii
            if jj < n / 2:
                circle_j = jj
            else:
                circle_j = n - 1 - jj
            circle = min(circle_i, circle_j)

            m_c = m - 2 * circle
            n_c = n - 2 * circle
            r_c = r % ((m_c + n_c - 2) * 2)
            new_ii = ii
            new_jj = jj
            while r_c > 0:
                new_ii, new_jj, r_c = aux(new_ii, new_jj, r_c, circle, n, m)
            new_matrix[new_ii][new_jj] = matrix[ii][jj]

    p = ''
    for ii in range(len(new_matrix)):
        p += ' '.join(map(str, new_matrix[ii])) + '\n'
    print(p.strip())



data1 = '''1 2 3 4
7 8 9 10
13 14 15 16
19 20 21 22
25 26 27 28'''

data2 = '''1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16'''

data3 = '''1 1
1 1'''

data4 = '''9718805 60013003 5103628 85388216 21884498 38021292 73470430 31785927
69999937 71783860 10329789 96382322 71055337 30247265 96087879 93754371
79943507 75398396 38446081 34699742 1408833 51189 17741775 53195748
79354991 26629304 86523163 67042516 54688734 54630910 6967117 90198864
84146680 27762534 6331115 5932542 29446517 15654690 92837327 91644840
58623600 69622764 2218936 58592832 49558405 17112485 38615864 32720798
49469904 5270000 32589026 56425665 23544383 90502426 63729346 35319547
20888810 97945481 85669747 88915819 96642353 42430633 47265349 89653362
55349226 10844931 25289229 90786953 22590518 54702481 71197978 50410021
9392211 31297360 27353496 56239301 7071172 61983443 86544343 43779176'''


matrix = [list(map(int, x.split(' '))) for x in data4.split('\n')]

matrixRotation(matrix, 40)