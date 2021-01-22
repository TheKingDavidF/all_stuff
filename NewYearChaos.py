

def minimumBribes(q):
    n = len(q)
    counter = 0
    for ii in range(n):
        if q[ii] - (ii+1) > 2:
            print('Too chaotic')
            return
        for jj in range(max(q[ii]-2, 0), ii):
            if q[jj] > q[ii]:
                counter += 1
    print(counter)


test1 = list(map(int, '2 1 5 3 4'.rstrip().split()))
test2 = list(map(int, '2 5 1 3 4'.rstrip().split()))
test3 = list(map(int, '1 2 5 3 7 8 6 4'.rstrip().split()))

minimumBribes(test3)