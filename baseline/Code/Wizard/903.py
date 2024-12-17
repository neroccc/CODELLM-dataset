from typing import List
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [1] * (n + 1)

        for c in s:
            if c == 'D':
                dp = [dp[i + 1] + dp[i] for i in range(n - 1, -1, -1)]
            else:
                dp = [dp[i] + dp[i + 1] for i in range(n)]

            for i in range(n):
                dp[i] %= MOD

        return dp[0]