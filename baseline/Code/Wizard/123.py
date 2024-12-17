from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        dp = [[0] * n for _ in range(3)]

        for i in range(n):
            dp[0][i] = 0
            dp[1][i] = -prices[i]
            dp[2][i] = float('-inf')

        for i in range(2, n):
            dp[0][i] = max(dp[0][i - 1], dp[2][i - 1])
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - prices[i])
            dp[2][i] = max(dp[2][i - 1], dp[1][i - 1] + prices[i])

        return max(dp[2][n - 1], 0)