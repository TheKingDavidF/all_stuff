from random import randint, choice
import string

# https://codeburst.io/100-coding-interview-questions-for-programmers-b1cf74885fb7

def find_sum_of_two(array_, a):
    n = len(array_)
    array_ = sorted(array_)
    ii = 0
    jj = n-1
    res = []
    while ii < jj:
        aux  = array_[ii] + array_[jj]
        if aux == a:
            res.append((array_[ii], array_[jj]))
            ii += 1
            jj -= 1
        else:
            if aux < a:
                ii += 1
            else:
                jj -= 1
    return res

def bubble_sort(L):
    n = len(L)
    for ii in range(n):
        for jj in range(n-ii-1):
            if L[jj] > L[jj+1]:
                L[jj], L[jj+1] = L[jj+1], L[jj]
    return L

def mergeSort(L):
    if len(L)>1:
        mid = len(L)//2
        lefthalf = L[:mid]
        righthalf = L[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                L[k]=lefthalf[i]
                i=i+1
            else:
                L[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            L[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            L[k]=righthalf[j]
            j=j+1
            k=k+1
    return L

def charCount(str_, char_):
    count = 0
    for char_aux in str_:
        if char_aux == char_:
            count += 1
    return count

# rand_list = [randint(-1000, 1000) for _ in range(randint(10, 1000))]
N = randint(1, 100000)
str_ = ''.join(choice(string.ascii_uppercase) for _ in range(N))
char_ = choice(string.ascii_uppercase)
result = charCount(str_, char_)
print(result)