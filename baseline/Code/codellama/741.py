from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for i in range(1, n):
            dp[i][i] = dp[i - 1][i - 1] + grid[i][i]
            if i > 1:
                dp[i][i] = max(dp[i][i], dp[i - 2][i - 2] + grid[i][i])

        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if i < n - 1:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - 1])

        return dp[n - 1][n - 1]