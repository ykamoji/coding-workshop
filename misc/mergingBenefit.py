from utils.dputil import putValue, getValue, printDP, putBacktrack, getBacktrack

items = [110, 10, 112, 10, 50, 5]
total = len(items)


def maximumBenefit(level, m_items, usedp=False):
    if level == total - 1:
        return 0

    if usedp: getValue(level, -1)

    value = 0
    for i in range(len(m_items) - 1):
        # print(f"level={level}, index={i}, modified items = {m_items}")
        temp_items = m_items[:i] + [(m_items[i] + m_items[i + 1]) % 100] + m_items[i + 2:]
        temp_values = m_items[i] * m_items[i + 1] + maximumBenefit(level + 1, temp_items, usedp)
        # putBacktrack(level, i, 0)
        if temp_values > value:
            # print(f"level={level}, best index={i}, old_value={value} new value={temp_values}")
            value = temp_values
            putBacktrack(level, -1, i)

    if usedp: putValue(level, -1, value)

    return value


value = maximumBenefit(0, items.copy(), usedp=True)
print(f"Maximum benefit = {value}\n")
# printDP()


def generate(m_items, level, benefit):

    if level == total - 1: return
    index = getBacktrack()[level][-1]
    new_m_items = m_items[:index] + [(m_items[index] + m_items[index + 1]) % 100] + m_items[index + 2:]
    benefit += m_items[index] * m_items[index + 1]
    print(f"{m_items} => {new_m_items}\nBenefit = {m_items[index] * m_items[index + 1]} Total = {benefit}\n")
    generate(new_m_items, level + 1, benefit)

generate(items, 0, 0)

## Wrong answer for more than 100 values
# def maximumBenefit(l, r, usedp=False):
#     if l == r:
#         return 0
#
#     if usedp: getValue(l, r)
#
#     value = 0
#     s = 0
#     total = sum(items[l:r + 1])
#     for i in range(l, r):
#         s += items[i]
#         temp_values = maximumBenefit(l, i) + maximumBenefit(i + 1, r) + (s % 100) * ((total - s) % 100)
#         if temp_values > value:
#             value = temp_values
#
#     if usedp: putValue(l, r, value)
#
#     return value
#
#
# value = maximumBenefit(0, len(items), usedp=True)
# print(f"Maximum benefit = {value}")
# printDP()
