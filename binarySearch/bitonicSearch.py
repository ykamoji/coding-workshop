arr = [1, 2, 5, 3, 2, 1]
X = 5

def check(mid):
    if mid == len(arr) - 1: return 1
    return arr[mid] > arr[mid + 1]

low = 0
high = len(arr) - 1
peak = 0
while low <= high:
    mid = (low + high) // 2
    if check(mid):
        peak = mid
        high = mid - 1
    else:
        low = mid + 1


def searchX():

    ans = []
    low = 0
    high = peak
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == X:
            ans.append(mid + 1)
        if arr[mid] > X:
            high = mid - 1
        else:
            low = mid + 1

    low = peak + 1
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == X:
            ans.append(mid + 1)

        if arr[mid] < X:
            high = mid - 1
        else:
            low = mid + 1

    return ans


ans = searchX()
print(f"Index: {ans}")
for index in range(len(arr)):
    if index + 1 in ans:
        print(f'|{arr[index]}|', end=' ')
    else:
        print(arr[index], end=' ')