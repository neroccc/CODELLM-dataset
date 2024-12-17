from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        dp = [False] * (30 + 1)
        res = []

        def dfs(word):
            n = len(word)
            if n == 0:
                return True
            dp[n] = False
            for i in range(1, n + 1):
                if word[:i] in word_set and (dp[n - i] or dfs(word[i:])):
                    dp[n] = True
                    break
            return dp[n]

        for word in words:
            if dfs(word):
                res.append(word)
        return res