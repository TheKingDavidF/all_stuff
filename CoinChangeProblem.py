def getWays(n, c):
    if n < min(c):
        return 0
    m = len(c)
    c.sort()
    dp = [[0]*(n+1) for _ in range(m)]
    for jj in range(1, n+1):
        if jj % c[0] == 0:
            dp[0][jj] = 1
    for ii in range(1, m):
        for jj in range(1, n+1):
            if jj - c[ii] < 0:
                dp[ii][jj] = dp[ii - 1][jj]
            elif jj - c[ii] == 0:
                dp[ii][jj] = dp[ii - 1][jj] + 1
            else:
                dp[ii][jj] = dp[ii - 1][jj] + dp[ii][jj - c[ii]]

    return dp[m-1][n]






n1 = 4
c1 = [1, 2, 3]

n2 = 10
c2 = [2, 5, 3, 6]
print(getWays(n2, c2))