from utils.dputil import getValue, putValue, getDP

# n = 6
# v = [6, 2, 3, 5, 1, 4]
# w = [3, 24, 50, 84, 45, 57]
# W = 200

n = 4
v = [2, 3, 5, 6]
w = [3, 2, 5, 3]
W = 10

dp = {}


def knapsack(index, weight, usedp=False):
    if index == n:
        return 0

    if usedp: getValue(index, weight)

    ans = knapsack(index + 1, weight, usedp)

    if w[index] <= weight:
        ans = max(ans, knapsack(index + 1, weight - w[index]) + v[index], usedp)

    if usedp: putValue(index, weight, ans)

    return ans


final_list = []


## Showing selected items
def generate(index, weight):
    if index == n:
        return 0

    ans = knapsack(index + 1, weight)

    if w[index] <= weight:
        next_ans = knapsack(index + 1, weight - w[index]) + v[index]

        if ans > next_ans:
            generate(index + 1, weight)
        else:
            final_list.append((v[index], w[index]))
            generate(index + 1, weight - w[index])
    else:
        generate(index + 1, weight)


## Selecting same item multiple times
def knapsack_multiple(index, weight, usedp=False):
    if index == n:
        return 0

    if usedp: getValue(index, weight)

    ans = 0

    for m_times in range(0, weight // w[index]+1):
        ans = max(ans, knapsack_multiple(index+1, weight - m_times*w[index]) + m_times*v[index], usedp)

    if usedp: putValue(index, weight, ans)

    return ans


print(f"Maximum value = {knapsack(0, W, True)}")

generate(0, W)

print(f"Items={final_list}")

print(f"Values = {', '.join([str(v) for v,w in final_list])}")

print(f"Weights = {', '.join([str(w) for v,w in final_list])} = {sum([w for v,w in final_list])}")
