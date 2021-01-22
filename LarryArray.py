
def larrysArray(A):
    n = len(A)
    inv_count = 0
    for ii in range(n):
        for jj in range(ii + 1, n):
            if A[jj] < A[ii]:
                inv_count += 1

    if inv_count % 2 == 0:
        return 'YES'
    else:
        return 'NO'




