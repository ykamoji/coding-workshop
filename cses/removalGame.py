from utils.dputil import getValue, putValue, getDP, printDP
import random

arr = [random.randint(-10,10) for _ in range(10)]
arr_len = len(arr)


def withRec_2():

    def maximumScore(start, end, usedp=False):

        if start > end:
            return 0

        if usedp: getValue(start, end)

        op1 = arr[start] + min(maximumScore(start + 2, end, usedp), maximumScore(start + 1, end - 1, usedp))
        op2 = arr[end] + min(maximumScore(start + 1, end - 1, usedp), maximumScore(start, end - 2, usedp))
        val = max(op1, op2)

        if usedp: putValue(start, end, val)

        return val

    score = maximumScore(0, arr_len-1, usedp=True)
    # printDP()
    print(f"Maximum score = {score}")
    getDP().clear()


print(arr)

withRec_2()