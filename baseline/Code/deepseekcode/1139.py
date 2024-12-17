from typing import List
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        left = [[0]*n for _ in range(m)]
        up = [[0]*n for _ in range(m)]
        max_edge = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left[i][j] = (left[i][j-1]+1 if j > 0 else 1) if grid[i][j] == 1 else 0
                    up[i][j] = (up[i-1][j]+1 if i > 0 else 1) if grid[i][j] == 1 else 0
                    edge = min(left[i][j], up[i][j])

                    while left[i-edge+1][j] < edge or up[i][j-edge+1] < edge:
                        edge -= 1

                    max_edge = max(max_edge, edge)

        return max_edge*max_edge
