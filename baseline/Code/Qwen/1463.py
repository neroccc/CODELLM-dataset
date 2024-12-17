from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0] * n for _ in range(n)] for _ in range(m)]
        dp[0][0][n - 1] = grid[0][0] + grid[0][n - 1]

        for i in range(1, m):
            for j1 in range(n):
                for j2 in range(n):
                    for k1 in range(max(0, j1 - 1), min(n, j1 + 2)):
                        for k2 in range(max(0, j2 - 1), min(n, j2 + 2)):
                            if k1 != k2:
                                dp[i][j1][j2] = max(dp[i][j1][j2], dp[i - 1][k1][k2] + grid[i][j1] + grid[i][j2])

        return max(dp[m - 1][j1][j2] for j1 in range(n) for j2 in range(n))