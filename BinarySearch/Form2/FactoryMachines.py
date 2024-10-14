# arr = [3, 2, 5]
# T = 7
# arr_len = len(arr)

n_t = list(map(int, input().split()))
arr_len = n_t[0]
T = n_t[1]
arr = list(map(int, input().split()))


def check(mid):
    total = 0
    for i in range(arr_len):
        total += mid // arr[i]
        if total >= T:
            return True


def minimizeTime():
    low = 0
    high = T * max(arr)
    ans = -1
    while low <= high:
        mid = (low + high)//2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


time = minimizeTime()
print(time)
# print(f"The best maximum time is {time}")