from DynamicProgramming.utils.dputil import getValue, putValue

MOD = 1e9 + 7

def countTowers(T):

    for h in range(1, T+1):
        if h == 1:
            putValue(h, 0, 1)
            putValue(h, 1, 1)
        else:
            putValue(h, 0, (2 * getValue(h - 1, 0) + getValue(h - 1, 1)) % MOD)
            putValue(h, 1, (getValue(h - 1, 0) + 4 * getValue(h - 1, 1)) % MOD)


countTowers(1000000)
# printDP()

for t in [2, 6, 1337]:
    count = int(getValue(t, 0) + getValue(t, 1))
    print(f"Number of ways to build tower with height {t} = {count}")
