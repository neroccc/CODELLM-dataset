from typing import List
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)
        dp[2] = 1
        dp[3] = 2

        for i in range(4, n + 1):
            dp[i] = max(dp[j] * dp[i - j] for j in range(2, i))

        return dp[n]