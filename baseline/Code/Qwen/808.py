from typing import List
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1.0
        n = (n + 24) // 25
        dp = [[0.0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
            dp[i][0] = 1.0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = 0.25 * (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] + dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)])
        return dp[n][n]