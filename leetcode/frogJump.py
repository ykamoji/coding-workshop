stones = [0, 2]

stones_len = len(stones)

dp = [[-1 for _ in range(stones_len + 1)] for _ in range(stones_len + 1)]


def pathCrossing(index, last):

    if index == stones_len - 1:
        return True

    # if index > stones_len or index < 0:
    #     return False

    if dp[index][last] != -1:
        return dp[index][last]

    possible = False
    for k in range(max(1, last - 1), last + 2):
        next_id = index + 1
        if next_id < stones_len:
            leave = False
            while not leave:
                if stones[next_id] == stones[index] + k:
                    print(stones[index], stones[next_id], k)
                    possible = pathCrossing(next_id, k)
                    if possible:
                        leave = True
                next_id += 1
                if next_id > stones_len - 1 or stones[next_id] > stones[index] + k:
                    leave = True

        if possible:
            break

    dp[index][last] = possible

    return possible


if stones_len > 1 and stones[1] > 1:
    possible =  False
else:
    possible = pathCrossing(1, 1)

print(possible)