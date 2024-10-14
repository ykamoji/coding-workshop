st = "abac"

st_len = len(st)

last = [-1]*26
count = 0
dp = {}


def distinct_sequences():

    dp[0] = 1
    prefixes = [1] + [0]*20
    for i in range(1, st_len+1):
        dp[i] = prefixes[i-1]
        if last[ord(st[i-1]) - ord('a')] != 1:
            index = last[ord(st[i-1]) - ord('a')]
            dp[i] -= prefixes[index]
        last[ord(st[i-1]) - ord('a')] = i - 1
        prefixes[i] = prefixes[i - 1] + dp[i]

    print(prefixes[st_len] - 1)

distinct_sequences()
