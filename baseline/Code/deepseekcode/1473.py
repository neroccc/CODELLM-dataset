from typing import List
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf')] * (n + 1) for _ in range(target + 1)] for _ in range(m + 1)]
        dp[0][0] = [0] * (n + 1)

        for i in range(m):
            for j in range(i + 1):
                for k in range(1, n + 1):
                    if houses[i] == 0 or houses[i] == k:
                        for l in range(j, target):
                            dp[i + 1][l + 1][k] = min(dp[i + 1][l + 1][k], dp[i][j][k] + (houses[i] != k))
                if houses[i] == 0:
                    for l in range(j):
                        for k in range(1, n + 1):
                            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k] + cost[i][k - 1])
                else:
                    dp[i + 1][j + 1][houses[i]] = min(dp[i + 1][j