from utils.dputil import getValue, putValue, printDP

candies = [1, 2, 3]
K = 4
N = len(candies)


def candiesDistribution(level, target, usedp=False):

    if level == N:
        if target == 0:
            return 1
        else:
            return 0

    if usedp: getValue(level, target)

    count = 0
    for j in range(candies[level]+1):
        if target >= j:
            count += candiesDistribution(level+1, target-j, usedp)

    if usedp: putValue(level, target, count)

    return count


count = candiesDistribution(0, K, usedp=True)
# printDP()
print(f"Total number of candies distributions = {count}")