
def candies(n, arr):
    candies = [1]*n
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            candies[i+1] = candies[i]+1
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i] and candies[i-1] <= candies[i]:
            candies[i-1] = candies[i]+1
    return sum(candies)


test1 = [1, 2, 2]
ans1 = [1, 2, 1]

test2 = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]
ans2 = [1, 2, 1, 2, 1, 2, 3, 4, 2, 1]

print('input: {}, correct answer: {}, my answer: {}'.format(test2, ans2, candies(len(test2), test2)))