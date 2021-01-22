

def surfaceArea(A):
    area = 0
    for ii in range(len(A)):
        for jj in range(len(A[ii])):
            area += 1 + 1 + 4 * A[ii][jj]
            if jj > 0:
                area -= 2 * min(A[ii][jj], A[ii][jj-1])
            if ii > 0:
                area -= 2 * min(A[ii][jj], A[ii-1][jj])
    return area



A1 = [[1]]
A2 =[[1, 3, 4], [2, 2, 3], [1, 2, 4]]

print(surfaceArea(A2))