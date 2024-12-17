from typing import List
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        m, n = len(grid), len(grid[0])
        cat, mouse = None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    cat = (i, j)
                elif grid[i][j] == 'M':
                    mouse = (i, j)
        if not cat or not mouse:
            return False
        seen = set()
        return self.dfs(grid, catJump, mouseJump, cat, mouse, seen)

    def dfs(self, grid, catJump, mouseJump, cat, mouse, seen):
        m, n = len(grid), len(grid[0])
        if (cat[0], cat[1], mouse[0], mouse[1]) in seen:
            return False
        seen.add((cat[0], cat[1], mouse[0], mouse[1]))
        if cat[0] == mouse[0] and cat[1] == mouse[1]:
            return True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y =