from typing import List
class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][n] = 1
            dp[n][i] = 1

        for i in range(n, 0, -1):
            for j in range(n, 0, -1):
                if i == j:
                    dp[i][j] = 1
                elif i == 1 or j == 1:
                    dp[i][j] = 1 if i == j else 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

        return dp[n // 2][n // 2]