from DynamicProgramming.utils.dputil import getValue, putValue

projects = [
    [3, 6, 6],
    [2, 4, 4],
    [5, 7, 3],
    [6, 8, 2],
    # [1, 2, 4]
]

projects_len = len(projects)


def maximumMoney(level, target, usedp=False):

    if level == projects_len:
        val = getValue(-1, target)
        return val if val else 0

    if usedp: getValue(-1, target)

    money = maximumMoney(level + 1, target, usedp)
    if projects[level][1] <= target:
        money = max(money, maximumMoney(level + 1, projects[level][0] - 1, usedp) + projects[level][2])

    if usedp: putValue(-1, target, money)

    return money


min_date = min([st for st, end, _ in projects])
max_date = max([end for st, end, _ in projects])

for target in range(min_date, max_date+1):
    maxMoney = maximumMoney(0, target, usedp=True)
    print(f"Maximum money for {target} days = {maxMoney}")

# printDP()