from typing import List
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * 3 for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
            dp[i][1] = dp[i - 1][0]
            dp[i][2] = dp[i - 1][1]

        return (dp[n][0] + dp[n][1] + dp[n][2]) % MOD