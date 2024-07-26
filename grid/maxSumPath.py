from utils.dputil import getValue, putValue, getDP

paths = [
    [2, 3, 5, 1],
    [9, 1, 10, 11],
    [5, 5, -3, 2],
    [1, 11, 5, 3]
]

path_walked = []

def walk(m, n, usedp=False):

    if m == len(paths[0]) or n == len(paths):
        return 0

    if usedp: getValue(m, n)

    hor, ver = walk(m + 1, n), walk(m, n + 1)

    sum = max(hor, ver) + paths[m][n]

    if usedp: putValue(m, n, sum)

    return sum


print(f"sum = {walk(0,0, True)}")
print(getDP())