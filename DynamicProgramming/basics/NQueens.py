## Put N queens that don't attack each other
from pyarrow import duration

N = 10

queens = [-1] * N


def check(row, col):
    for i in range(row):
        prev_row = i
        prev_col = queens[i]

        if prev_col == col or abs(col - prev_col) == abs(row - prev_row):
            return False

    return True


def NQueens(level):
    if level > N: return 0
    if level == N: return 1

    count = 0
    for i in range(N):
        if check(level, i):
            queens[level] = i
            count += NQueens(level + 1)
            queens[level] = -1

    return count


from DynamicProgramming.utils.dputil import getValue, putValue
import time


def NQueens_DP(level):
    if level > N: return 0
    if level == N: return 1

    getValue(-1, level)

    count = 0
    for i in range(N):
        if check(level, i):
            queens[level] = i
            count += NQueens(level + 1)
            putValue(-1, level, count)
            queens[level] = -1


start = time.time()
count = NQueens(0)
duration = time.time() - start
print(f"NQueens {count}  & recursion Time {duration:.5f}" )

start = time.time()
NQueens_DP(0)
duration = time.time() - start
print(f"NQueens {getValue(-1, 0)} & DP Time {duration:.5f}")
