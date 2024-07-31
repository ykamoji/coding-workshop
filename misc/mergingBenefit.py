from utils.dputil import putValue, getValue, printDP, putBacktrack, getBacktrack

items = [4, 2, 5, 8]
total = len(items)


def maximumBenefit(level, m_items, usedp=False):

    if level == total - 1:
        return 0

    if usedp: getValue(level, -1)

    value = 0
    for i in range(len(m_items) - 1):
        temp_items = m_items[:i] + [(m_items[i] + m_items[i + 1]) % 100] + m_items[i + 2:]
        # print(temp_items)
        temp_values = m_items[i] * m_items[i + 1] + maximumBenefit(level + 1, temp_items, usedp)
        if temp_values > value:
            value = temp_values
            putBacktrack(level, -1, i)

    if usedp: putValue(level, -1, value)

    return value

value = maximumBenefit(0, items.copy(), usedp=True)

print(f"Maximum benefit = {value}")
printDP()


def maximumBenefit(l, r, usedp=False):

    if l == r:
        return 0

    if usedp: getValue(l, r)

    value = 0
    s=0
    for i in range(l,r):
        s += items[i]
        temp_values = maximumBenefit(l, i) + maximumBenefit(i+1, r) + (s%100)*((sum(items[l:r+1])-s)%100)
        if temp_values > value:
            value = temp_values

    if usedp: putValue(l, r, value)

    return value

value = maximumBenefit(0, len(items)-1, usedp=True)

print(f"Maximum benefit = {value}")

printDP()
print(getBacktrack())


