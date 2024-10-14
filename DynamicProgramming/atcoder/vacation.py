from DynamicProgramming.utils.dputil import getValue, putValue, printDP

vacation_points = [3, 1, 2]
points_len = len(vacation_points)
N = 10


def maxGains(target, current, usedp=False):

    if target >= N:
        return 0

    if usedp: getValue(-1, target)

    val = -1e10

    for i in range(points_len):
        if i != current:
            val = max(val, vacation_points[i] + maxGains(target+1, i, usedp))

    if usedp: putValue(-1, target, val)

    return val


max_gains = maxGains(0, -1, usedp=True)

printDP()
print(f"Maximum gain = {max_gains}")