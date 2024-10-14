n = 3

combinations = []


def generate(index, left, right, arr=""):

    if left > right:
        return

    if index == n * 2:
        if left == 0 and right == 0:
            combinations.append(arr)
        return

    if index == 0:
        generate(index + 1, left - 1, right, arr=arr + "(")
    else:
        generate(index + 1, left - 1, right, arr=arr + "(")
        generate(index + 1, left, right - 1, arr=arr + ")")


total_count = generate(0, n, n)
print(f"Total possibilities = {total_count}")
print(f"Combinations = {combinations}")
