from DynamicProgramming.utils.dputil import getValue, putValue, printDP
paths = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]


def walk(m, n, usedp=False):

    if m == len(paths[0]) - 1 and n == len(paths) - 1:
        return paths[m][n]

    if m > len(paths[0]) - 1 or n > len(paths) - 1:
        return 1e10

    if usedp: getValue(m, n)

    hor, ver = walk(m + 1, n, usedp), walk(m, n + 1, usedp)

    sum = min(hor, ver) + paths[m][n]

    if usedp: putValue(m, n, sum)

    return sum


print(f"sum = {walk(0, 0, True)}")
printDP()