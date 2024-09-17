dungeon = [[5,23,-48,-21,-72,-62,-19,-55,-3,-93,-84,14,-34,46,-82,-46,39,26,47,-71,-46,-3,-59,-93,-13,-72,19,-43,-51,-2,-6,-53,12,-40,15,-94,37,-3,-32,-97]]

m, n = len(dungeon), len(dungeon[0])

dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]


def minPath():
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if i == m - 1 and j == n - 1:
                dp[i][j] = 1 + max(0, - dungeon[i][j])
            else:
                val_h = 1e10 if i + 1 > m - 1 else dp[i + 1][j]
                val_v = 1e10 if j + 1 > n - 1 else dp[i][j + 1]
                dp[i][j] = max(1, - dungeon[i][j] + min(val_h, val_v))

    return dp[0][0]


minimum_health = minPath()

print(f"Minimum Health: {minimum_health}")

