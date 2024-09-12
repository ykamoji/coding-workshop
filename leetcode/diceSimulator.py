N = 3
rollMax = [1,1,1,2,2,3]

MOD = 1000000007


def countSequences(index, last, c, comb = []):

    if index == N:
        print(comb)
        return 1

    count = 0
    for dice in range(6):
        if (last == dice and c < rollMax[last]) or last == -1:
            count = (count + countSequences(index + 1, dice, c + 1, comb=comb + [dice + 1])) % MOD

        elif last != dice:
            count = (count + countSequences(index + 1, dice, c, comb=comb + [dice + 1])) % MOD

    return count


sequences = countSequences(0, -1,0)

print(f"Sequences = {sequences}")