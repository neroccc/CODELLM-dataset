from typing import List
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        mod = 10**9 + 7

        for i in range(n):
            dp[i][i] = 1

        for diff in range(1, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j]:
                    dp[i][j] = (
                        dp[i + 1][j - 1] * 2 + 2
                    ) % mod  # Include the middle character
                else:
                    dp[i][j] = (
                        dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                    ) % mod  # Exclude the middle character

        return dp[0][n - 1]