from math import inf


def merge(l, r, dp, arr):

    if l == r: return 0

    if dp[l][r] != -1: return dp[l][r]

    total = 0
    for i in range(l, r + 1):
        total += arr[i]

    s = 0
    ans = inf
    for i in range(l, r):
        s += arr[i]
        ans = min(ans, merge(l, i, dp, arr) + merge(i + 1, r, dp, arr) + (s % 100) * ((total - s) % 100))

    dp[l][r] = ans

    return dp[l][r]


def merge2(n, arr):

    dp = [[-1] * (n + 1) for _ in range(n + 1)]

    for l in range(1, n + 1):



def main():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [[-1] * (n + 1) for _ in range(n + 1)]
    # print(merge(0, n - 1, dp, arr))
    print(merge2(n, arr))


if __name__ == '__main__':
    main()