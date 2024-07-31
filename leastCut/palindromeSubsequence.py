from utils.dputil import putValue, getValue, putBacktrack, getBacktrack

st = "ABACACADACA"
arr = list(st)


def check(l, r, usedp):
    if l >= r: return True
    if usedp: getValue(l, r)
    val = arr[l-1] == arr[r-1] and check(l+1, r-1, usedp)
    if usedp: putValue(l, r, val)
    return val


def palindromeSequence(i, usedp=False):

    if i == 0:
        return -1

    if usedp: getValue(i, -1)

    ans = 1e9
    for j in range(i):
        if check(j+1, i, usedp):
            temp = 1 + palindromeSequence(j, usedp)
            putBacktrack(j, i - 1, 0)
            if temp < ans:
                ans = temp
                putBacktrack(j, i - 1, 1)

    if usedp: putValue(i, -1, ans)

    return ans


count = palindromeSequence(len(arr), usedp=True)

print(f"Minimum number of cuts with palindrome sequences = {count}")

cut_string = []
running_index = len(arr) - 1
while running_index >= 0:
    for i, v in getBacktrack().items():
        for j, v in getBacktrack()[i].items():
            if v == 1 and running_index == j:
                cut_string.append(st[i:running_index + 1])
                running_index = i - 1
                break

print(st)
print(" | ".join(cut_string[::-1]))




