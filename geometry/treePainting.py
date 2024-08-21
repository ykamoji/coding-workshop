from utils.dputil import getValue, putValue, printDP, getBacktrack, putBacktrack

# trees = [
#     [1, 2],
#     [2, 3]
# ]
# N = 3

# trees = [
#     [1, 2],
#     [1, 3],
#     [1, 4]
# ]
# N = 4

trees = [
    [8, 5],
    [10, 8],
    [6, 5],
    [1, 5],
    [4, 8],
    [2, 10],
    [3, 6],
    [9, 2],
    [1, 7]
]
N = 10

edges = len(trees)
painted = [0] * N

treeMap = {}
keys = set()
for e in trees:
    if e[0] in keys:
        treeMap[e[0]] = treeMap[e[0]] + [e[1]]
    else:
        keys.add(e[0])
        treeMap[e[0]] = [e[1]]

    if e[1] in keys:
        treeMap[e[1]] = treeMap[e[1]] + [e[0]]
    else:
        keys.add(e[1])
        treeMap[e[1]] = [e[0]]


def paintDistribution(level, last, usedp=False):

    # if usedp: getValue(level, last)

    putValue(level, 0, 1)
    putValue(level, 1, 1)
    for vertex in treeMap[level]:
        if last != vertex:
            paintDistribution(vertex, level, usedp)
            putValue(level, 0, getValue(level, 0) * (getValue(vertex, 0) + getValue(vertex, 1)))
            putValue(level, 1, getValue(level, 1) * getValue(vertex, 0))

    # if usedp: putValue(level, last, count)


paintDistribution(1, 0, usedp=True)
printDP()
count = getValue(1, 0) + getValue(1, 1)
print(f"Total number of ways to print = {count}")