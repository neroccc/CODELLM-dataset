from typing import List
class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] < '7'):
                dp[i] += dp[i - 2]
            dp[i] %= MOD

        return dp[n]