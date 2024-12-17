from typing import List
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 1

        for mask in range(1 << n):
            for i in range(n):
                if mask & (1 << i):
                    for j in range(n):
                        if i != j:
                            dp[mask | (1 << j)][j] += dp[mask][i]
                            dp[mask | (1 << j)][j] %= 1000000007

        return dp[(1 << n) - 1][finish]