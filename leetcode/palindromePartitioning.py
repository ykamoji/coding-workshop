s = "aabbc"
K = 3
arr = list(s)
arr_len = len(s)


dp = []
for _ in range(arr_len+1):
    dp.append([-1 for _ in range(K+1)])

palinCheck = []
for _ in range(arr_len+1):
    palinCheck.append([-1 for _ in range(arr_len+1)])


def getMinimumPalinChange(l, r):
    if l >= r: return 0
    if palinCheck[l][r] != -1: return palinCheck[l][r]
    if arr[l] == arr[r]:
        val = getMinimumPalinChange(l+1, r-1)
    else:
        val = 1 + getMinimumPalinChange(l+1, r-1)
    palinCheck[l][r] = val
    return val


def palindromePartition(index, k):

    if k == 0:
        return getMinimumPalinChange(index, arr_len - 1)

    if index == arr_len:
        return 0

    if dp[index][k] != -1:
        return dp[index][k]

    count = arr_len
    for i in range(index, arr_len-1):
        count = min(count, getMinimumPalinChange(index, i) + palindromePartition(i + 1, k - 1))

    dp[index][k] = count

    return count


minimumCount = palindromePartition(0, K - 1)

print(f"Minimum Count = {minimumCount}")






