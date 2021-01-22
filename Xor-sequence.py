# if ii % 4 == 0:
#     element = ii
# elif ii % 4 == 1:
#     element = 1
# elif ii % 4 == 2:
#     element = ii + 1
# elif ii % 4 == 3:
#     element = 0

def xor_sum(n):
    # XOR sum is periodic
    # print the first 30 or so XOR sums (e.g. A[1]...A[30])
    # and you'll notice the pattern below
    # which is periodic with period 8
    m = n % 8
    if m == 3 or m == 4:
        return 2
    if m == 7 or m == 0:
        return 0
    if m == 1 or m == 2:
        return n - 1
    if m == 5 or m == 6:
        return n + 1


def xorSequence(l, r):
    # key idea is to notice that
    # 1) x XOR x = 0s
    # 2) 0s XOR x = x
    # 3) x XOR y = y XOR x

    # with these relations it's straightforward to show that
    # XOR_SUM = A[L] XOR ... XOR A[R] = A[R] XOR A[L-1]

    # finally, make sure you index correctly with l and r
    # for example, to be r inclusive, you need to index r+1

    # solution is O(r-l) time and O(1) space
    return xor_sum(r + 1) ^ xor_sum(l)
xorSequence(1, 16)