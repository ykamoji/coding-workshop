import time
bounds = [4, 6, 2, 1, 3, 5, 4, 1, 5, 7, 3, 6, 1, 4, 2, 6, 5]
S = 25
bounds_len = len(bounds)


def withRec():
    dp = {}

    def totalCombinations(index, target, comb=[]):

        if index == bounds_len:
            if target == 0:
                # print(comb)
                return 1
            else:
                return 0

        if (index, target) in dp:
            return dp[(index, target)]

        count = 0
        for i in range(bounds[index]+1):
            if i <= target:
                count += totalCombinations(index + 1, target - i, comb=comb + [i])

        dp[(index, target)] = count

        return count

    start = time.time()
    total_combinations = totalCombinations(0, S)
    duration = (time.time() - start)*1000
    print(f"Total combinations: {total_combinations} ({duration:5f} ms)")


def withIterative():
    dp = {}
    start = time.time()
    for index in range(bounds_len, -1, -1):
        for target in range(S+1):
            if index == bounds_len:
                if target == 0:
                    dp[(index, target)] = 1
                else:
                    dp[(index, target)] = 0
            else:
                count = 0
                for i in range(bounds[index] + 1):
                    if i <= target:
                        count += dp[(index + 1, target - i)]
                dp[(index, target)] = count

    duration = (time.time() - start)*1000
    print(f"Total combinations: {dp[(0, S)]} ({duration:5f} ms)")


def withPrefixSum():
    dp = {}
    start = time.time()
    for index in range(bounds_len, -1, -1):
        for target in range(S + 1):
            if index == bounds_len:
                if target == 0:
                    dp[(index, target)] = 1
                else:
                    dp[(index, target)] = 0
            else:
                x = target - bounds[index] - 1
                dp[(index, target)] = dp[(index + 1, target)]
                if x >= 0:
                    dp[(index, target)] -= dp[(index + 1, x)]

        if index < bounds_len:
            for target in range(1, S + 1):
                dp[(index, target)] += dp[(index, target - 1)]

    duration = (time.time() - start) * 1000
    print(f"Total combinations: {dp[(0, S)]} ({duration:5f} ms)")


withRec()
withIterative()
withPrefixSum()