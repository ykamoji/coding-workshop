n = 50
m = 100
k = 25

MOD = 1000000007

dp = []
for _ in range(n+1):
    dp_inside = []
    for _ in range(m+1):
        dp_inside.append([-1 for _ in range(k+1)])
    dp.append(dp_inside)


def arrayCount(index, cost, previousMax):

    if cost > k:
        return 0

    if index == n:
        if k == cost:
            return 1
        else:
            return 0

    if dp[index][previousMax][cost] != -1:
        return dp[index][previousMax][cost]

    count = 0
    for i in range(1, m+1):
        if previousMax < i:
            count = (count + arrayCount(index + 1, cost + 1, i)) % MOD
        else:
            count = (count + arrayCount(index + 1, cost, previousMax)) % MOD

    dp[index][previousMax][cost] = count

    return count


# def arrayCount_iter():
#
#     for index in range(n, -1, -1):
#         for cost in range(k, -1, -1):
#             for previousMax in range(m, -1, -1):
#                 if index == n:
#                     if k == cost:
#                         dp[index][previousMax][cost] = 1
#                     else:
#                         dp[index][previousMax][cost] = 0
#                 else:
#                     count = 0
#                     for i in range(1, m + 1):
#                         if previousMax < i or previousMax == 0:
#                             count = (count + dp[index + 1][i][cost + 1]) % MOD
#                         else:
#                             count = (count + dp[index + 1][previousMax][cost]) % MOD
#
#                     dp[index][previousMax][cost] = count
#
#     return dp[0][0][0]


totalCount = arrayCount(0, 0, 0)
# totalCount = arrayCount_iter()
print(f"Total ways to build array = {totalCount}")
