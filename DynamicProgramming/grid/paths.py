from DynamicProgramming.utils.dputil import getValue, putValue, getDP

grid = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 0, 0],
]


def paths(i, j, k, usedp=False):

    if i == len(grid) - 1 and j == len(grid[0]) - 1:

        if k < 0:
            return 0
        else:
            return 1

    if i > len(grid) - 1 or j > len(grid[0]) - 1:
        return 0

    if usedp: getValue(i, j)

    if grid[i][j] != 1:
        count = paths(i + 1, j, k, usedp) + paths(i, j + 1, k, usedp)
    else:
        count = paths(i + 1, j, k - 1, usedp) + paths(i, j + 1, k - 1, usedp)

    if usedp: putValue(i, j, count)

    return count

count = paths(0,0, 2, usedp=True)

print(f"Total number of paths = {count}")
print(f"DP = {getDP()}")