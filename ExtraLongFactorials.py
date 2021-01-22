import math

def factorial(n):
    if n>1:
        res = n * factorial(n-1)
    else:
        res = 1
    return res


N=40
print('my factorial: {}'.format(factorial(N)))
print('ideal factorial: {}'.format(math.factorial(N)))