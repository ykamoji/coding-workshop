from DynamicProgramming.utils.dputil import putValue, getValue, printDP, putBacktrack, getBacktrack

# items = [10, 20, 30, 40]
items = [7, 6, 8, 6, 1, 1]
total = len(items)

## Incorrect solution
def maximumBenefit(level, m_items, usedp=False):
    if level == total - 1:
        return 0

    if usedp: getValue(level, -1)

    value = 1e10
    for i in range(len(m_items) - 1):
        # print(f"level={level}, index={i}, modified items = {m_items}")
        temp_items = m_items[:i] + [m_items[i] + m_items[i + 1]] + m_items[i + 2:]
        temp_values = m_items[i] + m_items[i + 1] + maximumBenefit(level + 1, temp_items, usedp)
        # putBacktrack(level, i, 0)
        if temp_values <= value:
            # print(f"level={level}, best index={i}, old_value={value} new value={temp_values}")
            value = temp_values
            putBacktrack(level, -1, i)

    if usedp: putValue(level, -1, value)

    return value


value = maximumBenefit(0, items.copy(), usedp=True)
print(f"Minimum benefit = {value}\n")
# printDP()
# print(getBacktrack())


def generate(m_items, level, benefit):

    if level == total - 1: return
    index = getBacktrack()[level][-1]
    new_m_items = m_items[:index] + [m_items[index] + m_items[index + 1]] + m_items[index + 2:]
    benefit += m_items[index] + m_items[index + 1]
    print(f"{m_items} => {new_m_items}\nCost = {m_items[index] + m_items[index + 1]} Total = {benefit}\n")
    generate(new_m_items, level + 1, benefit)


generate(items, 0, 0)
