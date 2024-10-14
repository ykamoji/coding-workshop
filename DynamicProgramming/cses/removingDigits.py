from DynamicProgramming.utils.dputil import getValue, putValue, printDP
num = 27


def getDigits(number):
    return list(str(number).replace('0',''))


def withRec():
    def minimumSteps(target, usedp=False):

        if target <= 0:
            return 0

        if usedp: getValue(-1, target)

        count = 1e7
        for digit in getDigits(target):
            count = min(count, minimumSteps(target - int(digit), usedp) + 1)

        if usedp: putValue(-1, target, count)

        return count

    count = minimumSteps(num, usedp=True)
    printDP()
    print(f"Minimum number of steps required = {count}")


def withIteration():

    for i in range(num+1):
        if i == 0:
            putValue(-1, i, 0)
        else:
            putValue(-1, i, 1e7)
            for digit in getDigits(i):
                putValue(-1, i, min( getValue(-1, i) , getValue(-1, i - int(digit)) + 1 ))

    printDP()
    print(f"Minimum number of steps required = {getValue(-1, num)}")


# withRec()
withIteration()