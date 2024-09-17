n = 1000000000
count = 0
multiplier = 1
while multiplier <= n:
    divider = multiplier * 10
    count += (n // divider) * multiplier
    count += min(max(n % divider - multiplier + 1, 0), multiplier)
    multiplier *= 10

print(f"Number of 1s = {count}")


