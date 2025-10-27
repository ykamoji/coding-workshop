n = 50


def digitSum(number):
    s = 0
    while number > 0:
        s += int(number % 10)
        number = int(number / 10)
    return s

matches = {}
max_count = 1
max_counter = 0
for num in range(1, n + 1):
    s = digitSum(num)
    if s in matches.keys():
        matches[s] = matches[s] + 1
    else:
        matches[s] = 1

    if matches[s] > max_count:
        max_count = matches[s]
        max_counter = 1
    elif matches[s] == max_count:
        max_counter += 1

print(matches, max_count, max_counter)
