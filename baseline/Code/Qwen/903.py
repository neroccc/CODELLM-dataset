from typing import List
class Solution:
    def countPermutations(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, n + 1):
            for j in range(i + 1):
                if s[i - 1] == 'D':
                    dp[i][j] = (dp[i - 1][j] + (dp[i - 1][j - 1] if j > 0 else 0)) % mod
                else:
                    dp[i][j] = (dp[i - 1][j - 1] if j > 0 else 0) + (dp[i - 1][j] - dp[i - 1][j - 1] if j > 0 else dp[i - 1][j]) % mod

        return dp[n][0]