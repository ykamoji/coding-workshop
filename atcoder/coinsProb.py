from utils.dputil import getValue, putValue, printDP

# coin_ps = [0.30, 0.60, 0.80]
coin_ps = [0.42, 0.01, 0.42, 0.99, 0.42]
coin_len = len(coin_ps)


def probability(index, heads, usedp=False):

    if index == coin_len:
        if heads > coin_len // 2:
            return 1
        else:
            return 0

    if usedp: getValue(index, heads)

    prob = coin_ps[index] * probability(index + 1, heads + 1, usedp) + \
           (1 - coin_ps[index]) * probability(index + 1, heads, usedp)

    if usedp: putValue(index, heads, prob)

    return prob


total_prob = probability(0, 0, usedp=True)
printDP()
print(f"Probability of more heads = {total_prob}")

