import math
from utils.dputil import putValue, getValue, printDP


def play(available, usedp=False):

    if available == 0:
        return False

    if usedp: getValue(available, -1)

    ans = False
    i = 0
    while 2 ** i <= available:
        if not play(available - 2 ** i, usedp):
            ans = True
            break
        i += 1

    if usedp:putValue(available, -1, ans)

    return ans


for chips in range(101):
    print(f"Chips = {chips}, player { 'wins' if play(chips, usedp=True) else 'loses' }")

# printDP()
