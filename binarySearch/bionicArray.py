arr = [1, 5, 9, 10, 11, 2, 1]


def check(mid):
    if mid == len(arr) - 1: return 1
    return arr[mid] > arr[mid + 1]


def searchPeak():
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


idx = searchPeak()
print(f"Peak at index {idx}")
for index in range(len(arr)):
    if index == idx:
        print(f'|{arr[index]}|', end=' ')
    else:
        print(arr[index], end=' ')