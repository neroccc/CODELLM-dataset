from collections import deque
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        q = deque()
        q.append((0, 0))
        while q:
            i, j = q.popleft()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < n and dp[x][y] > grid[x][y]:
                    dp[x][y] = grid[x][y]
                    q.append((x, y))
        return dp[-1][-1]
