nums = [1, 2, 3]
k = 2
res = 0
curSum = 0
prefix = {0: 1}

for item in nums:
    curSum += item
    diff = curSum - k
    res += prefix.get(diff, 0)
    prefix[curSum] = 1 + prefix.get(curSum, 0)
    print(f"{prefix}" + f" s={curSum}" + f" res={res}")


print(f"Total number of ways = {res}")
