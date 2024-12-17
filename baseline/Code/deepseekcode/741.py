from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(2)]
        dp[0][0][0] = grid[0][0]
        grid[0][0] = 0
        for k in range(1, 2 * n - 1):
            for x1 in range(min(n, k + 1), max(0, k - n + 1) - 1, -1):
                y1 = k - x1
                for x2 in range(min(n, k + 1), max(0, k - n + 1) - 1, -1):
                    y2 = k - x2
                    if grid[x1][y1] < 0 or grid[x2][y2] < 0:
                        continue
                    cherries = grid[x1][y1] if x1 == x2 else grid[x1][y1] + grid[x2][y2]
                    for i in range(2):
                        for j in range(2):
                            if x1 + 1 < n and dp[i][x1 + 1][y1] > -1 and dp[i][x1 + 1][y1] + cherries > dp[1 - i][x2][y2]:
                                dp[1 - i][x2][y2] = dp[i][x1 + 1][y1] + cherries
                            if y1 + 1 < n and dp[i][x1][y1 + 1] > -1 and dp[i][x1][y1 + 1] + cherries > dp[1 - i][x2][y2]:
                                dp[1 - i][x2][y2] = dp[i][x1][y1 + 1] + cherries
                            if x2 + 1 < n and dp[1 - i][x2 + 1][y2] > -1