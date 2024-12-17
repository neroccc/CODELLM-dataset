from typing import List
class Solution:
    def numberOfWays(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = 1
            for j in range(1, min(i, k) + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] * (i - j + 1)) % mod

        return dp[n][k]