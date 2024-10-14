import math
from DynamicProgramming.utils.dputil import getValue, putValue, getDP

points = [
    (76, 24),
    (24, 52),
    (67, 72),
    (36, 67),
    (24, 63)
]

len_p = len(points)


def cost(p1, p2):
    dist = ((points[p1-1][0] - points[p2-1][0]) ** 2 + (points[p1-1][1] - points[p2-1][1]) ** 2) ** 0.5
    return math.sin(dist)


def triangulation():

    for i in range(3, len_p+1):
        for start in range(1, len_p - i + 2):
            end = start + i - 1
            if i == 3:
                putValue(start, end, 0)
            else:
                ans = 1e9
                for k in range(start + 1, end):
                    if k == start + 1:
                        ans = min(ans, cost(start + 1, end) + getValue(start + 1, end))
                    elif k == end - 1:
                        ans = min(ans, cost(start, end-1) + getValue(start, end-1))
                    else:
                        ans = min(ans, cost(start, k) + cost(k, end) + getValue(start, k) + getValue(k, end))

                putValue(start, end, ans)


triangulation()

# printDP()

print(f"Minimum cost = {getDP()[1][len_p]} ")
