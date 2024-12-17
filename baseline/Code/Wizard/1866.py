from typing import List
class Solution:
    def countArrangement(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if i % j == 0:
                    dp[i] += dp[i - j]
                    dp[i] %= MOD

        return dp[k]