from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(3)]
        for k in range(1, 3):
            hold = -prices[0]
            for i in range(1, n):
                dp[k][i] = max(dp[k][i - 1], hold + prices[i])
                hold = max(hold, dp[k - 1][i - 1] - prices[i])
        return dp[2][n - 1]