from typing import List
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if grid[i][j] == 1:
                    dp[i][j] = dp[i][j - 1] + 1
                else:
                    break
        for i in range(n - 1, -1, -1):
            dp[i][i] = max(dp[i][i], dp[i + 1][i] + 1)
        for i in range(n - 1):
            for j in range(n - 1):
                if grid[i][j] == 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return max(dp[i][j] for i in range(n) for j in range(n))