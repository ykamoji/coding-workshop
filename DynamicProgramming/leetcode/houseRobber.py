nums = [200,3,140,20,10]

arr_len = len(nums)

dp = [[[-1 for _ in range(2)] for _ in range(2)] for _ in range(arr_len + 1)]


def robber(index, prev, end):
    if end == 0 and index == arr_len - 1:
        return 0
    elif end == 1 and index == arr_len:
        return 0

    if dp[index][prev][end] != -1:
        return dp[index][prev][end]

    money = robber(index + 1, 0, end)
    if prev == 0:
        money = max(money, robber(index + 1, 1, end) + nums[index])

    dp[index][prev][end] = money

    return money


if arr_len == 1:
     max_money = nums[0]
else:
    max_money = max(robber(0, 0, 0), robber(1, 0, 1))


print(f"Max money: {max_money}")