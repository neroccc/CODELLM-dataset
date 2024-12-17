from typing import List
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[float('inf')] * (target + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(1, target + 1):
                    if houses[i - 1] == 0:
                        for l in range(1, n + 1):
                            if l != j:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][l][k - 1] + cost[i - 1][j - 1])
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][l][k])
                    else:
                        if houses[i - 1] == j:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                        else:
                            dp[i][j][k] =