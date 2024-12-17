from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        sell = [0] * len(prices)
        buy = [0] * len(prices)
        cooldown = [0] * len(prices)

        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            cooldown[i] = max(cooldown[i-1], sell[i-1])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            buy[i] = max(buy[i-1], cooldown[i-1] - prices[i])

        return max(sell[-1], cooldown[-1])