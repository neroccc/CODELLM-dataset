from typing import List
class Solution:
    def numberOfWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if k == 1:
            return 0

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[1][1] = k
        dp[2][2] = k * (k - 1)
        dp[2][3] = k * (k - 1) * (k - 2)

        for i in range(3, n + 1):
            for j in range(3, i + 1):
                dp[i][j] = (dp[i - 1][j - 1] * (k - 1) + dp[i - 2][j - 2] * (k - 1)) % (10 ** 9 + 7)

        return dp[n][n]