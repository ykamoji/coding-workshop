## Find no. of ways to cross stairs
N = 4
steps = 3


def staircase(level):
    if level > N: return 0

    if level == N: return 1

    count = 0
    for i in range(1, steps + 1):
        if level + i <= N:
            count += staircase(level + i)

    return count


print(staircase(1))
