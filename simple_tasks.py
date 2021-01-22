from random import randint

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

rand_list = [randint(-1000, 1000) for _ in range(randint(10, 1000))]
# result = find_sum_of_two([-2, -1, 2, 0, 3, 5, 6,6,6,7, 10, 9, 13, 14], 9)
result = mergeSort(rand_list)
print(result)