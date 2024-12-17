from typing import List
class Solution:
    def countVowelStrings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * 5

        for _ in range(n - 1):
            new_dp = [0] * 5
            new_dp[0] = dp[0]
            new_dp[1] = dp[0] + dp[1]
            new_dp[2] = dp[1] + dp[2]
            new_dp[3] = dp[2] + dp[3]
            new_dp[4] = dp[3] + dp[4]
            dp = new_dp

        return sum(dp) % MOD