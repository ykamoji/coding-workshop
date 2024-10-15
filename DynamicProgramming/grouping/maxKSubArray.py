arr = [1,15,7,9,2,5,10]
K  = 3
arr_len = len(arr)
dp = {}


def maxSum(index):
    if index >= arr_len:
        return 0

    if index in dp:
        return dp[index]

    mxSum = 0
    currentMax = 0
    for i in range(index, min(index + K, arr_len)):
        currentMax = max(currentMax, arr[i])
        mxSum = max(mxSum, currentMax * (i - index + 1) + maxSum(i + 1))

    dp[index] = mxSum

    return mxSum

maxVal = maxSum(0)
print(f"Maximum value = {maxVal}")
