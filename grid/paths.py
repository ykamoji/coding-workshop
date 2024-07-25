grid = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0],
]

dp = {}


def paths(i, j, k, usedp=False):

    if i == len(grid) - 1 and j == len(grid[0]) - 1:

        if k < 0:
            return 0
        else:
            return 1

    if i > len(grid) - 1 or j > len(grid[0]) - 1:
        return 0

    if usedp:
        if i in dp.keys():
            if j in dp[i].keys():
                return dp[i][j]

    if grid[i][j] != 1:
        count = paths(i + 1, j, k, usedp) + paths(i, j + 1, k, usedp)
    else:
        count = paths(i + 1, j, k - 1, usedp) + paths(i, j + 1, k - 1, usedp)

    if usedp:
        if i not in dp.keys():
            dp[i] = {}

        if j not in dp[i].keys():
            if len(dp[i].keys()) == 0:
                dp[i] = {j: count}
            else:
                dp[i] = {**dp[i], **{j: count}}

    return count

count = paths(0,0, 1, usedp=True)

print(f"Total number of paths = {count}")
print(f"DP = {dp}")