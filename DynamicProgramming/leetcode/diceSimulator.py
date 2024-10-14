N = 3
rollMax = [1,1,1,2,2,3]

MOD = 1000000007

dp = []
for _ in range(N):
    temp = []
    for _ in range(6):
        temp.append([-1 for _ in range(15)])
    dp.append(temp)


def countSequences(index, last, c, comb = []):

    if index == N:
        # print(comb)
        return 1

    if dp[index][last][c] != -1:
        return dp[index][last][c]

    count = 0
    for dice in range(6):
        if last == dice and c > 0:
            count = (count + countSequences(index + 1, dice, c - 1, comb=comb + [dice + 1])) % MOD

        elif last != dice:
            count = (count + countSequences(index + 1, dice, rollMax[dice] - 1, comb=comb + [dice + 1])) % MOD

    dp[index][last][c] = count

    return count


sequences = countSequences(0, 0, rollMax[0])

print(f"Sequences = {sequences}")