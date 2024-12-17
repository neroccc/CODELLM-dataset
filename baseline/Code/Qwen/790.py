from typing import List
class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5

        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10 ** 9 + 7)

        return dp[n]