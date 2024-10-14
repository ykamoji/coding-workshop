from DynamicProgramming.utils.dputil import getValue, putValue

s = [1, 2, 5, 9]

total_len = len(s)


def check_exists(index, target, usedp=False):

    if target == 0:
        return True

    if index == total_len:
        return False

    if usedp: getValue(index, target)

    ans = check_exists(index + 1, target, usedp) or check_exists(index + 1, target - s[index], usedp)

    if usedp: putValue(index, target, ans)

    return ans


def groups(index, target, items):

    if target == 0 or index == total_len:
        return

    if check_exists(index + 1, target - s[index], True):
        items.append(s[index])
        groups(index + 1, target - s[index], items)
    else:
        groups(index + 1, target, items)


for T in [3, 4, 16]:

    present = check_exists(0, T, True)
    print(f"Grouping set possible for {T} = {present}")

    if present:
        items = []
        groups(0, T, items)
        print(f"Items = {items}")