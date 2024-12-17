from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            dp[i][j] = 1
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], dfs(x, y) + 1)
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans