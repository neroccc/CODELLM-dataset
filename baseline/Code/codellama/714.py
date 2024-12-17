from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = -prices[0]
        for i in range(1, n):
            dp[i % 2][i] = max(dp[(i - 1) % 2][i - 1], prices[i] - fee)
            for j in range(i):
                dp[i % 2][i] = max(dp[i % 2][i], dp[(i - 1) % 2][j] + prices[i] - prices[j])
        return dp[n % 2][n - 1]