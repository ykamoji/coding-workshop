from utils.dputil import getValue, putValue, printDP
import operator
from collections import Counter
from functools import reduce
from math import factorial

dice = [1, 2, 3, 4, 5, 6]
dice_len = len(dice)
N = 4


def withRec():

    def npermutations(l):
        num = factorial(len(l))
        mults = Counter(l).values()
        den = reduce(operator.mul, (factorial(v) for v in mults), 1)
        return int(num / den)

    def combinationsCount(level, target, nums=[], usedp=False):

        if target == 0:
            return npermutations(nums)

        if level == dice_len:
            return 0

        if usedp: getValue(level, target)

        count = 0
        for times in range(target // dice[level] + 1):
            count += combinationsCount(level + 1, target - times * dice[level], nums + times*[dice[level]], usedp)
            # print(f"level {level}, times {times} target {target} = {count}")

        if usedp: putValue(level, target, count)

        return count

    count = combinationsCount(0, N, usedp=True)
    # printDP()
    print(f"Number of combinations = {count}")


def withRecOptimized():

    def combinationsCount(target, usedp=False):

        if target == 0:
            return 1

        if usedp: getValue(-1, target)

        count = 0
        for i in range(1, dice_len+1):
            if i <= target:
                count += combinationsCount(target - i, usedp)

        if usedp: putValue(-1, target, count)

        return count

    count = combinationsCount(N, usedp=True)
    # printDP()
    print(f"Number of combinations = {count}")


def withIterative():

    for i in range(N+1):
        if i == 0:
            putValue(-1, i, 1)
        else:
            putValue(-1, i, 0)
            for j in range(1, dice_len+1):
                if j <= i:
                    putValue(-1, i, getValue(-1, i) + getValue(-1, i-j))

    print(f"Number of combinations = {getValue(-1, N)}")
    printDP()

# withRec()
# withRecOptimized()
# withIterative()