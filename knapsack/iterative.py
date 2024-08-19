from utils.dputil import getValue, putValue, printDP, getDP

n = 3
w = [4, 2, 6]
W = 50


def knapsack():

    for i in range(n, -1, -1):
        for j in range(W+1):
            if i == n:
                if j == 0:
                    putValue(i, j, 1)
                else:
                    putValue(i, j, 0)
            else:
                putValue(i, j, 0)

                if getValue(i+1, j) == 1:
                    putValue(i, j, 1)

                if j >= w[i] and getValue(i, j - w[i]) == 1:
                    putValue(i, j, 1)


knapsack()

# printDP()

print(f"{ '' if getDP()[0][W] == 1 else 'Not ' }Possible")