grid = [
    [1, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 0],
    [1, 0, 1, 1],
]

# grid = [
#     [0,0],
#     [0,0]
# ]

# grid = [
#     [0, 1, 1],
#     [0, 0, 1]
# ]

# grid = [
#     [1, 0, 1],
#     [1, 1, 0],
#     [1, 1, 1]
# ]

dp = {}

def maxArea(i, j, usedp=False):

    if i >= len(grid) or j >= len(grid[0]):
        return 0

    if i < 0 or j < 0:
        return 0

    if usedp:
        if i in dp.keys():
            if j in dp[i].keys():
                return dp[i][j]

    area = 0

    if grid[i][j] == 1:
        area = 1 + min(min(maxArea(i - 1, j, usedp), maxArea(i, j - 1, usedp)), maxArea(i - 1, j - 1, usedp))

    if usedp:
        if i not in dp.keys():
            dp[i] = {}

        if j not in dp[i].keys():
            if len(dp[i].keys()) == 0:
                dp[i] = {j: area}
            else:
                dp[i] = {**dp[i], **{j: area}}

    return area


for row in grid:
    print(" ".join([str(item) for item in row]))

maxArea(len(grid) - 1, len(grid[0]) - 1, usedp=True)**2

max_area = 0
for i in dp.keys():
    max_area = max(max_area, max(dp[i].values()))

print(f"DP = {dp}")

print(f"Maximum Area = {max_area**2}")

