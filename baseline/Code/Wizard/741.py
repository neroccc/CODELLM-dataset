from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(1, n):
            for j in range(n):
                for k in range(n):
                    if grid[i][j] == 1:
                        if j > 0 and grid[i - 1][j - 1] == 1:
                            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])
                        if k > 0 and grid[i - 1][k - 1] == 1:
                            dp[i][j] = max(dp[i][j], dp[i - 1][k - 1])
                        dp[i][j] += grid[i][j]

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, -1, -1):
                for k in range(n - 1, -1, -1):
                    if grid[i][j] == 1:
                        if j < n - 1 and grid[i + 1][j + 1] == 1:
                            dp[i][j] = max(dp[i][j], dp[i + 1][j + 1])
                        if k < n - 1 and grid[i + 1][k + 1] == 1:
                            dp[i][j] = max(dp[i][j], dp[i + 1][k + 1])
                        dp[i][j] += grid[i][j]

        return dp[0][0]