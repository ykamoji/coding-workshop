arr = [10, 31, 45, 1, 5]


def check(ind):
    return arr[ind] < arr[0]


def searchRotation():
    low = 0
    high = len(arr) - 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


idx = searchRotation()
print(f"Array is rotated {idx} times")
print(arr)
print(arr[idx:] + arr[:idx])

