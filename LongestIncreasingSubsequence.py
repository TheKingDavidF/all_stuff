def longestIncreasingSubsequence_O2(arr):
    n = len(arr)
    dp = [1] * n
    for ii in range(n):
        for jj in range(ii):
            if arr[ii] > arr[jj]:
                if dp[ii] <= dp[jj]:
                    dp[ii] = dp[jj] + 1
    return max(dp)


test_set = []
with open('/Users/davidfinkelstejn/Desktop/testLIS.txt') as file:
    for num in file:
        test_set.append(int(num))


result = longestIncreasingSubsequence_O2(test_set)

print('True result = 195, my result = {}'.format(result))