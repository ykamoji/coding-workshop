n = 6
v = [6, 2, 3, 5, 1, 4]
w = [3, 24, 245, 84, 45, 57]
W = 200

dp = {}


def knapsack(index, weight, usedp=False):
    if index == n:
        return 0

    if usedp:
        if index in dp.keys():
            if weight in dp[index].keys():
                return dp[index][weight]

    ans = knapsack(index + 1, weight)

    if w[index] <= weight:
        ans = max(ans, knapsack(index + 1, weight - w[index]) + v[index])

    if usedp:
        if index not in dp.keys():
            dp[index] = {}

        if weight not in dp[index].keys():
            if len(dp[index].keys()) == 0:
                dp[index] = {weight: ans}
            else:
                dp[index] = {**dp[index], **{weight: ans}}

    return ans


print(f"Maximum value = {knapsack(0, W, True)}")
