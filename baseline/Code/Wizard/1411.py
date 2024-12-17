from typing import List
class Solution:
    def countWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * 3
        dp[0] = 1

        for _ in range(n):
            new_dp = [0] * 3
            for i in range(3):
                for j in range(3):
                    if i != j:
                        new_dp[(i + j) % 3] += dp[i]
                        new_dp[(i + j) % 3] %= MOD
            dp = new_dp

        return dp[0]