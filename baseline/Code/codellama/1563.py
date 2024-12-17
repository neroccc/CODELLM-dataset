from typing import List
class Solution:
    def lastStoneWeightII(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - 1] + stoneValue[i])
        return dp[0][n]