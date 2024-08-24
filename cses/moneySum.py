from utils.dputil import getValue, putValue, printDP, getDP

arr = [4, 2, 5, 2]
arr_len = len(arr)
max_sum = sum(arr)


def checkIfSumPossible(level, target, usedp=False):

    if target == 0:
        return True
    elif target < 0:
        return False

    if level == arr_len:
        return False

    if usedp: getValue(level, target)

    ans = checkIfSumPossible(level + 1, target, usedp) or checkIfSumPossible(level + 1, target - arr[level], usedp)

    if usedp: putValue(level, target, ans)

    return ans


possible_sums = []
count = 0
for s in range(1, max_sum+1):
    if checkIfSumPossible(0, s, usedp=True):
        possible_sums.append(s)
        count += 1

# printDP()
print(f"Total possible sum values = {count}")
print(f"{possible_sums}")



