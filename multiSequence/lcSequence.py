from utils.dputil import getValue, putValue, getDP

str1 = "AGGTAB"
str2 = "GXTXATB"
## GTAB

arr_1 = list(str1)
arr_2 = list(str2)


def lcs(i, j, usedp=False):

    if i >= len(arr_1) or j >= len(arr_2):
        return 0

    if usedp: getValue(i, j)

    ans = max(lcs(i + 1, j, usedp), lcs(i, j + 1, usedp))

    if arr_1[i] == arr_2[j]:
        ans = max(ans, 1 + lcs(i + 1, j + 1, usedp))

    if usedp: putValue(i, j, ans)

    return ans


count = lcs(0,0, usedp=True)

print(f"DP:")
dp = getDP()
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


