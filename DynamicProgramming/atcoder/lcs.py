def lcs(i, j, n, m, s, t, dp):

    if i >= n or j >= m:
        return 0

    if dp[i][j] != -1: return dp[i][j]

    dp[i][j] = 0
    if i + 1 < n:
        dp[i][j] = max(dp[i][j], lcs(i + 1, j, n, m, s, t, dp))

    if j + 1 < m:
        dp[i][j] = max(dp[i][j], lcs(i, j + 1, n, m, s, t, dp))

    if s[i] == t[j]:
        dp[i][j] = max(dp[i][j], 1 + lcs(i + 1, j + 1, n, m, s, t, dp))

    return dp[i][j]


def lcs2(s, t):
    n = len(s)
    m = len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]
    backtrack = [[-1] * (m+1) for _ in range(n+1)]
    for i in reversed(range(n)):
        for j in reversed(range(m)):
            x_inc = dp[i+1][j]
            y_inc = dp[i][j + 1]
            if x_inc > y_inc:
                dp[i][j] = x_inc
                backtrack[i][j] = 0
            else:
                dp[i][j] = y_inc
                backtrack[i][j] = 1

            if s[i] == t[j]:
                x_y_inc = 1 + dp[i+1][j + 1]
                if x_y_inc > dp[i][j]:
                    dp[i][j] = x_y_inc
                    backtrack[i][j] = 2

    return dp[0][0], backtrack


def generate(s, t, backtrack):
    i, j = 0, 0
    n = len(s)
    m = len(t)
    lcs_str = ""
    while i < n and j < m:
        if backtrack[i][j] == 0:
            i += 1
        elif backtrack[i][j] == 1:
            j += 1
        elif backtrack[i][j] == 2:
            lcs_str += s[i]
            i += 1
            j += 1

    return lcs_str


def main():
    s, t = input(), input()
    # n = len(s)
    # m = len(t)
    # dp = [[-1]*m for _ in range(n)]
    # print(lcs(0, 0, n, m, s, t, dp))

    count, backtrack = lcs2(s, t)
    # print(count)
    print(generate(s, t, backtrack))



if __name__ == '__main__':
    main()