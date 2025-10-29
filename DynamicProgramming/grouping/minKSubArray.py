from DynamicProgramming.utils.dputil import getValue, putValue, getDP

arr = [1, 3, 2, 5, 4]
K = 3
arr_len = len(arr)

def k_partitions(index, k, usedp=False):

    if k < 0:
        return 1000

    if index == arr_len:
        if k == 0:
            return 0
        else:
            return 1000

    if usedp: getValue(index, k)

    sum = 1000
    prev_min = arr[index]
    for j in range(index + 1, arr_len + 1):
        val = k_partitions(j, k - 1)
        sum = min(sum, val + prev_min)
        prev_min = min(prev_min, arr[j - 1])

    if usedp: putValue(index, k, sum)

    return sum


print(f"Sum of minimum partitions = {k_partitions(0, K, True)}")

print(getDP())

dp = [[-1] * (K + 1) for _ in range(arr_len + 1)]


def min_k_subarray(i, k):
    if k < 0: return 1e10

    if i == -1: return 0 if k == 0 else 1e10

    if dp[i][k] != -1: return dp[i][k]

    dp[i][k] = 1e10
    sub_min = arr[i]
    for j in range(i - 1, -2, -1):  # looping backwards for -1,0,...i-1
        dp[i][k] = min(dp[i][k], sub_min + min_k_subarray(j, k - 1))
        sub_min = min(sub_min, arr[j])

    return dp[i][k]


print(min_k_subarray(arr_len - 1, K))
