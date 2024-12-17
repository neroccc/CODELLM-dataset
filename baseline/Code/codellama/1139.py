from typing import List
class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    ans = max(ans, dp[i][j])

        return ans ** 2