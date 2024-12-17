from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(2)]
        dp[0][0][0] = grid[0][0]

        for k in range(1, 2 * n - 1):
            for i in range(max(0, k - n + 1), min(n, k + 1)):
                for j in range(max(0, k - n + 1), min(n, k + 1)):
                    if grid[i][k - i] == -1 or grid[j][k - j] == -1:
                        dp[k % 2][i][j] = -float("inf")
                        continue

                    if i == j:
                        dp[k % 2][i][j] = dp[(k - 1) % 2][i - 1][j - 1] + grid[i][k - i]
                    else:
                        dp[k % 2][i][j] = max(
                            dp[(k - 1) % 2][i - 1][j - 1],
                            dp[(k - 1) % 2][i - 1][j],
                            dp[(k - 1) % 2][i][j - 1],
                        ) + grid[i][k - i] + grid[j][k - j]

        return max(0, dp[(2 * n - 2) % 2][n - 1][n - 1])