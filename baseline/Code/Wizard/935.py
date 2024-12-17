from typing import List
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = {(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)}
        memo = {}

        def dfs(x, y, steps):
            if (x, y, steps) in memo:
                return memo[(x, y, steps)]
            if steps == n:
                return 1
            if x < 0 or x >= 10 or y < 0 or y >= 10 or s[x][y] == " ":
                return 0

            count = 0
            for dx, dy in moves:
                count += dfs(x + dx, y + dy, steps + 1)
            memo[(x, y, steps)] = count
            return count
