s = "cbbd"

str_len = len(s)
str_arr = list(s)
dp = [[False for _ in range(str_len)] for _ in range(str_len)]


def sequence():

    if str_len <= 1:
        return s

    max_Len = 1
    max_Str = s[0]
    for i in range(str_len):
        dp[i][i] = True
        for j in range(i):
            if s[i] == s[j] and (i - j <= 2 or dp[j+1][i-1]):
                dp[j][i] = True

                if i - j + 1 > max_Len:
                    max_Len = i - j + 1
                    max_Str = s[j:i+1]

    return max_Str

print(f"Substring : {sequence()}")


dp = [-1 for _ in range(str_len+1)]

palin_check = []
for _ in range(str_len+1):
    palin_check.append([-1 for _ in range(str_len+1)])


def check(l, r):
    if l >= r: return True
    if palin_check[l][r] != -1: return palin_check[l][r]
    val = str_arr[l - 1] == str_arr[r - 1]  and check(l + 1, r - 1)
    palin_check[l][r] = val
    return val


max_index = {}

def sequence(index):

    if index == -1:
        return 0

    if dp[index] != -1:
        return dp[index]

    val = 0
    for i in range(index):
        if check(i + 1, index):
            current = index - i
            next = sequence(i)

            if current > val:
                val = current
                max_index[val] = i

            if next > val:
                val = next

    dp[index] = val

    return val


max_len = sequence(str_len)
index = max_index[max_len]

print(f"Substring : {s[index:index + max_len]}")




