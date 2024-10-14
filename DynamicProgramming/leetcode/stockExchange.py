prices = [7,1,5,3,6,4]


def maxProfit():

    max_profit = 0
    min_price = 1e5
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit

max_profit = maxProfit()

print(f"Maximum profit: {max_profit}")