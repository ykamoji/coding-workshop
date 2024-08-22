from utils.dputil import getValue, putValue, printDP

arr = [4, 6, 2, 8]
arr_len = len(arr)

total_sum = sum(arr)


def possibleGroups(level, sumA, group=None, usedp=False):

    if group is None:
        group = []

    if level == arr_len:
        if sumA != total_sum and sumA != 0 and sumA % (total_sum - sumA) == 0:
            print(f"{group}\t{[item for item in arr if item not in group]}")
            return 1
        else:
            return 0

    if usedp: getValue(level, sumA)

    count = possibleGroups(level + 1, sumA + arr[level], group+[arr[level]], usedp) \
            + possibleGroups(level + 1, sumA, group, usedp)

    if usedp: putValue(level, sumA, count)

    return count


count = possibleGroups(0, 0, usedp=True)
# printDP()
print(f"Total number of ways to create 2 groups = {count}")