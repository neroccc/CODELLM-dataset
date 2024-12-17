from typing import List
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if j - i == 1:
                    dp[i][j] = 0
                elif j - i == 2:
                    dp[i][j] = values[i] * values[i] * values[j]
                else:
                    for k in range(i + 1, j):
                        dp[i][j] = min(dp[i][k] + dp[k][j] + values[i] * values[k] * values[j], dp[i][j])

        return dp[0][n - 1]