from utils.dputil import getValue, putValue, printDP, getBacktrack, putBacktrack

# points = [
#     (1,2), (1,3), (3,2), (2,4), (3,4)
# ]
# vertices = 4
# edges = 5

# points = [
#     (2,3), (4, 5), (5,6)
# ]
# vertices = 6
# edges = 3

points = [
    (5, 3), (2, 3), (2, 4), (5, 2), (5, 1), (1, 4), (4, 3), (1, 3)
]
vertices = 5
edges = 8


def withoutOptimization():

    def directedPath(level, current, usedp=False):

        if level >= edges:
            return 0

        if usedp: getValue(level, current)

        count = 0
        end = True
        for e in range(edges):
            if e != current and points[current][1] == points[e][0]:
                end = False
                putBacktrack(level, e, 0)
                temp = 1 + directedPath(level + 1, e, usedp)
                if temp > count:
                    count = temp
                    for item in getBacktrack()[level]:
                        putBacktrack(level, item, 0)
                    putBacktrack(level, e, 1)

        if end: count = 1

        if usedp: putValue(level, current, count)

        return count

    def get_path(starting):
        path = ""
        last = points[starting][1]
        if getBacktrack().keys():
            path = f"{points[starting]}"
            for level in range(max(getBacktrack().keys())+1):
                for k, v in getBacktrack()[level].items():
                    if v == 1 and last == points[k][0]:
                        last = points[k][1]
                        path += f" -> {points[k]}"
                        continue
        return path

    max_count = 0
    best_path = ""
    for i in range(edges):
        count = directedPath(0, i, usedp=True)
        path = get_path(i)
        if count > max_count:
            max_count = count
            best_path = path
            # print(i, getBacktrack())
        getBacktrack().clear()

    print(f"Max length = {max_count}")
    print(f"{best_path}")


def withOptimization():

    dag = {}
    keys = set()
    for point in points:
        if point[0] in keys:
            updated = dag[point[0]] + [point[1]]
            dag[point[0]] = updated
        else:
            dag[point[0]] = [point[1]]
            keys.add(point[0])

    def directedPath(level, usedp=True):

        if usedp: getValue(-1, level)

        count = 0
        if level in dag.keys():
            for vertex in dag[level]:
                count = max(count, 1 + directedPath(vertex, usedp))

        if usedp: putValue(-1, level, count)

        return count

    count = 0
    for i in range(1, vertices+1):
        count = max(count, directedPath(i, usedp=True))

    print(f"Max length = {count}")


withoutOptimization()
withOptimization()