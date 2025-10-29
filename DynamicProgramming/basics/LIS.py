arr = [2, 1, 5, 3, 6]
n = len(arr)
dp = [-1]* (n+1)


def LIS(i):
    if i < 0: return 0

    if dp[i] != -1: return dp[i]

    dp[i] = 1
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], LIS(j) + 1)

    return dp[i]

best = 0
for i in range(n):
    best = max(best, LIS(i))

print(best)