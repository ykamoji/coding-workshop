arr = [0, 0, 0, 0, 0, 0, 1, 1, 1]

low = 0
high = len(arr) - 1
ans = -1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == 1:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(f"First index with 1 is at index {ans}")
for index in range(len(arr)):
    if index == ans:
        print(f'|{arr[index]}|', end=' ')
    else:
        print(arr[index], end=' ')

