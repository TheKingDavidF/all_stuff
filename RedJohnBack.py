import math

def issimple(n):
    for ii in range(2,n):
        if n % ii == 0:
            return False
    return True


def redJohn_wrong(n):
    dp = [0]*(n+1)
    for ii in range(1, n+1):
        if 0 <= ii < 4:
            dp[ii] = 1
        elif ii % 4 == 0:
            dp[ii] = dp[ii-1] + 1 + dp[ii-4]*2
        else:
            dp[ii] = dp[ii-1] + 1
    print(dp)
    res1 = dp[-1]
    res = 0
    for ii in range(2, res1+1):
        if issimple(ii):
            res += 1
    return res


def redJohn(n):
    combinations_1_4 = list()
    k = 0
    while k*4 <= n:
        combinations_1_4.append((k, n-4*k))
        k += 1
    all_perms = 0
    for combination in combinations_1_4:
        all_perms +=  math.factorial(combination[0] + combination[1])/\
        (math.factorial(combination[0]) * math.factorial(combination[1]))
    result = len(sieve(int(all_perms)))
    return result


def sieve(n):
    A = [1] * (n + 1)
    A[0], A[1] = 0, 0

    for i in range(2, n + 1):
        if A[i] == 1:
            A[i * i::i] = [0 for k in A[i * i::i]]

    return [k for k in range(n + 1) if A[k] == 1]


print(redJohn(7))