from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        n = len(obstacles)
        dp = [[float('inf')] * 4 for _ in range(n)]
        dp[0][2] = 0

        for i in range(1, n):
            for j in range(1, 4):
                if obstacles[i] != j:
                    dp[i][j] = dp[i - 1][j]
                for k in range(1, 4):
                    if k != j and obstacles[i] != k:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + 1)

        return min(dp[-1][1:])