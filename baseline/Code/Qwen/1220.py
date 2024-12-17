from typing import List
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] * 5
        for _ in range(n - 1):
            dp2 = [0] * 5
            dp2[0] = dp[1]
            dp2[1] = (dp[0] + dp[2]) % MOD
            dp2[2] = (dp[0] + dp[1] + dp[3] + dp[4]) % MOD
            dp2[3] = (dp[2] + dp[4]) % MOD
            dp2[4] = dp[0]
            dp = dp2
        return sum(dp) % MOD