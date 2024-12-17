from typing import List
class Solution:
    def countNonoverlappingLines(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD
        return dp[n][k]