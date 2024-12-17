from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)]
        ans = 0

        for i in range(n):
            dp[0][i] = max(dp[0][i - 1], prices[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i] - prices[i])
            ans = max(ans, dp[1][i])

        return ans