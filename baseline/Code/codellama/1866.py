from typing import List
class Solution:
    def stickers(self, n: int, k: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i > j:
                    dp[i][j] = dp[i][j - 1]
                elif i <= j:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
        return dp[n][k] % (10 ** 9 + 7)
