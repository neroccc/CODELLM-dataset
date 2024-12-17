from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0] = grid[0]
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == n - 1:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
                else:
                    dp[i][j] = grid[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
        return min(dp[-1])