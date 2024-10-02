n = 6
K = 2
v = [6, 2, 3, 5, 1, 4]
w = [3, 24, 84, 100, 45, 57]
W = 100

dp = {}


def continuesKnapsack(index, s, c):

    if index == n:
        return 0

    if (index, s, c) in dp:
        return dp[(index, s, c)]

    max_value = continuesKnapsack(index + 1, 0, 0)
    if c < K and w[index] + s <= W:
        max_value = max(max_value, v[index] + continuesKnapsack(index + 1, s + w[index], c + 1))

    dp[(index, s, c)] = max_value

    return max_value


max_val = continuesKnapsack(0, 0, 0)
print(f"Maximum value of weights {W} is {max_val}")
