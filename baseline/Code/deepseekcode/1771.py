from typing import List
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [[0] * m for _ in range(n)]
        dp2 = [[0] * m for _ in range(n)]
        ans = 0

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, m):
                if word1[i] == word2[j]:
                    if j == m - 1 or i == n - 1 or dp2[i + 1][j - 1]:
                        dp[i][j] = dp2[i + 1][j - 1] + 2
                        ans = max(ans, dp[i][j])
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if word1[i] == word2[j]:
                    if i == n - 1 or j == m - 1 or dp[i + 1][j + 1]:
                        dp2[i][j] = dp[i + 1][j + 1] + 1
                        ans = max(ans, dp2[i][j])
                    else:
                        dp2[i][j] = max(dp2[i + 1][j], dp2[i][j + 1])
                else:
                    dp2[i][j] = max(dp2[i + 1][j], dp2[i][j + 1])

        return ans