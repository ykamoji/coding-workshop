N, W = map(int, input().split())
weights = []
values = []

for i in range(N):
   w, v = map(int, input().split())
   weights.append(w)
   values.append(v)

dp = [[-1]*(W+1) for _ in range(N+1)]

for i in range(N, -1, -1):
    for t in range(W, -1, -1):
        if i == N: dp[i][t] = 0
        else:
            dp[i][t] = dp[i+1][t]
            if t >= weights[i]:
                dp[i][t] = max(dp[i][t], dp[i+1][t-weights[i]] + values[i])

print(dp[0][W])