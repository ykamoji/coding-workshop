from  import getDP, getValue, putValue

str1 = "AATU"
str2 = "ATUA"
arr_1 = list(str1)
arr_2 = list(str2)

backtrack = {}


def diff(i, j, usedp=False):

    if i == len(arr_1) and j == len(arr_2) :
        return 0

    if usedp: return getValue(i,j)

    count = 1e9

    if i < len(arr_1):
        temp = 1 + diff(i + 1, j, usedp)
        if temp < count:
            count = temp
            add_kv(i, j,0)

    if j < len(arr_2):
        temp = 1 + diff(i, j + 1, usedp)
        if temp < count:
            count = temp
            add_kv(i, j,1)

    if i < len(arr_1) and j < len(arr_2) and arr_1[i] == arr_2[j]:
        temp = 1 + diff(i + 1, j + 1, usedp)
        if temp < count:
            count = temp
            add_kv(i, j,2)

    if usedp: putValue(i, j, count)

    return count


def add_kv(i, j, value):

    if i not in backtrack.keys():
        backtrack[i] = {}

    if j not in backtrack[i].keys():
        if len(backtrack[i].keys()) == 0:
            backtrack[i] = {j: value}
        else:
            backtrack[i] = {**backtrack[i], **{j: value}}
    else:
        backtrack[i][j] = value

count = diff(0,0, usedp=True)

print(f"Diff Utility count = {count}")

print(f"DP = {getDP()}")
# for i in dp.keys():
#     for j in dp[i].keys():
#         print(f"i={i}, j={j}: {dp[i][j]}")

print(f"Backtrack = {backtrack}")


def generate(i, j):

    if i == len(arr_1) and j == len(arr_2):
        return

    choice = backtrack[i][j]

    if choice == 0:
        print(f'-{arr_1[i]}',end=' ')
        generate(i + 1, j)
    elif choice == 1:
        print(f'+{arr_2[j]}', end=' ')
        generate(i, j + 1)
    else:
        print(f'{arr_1[i]}', end=' ')
        generate(i + 1, j + 1)

generate(0,0)
print()