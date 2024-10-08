from utils.dputil import getValue, putValue, printDP

# stones_len, K = map(int, input().split())
# stones = list(map(int, input().split()))

stones = [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
K = 4

# stones = [10, 30, 40, 50, 20]
# K = 3

# stones = [10, 20, 10]
# K = 1

stones_len = len(stones)


def withRec():
    dp = {}
    def minJumps(index, usedp=False):

        if index <= 0:
            return 0

        # if usedp: getValue(-1, index)
        if index in dp:
            return dp[index]

        cost = 1e9
        for i in range(max(index-K, 0), index):
            cost = min(cost, abs(stones[index] - stones[i]) + minJumps(i, usedp))

        # if usedp: putValue(-1, index, cost)
        dp[index] = cost
        return cost

    cost = minJumps(stones_len-1, usedp=True)
    # print(dp)
    print(f"Total cost (DP) = {cost}")


def withDP():
    dp = {}
    def minJumps():
        for index in range(stones_len):
            if index == 0:
                dp[index] = 0
            else:
                cost = 1e9
                for i in range(max(index - K, 0), index):
                    cost = min(cost, abs(stones[index] - stones[i]) + dp[i])
                dp[index] = cost

        return dp[stones_len-1]

    cost = minJumps()
    # print(dp)
    print(f"Total cost = {cost}")

withRec()
withDP() ## Optimized