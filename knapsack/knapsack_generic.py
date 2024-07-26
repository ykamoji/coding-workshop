from utils.dputil import getValue, putValue, getDP

n = 6
v = [6, 2, 3, 5, 1, 4]
w = [3, 24, 245, 84, 45, 57]
W = 200


def knapsack(index, weight, usedp=False):
    if index == n:
        return 0

    if usedp: getValue(index, weight)

    ans = knapsack(index + 1, weight, usedp)

    if w[index] <= weight:
        ans = max(ans, knapsack(index + 1, weight - w[index]) + v[index], usedp)

    if usedp: putValue(index, weight, ans)

    return ans


print(f"Maximum value = {knapsack(0, W, True)}")
