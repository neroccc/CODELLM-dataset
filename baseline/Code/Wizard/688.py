from typing import List
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        moves = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

        for _ in range(k):
            new_dp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n:
                            new_dp[i][j] += dp[x][y] / 8
            dp = new_dp

        return sum(map(sum, dp)) / (8 ** k)