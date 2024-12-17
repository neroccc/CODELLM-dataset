from typing import List
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            dp[i][i] = 0

        for diff in range(2, n + 1):
            for i in range(1, n - diff + 2):
                j = i + diff - 1
                dp[i][j] = float("inf")
                for k in range(i, j + 1):
                    dp[i][j] = min(dp[i][j], k + max(dp[i][k - 1], dp[k + 1][j]))

        return dp[1][n]
