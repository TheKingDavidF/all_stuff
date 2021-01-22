

def longestCommonSubsequence(a, b):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for ii in range(1, n + 1):
        for jj in range(1, m + 1):
            if a[ii-1] == b[jj-1]:
               dp[ii][jj] = dp[ii-1][jj-1] + 1
            else:
                dp[ii][jj] = max(dp[ii - 1][jj], dp[ii][jj - 1])
    for row in dp:
        print(row)
    ii = 0
    jj = 0
    res = []
    while n - ii - 1 >= 0 and m - jj - 1 >= 0:
        if dp[n-ii][m-jj] == dp[n-(ii+1)][m-jj]:
            ii += 1
        elif dp[n-ii][m-jj] == dp[n-ii][m-(jj+1)]:
            jj += 1
        else:
            res.insert(0, a[n - ii - 1])
            ii += 1
            jj += 1

    return res




a_aux = '1 2 3 4 1'
b_aux = '3 4 1 2 1 3'

a = list(map(int, a_aux.rstrip().split()))
b = list(map(int, b_aux.rstrip().split()))

print(longestCommonSubsequence(a, b))