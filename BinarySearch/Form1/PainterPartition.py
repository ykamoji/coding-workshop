arr = [1, 3, 8, 7, 2, 5]
K = 3


def check(mid):

    k=K
    i = 0
    sum = 0
    skip = 0
    while k > 0 and i < len(arr) and skip < 2:
        if sum + arr[i] <= mid:
            sum += arr[i]
            i += 1
            skip = 0
        else:
            k -= 1
            sum = 0
            skip += 1

    return i == len(arr)


def minimizeMaximumTime():
    low = 0
    high = sum(arr)
    ans = 0
    while low <= high:
        mid = (low + high)//2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


time = minimizeMaximumTime()
print(f"The best maximum time is {time}")