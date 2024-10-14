from DynamicProgramming.utils.dputil import getValue, putValue, printDP, putBacktrack, getBacktrack

Airplane = [10, 40, 10, 50, 20]
Bus =      [10, 30, 10, 10, 10]
K = 3
N = len(Airplane)


def minCost(level, usedp=False):

    if level <= 0:
        return 0

    if usedp: getValue(-1, level)

    cost = 1e10
    for j in range(max(level-K, 0), level):
        previous_cost = minCost(j, usedp)
        airplane_cost = Airplane[level] + Airplane[j]
        bus_cost = sum(Bus[j:level])
        choice = airplane_cost < bus_cost
        optim_cost = (airplane_cost if choice else bus_cost) + previous_cost
        putBacktrack(level, j, -1)
        if optim_cost < cost:
            cost = optim_cost
            getBacktrack()[level] = {}
            putBacktrack(level, j, choice)

    if usedp: putValue(-1, level, cost)

    return cost


cost = minCost(N-1, usedp=True)
printDP()
print(getBacktrack())
print(f"Minimum cost = {cost}")
