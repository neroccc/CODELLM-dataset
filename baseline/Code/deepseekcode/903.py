from typing import List
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10**9 + 7
        N = len(s)
        dp = [[0]*(N+1) for _ in range(N+1)]
        dp[0][0] = 1
        for n in range(1,N+1):
            dp[n][0] = dp[n-1][0]
            for m in range(1,n+1):
                if s[n-1] == 'D':
                    dp[n][m] = (dp[n][m-1] + dp[n-1][m-1]) % MOD
                else:
                    dp[n][m] = (dp[n-1][m-1] + dp[n-1][m]) % MOD
        return sum(dp[-1]) % MOD