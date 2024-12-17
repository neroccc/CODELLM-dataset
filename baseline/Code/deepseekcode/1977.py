from typing import List
class Solution:
    def numberOfArrays(self, s: str, MOD = 10**9 + 7) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, 2 if s[i - 1] != '0' else i):
                if i - j >= 0:
                    dp[i] = (dp[i] + dp[i - j]) % MOD
        return dp[-1]