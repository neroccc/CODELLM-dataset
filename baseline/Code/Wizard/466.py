from typing import List
class Solution:
    def maxRepeating(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m = len(s2)
        n = len(s1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 0
        for i in range(n + 1):
            dp[0][i] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s2[i - 1] == s1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j]

        for k in range(1, n1 + 1):
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])
                    if s2[i - 1] == s1[j - 1]:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[m][n]