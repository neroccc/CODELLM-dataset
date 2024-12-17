from typing import List
class Solution:
    def numberOfPaths(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(n):
                for k in range(i + 1, n):
                    if i == 0 or j == 0:
                        dp[i][k] = dp[i][k - 1] + dp[i - 1][k]
                    else:
                        dp[i][k] = (dp[i][k - 1] + dp[i - 1][k]) % MOD

        return dp[n - 1][n - 1]