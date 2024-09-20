n = 124

# dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
dp = [-1 for _ in range(n + 1)]


def sumOfSquares(index, target, tracker):
    if target == 0:
        print(tracker)
        return 0

    if dp[target] != -1:
        return dp[target]

    count = 1e10
    squared_index = index ** 2
    if squared_index <= target:
        for i in range((target // squared_index) + 1):
            val = i * squared_index
            if target >= val:
                count = min(count, i + sumOfSquares(index + 1, target - val, tracker=tracker + [squared_index] * i))

    dp[target] = count

    return count


count = sumOfSquares(1, n, [])
print(f"\nMinimum squares required = {count}")
