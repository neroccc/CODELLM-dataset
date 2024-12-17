from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        def helper(self, s, wordDict, n, path):
            if n == 0:
                return [path[:]]
            res = []
            for i in range(n):
                if s[i:n] in wordDict:
                    path.append(s[i:n])
                    res += self.helper(s, wordDict, i, path)
                    path.pop()
            return res

        if dp[n]:
            return helper(s, wordDict, n, [])
        return []

