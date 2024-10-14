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