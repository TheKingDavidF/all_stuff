import math


def define_bounds(l):
    sqrt = math.sqrt(l)
    lower_bound = math.floor(sqrt)
    if lower_bound == sqrt:
        upper_bound = lower_bound
    else:
        upper_bound = lower_bound + 1
    if lower_bound * upper_bound < l:
        lower_bound += 1
    return lower_bound, upper_bound

def encryption(s):
    l = len(s)
    lb, ub = define_bounds(l)
    matrix = []
    for ii in range(math.ceil(l/lb)):
        matrix.append(s[ii * ub: (ii+1) * ub])

    for ii in range(1,3):
        if len(matrix[-ii]) < ub:
            matrix[-ii] = matrix[-ii] + ' '*(ub - len(matrix[-ii]))
    res = ''
    for ii in range(ub):
        for jj in range(lb):
            if matrix[jj][ii] != ' ':
                res = res + matrix[jj][ii]
        res = res + ' '
    return res.strip()

# feedthedog
# haveaniceday
# chillout
s = 'haveaniceday'
print(encryption(s))

