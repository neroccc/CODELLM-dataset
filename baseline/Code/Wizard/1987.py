from typing import List
class Solution:
    def countBinarySubsequences(self, binary: str) -> int:
        n = len(binary)
        dp = [1] * n
        mod = 10**9 + 7

        for i in range(1, n):
            dp[i] = 2
            for j in range(i):
                if binary[i] != binary[j]:
                    dp[i] += dp[j]
                    dp[i] %= mod

        return dp[-1]