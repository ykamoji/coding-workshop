from utils.dputil import getValue, putValue, getDP, printDP

paths = [
    [2, 3, 5, 1],
    [9, 1, 10, 11],
    [5, 5, -3, 2],
    [1, 11, 5, 3]
]

path_walked = []


def withRec():
    def walk(m, n, usedp=False):

        if m == len(paths[0]) or n == len(paths):
            return 0

        if usedp: getValue(m, n)

        hor, ver = walk(m + 1, n, usedp), walk(m, n + 1, usedp)

        sum = max(hor, ver) + paths[m][n]

        if usedp: putValue(m, n, sum)

        return sum

    print(f"sum = {walk(0,0, True)}")
    print(getDP())


def withIteration():

    rows = len(paths)
    cols = len(paths[0])

    def walk():
        for i in range(rows, -1, -1):
            for j in range(cols, -1, -1):
                if i == rows or j == cols:
                    putValue(i, j, 0)
                else:
                    putValue(i, j, max(getValue(i + 1, j), getValue(i, j + 1)) + paths[i][j])

    walk()
    print(f"sum = {getValue(0, 0)}")

# withRec()
withIteration()