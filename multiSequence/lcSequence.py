str1 = "AGGTAB"
str2 = "GXTXATB"
## GTAB

arr_1 = list(str1)
arr_2 = list(str2)

dp = {}


def lcs(i, j, usedp=False):

    if i >= len(arr_1) or j >= len(arr_2):
        return 0

    if usedp:
        if i in dp.keys():
            if j in dp[i].keys():
                return dp[i][j]

    ans = max(lcs(i + 1, j, usedp), lcs(i, j + 1, usedp))

    if arr_1[i] == arr_2[j]:
        ans = max(ans, 1 + lcs(i + 1, j + 1, usedp))

    if usedp:
        if i not in dp.keys():
            dp[i] = {}

        if j not in dp[i].keys():
            if len(dp[i].keys()) == 0:
                dp[i] = {j: ans}
            else:
                dp[i] = {**dp[i], **{j: ans}}

    return ans


count = lcs(0,0, usedp=True)

print(f"DP:")
for i in dp.keys():
    for j in dp[i].keys():
        print(f"i={i}, j={j}: {dp[i][j]}")

print(f"Longest common subsequence count = {count}")

remaining = count
sequence = ""
while remaining > 0:
    for i in range(len(arr_1)-1, -1, -1):
        if remaining in dp[i].values():
            sequence += arr_1[i]
            remaining -= 1
            break

print(f"Longest common subsequence = {sequence}")


