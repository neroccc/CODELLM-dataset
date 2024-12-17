from typing import List
class Solution:
    def distinctSubsequences(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7
        dp = [1] * n

        for i in range(n):
            temp = [0] * n
            for j in range(n):
                if i == j:
                    temp[j] = 1
                elif s[i] != s[j]:
                    temp[j] = dp[j]
                else:
                    temp[j] = (dp[j] + dp[j - 1]) % MOD
            dp = temp

        return dp[-1]