def subset(i, t, arr, dp, N):
    if i == N:
        if t == 0:
            return True
        else:
            return False

    if dp[i][t] != -1: return dp[i][t]

    dp[i][t] = subset(i + 1, t, arr, dp, N)
    if t >= arr[i]:
        dp[i][t] = dp[i][t] or subset(i + 1, t - arr[i], arr, dp, N)

    return dp[i][t]


def subset_queries(arr, queries, N):
    ans = []
    dp = [[-1] * 100010 for _ in range(100)]
    for t in queries:
        if subset(0, t, arr, dp, N):
            ind = []
            i = len(arr) - 1
            while t:
                if subset(i - 1, t - arr[i], arr, dp, N):
                    t -= arr[i]
                    ind.append(i)
                i -= 1
            ind.reverse()
            ans.append(ind)
        else:
            ans.append([-1])

    return ans


def main():

    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    ans = subset_queries(arr, queries, N)

    for i, t in enumerate(queries):
        if sum(arr[ind] for ind in ans[i]) == t:
            print(1)
        else:
            print(-1)


if __name__ == "__main__":
    main()
