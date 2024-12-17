from typing import List
class Solution:
    def shortestPath(self, grid: List[List[int]], int, int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[m - 1][n - 1] = grid[m - 1][n - 1]

        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = dp[i + 1][n - 1] + grid[i][n - 1]

        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = dp[m - 1][j + 1] + grid[m - 1][j]

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if grid[i][j] == "X":
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + grid[i][j]

        return dp[0][0]

    def countPaths(self, board: List[List[str]]) -> List[int]:
        MOD = 10**9 + 7
        m, n = len(board), len(board[0])
        dp = [[0] * n for _ in range(m)]
        paths = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "S":
                    dp[i][j] = 0
                    paths[i][j] = 1
                elif board[i][j] == "E":
                    dp[i][j] = float