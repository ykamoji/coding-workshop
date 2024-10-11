X = 31
arr = [1, 5, 10, 31, 31, 33, 34, 35, 100]


def check(mid):
    return arr[mid] >= X


def searchGreatestX():
    low = 0
    high = len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = (low + high)//2
        if check(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


idx = searchGreatestX()
print(f"First index with >={X} is at index {idx}")
for index in range(len(arr)):
    if index == idx:
        print(f'|{arr[index]}|', end=' ')
    else:
        print(arr[index], end=' ')

