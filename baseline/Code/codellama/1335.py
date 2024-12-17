from typing import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        dp = [[float('inf')] * n for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])
        
        for i in range(1, d):
            for j in range(i, n):
                dp[i][j] = min(dp[i - 1][k] + jobDifficulty[j] for k in range(i, j + 1))
        
        return dp[-1][-1]
