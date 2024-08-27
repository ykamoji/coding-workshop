steps = 47
arrLen = 38

dp = []
for _ in range(steps + 1):
    dp.append([-1 for _ in range(steps + 1)])


def countWays(index, current):
    if current < 0 or current >= arrLen:
        return 0

    if index == steps:
        if current == 0:
            return 1
        else:
            return 0

    if dp[index][current] != -1:
        return dp[index][current]

    count = 0
    for step in [-1, 0, 1]:
        count = (count + countWays(index + 1, current + step)) % 1000000007

    dp[index][current] = count

    return count


count = countWays(0, 0)
# print(dp)
print(f"Ways = {count}")

