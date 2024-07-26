from utils.dputil import getValue, putValue, printDP, putBacktrack, getBacktrack

str1 = "AGGTAB"
str2 = "GXTXATB"
## GTAB

arr_1 = list(str1)
arr_2 = list(str2)


def lcs(i, j, usedp=False):

    if i >= len(arr_1) or j >= len(arr_2):
        return 0

    if usedp: getValue(i, j)

    i_inc = lcs(i + 1, j, usedp)
    j_inc = lcs(i, j + 1, usedp)

    if i_inc > j_inc:
        ans = i_inc
        putBacktrack(i, j, 0)
    else:
        ans = j_inc
        putBacktrack(i, j, 1)

    if arr_1[i] == arr_2[j]:
        temp = 1 + lcs(i + 1, j + 1, usedp)
        if temp > ans:
            ans = temp
            putBacktrack(i, j, 2)

    if usedp: putValue(i, j, ans)

    return ans


count = lcs(0,0, usedp=True)

print(f"DP:")
printDP()

print(f"Longest common subsequence count = {count}")

# remaining = count
# sequence = ""
# while remaining > 0:
#     for i in range(len(arr_1)-1, -1, -1):
#         if remaining in dp[i].values():
#             sequence += arr_1[i]
#             remaining -= 1
#             break


sequence = []

def generate(i, j):
    if i == len(arr_1) and j == len(arr_2):
        return

    choice = getBacktrack()[i][j]
    if choice == 0 :
        generate(i + 1, j)
    elif choice == 1:
        generate(i, j + 1)
    else:
        sequence.append(str1[i])
        generate(i + 1, j + 1)


generate(0,0)

print(f"Longest common subsequence = {''.join(sequence)}")


