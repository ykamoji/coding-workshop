from DynamicProgramming.utils.dputil import getValue, putValue, printDP

str_1 = list("LOVE")
str_len_1 = len(str_1)
str_2 = list("MOVIE")
str_len_2 = len(str_2)


def operationsCount():

    for i in range(str_len_1, -1, -1):
        for j in range(str_len_2, -1, -1):
            if i == str_len_1 or j == str_len_2:
                putValue(i, j, (str_len_1 - i) + (str_len_2 - j))
            else:
                val = 1 + min(getValue(i, j + 1), getValue(i + 1, j))
                val = min(val, getValue(i + 1, j + 1) + (0 if str_1[i] == str_2[j] else 1))
                putValue(i, j, val)

    printDP()
    print(f"Total operations = {getValue(0, 0)}")


operationsCount()