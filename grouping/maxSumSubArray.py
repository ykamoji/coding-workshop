from utils.dputil import getValue, putValue, printDP, getDP

arr = [-1, 5, -3, 2, 9, -1, 5, -10, 3, 2]
arr_len = len(arr)


def withRecursion_1():
    def maxSum(l, r, usedp=True):

        if l >= r:
            return 0

        if usedp: getValue(l, r)

        val = -1e9
        for i in range(l, r):
            val = max(val, sum(arr[l:r + 1]), maxSum(l, i, usedp), maxSum(i + 1, r, usedp))

        if usedp: putValue(l, r, val)

        return val

    value = maxSum(0, arr_len, usedp=True)
    # printDP()
    dp = getDP()

    start, end = 0, arr_len
    for i, val in dp.items():
        for j, v in val.items():
            if v == value:
                if start < i:
                    start = i
                if end > j:
                    end = j

    print(f"Arr = {arr}")
    print(f"Sub array = {arr[start:end + 1]}")
    print(f"Maximum sum = {value}")


def withRecursion_2():
    def maxSum(index):

        if index == arr_len:
            return 0

        getValue(-1, index)

        if index == 0:
            val = arr[0]
        else:
            val = max(getValue(-1, index - 1), 0) + arr[index]

        putValue(-1, index, val)

        return max(val, maxSum(index + 1))

    value = maxSum(0)

    # printDP()

    print(f"Arr = {arr}")
    print(f"Maximum sum = {value}")


def withIterative():

    last = -1e10
    sum = -1e10

    for i in range(arr_len):
        last = max(last, 0) + arr[i]
        sum = max(sum, last)

    print(f"Arr = {arr}")
    print(f"Maximum sum = {sum}")

# withRecursion_1()
# withRecursion_2()  ## Optimized
withIterative() ## Best
