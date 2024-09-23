stones = [0,1,3,5,6,8,12,17]

stones_len = len(stones)

dp = {}


def pathCrossing(index, last):

    if index == stones_len - 1:
        return True

    # if index > stones_len or index < 0:
    #     return False

    if (index,last) in dp:
        return dp[(index,last)]

    possible = False
    if index + 1 < stones_len:
        for k in range(max(1, last - 1), last + 2):
            next_id = index + 1
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

    dp[(index,last)] = possible

    return possible


if stones_len > 1 and stones[1] > 1:
    possible = False
else:
    possible = pathCrossing(1, 1)

print(possible)