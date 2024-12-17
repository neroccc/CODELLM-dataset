from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * (n + 1)
        dp[-1] = 0

        for i in range(n - 1, -1, -1):
            dp[i] = float('inf')
            for j in range(n - 1, i - 1, -1):
                if days[i] - days[j] <= 1:
                    dp[i] = min(dp[i], dp[j] + costs[0])
                elif days[i] - days[j] <= 7:
                    dp[i] = min(dp[i], dp[j] + costs[1])
                elif days[i] - days[j] <= 30:
                    dp[i] = min(dp[i], dp[j] + costs[2])

        return dp[0]