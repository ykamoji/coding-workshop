dp = {}
backtrack = {}


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


def putBacktrack(i, j, value):

    if i not in backtrack.keys():
        backtrack[i] = {}

    if j not in backtrack[i].keys():
        if len(backtrack[i].keys()) == 0:
            backtrack[i] = {j: value}
        else:
            backtrack[i] = {**backtrack[i], **{j: value}}
    else:
        backtrack[i][j] = value


def getBacktrack():
    return backtrack

def getDP():
    return dp

