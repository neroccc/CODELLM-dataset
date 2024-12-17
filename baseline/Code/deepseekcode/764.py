from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1]*n for _ in range(n)]
        left, right, up, down = [[0]*n for _ in range(n)], [[0]*n for _ in range(n)], [[0]*n for _ in range(n)], [[0]*n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if i > 0:
                    up[i][j] = up[i-1][j] + 1
                else:
                    up[i][j] = 1
                if j > 0:
                    left[i][j] = left[i][j-1] + 1
                else:
                    left[i][j] = 1
        maximum = 0
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if grid[i][j] == 0:
                    continue
                if i < n-1:
                    down[i][j] = down[i+1][j] + 1
                else:
                    down[i][j] = 1
                if j < n-1:
                    right[i][j] = right[i][j+1] + 1
                else:
                    right[i][j] = 1
                maximum = max(maximum, min(left[i][j], right[i][j], up[i][j], down[i][j]))
        return maximum