from typing import List
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                count = 0
                if s[i] == s[j]:
                    count = 2
                    if diff > 1:
                        count += dp[i + 1][j - 1]
                dp[i][j] = count

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                for k in range(i + 1, j):
                    if s[i] == s[j]:
                        dp[i][j] = (dp[i][j] + dp[i + 1][k - 1] + dp[k + 1][j - 1] - dp[i + 1][j - 1]) % MOD

        return dp[0][n - 1] % MOD