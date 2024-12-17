from typing import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1

        dp = [[float('inf')] * n for _ in range(d)]
        dp[0][0] = 0

        for i in range(1, d):
            for j in range(i, n):
                for k in range(j, -1, -1):
                    if k == 0:
                        dp[i][j] = max(dp[i][j], jobDifficulty[k])
                    else:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + jobDifficulty[k])

        for i in range(d - 1, -1, -1):
            for j in range(i + 1, n):
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k - 1] + jobDifficulty[k])

        return dp[0][n - 1] if dp[0][n - 1] != float('inf') else -1