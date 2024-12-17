from typing import List
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(2, n + 1):
            for i in range(1, n - l + 2):
                dp[i][i + l - 1] = min(x + max(dp[i][x - 1], dp[x + 1][i + l - 1]) for x in range(i, i + l))
        return dp[1][n]