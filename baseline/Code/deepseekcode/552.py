from typing import List
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n+1)]
        dp[0][0][0] = 1
        for i in range(n):
            for j in range(2):
                for k in range(3):
                    dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k]) % mod
                    if j < 1: 
                        dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][k]) % mod
                    if k < 2: 
                        dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % mod
        return sum(dp[n][j][k] for j in range(2) for k in range(3)) % mod