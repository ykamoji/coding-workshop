s = "catsandogcat"
wordDict = ["cats","dog","sand","and","cat","an"]
wordDict_len = len(wordDict)

dp = [-1 for _ in range(len(s)+1)]
s_len = len(s)


def combinationAvailable(start):

    if start == s_len:
        return True

    if dp[start] != -1:
        return dp[start]

    result = False
    for word in wordDict:

        word_len = len(word)

        if s[start: start + word_len] == word:
            result = result or combinationAvailable(start + word_len)

    dp[start] = result

    return result

print(f"{combinationAvailable(0)}")
