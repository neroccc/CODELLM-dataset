from typing import List
class Solution:
    def shortestDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        dp = [[float('inf')] * n for _ in range(k)]
        for i in range(n):
            for j in range(k):
                if i == 0:
                    dp[j][i] = houses[i] - houses[i]
                else:
                    dp[j][i] = min(dp[j][i - 1] + houses[i] - houses[i - 1], houses[i] - houses[i])
        return min(dp[j][n - 1] for j in range(k))