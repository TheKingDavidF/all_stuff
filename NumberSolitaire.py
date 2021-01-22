from random import randint
import math

def input_args():
    n = randint(2, 100)
    A = [randint(-10000,10000) for ii in range(n)]
    return A


def division_by_sign(A):
    n = len(A)
    res_set = []
    aux_set = []
    count = 0
    for ii in range(n):
        if A[ii] > 0:
            count += A[ii]
            if aux_set:
                res_set.append(aux_set)
                aux_set = []
        else:
            aux_set.append(A[ii])
    if aux_set:
        res_set.append(aux_set)
    return count, res_set


def solution(S):
    s0 = S.pop(0)
    n = len(S)
    M = []
    M.append(S[0])
    for ii in range(1, n):
        m_aux = []
        for jj in range(1, 7):
            if ii - jj < -1:
                m_aux.append(-math.inf)
            elif ii - jj == -1:
                m_aux.append(S[ii])
            else:
                m_aux.append(M[ii-jj]+S[ii])
        M.append(max(m_aux))
    return M[-1] + s0



S = input_args()
# S = [931, 6388, 539, -5226, 998, -2711, 3639, -9517, -6939]
print('full set: {}'.format(S))
res = solution(S)
print('answer, calcultate by programm: {}'.format(res))

# count, res_set = division_by_sign(A)
# print('A: '+ str(A))
# print(count)
# print('res_set: '+ str(res_set))