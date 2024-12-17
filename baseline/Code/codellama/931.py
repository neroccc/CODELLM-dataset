from typing import List
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0] = matrix[0]
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif j == n - 1:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
                dp[i][j] += matrix[i][j]
        return min(dp[-1])