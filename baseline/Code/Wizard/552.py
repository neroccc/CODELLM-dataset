from typing import List
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * 3
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4

        for _ in range(3, n + 1):
            new_dp = [0] * 3
            new_dp[0] = dp[0] + dp[1] + dp[2]
            new_dp[1] = dp[0] + dp[2]
            new_dp[2] = dp[0]
            dp = new_dp

        return dp[0] % MOD