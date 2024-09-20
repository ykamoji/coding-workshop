arr_len = int(input())

heights = [int(ele) for ele in input().split()]
beauty = [int(ele) for ele in input().split()]

height_beauty_map = dict(zip(heights, beauty))

dp = [-1 for _ in range(arr_len+1)]


def maxBeauty(index):

    if index == arr_len:
        return []

    if dp[index] != -1:
        return dp[index]

    best_seq = [heights[index]]
    best_sum = height_beauty_map[heights[index]]
    for i in range(index+1, arr_len):
        local_seq = [heights[index]]
        if heights[i] > heights[index]:
            next_seq = maxBeauty(i)
            if heights[index] < next_seq[0]:
                local_seq += next_seq
            else:
                continue

        local_sum = sum([height_beauty_map[idx] for idx in local_seq])
        if local_sum > best_sum:
            best_seq = local_seq
            best_sum = local_sum

    dp[index] = best_seq

    return best_seq


best_height_sequence = [heights[0]]
best_sum = 0
for i in range(arr_len):
    seq = maxBeauty(i)
    # if len(best_height_sequence) == len(seq):
    #     print(f"Intermediate arr = {seq}")

    local_sum = sum([height_beauty_map[idx] for idx in seq])
    if local_sum > best_sum:
        best_height_sequence = seq
        best_sum = local_sum

print(f"Best height sequence: {best_height_sequence}")
print(f"Max beauty : {best_sum}")
