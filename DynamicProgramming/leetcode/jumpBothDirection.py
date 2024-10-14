import time
arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2

arr_len = len(arr)

dp = [-1 for _ in range(arr_len+1)]


def maxNumJumps(index):

    if index < 0 or index >= arr_len:
        return 0

    if dp[index] != -1:
        return dp[index]

    count = 1
    for i in range(index - 1, max(index - d - 1, -1), -1):
        if arr[i] < arr[index]:
            count = max(count, maxNumJumps(i) + 1)
        else:
            break

    for i in range(index + 1, min(index + d + 1, arr_len)):
        if arr[i] < arr[index]:
            count = max(count, maxNumJumps(i) + 1)
        else:
            break

    dp[index] = count

    return count


st = time.time()
maxJumps = 0
for i in range(arr_len):
    maxJumps = max(maxJumps, maxNumJumps(i))
diff = (time.time() - st) * 1000
print(f"Maximum number of jumps = {maxJumps} ({diff:0.3f} ms)")
