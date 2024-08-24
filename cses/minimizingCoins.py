from utils.dputil import getValue, putValue, printDP

coins = [1, 5, 7]
N = 11


def withRec():
    def minimumCoins(target, usedp=False):

        if target == 0:
            return 0

        if usedp: getValue(-1, target)

        count = 1e10
        for c in coins:
            if c <= target:
                count = min(count, minimumCoins(target - c, usedp) + 1)

        if usedp: putValue(-1, target, count)

        return count

    count = minimumCoins(N, usedp=True)
    printDP()
    print(f"Minimum number of coins needed = {count}")


def withIterative():

    for i in range(N+1):
        if i == 0:
            putValue(-1, i, 0)
        else:
            putValue(-1, i, 1e10)
            for c in coins:
                if c <= i:
                    putValue(-1, i, min(getValue(-1, i), getValue(-1, i - c) + 1))

    printDP()
    print(f"Minimum number of coins needed = {getValue(-1, N)}")


# withRec()
withIterative()