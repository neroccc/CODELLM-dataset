from typing import List
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1

        for _ in range(k):
            dp2 = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for dr, dc in moves:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            dp2[r][c] += dp[nr][nc] / 8
            dp = dp2

        return sum(sum(dp, []))