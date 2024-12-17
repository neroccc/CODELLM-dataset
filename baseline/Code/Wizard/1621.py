from typing import List
class Solution:
    def numberOfCombinations(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [1] * n
        for i in range(1, n):
            for j in range(1, k):
                if i - j >= 0:
                    dp[i] = (dp[i] + dp[i - j]) % MOD
        return dp[-1]