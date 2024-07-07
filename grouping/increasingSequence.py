seq = [3, 2, 5, 4, 5, 7, 8, 1, 11, 9]
# seq = [2, 1, 5, 3, 6, 2]
seq_len = len(seq)
dp = {}


def sequence(index, usedp=False):

    if index == seq_len:
        return []

    if usedp:
        if index in dp.keys():
            return dp[index]

    sub_sq = [seq[index]]
    for i in range(index+1, seq_len):
        local_sub_sq = [seq[index]]
        if seq[i] > seq[index]:
            next_sq = sequence(i, usedp)
            if seq[index] < min(next_sq):
                local_sub_sq += next_sq
            else:
                return []

        if len(local_sub_sq) > len(sub_sq):
            sub_sq = local_sub_sq

    if usedp:
        dp[index] = sub_sq

    return sub_sq


print(f"Arr = {seq}")
best = [0]
for i in range(seq_len):
    best_sub_seq = sequence(i, True)

    if len(best_sub_seq) == len(best):
        print(f"Intermediate arr = {best_sub_seq}")

    if len(best_sub_seq) > len(best):
        best = best_sub_seq


print(f"Best increasing array = {best}")

# print(dp)