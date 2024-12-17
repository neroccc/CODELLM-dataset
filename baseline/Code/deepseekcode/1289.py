from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[0]*n for _ in range(n)]
        dp[0] = grid[0]
        
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j+1:]) + grid[i][j]
                elif j == n-1:
                    dp[i][j] = min(dp[i-1][:j]) + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][:j] + dp[i-1][j+1:]) + grid[i][j]
        return min(dp[-1])