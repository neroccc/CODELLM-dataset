from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        left_min = prices[0]
        right_max = prices[-1]

        left_profits = [0] * n
        right_profits = [0] * (n + 1)

        for i in range(1, n):
            left_profits[i] = max(left_profits[i - 1], prices[i] - left_min)
            left_min = min(left_min, prices[i])

        for i in range(n - 1, 0, -1):
            right_profits[i] = max(right_profits[i + 1], right_max - prices[i])
            right_max = max(right_max, prices[i])

        max_profit = 0
        for i in range(0, n):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])

        return max_profit