from DynamicProgramming.utils.dputil import getValue, putValue, printDP

A, B = 3, 5


def withIterative():

    for a in range(1, A + 1):
        for b in range(1, B + 1):
            if a == b:
                putValue(a, b, 0)
            else:
                val = 1e10
                for i in range(1, a):
                    val = min(val, getValue(i, b) + getValue(a - i, b) + 1)

                for j in range(1, b):
                    val = min(val, getValue(a, j) + getValue(a, b - j) + 1)

                putValue(a, b, val)

    printDP()
    print(f"Minimum number of cuts = {getValue(A, B)}")


withIterative()