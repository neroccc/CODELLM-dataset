from typing import List
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[[-1] * cols for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c1, c2):
            if c1 < 0 or c1 >= cols or c2 < 0 or c2 >= cols:
                return 0
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]
            cherries = grid[r][c1] if c1 != c2 else grid[r][c1] * 2
            max_cherries = 0
            for nc1, nc2 in [(c1 - 1, c2 - 1), (c1 - 1, c2), (c1 - 1, c2 + 1), (c1, c2 - 1), (c1, c2 + 1), (c1 + 1, c2 - 1), (c1 + 1, c2), (c1 + 1, c2 + 1)]:
                max_cherries = max(max_cherries, dfs(r + 1, nc1, nc2))
            dp[r][c1][c2] = max_cherries + cherries
            return dp[r][c1][c2]

        return dfs(0, 0, cols - 1)