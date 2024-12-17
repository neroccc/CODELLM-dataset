from typing import List
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            dp[i][1] = 1
            dp[i][2] = 2
        for i in range(1, k + 1):
            for j in range(3, n + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1] + 1
        return dp[k][n]