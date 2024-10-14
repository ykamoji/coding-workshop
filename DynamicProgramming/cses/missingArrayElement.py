from DynamicProgramming.utils.dputil import getValue, putValue, getDP

arr = [2, 0, 2, 3, 0, 4]
arr_len = len(arr)
M = 5


def withRec_1():
    def arrayCount(level, usedp=False):

        if level == arr_len:
            return 1

        if usedp: getValue(-1, level)

        count = 0
        if arr[level] != 0:
            count = arrayCount(level + 1, usedp)
        else:
            miniCount = 0
            for possible in range(1, M+1):
                if 0 < level < arr_len - 1:
                    if abs(arr[level - 1] - possible) <= 1 and abs(arr[level + 1] - possible) <= 1:
                        miniCount += 1
                elif level > 0:
                    if abs(arr[level - 1] - possible) <= 1:
                        miniCount += 1
                else:
                    if abs(arr[level + 1] - possible) <= 1:
                        miniCount += 1

            count += arrayCount(level + 1, usedp) * miniCount

        if usedp: putValue(-1, level, count)

        return count

    count = arrayCount(0, usedp=True)
    # printDP()
    print(f"Total number of arrays = {count}")
    getDP().clear()


def withRec_2():

    def arrayCount(level, last, usedp=False):

        if level == arr_len:
            return 1

        if usedp: getValue(level, last)

        count = 0
        if arr[level] != 0:
            if level == 0 or abs(last - arr[level]) <= 1:
                count = arrayCount(level + 1, arr[level], usedp)
        else:
            for i in range(max(last - 1, 1), M if level == 0 else min(last + 2, M + 1)):
                count += arrayCount(level + 1, i, usedp)

        if usedp: putValue(level, last, count)

        return count

    count = arrayCount(0, 0, usedp=True)
    # printDP()
    print(f"Total number of arrays = {count}")
    getDP().clear()


def withIteration():

    for level in range(arr_len, -1, -1):
        for last in range(1, M+1):
            if level == arr_len:
                putValue(level, last, 1)
            else:
                putValue(level, last, 0)
                if arr[level] != 0:
                    if level == 0 or abs(last - arr[level]) <= 1:
                        putValue(level, last, getValue(level + 1, arr[level]))
                else:
                    for i in range(max(last-1, 1), min(last + 2, M + 1)):
                        putValue(level, last, getValue(level, last) + getValue(level + 1, i))

    # printDP()
    count = 0
    if arr[0] == 0:
        for i in range(1, M+1):
            count += getValue(1, i)
    else:
        count = getValue(1, arr[0])

    print(f"Total number of arrays = {count}")
    getDP().clear()


withRec_1()
withRec_2()
withIteration()