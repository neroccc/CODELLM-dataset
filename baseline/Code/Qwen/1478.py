from typing import List
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        prefix = [0] * n
        for i in range(n):
            prefix[i] = prefix[i - 1] + houses[i] if i > 0 else houses[i]

        for i in range(n):
            for j in range(1, min(i + 1, k) + 1):
                if i == j - 1:
                    dp[i][j] = 0
                else:
                    for x in range(i - 1, j - 2, -1):
                        dp[i][j] = min(dp[i][j], dp[x][j - 1] + prefix[i] - prefix[x] + prefix[n - 1] - prefix[i])

        return dp[n - 1][k]