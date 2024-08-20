from utils.dputil import getValue, putValue, printDP

stones = [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
K = 4

# stones = [10, 30, 40, 50, 20]
# K = 3

# stones = [10, 20, 10]
# K = 1

stones_len = len(stones)


def withDP():

    def minJumps(index, usedp=False):

        if index <= 0:
            return 0

        if usedp: getValue(-1, index)

        cost = 1e9
        for i in range(max(index-K, 0), index):
            cost = min(cost, abs(stones[index] - stones[i]) + minJumps(i, usedp))

        if usedp: putValue(-1, index, cost)

        return cost

    cost = minJumps(stones_len-1, usedp=True)
    printDP()
    print(f"Total cost (DP) = {cost}")


def withoutDP():

    def minJumps(index):

        if index <= 0:
            return 0

        cost = 1e9
        min_stone = stones[index]
        for i in range(max(index-K, 0), index):
            temp = abs(stones[index] - stones[i])
            if temp < cost:
                cost = temp
                min_stone = i

        return cost + minJumps(min_stone)

    cost = minJumps(stones_len-1)
    print(f"Total cost = {cost}")

withDP()
withoutDP() ## Optimized