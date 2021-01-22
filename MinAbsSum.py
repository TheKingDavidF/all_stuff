from random import randint
from datetime import datetime

def rand_list():
    N = randint(0,20000)
    res_list = []
    for n in range(N):
        res_list.append(randint(-100,100))
    return res_list

def solution(A):
    n = len(A)
    Apos = [abs(A[ii]) for ii in range(n)]
    k = sum(Apos)//2
    M = [0]
    for a in Apos:
        M.extend([m + a for m in M])
    M = sorted(M)
    if sum(Apos) % 2 == 0:
        ii = 0
        while M[ii] < k:
            ii += 1
        print('even sum: ii = {}; k = {} ; lowlim = {}; uplim = {}\n and M: {}'.format(ii, k, M[ii], M[ii+1], M))
        lowlim = M[ii - 1]
        uplim = M[ii]
        return min(abs(lowlim - k), abs(uplim - k))*2
    elif sum(Apos) % 2 == 1:
        ii = 0
        while M[ii] < k:
            ii += 1
        print('odd sum: ii = {}; k = {} ; lowlim = {}; uplim = {}\n and M: {}'.format(ii, k, M[ii-1], M[ii], M))
        lowlim = M[ii - 1]
        uplim = M[ii]
        return min(abs(lowlim - k), abs(uplim - k))*2+1


start_time = datetime.now()


A = rand_list()
A = [1, 5, -2, 5, 2, 3, 1, 2, 2, 2, 2, 2, 2]
res_comp_new = solution(A)
print(res_comp_new)
print(datetime.now() - start_time)
# [S, counter] = solution(A)
# print('S: '+ str(S))
# print('result sum: ' + str(abs(sum(a*s for a,s in zip(A,S)))))
# print('amount of steps: ' + str(counter))