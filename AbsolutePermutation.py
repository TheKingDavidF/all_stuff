

def is_abs_permutation(list_, k):
    end = len(list_) - 1
    diff = list_[0] - 1
    for ii in range(len(list_)):
        if abs(list_[end - ii] - (end - ii + 1)) != k:
            return False
    return True

def create_abs_permutation(n, k):
    if k == 0:
        return list(range(1, n+1))
    perm = []
    for ii in range(1, n+1):
        diff1 = k + ii
        diff2 = ii - k
        if 0 < diff2 < n + 1 and diff2 not in perm:
            perm.append(diff2)
        elif 0 < diff1 < n + 1 and diff1 not in perm:
            perm.append(diff1)
        else:
            return -1
    return perm

def absolutePermutation(n, k):
    if k ==0:
    #When k=0 we just have to print 1 to n
        return list(range(1,n+1))
    elif (n / k) % 2 != 0.0:
    #pattern is not possible when k*2 is not divisible by n
        return -1
    else:
    #initialize an empty list
        arr = []
        #create a for loop with k*2 difference, example when k=3 --> 1,7,13,19,25....
        for i in range(1, n, k*2):
        #numbers from i to i+k*2 example when k=3 and i = 1 --> [1,2,3,4,5,6]
            d = list(range(i, i + k*2))
            #Slice and interchange left and right part, example [1,2,3,4,5,6] --> [4,5,6,1,2,3]
            arr += d[k:]+d[:k]
        return list(arr)



print(create_abs_permutation(3, 2))