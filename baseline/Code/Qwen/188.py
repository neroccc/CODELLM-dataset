from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        dp = [[0] * (k + 1) for _ in range(n)]

        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i] - prices[i - 1])

        return dp[n - 1][k]