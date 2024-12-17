from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[[0] * (cols + 1) for _ in range(cols + 1)] for _ in range(rows + 1)]
        dp[0][0][0] = grid[0][0]
        for i in range(1, rows + 1):
            for j in range(cols + 1):
                for k in range(cols + 1):
                    if j > 0:
                        dp[i][j][k] = max(dp[i - 1][j - 1][k], dp[i - 1][j][k])
                    if k > 0