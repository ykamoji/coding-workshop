from math import inf
import time

grid = [[6,7,1,20,11],[4,5,18,23,28]]
K = 1

start_time = time.time()

flatten_list = []
m = len(grid)
n = len(grid[0])

for item in grid:
    flatten_list.extend(item)

transports = {}

dp = [[[-1] * (K + 1) for _ in range(n+1)] for _ in range(m+1)]


def add_jumps(from_i, from_j, to_i, to_j):
    if (from_i, from_j) in transports:
        transports[(from_i, from_j)] += [(to_i, to_j)]
    else:
        transports[(from_i, from_j)] = [(to_i, to_j)]


number_point_map = {}
# count = 0
for i in range(m * n):
    start_i = i // n
    start_j = i % n
    for j in range(i + 1, m * n):
        end_i = j // n
        end_j = j % n
        # print(f"{count} Comparing {flatten_list[i]}({start_i},{start_j}) & {flatten_list[j]}({end_i},{end_j})")
        # count += 1
        if flatten_list[i] >= flatten_list[j]:
            add_jumps(start_i, start_j, end_i, end_j)
        else:
            add_jumps(end_i, end_j, start_i, start_j)

# for start, jumps in transports.items():
#     print(f"({start}) => {jumps}")


def traverse(i, j, k):

    if i == m - 1 and j == n - 1:
        return 0

    if dp[i][j][k] != -1: return dp[i][j][k]

    ans = inf
    if i + 1 < m:
        dp_cost = traverse(i + 1, j, k) + grid[i + 1][j]
        if dp_cost < ans:
            ans = dp_cost

    if j + 1 < n:
        dp_cost = traverse(i, j + 1, k) + grid[i][j + 1]
        if dp_cost < ans:
            ans = dp_cost

    if k > 0 and (i, j) in transports:
        for x, y in transports[(i, j)]:
            dp_cost = traverse(x, y, k - 1)
            if dp_cost < ans:
                ans = dp_cost

    dp[i][j][k] = ans

    return ans

# def traverse():
#     dp = [[[inf] * (K + 1) for _ in range(n+1)] for _ in range(m+1)]
#
#     for k in range(K):
#         dp[m-1][n-1][k] = 0
#
#     for i in range(m-1, -1, -1):
#         for j in range(n-1, -1, -1):
#             for k in range(K):
#                 ans_1 = dp[i+1][j][k] + grid[i + 1][j]
#                 ans_2 = dp[i][j+1][k] + grid[i][j + 1]
#                 ans_3 = inf
#                 if (i, j) in transports:
#                     for x, y in transports[(i, j)]:
#                         dp_cost = dp[x][y][k-1]
#                         if dp_cost < ans_3:
#                             ans_3 = dp_cost


def generate(i, j, k):

    if i == m - 1 and j == n - 1: return

    dp_cost_1, dp_cost_2, dp_cost_3 = inf, inf, inf

    if i + 1 < m:
        dp_cost_1 = traverse(i + 1, j, k) + grid[i + 1][j]

    if j + 1 < n:
        dp_cost_2 = traverse(i, j + 1, k) + grid[i][j + 1]

    teleport = ()
    if k > 0 and (i, j) in transports:
        for x, y in transports[(i, j)]:
            dp_cost = traverse(x, y, k - 1)
            if dp_cost <= dp_cost_3:
                dp_cost_3 = dp_cost
                teleport = (x, y)

    if dp_cost_1 < dp_cost_2 and dp_cost_1 < dp_cost_3:
        print(f"{grid[i][j]} ({i}, {j}) => {grid[i+1][j]} ({i+1}, {j}) Cost = {grid[i+1][j]}")
        generate(i + 1, j, k)
    elif dp_cost_2 < dp_cost_1 and dp_cost_2 < dp_cost_3:
        print(f"{grid[i][j]} ({i}, {j}) => {grid[i][j+1]} ({i}, {j+1}) Cost = {grid[i][j+1]}")
        generate(i, j+1, k)
    elif dp_cost_3 < dp_cost_1 and dp_cost_3 < dp_cost_2:
        print(f"{grid[i][j]} ({i},  {j}) => {grid[teleport[0]][teleport[1]]} {teleport}")
        generate(teleport[0], teleport[1], k - 1)


cost = traverse(0, 0, K)
print(f"Time: {(time.time() - start_time)*1000:.3f} ms\n")

for item in grid:
    print(item)

# print(dp)

print('\nMoves:')
generate(0, 0, K)
print()

print(cost)