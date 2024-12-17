from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]

            dp[i][j] = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[i][j] < matrix[ni][nj]:
                    dp[i][j] = max(dp[i][j], dfs(ni, nj) + 1)

            return dp[i][j]

        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))

        return ans