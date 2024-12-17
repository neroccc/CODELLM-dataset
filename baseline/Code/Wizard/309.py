from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        buy, sell, cooldown = float('-inf'), 0, 0

        for price in prices:
            prev_buy = buy
            buy = max(prev_buy, cooldown - price)
            prev_sell = sell
            sell = max(prev_sell, prev_buy + price)
            prev_cooldown = cooldown
            cooldown = max(prev_cooldown, sell)

        return sell