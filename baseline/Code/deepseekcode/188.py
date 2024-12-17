from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k==0:
            return 0
        n = len(prices)
        if k >= n // 2:
            return sum(prices[i] - prices[i - 1] for i in range(1, n) if prices[i] > prices[i - 1])
        dp = [[0] * n for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_profit = dp[i - 1][0] - prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_profit)
                max_profit = max(max_profit, dp[i - 1][j - 1] - prices[j])
        return dp[k][-1]