dp = {}


def getValue(i, j):
    if i in dp.keys():
        if j in dp[i].keys():
            return dp[i][j]


def putValue(i, j, value):
    if i not in dp.keys():
        dp[i] = {}

    if j not in dp[i].keys():
        if len(dp[i].keys()) == 0:
            dp[i] = {j: value}
        else:
            dp[i] = {**dp[i], **{j: value}}
    else:
        dp[i][j] = value


def getDP():
    return dp
