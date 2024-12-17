from typing import List
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        dp = [[[None]*3 for _ in range(cols)] for _ in range(rows)]
        cat, mouse, food = None, None, None

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'C':
                    cat = (i, j)
                elif grid[i][j] == 'M':
                    mouse = (i, j)
                elif grid[i][j] == 'F':
                    food = (i, j)

        def dfs(x: int, y: int, z: int) -> bool:
            if dp[x][y][z] is not None:
                return dp[x][y][z]

            if z == 0:
                dp[x][y][z] = any(grid[i][j] == 'F' for i, j in get_next_positions(x, y, z))
            else:
                dp[x][y][z] = all(dfs(*get_next_positions(x, y, z)) for _ in range(z))

            return dp[x][y][z]