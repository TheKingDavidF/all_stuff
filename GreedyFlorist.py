

def getMinimumCost(k, c):
    cost = 0
    n = len(c)
    if k >= n:
        return sum(c)
    c.sort(reverse=True)
    ii = 0
    while ii + k <= n - 1:
        for jj in range(ii, ii + k):
            cost += c[jj] * (1 + ii/k)
        ii += k
    for jj in range(ii, n):
        cost += c[jj]*(1 + ii/k)
    return cost









k1 = 3
c1 = [1, 3, 5, 7, 9]

print(getMinimumCost(k1, c1))