from DynamicProgramming.utils.dputil import putValue, getValue, printDP, putBacktrack, getBacktrack

x = [10, 30, 5, 60, 3]
y = [30, 5, 60, 3, 15]


def matrixChain(l, r, usedp=False):

    if l >= r:
        return 0

    if usedp: getValue(l, r)

    ans = 1e9
    for i in range(l, r):
        temp = matrixChain(l, i) + matrixChain(i + 1, r) + x[l]*y[i]*y[r]
        if temp < ans:
            ans = temp
            putBacktrack(l, r, i)

    if usedp: putValue(l, r, ans)

    return ans


value = matrixChain(0, len(x)-1, usedp=True)

print(f"Optimal value = {value}")

# printDP()

open_brackets = [0]*10
close_brackets = [0]*10


def generate(l, r):

    if l >= r:
        return

    open_brackets[l] += 1
    close_brackets[r] += 1

    mid = getBacktrack()[l][r]

    generate(l, mid)
    generate(mid + 1, r)


generate(0, len(x) - 1)

print("Optimal multiplication:")

for i in range(len(x)):
    for j in range(open_brackets[i]):
        print("(", end='')

    print(f" {x[i]}x{y[i]} ", end='')

    for j in range(close_brackets[i]):
        print(")", end='')