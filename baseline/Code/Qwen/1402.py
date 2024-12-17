from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        n = len(satisfaction)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + satisfaction[i - 1] * j)

        return dp[n][n]