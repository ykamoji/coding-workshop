from utils.dputil import getValue, putValue, getDP

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


def maxArea(i, j, usedp=False):

    if i >= len(grid) or j >= len(grid[0]):
        return 0

    if i < 0 or j < 0:
        return 0

    if usedp: getValue(i, j)

    area = 1 + min(min(maxArea(i - 1, j, usedp), maxArea(i, j - 1, usedp)), maxArea(i - 1, j - 1, usedp))
    if grid[i][j] != 1:
        area = 0

    if usedp: putValue(i, j, area)

    return area


for row in grid:
    print(" ".join([str(item) for item in row]))

maxArea(len(grid) - 1, len(grid[0]) - 1, usedp=True)**2

max_area = 0
dp = getDP()
for i in dp.keys():
    max_area = max(max_area, max(dp[i].values()))

print(f"DP = {dp}")

print(f"Maximum Area = {max_area**2}")

