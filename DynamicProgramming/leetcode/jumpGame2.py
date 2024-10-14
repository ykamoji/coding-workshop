nums = [2,3,1,1,4]

l = len(nums)

dp = [-1 for _ in range(l + 1)]
# backtrack = [0 for _ in range(l + 1)]


def jumpCount(index):

    if index >= l - 1:
        return 0

    if dp[index] != -1:
        return dp[index]

    count = 1e10
    for i in range(index + 1, min(index + nums[index] + 1, l)):
        if i < l:
            temp = 1 + jumpCount(i)
            if temp < count:
                count = temp
                # backtrack[index] = index + i

    dp[index] = count

    return count


count = jumpCount(0)
# print(backtrack)
print(f"Minimum jumps = {count}")

dp = [-1 for _ in range(l+1)]

for index in range(l - 1, -1, -1):
    if index == l - 1:
        dp[index] = 0
    else:
        count = 1e10
        for i in range(index + 1, min(index + nums[index] + 1, l)):
            count = min(count, 1 + dp[i])
        dp[index] = count

print(f"Minimum jumps = {dp[0]}")


def minJumps(index):
    if index <= 0:
        return 0

    min_jump = index - 1
    for i in range(index - 1, -1, -1):
        if nums[i] + i >= index and i < min_jump:
            min_jump = i

    return 1 + minJumps(min_jump)

print(f"Minimum jumps = {minJumps(l-1)}")


def minJumps():

    index = l - 1
    jumps = 0
    while index > 0 :
        min_jump = index - 1
        for i in range(index - 1, -1, -1):
            if nums[i] + i >= index and i < min_jump:
                min_jump = i
        index = min_jump
        jumps += 1

    return jumps

print(f"Minimum jumps = {minJumps()}")






