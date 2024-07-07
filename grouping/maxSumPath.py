paths = [
    [2, 3, 5, 1],
    [9, 1, 10, 11],
    [5, 5, -3, 2],
    [1, 11, 5, 3]
]

path_walked = []
dp = {}

def walk(m, n, usedp=False):

    if m == len(paths[0]) or n == len(paths):
        return 0

    if usedp:
        if m in dp.keys():
            if n in dp[m].keys():
                return dp[m][n]

    hor, ver = walk(m + 1, n), walk(m, n + 1)

    sum = max(hor, ver) + paths[m][n]

    if usedp:
        if m not in dp.keys():
            dp[m] = {}

        if n not in dp[m].keys():
            if len(dp[m].keys()) == 0:
                dp[m] = {n: sum}
            else:
                dp[m] = {**dp[m], **{n: sum}}

    return sum


print(f"sum = {walk(0,0, True)}")
print(dp)