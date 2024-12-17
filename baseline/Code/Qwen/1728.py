from typing import List
class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        cat, mouse, food = None, None, None

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "C":
                    cat = (i, j)
                elif grid[i][j] == "M":
                    mouse = (i, j)
                elif grid[i][j] == "F":
                    food = (i, j)

        @lru_cache(None)
        def dfs(cat_pos, mouse_pos, turn):
            if turn > 1000:
                return False

            if cat_pos == mouse_pos:
                return False

            if cat_pos == food:
                return True

            if mouse_pos == food:
                return True

            if turn % 2 == 0:
                for i in range(-catJump, catJump + 1):
                    for j in range(-catJump, catJump + 1):
                        if abs(i) + abs(j) > catJump:
                            continue
                        new_cat_pos = (cat_pos[0] + i, cat_pos[1] + j)
                        if 0 <= new_cat_pos[0] < rows and 0 <= new_cat_pos[1] < cols and grid[new_cat_pos[0]][new_cat_pos[1]] != "#":