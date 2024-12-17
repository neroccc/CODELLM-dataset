from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    up = down = left = right = 1
                    if i > 0:
                        up = grid[i - 1][j] + 1
                    if i < n - 1:
                        down = grid[i + 1][j] + 1
                    if j > 0:
                        left = grid[i][j - 1] + 1
                    if j < n - 1:
                        right = grid[i][j + 1] + 1
                    grid[i][j] = min(up, down, left, right)

        max_order = 0
        for i in range(n):
            for j in range(n):
                max_order = max(max_order, grid[i][j])

        return max_order