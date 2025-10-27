## Put N queens that don't attack each other
N = 8

queens = [-1]*N


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


print(NQueens(0))