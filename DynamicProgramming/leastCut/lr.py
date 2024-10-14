from DynamicProgramming.utils.dputil import putValue, getValue

rod = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def lr(l, r, usedp=False):

    if l + 1 == r:
        return 0

    if usedp: getValue(l, r)

    value = 1e9
    for i in range(l+1, r):
        value = min(value, rod[r] - rod[l] + lr(l, i, usedp) + lr(i, r, usedp))

    if usedp: putValue(l, r, value)

    return value


value = lr(0, len(rod) - 1, usedp=True)

print(f"Best minimum cut = {value}")

# printDP()

