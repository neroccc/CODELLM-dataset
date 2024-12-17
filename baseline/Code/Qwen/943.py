from typing import List
class Solution:
    def minString(self, words):
        n = len(words)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = words[i]
        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1], key=len)
                if words[i] == words[j][::-1]:
                    dp[i][j] = words[i] + words[j] + dp[i + 1][j - 1]
        return dp[0][n - 1]