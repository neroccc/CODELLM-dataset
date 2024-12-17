from typing import List
class Solution:
    def stoneGame(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = stoneValue[i]
            for j in range(i + 1, n):
                dp[i][j] = max(stoneValue[i] - dp[i + 1][j], stoneValue[j] - dp[i][j - 1])

        return dp[0][n - 1]