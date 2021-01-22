import math

def sum_of_multiples(n, k):
    '''That function find sum of all multiples for k less then n'''
    res = 0
    for ii in range(1, n):
        if ii % k == 0:
            res += ii
    return res


def sum_even_fibonacci(n):
    '''That function find sum of all even-valued Fibonacci secuence member that less then n'''
    res = 0
    fibonacci1 = 1
    fibonacci2 = 2
    while fibonacci2 <= n:
        if fibonacci2 % 2 == 0:
            res += fibonacci2
        fibonacci_aux = fibonacci2
        fibonacci2 = fibonacci2 + fibonacci1
        fibonacci1 = fibonacci_aux
    return res


def is_simple(n):
    n = int(n)
    print(n)
    for ii in range(2, n):
        if n % ii == 0:
            return False
    return True


def largest_prime_factor(n):
    for ii in range(2, n//2):
        if n % ii == 0:
            if is_simple(n/ii):
                return n/ii


def half_prob_blue_discs(n):
    blue_step = n // (3*10**3)
    blue_prev = 0
    n_step = 1
    blue = n * 2.8 // 4
    while True:
        n += n_step
        print('n: {}'.format(n))
        while True:
            blue_prev = blue
            prob = (blue/n)*((blue-1)/(n-1))
            print('probability: {}'.format(prob))
            diff = 0.5 - prob
            if diff != 0:
                blue += math.ceil(blue_step * diff / 0.5)
            else:
                return n, blue
            if abs(blue_prev - blue) <= 1:
                break
# 707107044975
# 1000000030324 - 707106802629
# 1000000373053, 707107044975



def execute_():
    print(half_prob_blue_discs(10**12))





execute_()